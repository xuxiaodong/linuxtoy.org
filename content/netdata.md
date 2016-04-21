Title: netdata：实时监视 Linux 系统性能
Date: 2016-04-21 09:54:13
Authors: toy
Category: Apps
Tags: netdata, monitor
Slug: netdata
Via: netdata|https://github.com/firehol/netdata

作为一个 Linux 系统的管理员，为了随时了解系统资源的占用情况，有必要使用专门的系统监视工具。如果你需要对 Linux 系统、应用程序、SNMP 设备进行实时的性能监视，那么 netdata 这个工具将是你的好帮手。

<!-- PELICAN_END_SUMMARY -->

[![netdata]({filename}/images/netdata.thumb.png)]({filename}/images/netdata.png)

netdata 能够监视 CPU、内存、磁盘、网络、进程、应用程序、Apache、NGINX、MySQL、Postfix、Squid 等总计 2000 多项度量指标，并提供可视化的实时显示图表，看起来可谓一目了然。

在安装 netdata 之前，需要先准备好编译依赖：

```
apt-get install zlib1g-dev gcc make git \
    autoconf autogen automake pkg-config           # Debian/Ubuntu
yum install zlib-devel gcc make git autoconf \
    autogen automake pkgconfig                     # CentOS/RHEL
pacman -S --needed base-devel libmnl \
    libnetfilter_acct zlib                         # Arch Linux
```

接着克隆 netdata 的源代码，并执行编译脚本：

```
git clone https://github.com/firehol/netdata.git --depth=1
cd netdata
./netdata-installer.sh
```

一旦编译安装完毕，netdata 将执行 `/usr/sbin/netdata` 启动 daemon 程序，并监听本机的 `19999` 端口。

为了访问 netdata 的 Web Dashboards，在此我们通过 NGINX 配置一个反向代理：

```nginx
upstream backend {
    server 127.0.0.1:19999;
    keepalive 64;
}

server {
    listen 80;
    server_name n.linuxtoy.org;

    location / {
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_pass_request_headers on;
        proxy_set_header Connection "keep-alive";
        proxy_store off;
    }
}
```

重载 NGINX 配置后，就可以通过 <http://n.linuxtoy.org> 访问了。如果你使用其它 Web 服务器，那么参照 [netdata 的 Wiki][w] 了解配置说明即可。

[w]: https://github.com/firehol/netdata/wiki
