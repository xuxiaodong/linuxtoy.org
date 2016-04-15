Title: 利用 PPTP Client 连接 YTVPN
Date: 2016-04-15 10:04:29
Authors: toy
Category: Tips
Tags: pptp, vpn
Slug: pptpclient

最近在单位用得好好的翻墙代理因为机房搬迁也没法用了，不得已只好上付费 VPN。虽然 YTVPN 支持 PPTP 和 L2TP 协议，不过为了简单省事能够快速先用起来，这里选择使用 PPTP Client 通过 PPTP 协议来连接 VPN。

<!-- PELICAN_END_SUMMARY -->

**安装 PPTP Client**

PPTP Client 在各大 Linux 发行版的软件包仓库中应该都有收录，不过包名并不一样：

```
pacman -S pptpclient       # Arch Linux
emerge -av pptpclient      # Gentoo
apt-get install pptp-linux # Debian/Ubuntu
yum install pptp pptpsetup # Fedora/CentOS
```

**创建 VPN 连接**

通过 `pptpsetup` 这个 Perl 脚本可以快速创建一个 VPN 连接：

```
pptpsetup --create ytvpn --server <vpn 域名或 IP> --username <帐号> --password <密码> --encrypt
```

将 `<>` 替换成实际的值。该命令创建了名为 ytvpn 的连接，将以文本文件形式存储到 `/etc/ppp/peers/ytvpn` 目录，稍后可以再进行修改。同时，帐号及密码信息会保存到 `/etc/ppp/chap-secrets` 文件。

**配置 PPTP 选项**

打开 `/etc/ppp/options.pptp` 文件，将下面所在行前的注释去掉：

```
require-mppe-128
```

亦即开启 MPPE 功能，其它使用默认选项即可。

**添加路由**

在 `/etc/ppp/ip-up.d` 下添加一个路由脚本 `01-routes.sh`，其内容如下：

```bash
#!/bin/bash

# This script is called with the following arguments:
# Arg Name
# $1 Interface name
# $2 The tty
# $3 The link speed
# $4 Local IP number
# $5 Peer IP number
# $6 Optional ``ipparam'' value foo

ip route add default via $4
```

这样当连接时就会自动添加一条全局路由，将所有流量路由到 VPN 连接。

**连接 VPN**

首次连接可以执行 `pon ytvpn debug dump logfd 2 nodetach`，输出的调试信息方便排错。如果确认无误，那么直接运行 `pon ytvpn` 即可。

要断开连接，则可以执行 `poff ytvpn`。

**参考**

* [PPTP Client 官网](http://pptpclient.sourceforge.net/)
* [Arch Linux Wiki](https://wiki.archlinux.org/index.php/PPTP_Client)

P.S. 如果你对 YTVPN 感兴趣，不妨考虑使用我的[推荐链接][l]，这样你可以获得一些优惠。

[l]: http://speedtz.com/?r=34b1f3fe30f7dce9
