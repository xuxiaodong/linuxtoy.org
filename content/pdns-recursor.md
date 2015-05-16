Title: pdns-recursor：dns 解析器
Date: 2008-08-23 17:31
Author: hmy
Category: Apps
Tags: DNS, pdns-recursor
Slug: pdns-recursor

[撰文/hmy]

pdns-recursor 是一个 dns 解析器（recursor），是 debian 从 powerdns
里面单独编译出来的只做 dns 解析器应用的软件。

powerdns 本身是一个支持 mysql 数据库的 dns 服务器。

很多人应该都习惯了设置 isp 提供的 dns
服务器，然后忍受被劫持域名的搔扰，查不到内容就给你整到 114
页面（上海电信 dns），其实 linux 用户完全不必受这个气，自己装一个 dns
解析器就行了。优点是安全，不用受 dns 劫持，不用怕最新的 dns
安全漏洞，完全没有任何缺点。唯一的缺点可能就是多耗你几 M 内存而已。

再加上最近发现的 dns 协议漏洞，打过补丁的 bind 甚至还有问题，所以推荐用
pdns-recursor，powerdns 官方早就预防了这个问题。可以参考 powerdns
官方的文档。

pdns-recursor 跑起来以后，记的把 dns 地址改到
127.0.0.1，反正就是你监听到那个 ip，就修改你的 dns 到那个 ip。

使用 pppoe 联网一般会自动修改 dns，可以禁止自动修改 dns 就行。

**更新**

以 Ubuntu/Debian 为例，要安装
pdns-recursor，只需简单的执行下列命令即可：

`sudo apt-get install pdns-recursor`

注意，没有 pdns-recursor 的 Linux 发行版，可以安装 Bind 这个软件包。

然后在 /etc/resolv.conf 开头加一行：

`nameserver 127.0.0.1`

或者点 Ubuntu 桌面右上角网络图标，选“手动配置 → 解锁 → DNS”添
127.0.0.1。

[感谢雪梨朋友补充]
