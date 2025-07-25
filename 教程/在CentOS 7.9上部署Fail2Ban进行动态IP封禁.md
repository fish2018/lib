### 在CentOS 7.9上部署Fail2Ban进行动态IP封禁

**核心目标**：自动监控您的API日志，一旦发现来自任何IP的异常高频访问，立即通过 `iptables` 将其封禁24小时。

**此方案的优势**：
*   **完美适配CentOS 7**：使用 `yum` 安装，并与CentOS 7默认的 `iptables` 无缝集成。
*   **一劳永逸**：配置一次，即可长期自动运行，无需人工干预。
*   **资源高效**：在防火墙层面直接拒绝恶意连接，避免了Nginx等应用层软件处理这些无效请求所带来的资源消耗。

---

### 详细实施步骤

#### 第1步：启用iptables

```
# 1. 安装 iptables-services 包，它能让我们保存和重载规则
sudo yum install -y iptables-services

# 2. 启动 iptables 服务
sudo systemctl start iptables

# 3. 设置 iptables 开机自启
sudo systemctl enable iptables

# 4. （可选但推荐）确保你的SSH端口是放行的，防止把自己锁在外面
# 默认SSH端口是22
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 5. 保存当前规则，让它在重启后依然生效
sudo service iptables save
```

#### 第2步：安装Fail2Ban

CentOS 7的官方源中不包含Fail2Ban，需要先安装`epel-release`扩展源。

```bash
# 安装EPEL源
sudo yum install -y epel-release

# 清理缓存并安装Fail2Ban
sudo yum clean all
sudo yum install -y fail2ban
```

#### 第3步：创建Fail2Ban过滤规则

这个规则告诉Fail2Ban如何在您的日志文件中识别出IP地址。

```bash
# 编辑配置
sudo vi /etc/fail2ban/filter.d/nginx-api-abuse.conf
```

将以下内容**完整地**复制粘贴进去：

```ini
[Definition]
# 匹配任何以IP地址开头的日志行
failregex = ^<HOST> -.*
ignoreregex =
```

保存并关闭文件 (在`nano`中，按 `Ctrl+X`，然后按 `Y`，再按 `Enter`)。

#### 第4步：配置核心封禁策略 (Jail)

这是最关键的一步。我们将创建一个本地配置文件 `jail.local`，用于定义封禁的条件和动作。

```bash
# 创建并编辑本地配置文件
sudo vi /etc/fail2ban/jail.local
```

将以下配置**完整地**复制粘贴进去，并根据注释**务必修改**您自己的信息：

```
[DEFAULT]
# [!!!] 关键：将你自己的公网IP加入白名单，防止被误封！
# 可以是单个IP，也可以是IP段，用空格隔开。
ignoreip = 127.0.0.1/8 ::1 YOUR_OWN_IP_ADDRESS_HERE

# 封禁时长，3600秒 = 1小时
bantime  = 3600

# 监测时间窗口，300秒 = 5分钟
findtime = 300

# 在findtime内，同一个IP达到多少次请求就触发封禁
maxretry = 300

# [!!!] 关键：明确指定使用iptables执行封禁动作
banaction = iptables-multiport


# --- 针对您API日志的专属“监狱”配置 ---
[nginx-api-abuse]
enabled  = true
port     = http,https
filter   = nginx-api-abuse
# [!!!] 关键：将这里的路径修改为你API日志文件的真实绝对路径！
logpath  = /home/work/logs/pansou.log 
maxretry = 300
findtime = 300
bantime  = 3600
```
**配置说明**：
*   **`ignoreip`**: **必填项**。把您家或公司的公网IP填进去，避免调试时把自己封了。
*   **`logpath`**: **必填项**。请使用 `ls -l /path/to/your/log` 确认路径完全正确。
*   **`maxretry`**: `300`次是个好起点。爬虫的请求频率远高于此，而正常用户几乎不可能达到。

#### 第5步：启动Fail2Ban并验证效果

现在，让我们的自动化保安正式上岗。

```bash
# 启动Fail2Ban服务，并设置为开机自启
sudo systemctl start fail2ban
sudo systemctl enable fail2ban

# 等待一分钟，让Fail2Ban有时间读取和分析日志
echo "等待60秒, 让Fail2Ban开始工作..."
sleep 60

# --- 验证环节 ---

# 1. 检查Fail2Ban服务是否正常运行
sudo systemctl status fail2ban
# 应该会显示 active (running)

# 2. 检查我们创建的监狱是否被激活
sudo fail2ban-client status
# 你应该能在Jail list中看到 `nginx-api-abuse`

# 3. 查看具体监狱的状态和已封禁的IP列表 (这是最重要的检查)
sudo fail2ban-client status nginx-api-abuse
```

执行最后一条命令后，您应该会看到类似下面的输出：
```
Status for an jail: nginx-api-abuse
|- Filter
|  |- Currently failed: 0
|  |- Total failed: 15487
|  `- File list:        /path/to/your/pansou.log
`- Actions
   |- Currently banned: 4
   |- Total banned: 4
   `- Banned IP list:   172.68.22.132 172.68.22.207 66.103.211.214 172.68.22.169 
```
如果 `Banned IP list` 中出现了那些高频访问的IP，就代表您的自动化防御系统已经成功部署并开始工作了。

自此，您的服务器就有了一套可靠的、自动化的安全防护机制。