### GoAccess 实时 HTML 报告部署指南

GoAccess 能够生成一个实时的、可视化的 HTML 报告，用于动态监控 Web 服务器的访问日志。其核心是利用 **WebSocket** 协议，将服务器日志的持续变化实时推送到浏览器页面，从而实现数据的动态更新，而无需用户手动刷新。

所有面板和指标在 HTML 报告上可以实现每秒更新一次。这里主要用于监控`pansou`后端nginx日志。然后在前端域名+`/report.html`展示。

---

#### 1. 工作原理

实时报告的实现分为三个关键部分：

1.  **后台守护进程**：您需要启动一个 GoAccess 进程，并使用 `--daemonize` 参数使其在后台作为守护进程持续运行。
2.  **HTML 页面生成**：该进程会生成一个初始的 HTML 文件。这个文件内嵌了 JavaScript 代码，用于连接 WebSocket 服务器。
3.  **WebSocket 服务**：GoAccess 进程会启动一个内嵌的 WebSocket 服务器（默认监听 `7890` 端口），用于持续将新的日志分析数据推送给所有连接的浏览器客户端。

当用户通过浏览器访问生成的 HTML 页面时，页面会自动尝试连接到 GoAccess 的 WebSocket 服务，一旦连接成功，报告数据就会开始实时刷新。

---

#### 2. 基础实时模式（不推荐直接用于公网）

**安装goaccess**
```
# CentOS/RHEL 系统
sudo yum install goaccess

# Debian/Ubuntu 系统
sudo apt-get install goaccess
```

**修改goaccess配置文件**
`vi /etc/goaccess.conf`
```
# Nginx 日志的时间格式
time-format %H:%M:%S

# Nginx 日志的日期格式
date-format %d/%b/%Y

# 对应您 Nginx 日志的格式
# '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for"'
log-format %h %l %e [%d:%t %^] "%r" %s %b "%R" "%u" "%^"
```

这里说明一下，这个不是默认的日志格式，是为了匹配CF透传的IP做了调整，对应的后端nginx配置如下(因为后端api独立对外开放，所以没有和前端共用域名，主要针对这个域名的nginx日志监控):

```
# 定义一个新的日志格式，可以在 server 块中定义
log_format main_realip '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

# 每个IP限流每分钟最多60次调用
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=60r/m;

server {
    listen 80;
    server_name pansou.252035.xyz;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name pansou.252035.xyz;

    # --- 开始新增和修改的内容 ---

    # 1. 设置信任的代理服务器IP地址 (Cloudflare IP 段)
    # 官方列表: https://www.cloudflare.com/ips/
    set_real_ip_from 173.245.48.0/20;
    set_real_ip_from 103.21.244.0/22;
    set_real_ip_from 103.22.200.0/22;
    set_real_ip_from 103.31.4.0/22;
    set_real_ip_from 141.101.64.0/18;
    set_real_ip_from 108.162.192.0/18;
    set_real_ip_from 190.93.240.0/20;
    set_real_ip_from 188.114.96.0/20;
    set_real_ip_from 197.234.240.0/22;
    set_real_ip_from 198.41.128.0/17;
    set_real_ip_from 162.158.0.0/15;
    set_real_ip_from 104.16.0.0/13;
    set_real_ip_from 104.24.0.0/14;
    set_real_ip_from 172.64.0.0/13;
    set_real_ip_from 131.0.72.0/22;
    set_real_ip_from 2400:cb00::/32;
    set_real_ip_from 2606:4700::/32;
    set_real_ip_from 2803:f800::/32;
    set_real_ip_from 2405:b500::/32;
    set_real_ip_from 2405:8100::/32;
    set_real_ip_from 2a06:98c0::/29;
    set_real_ip_from 2c0f:f248::/32;

    # 2. 指定从哪个 header 获取真实IP (CF-Connecting-IP 更安全)
    real_ip_header CF-Connecting-IP;
    # (备选方案: real_ip_header X-Forwarded-For;)

    # 3. 使用我们在上面新定义的日志格式
    access_log /home/work/logs/pansou.log main_realip;
    
    # --- 结束新增和修改的内容 ---

    # 证书和密钥路径 (保持不变)
    ssl_certificate /etc/letsencrypt/live/252035.xyz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/252035.xyz/privkey.pem;

    # 增强 SSL 安全性 (保持不变)
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH;
    ssl_prefer_server_ciphers on;

    # 后端代理 (保持不变)
    location / {
        # 应用限流规则 (保持不变, 它现在会自动对真实IP生效)
        limit_req zone=api_limit burst=10 nodelay;
        limit_req_status 429;

        proxy_pass http://127.0.0.1:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr; # $remote_addr 现在是真实IP
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```


最基础的启动方式是直接生成一个实时报告，并让 GoAccess 在后台运行。

**查看字符集**
```
locale -a | grep "zh_CN"

>>>
zh_CN
zh_CN.gb18030
zh_CN.gb2312
zh_CN.gbk
zh_CN.utf8
```

**启动命令示例**：
```bash
LANG=zh_CN.utf8 goaccess /home/work/logs/pansou.log -o /home/jobs/pansou-web/report.html --real-time-html --daemonize --ws-url=wss://so.252035.xyz/ws --addr=127.0.0.1 --port=7890
```
**命令参数解析**：

*   `--ws-url=wss://so.252035.xyz/ws`: 这是关键。它告诉浏览器内的 JavaScript 通过标准的 HTTPS 端口（443）访问一个名为 `/ws` 的路径来建立 wss 连接。我们不再直接暴露 `7890` 端口。
*  `--addr=127.0.0.1`: 使 GoAccess 的 WebSocket 服务只在本地监听，不对外网开放。
*  `--port=7890`: GoAccess 仍然在本地的 `7890` 端口上监听，等待 Nginx 的转发。

此命令执行后，GoAccess 会开始在 `127.0.0.1:7890` 上监听 WebSocket 连接。

#### 第 2 步：配置 Nginx

在您的 Nginx 配置文件中（通常是 `/etc/nginx/conf.d/your-domain.conf`），添加一个 `location` 块来代理 WebSocket 请求。

```pansou-web.conf
server {
    listen 80;
    server_name so.252035.xyz;

    # 将 HTTP 重定向到 HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name so.252035.xyz;

    # 证书和密钥路径
    ssl_certificate /etc/letsencrypt/live/252035.xyz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/252035.xyz/privkey.pem;

    # 增强 SSL 安全性
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH;
    ssl_prefer_server_ciphers on;
    
    ##<- GoAccess ##
    location /report.html {
       alias /home/jobs/pansou-web/report.html;
    }

    location /ws {
        proxy_pass http://127.0.0.1:7890; # 代理到 GoAccess 守护进程的端口
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    ## GoAccess ->##

    location / {
       root /home/jobs/pansou-web/dist;
       index index.html;
       try_files $uri $uri/ /index.html;
    }

    # 后端代理
    location /api/ {
        proxy_pass http://127.0.0.1:8888/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**配置解析**：
*   `location /ws`：匹配您在 `--ws-url` 中设置的路径。
*   `proxy_pass http://127.0.0.1:7890;`：将匹配到的请求转发给在本地 `7890` 端口监听的 GoAccess 进程。
*   `proxy_set_header Upgrade` 和 `proxy_set_header Connection`：这两行是启用 WebSocket 代理的**必要**配置。

#### 第 3 步：重启服务并验证

1.  **保存** Nginx 配置文件。
2.  **检查** Nginx 配置是否正确：`sudo nginx -t`
3.  **重新加载** Nginx 服务：`sudo systemctl reload nginx`
4.  清空浏览器缓存后，重新访问您的报告页面 `https://so.252035.xyz/report.html`。
5.  **验证**：页面左上角（或右上角）的连接状态指示灯应该会变成**绿色**，表示 WebSocket 连接成功。您也可以按 `F12` 打开浏览器开发者工具，在“网络(Network)”面板下，应该能看到一个对 `/ws-goaccess` 的请求，其状态码为 `101 Switching Protocols`。
