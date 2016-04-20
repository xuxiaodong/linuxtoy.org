Title: 基于 OpenWrt 路由器和 SSH 的终极翻墙解决方案
Date: 2010-04-30 20:51
Author: ivan_wl
Category: Tips
Tags: OpenWrt, SSH
Slug: openwrt-and-ssh

这次我们的目标是来打造一台带有自动翻墙功能的路由器！

<!-- PELICAN_END_SUMMARY -->

当然，天上是不会掉馅饼的，为了打造这么一台自动翻墙路由器，还是需要一些条件的。

首先就是一台支持 OpenWrt 的路由器。淘宝上有卖的，刷好 OpenWrt 的带 USB 接口的无线路由，最便宜的也就 100 元左右。

其次就是要有一台 SSH 主机，不解释～

首先简单介绍一下 OpenWrt。OpenWrt 是一个基于 Linux 的开源路由固件。因为是开源而且基于 Linux 的，所以可定制性极强。OpenWrt 有类似软件源的东西，里面有很多已经编译好的软件包，包括 Transmission 和 aMule 等。而且有自己的开发环境，我就在 OpenWrt 上编译了校园网锐捷认证的客户端。所以如果你是牛人的话，理论上在 OpenWrt 上编译个 Tor 来翻墙也是完全可以的。

最新的 OpenWrt 固件可以使用 LUCI 网页管理界面，而且支持中文，非常方便。设置路由的过程我就不多说了，就建议大家更改一下 root 用户的密码。改过后，就可以用 SSH 登录路由器来进行管理了。

对于路由器的文件管理，可以使用任意一款的 FTP 客户端。用 root 用户和密码登录即可。如果你是使用 Linux/GNOME 的话，使用 Nautilus 文件管理器当然是最方便的了！直接就可以像操作本地文件一样来操作路由器中的文件。只需在文件管理器中选择文件 - 连接到服务器 即可。

由于 OpenWrt 中默认自带的 SSH 服务/客户端是 Dropbear，Dropbear 作为 SSH 客户端无法满足我们的需要，所以我们要安装 openssh-client。首先到路由器的文件系统中 /usr/bin 目录下，删除 ssh 和 scp。其实这两个文件都是到 Dropbear 的符号链接，所以放心删除。

然后我们打开终端，通过 ssh 登录路由器。一般情况下，就是

    ssh 192.168.1.1 -l root

登录后，先用

    opkg update

刷新一下软件包。（老版本的 OpenWrt 可能是使用 ipkg 来管理软件包，这点我也不太清楚）

然后安装一些需要的包

    opkg install openssh-client autossh

我们使用 OpenSSH 来登录主机并做端口转发，使用 Autossh 来自动管理 SSH 连接。

由于 OpenSSH 只支持 SOCKS 代理，如果需要 HTTP 代理的话，我们还要安装 Polipo

    opkg install polipo

安装完之后，我们首先要做的就是设置 SSH 的密钥，这样就可以自动登录，而不用输入密码。我是参照[这篇文章](http://www.fwolf.com/blog/post/279)来做的。

简单的说，就是几步。首先在自己的电脑上，用 sh-keygen 来生成密钥对。比如

    ssh-keygen -b 1024 -t rsa

会在 `~/.ssh` 文件夹下生成 id\_rsa 和 id\_rsa.pub 两个文件。然后把 id\_rsa.pub 公钥上传到 SSH 服务器 ~/.ssh/ 文件夹下，改名为 authorized\_keys，把 id\_rsa 私钥复制到路由器中 /root/.ssh 文件夹下。具体操作参见前面那篇文章，或者自行谷歌。然后我们 SSH 登录路由器，在路由的 SSH 中再用 ssh 命令登录下你的 SSH 服务器（这个有点绕～），看看是不是不用再输入密码了？如果提示你有关权限问题的话，可能还需要改下 id\_rsa 文件的属性。

    chmod -rw------- /root/.ssh/id_rsa

接下来我们用 Autossh 来试一下

    autossh -M20000 -f -q -N -D 192.168.1.1:[代理端口] [用户名@你的主机地址]

打开火狐，设置 SOCKS 代理为 192.168.1.1 和上面设置的端口，如果有 Autoproxy 就更方便了。试一下，墙是不是已经透明了？

接下来我们让路由器开机时自动运行代理。

在路由器 /etc/init.d/ 文件夹下，我们建立个文本文件，比如叫 iautossh，编辑其中的内容

```sh
#!/bin/sh /etc/rc.common  
# Copyright (C) 2007 OpenWrt.org  
START=99

start() {  
    autossh -M20000 -f -q -N -D 192.168.1.1:[代理端口] [用户名@你的主机地址]  
}

stop() {  
    killall autossh  
}
```

保存，加上执行属性

    chmod +x /etc/init.d/iautossh

然后使用命令

    /etc/init.d/iautossh enable

即可加入开机自动运行了！

因为很多的时候，我们更需要 HTTP 代理，所以接下来我们来配置 Polipo。如果你不需要 HTTP 代理，就忽略吧。

Polipo 的配置文件是 /etc/polipo/polipo，主要需要配置的就是 "proxyAddress = "0.0.0.0"、proxyPort = [你可以自己设置一个端口]" 和 "socksParentProxy = "192.168.1.1:[前面设置的ssh代理端口]"、socksProxyType = socks5"。

下面是我的 Polipo 配置文件，大家可以参考下

```
### Basic configuration  
### *******************

# Uncomment one of these if you want to allow remote clients to  
# connect:

# proxyAddress = "::0" # both IPv4 and IPv6  
# proxyAddress = "0.0.0.0" # IPv4 only

proxyAddress = "0.0.0.0"  
proxyPort = 8118

# If you do that, you'll want to restrict the set of hosts allowed to  
# connect:

# allowedClients = "127.0.0.1, 134.157.168.57"  
# allowedClients = "127.0.0.1, 134.157.168.0/24"

# Uncomment this if you want your Polipo to identify itself by  
# something else than the host name:

proxyName = "localhost"

# Uncomment this if there's only one user using this instance of
Polipo:

cacheIsShared = false

# Uncomment this if you want to use a parent proxy:

# parentProxy = "squid.example.org:3128"

# Uncomment this if you want to use a parent SOCKS proxy:

socksParentProxy = "192.168.1.1:9050"  
socksProxyType = socks5

### Memory  
### ******

# Uncomment this if you want Polipo to use a ridiculously small amount  
# of memory (a hundred C-64 worth or so):

# chunkHighMark = 819200  
# objectHighMark = 128

# Uncomment this if you've got plenty of memory:

# chunkHighMark = 50331648  
# objectHighMark = 16384

chunkHighMark = 33554432

### On-disk data  
### ************

# Uncomment this if you want to disable the on-disk cache:

diskCacheRoot = ""

# Uncomment this if you want to put the on-disk cache in a  
# non-standard location:

# diskCacheRoot = "~/.polipo-cache/"

# Uncomment this if you want to disable the local web server:

localDocumentRoot = ""

# Uncomment this if you want to enable the pages under /polipo/index?  
# and /polipo/servers?. This is a serious privacy leak if your proxy  
# is shared.

# disableIndexing = false  
# disableServersList = false

disableLocalInterface = true  
disableConfiguration = true

### Domain Name System  
### ******************

# Uncomment this if you want to contact IPv4 hosts only (and make DNS  
# queries somewhat faster):  
#  
# dnsQueryIPv6 = no

# Uncomment this if you want Polipo to prefer IPv4 to IPv6 for  
# double-stack hosts:  
#  
# dnsQueryIPv6 = reluctantly

# Uncomment this to disable Polipo's DNS resolver and use the system's  
# default resolver instead. If you do that, Polipo will freeze during  
# every DNS query:

dnsUseGethostbyname = yes

### HTTP  
### ****

# Uncomment this if you want to enable detection of proxy loops.  
# This will cause your hostname (or whatever you put into proxyName  
# above) to be included in every request:

disableVia = true

# Uncomment this if you want to slightly reduce the amount of  
# information that you leak about yourself:

# censoredHeaders = from, accept-language  
# censorReferer = maybe

censoredHeaders = from,accept-language,x-pad,link  
censorReferer = maybe

# Uncomment this if you're paranoid. This will break a lot of sites,  
# though:

# censoredHeaders = set-cookie, cookie, cookie2, from, accept-language  
# censorReferer = true

# Uncomment this if you want to use Poor Man's Multiplexing; increase  
# the sizes if you're on a fast line. They should each amount to a
few  
# seconds' worth of transfer; if pmmSize is small, you'll want  
# pmmFirstSize to be larger.

# Note that PMM is somewhat unreliable.

# pmmFirstSize = 16384  
# pmmSize = 8192

# Uncomment this if your user-agent does something reasonable with  
# Warning headers (most don't):

# relaxTransparency = maybe

# Uncomment this if you never want to revalidate instances for which  
# data is available (this is not a good idea):

# relaxTransparency = yes

# Uncomment this if you have no network:

# proxyOffline = yes

# Uncomment this if you want to avoid revalidating instances with a  
# Vary header (this is not a good idea):

# mindlesslyCacheVary = true

# Suggestions from Incognito configuration  
maxConnectionAge = 5m  
maxConnectionRequests = 120  
serverMaxSlots = 8  
serverSlots = 2  
tunnelAllowedPorts = 1-65535

# run polipo as a daemon  
### ********  
daemonise = true  
# logFile = false
```

同样，我们加入开机自动运行。创建 /etc/init.d/ipolipo，编辑内容

```sh
#!/bin/sh /etc/rc.common  
# Copyright (C) 2007 OpenWrt.org  
START=99

start() {  
    polipo -c '/etc/polipo/polipo'  
}

stop() {  
    killall polipo  
}
```

注意，Polipo 可能无法自动读取配置文件，所以我们用 -c 参数强制指定配置文件来运行。

然后

```
chmod +x /etc/init.d/ipolipo  
/etc/init.d/ipolipo enable
```

大功告成！接下来每次打开路由器，它就会自动连接上 SSH 主机，开放 SOCKS 和 HTTP 代理，这样你所有移动的设备只要连上 WiFi，设置好代理，就可以翻墙了！而且克服了 SSH 超时自动断开的缺点，只要一有连接，Autossh 就会自动连上 SSH 服务器。电脑上如果是火狐配合 Autoproxy，或者使用 Autoproxy2pac，墙就是完全透明的了！怎么样，打造这么一个终极翻墙解决方案，翻墙，你所要做的，仅仅是轻轻按下路由器的开关而已。

PS: 我能憋出这么一篇技术文，真的要感谢国家，感谢 GNU，感谢其他给过我帮助的朋友们。

本文作者：ivan\_wl ( twitter: @ivan\_wl )  投递并授权 [linuxtoy.org](http://linuxtoy.org) 网站发表，欢迎转载，转载请保留作者信息。本文只是对技术问题进行讨论，对于转载敏感主题所造成的任何后果本人不负任何责任。

{ Thanks ivan\_wl. }
