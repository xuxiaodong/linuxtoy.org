Title: 远程无人职守安装?
Date: 2010-03-31 08:51
Author: toy
Category: AskLinuxtoy
Slug: remote-install

fcicq 写道：

给一台只能用 ssh 登录的机器换系统，网速允许网络安装。网络环境可能是静态
IP 或者 DHCP。  
比如从 RHEL 4 换 Ubuntu Server (karmic)，怎么做比较好？

假设原系统在 /dev/hda1, 把新系统装到 /dev/sda2
(实际是同一块硬盘。为什么是 sda？因为 ATA 支持在较新的核心中被标为
DEPRECATED)

事实上最令人担心的就是重启的成败，光凭运气装系统总不是好事情。
