## 效果：
图片存放路径：
```
/home/jobs/webs/imgs/
├── default/
│   ├── image1.jpg
│   ├── image2.png
├── cats/
│   ├── cat1.jpg
│   ├── cat2.gif
├── dogs/
│   ├── dog1.jpg
```

访问http://www.fish2018.us.kg/imgs/default  随机返回`/home/jobs/webs/imgs/default`下的图片  
访问http://www.fish2018.us.kg/imgs/  随机返回`/home/jobs/webs/imgs/`所有的图片(包含所有子目录)

## 安装openresty
yum方式安装
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo
yum install -y openresty
```

修改默认配置  

vi /usr/local/openresty/nginx/conf/nginx.conf
```
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /usr/local/openresty/nginx/logs/nginx.pid;
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    gzip on;
    gzip_buffers 32 4K;
    gzip_comp_level 9;
    gzip_min_length 100;
    gzip_types text/plain application/xml application/json application/javascript text/css text/xml application/x-javascript;
    gzip_disable "MSIE [1-6]\."; #配置禁用gzip条件，支持正则。此处表示ie6及以下不启用gzip（因为ie低版本不支持）
    gzip_vary on;
    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;
    include /etc/nginx/conf.d/*.conf; # 后面配置会放在/etc/nginx/conf.d/xxx.conf
}

# tcp转发
include /etc/nginx/tcp.d/*.conf;
```

编写lua脚本，实现从指定路径下随机返回图片(包含子路径)  
vi /etc/nginx/conf.d/random_image.lua 
```
-- random_image.lua
package.path = package.path .. ";/usr/local/share/lua/5.1/?.lua;/usr/share/lua/5.1/?.lua"
package.cpath = package.cpath .. ";/usr/local/lib/lua/5.1/?.so;/usr/lib64/lua/5.1/?.so"

local lfs = require("lfs")
local images = {}

-- 从 Nginx 配置中获取 base_dir
local base_dir = ngx.var.base_dir

-- 确保 base_dir 以斜杠结尾
if not base_dir:match("/$") then
    base_dir = base_dir .. "/"
end

-- 遍历目录及其子目录
local function find_images(dir)
    for file in lfs.dir(dir) do
        if file ~= "." and file ~= ".." then
            local full_path = dir .. file
            local attr = lfs.attributes(full_path)
            if attr.mode == "directory" then
                -- 如果是目录，递归查找
                find_images(full_path .. "/")
            elseif attr.mode == "file" and (file:match("%.jpg$") or file:match("%.png$") or file:match("%.gif$")) then
                -- 如果是图片文件（jpg、png、gif），添加到列表
                table.insert(images, full_path)
            end
        end
    end
end

-- 开始查找图片
find_images(base_dir)

-- 随机选择一张图片
if #images > 0 then
    local random_image = images[math.random(#images)]
    local file = io.open(random_image, "rb")  -- 以二进制模式打开文件
    if file then
        local data = file:read("*all")  -- 读取文件内容
        file:close()
        
        -- 根据文件扩展名设置 Content-Type
        if random_image:match("%.jpg$") then
            ngx.header.content_type = "image/jpeg"
        elseif random_image:match("%.png$") then
            ngx.header.content_type = "image/png"
        elseif random_image:match("%.gif$") then
            ngx.header.content_type = "image/gif"
        else
            ngx.header.content_type = "application/octet-stream"  -- 默认类型
        end
        
        ngx.say(data)  -- 直接输出图片内容
    else
        ngx.say("Failed to open image.")
    end
else
    ngx.say("No images found.")
end
```

在server的配置使用lua脚本
vi /etc/nginx/conf.d/fish2018.conf
```
# 处理 /imgs/ 路径的请求
location /imgs/ {
    # 设置 base_dir 变量
    set $base_dir "/home/jobs/webs/imgs/";

    # 提取子路径（例如 /imgs/default -> default）
    set $sub_path "";
    if ($uri ~ ^/imgs/(.+)$) {
        set $sub_path $1;
        set $base_dir "$base_dir$sub_path/";
    }
    # 调用 Lua 脚本
    content_by_lua_file /etc/nginx/conf.d/random_image.lua;
}
```

启动openresty
```
systemctl start openresty
```

如果出现报错
tail -f /var/log/nginx/error.log
```
2025/02/11 15:32:47 [error] 15294#15294: *321 lua entry thread aborted: runtime error: /etc/nginx/conf.d/random_image.lua:1: module 'lfs' not found:
        no field package.preload['lfs']
        no file '/usr/local/openresty/site/lualib/lfs.ljbc'
        no file '/usr/local/openresty/site/lualib/lfs/init.ljbc'
        no file '/usr/local/openresty/lualib/lfs.ljbc'
```

安装lua开发包
```
yum -y install lua-devel
```

确保你已安装 luarocks
```
yum -y install luarocks
```

先确认 luafilesystem 是否已经安装。你可以使用 luarocks 命令列出已安装的模块：
```
luarocks list
```
如果列表中没有 luafilesystem，那么你需要安装它：
```
luarocks install luafilesystem
```
安装完成后，你可以通过以下命令来验证 lfs 模块是否成功安装，如果没有错误输出，说明安装成功：
```
lua -e "require'lfs'"
```
然后你可以通过以下命令查找它的路径：
```
luarocks show luafilesystem
```

修改 package.path 和 package.cpath
在你的 Lua 脚本的开头添加以下代码，确保包含 lfs 模块的路径：
```
package.path = package.path .. ";/usr/local/share/lua/5.1/?.lua;/usr/share/lua/5.1/?.lua"
package.cpath = package.cpath .. ";/usr/local/lib/lua/5.1/?.so;/usr/lib64/lua/5.1/?.so"
```
