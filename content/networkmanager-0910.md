Title: NetworkManager 0.9.10 新特性概览
Date: 2014-06-23 10:05
Author: toy
Category: News
Slug: networkmanager-0910

网络管理程序 NetworkManager 即将迎来新的 0.9.10 版本。根据其  
[开发者 Blog][b] 的介绍，该版本为用户带来了大量新增特性和改进。

![NetworkManager](https://linuxtoy.org/img/2014/06/nmtui.png)

* 新增基于 Curses 的用户界面 nmtui  
* 对 nmcli 加入了交互式编辑支持、单命令编辑、详细的帮助、Tab  
补全、及增强的 bash 补全等功能  
* 将 Wi-Fi、WWAN、Bluetooth、ADSL、WiMAX 分割成插件，用户可  
按需安装，且守护程序大小减少到 1MB  
* root 操作不再需要 dbus-daemon 和 PolicyKit，另外，at\\\_console  
D-Bus 权限已被移除  
* 添加 Data Center Bridging (DCB) 和 FibreChannel over Ethernet
(FCoE)  
支持  
* 不再默认监视连接配置文件更改，连接现在能锁定接口名称，新添  
ignore-carrier 选项，利用 dns=none 可以自行管理 /etc/resolv.conf、  
配置文件片断现在可以放到 /etc/NetworkManager/conf.d  
* NetworkManager dispatcher 添加 pre-up 和 pre-down 事件  
* 能识别外部工具对 IP 地址、路由、主从关系的更改  
* 改进了对 routing-only VPN 的支持  
* 对因特网连接共享添加定制 IP 范围支持，加入了 WWAN 自动连接  
支持，等等

对于 NetworkManager 0.9.10 完整的更改细节，可查看其 [NEWS][n]  
文件。有心尝鲜的同学，则可去[下载源码包][d]。

[b]:
http://blogs.gnome.org/dcbw/2014/06/20/well-build-a-dream-house-of-net/  
[n]:
http://cgit.freedesktop.org/NetworkManager/NetworkManager/plain/NEWS?h=nm-0-9-10  
[d]: http://ftp.gnome.org/pub/gnome/sources/NetworkManager/0.9/

{ 感谢 Iven 同学爆料 }
