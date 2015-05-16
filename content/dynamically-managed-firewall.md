Title: 动态管理防火墙 firewalld
Date: 2011-01-03 22:27
Author: lovenemesis
Category: News
Slug: dynamically-managed-firewall

Firewalld 是一款提供 D-Bus 接口从而**支持动态管理的防火墙守护进程**。

Firewalld 由 Red Hat 的 Thomas Woerner 为 Fedora 开发，在 Fedora 15
中将可以使用（**但不会成为默认！**）测试，目的是取代目前
system-config-firewall 的静态防火墙配置。它的特点是

该守护进程目前具有以下功能：

-   支持绝大多数 system-config-firewall 所具有的功能，除去：
    1.  不支持 iptables
        格式的自定义规则文件，但是提供有限的自定义规则支持。
    2.  ip\_forward 的 sysctl 变动尚未实现。
    3.  暂时不能保存永久性规则配置，意味着一旦服务重启所有配置都将丢失，永久性保存规则将在后续加入。
-   实现动态管理，**对于规则的更改不再需要重新创建整个防火墙**。
-   一个简单的系统托盘区图标来显示防火墙状态，方便开启和关闭防火墙。
-   提供 firewall-cmd 命令行界面进行管理及配置工作。
-   为 libvirt 提供接口及界面，会在必须的 PolicyKit
    相关权限完成的情况下实现。

下一步将实现以下功能：

-   实现 firewall-config 图形化配置工具。
-   实现系统全局及用户进程的防火墙规则配置管理。
-   区域 Zone 的支持。
-   NetworkManager 防火墙规则助手。

[项目主页及详细介绍](https://fedoraproject.org/wiki/FirewallD/)

*消息来源：*[邮件列表](http://lists.fedoraproject.org/pipermail/devel/2010-December/147426.html)
