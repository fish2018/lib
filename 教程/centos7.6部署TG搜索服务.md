## 初始化环境
```
yum -y install lrzsz wget
systemctl stop postfix && systemctl disable postfix
systemctl stop rpcbind.socket && systemctl disable rpcbind.socket

hostnamectl set-hostname hk-8C8G
timedatectl set-timezone Asia/Shanghai
```

## [目录结构及脚本工具](https://github.com/fish2018/lib/tree/main/教程/deploy)  
```
mkdir -p /home/{data,jobs/{archive,webs/{z,p},TGForwarder,PG/p,ZX/z},work/logs}
mount --bind  /home/jobs/ZX/z/ /home/jobs/webs/z/
mount --bind  /home/jobs/PG/p/ /home/jobs/webs/p/
ln -s /home/jobs /root/jobs
ln -s /home/data /root/data
ln -s /home/work /root/work
ln -s /home/work/logs /root/logs
```

## 配置yum源
```
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
或者
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
```

## 安装编译依赖
```
yum groupinstall 'Development Tools' -y
yum -y install sqlite sqlite-devel libffi-devel bzip2-devel xz-devel gdbm-devel readline-devel tk-devel zlib zlib-devel perl
```

## 编译安装opennssl
```
cd /home/data
wget https://www.openssl.org/source/openssl-1.1.1s.tar.gz
tar xf openssl-1.1.1s.tar.gz
cd openssl-1.1.1s
./config -fPIC --prefix=/usr/include/openssl enable-shared
make -j 4
make install
```

## 编译安装python3.11.11
```
cd /home/data
wget https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tar.xz
tar xf Python-3.11.11.tar.xz
cd Python-3.11.11
./configure --prefix=/usr/local/python3 --with-openssl-rpath=auto --with-openssl=/usr/include/openssl OPENSSL_LDFLAGS=-L/usr/include/openssl  OPENSSL_LIBS=-l/usr/include/openssl/ssl OPENSSL_INCLUDES=-I/usr/include/openssl --enable-shared
make -j 4
make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
echo "/usr/local/python3/lib/" | sudo tee -a /etc/ld.so.conf
sudo ldconfig
# 或者 cp libpython3.11.so, libpython3.11.so.1.0 /usr/lib64/
```

## 创建虚拟环境
```
cd /home/jobs/archive/
python3 -m venv venv
ln -s /home/jobs/archive/venv/bin/activate /home/jobs/activate
source /home/jobs/activate
```

## 以PG本地包同步脚本为例
[上传pg包同步脚本到/home/jobs/PG](https://github.com/fish2018/lib/tree/main/教程/deploy/home/jobs/PG)  
```
cd /home/jobs/PG
pip3 install -r requirements.txt

/home/jobs/PG/p目录下是解压后的pg包，用于提供在线接口
```

## 以真心本地包同步脚本为例

[传到真心包同步脚本到/home/jobs/ZX](https://github.com/fish2018/lib/tree/main/教程/deploy/home/jobs/ZX)
```
cd /home/jobs/ZX
pip3 install -r requirements.txt

/home/jobs/ZX/z目录下是解压后的真心包，用于提供在线接口
```

## 部署supervisor(tgsearch、tgsou进程管理/保活)
[使用rz命令或sftp上传tgsearch、tgsou到/home/work/](https://github.com/fish2018/lib/tree/main/教程/deploy/home/work)

先手动启动tgsearch、tgsou获取session，或者通过https://tg.uu8.pro/在线获取   

安装supervisor
```
/usr/local/python3/bin/python3.11 -m pip install --upgrade pip
pip3 install supervisor
mkdir -p /etc/supervisor/conf.d
```
[上传配置文件](https://github.com/fish2018/lib/tree/main/教程/deploy/etc/supervisor)    
需要修改tgsearch.conf中的session为自己的
```
/etc/supervisor/supervisor.conf 
/etc/supervisor/conf.d/tgsearch.conf 
/etc/supervisor/conf.d/tgsou.conf
```
启动服务
```
supervisorctl start all
```

## TG影视资源转发脚本
[上传脚本到/home/jobs/TGForwarder](https://github.com/fish2018/lib/tree/main/教程/deploy/home/jobs/TGForwarder) ,最新脚本参考项目[TGForwarder](https://github.com/fish2018/TGForwarder)  
```
cd /home/jobs/TGForwarder
pip3 install -r requirements.txt
```

## 添加定时任务
crontab -e
```
0 * * * * /home/jobs/TGForwarder/tgforward.sh
*/10 * * * * /home/jobs/PG/sync-pg.sh
*/13 * * * * /home/jobs/ZX/sync-zx.sh
*/50 * * * * supervisorctl restart tg
```

## 配置nginx
安装nginx
```
yum -y install epel-release
yum -y install nginx
```
[上传配置文件](https://github.com/fish2018/lib/tree/main/教程/deploy/etc/nginx)
```
/etc/nginx/nginx.conf
/etc/nginx/conf.d/tgsearch.conf
/etc/nginx/conf.d/tgsou.conf
/etc/nginx/conf.d/fish2018.conf
```
启动服务
```
service nginx start
```
