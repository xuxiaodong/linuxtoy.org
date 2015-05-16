Title: KVM 虚拟机故障排除一例
Date: 2010-03-19 19:34
Author: toy
Category: Tips
Tags: KVM
Slug: kvm-issue

{ 撰文/[逸飞](http://www.billdeng.com) }

笔者在部署 KVM  

虚拟机时曾遇到一个奇怪的问题，几经探索之后终于解决，现在写出来跟大家分享一下。

笔者在单位部署了一台服务器，上面运行着几部 KVM
虚拟机，分别执行不同的任务。系统上线之后，需要再增加几部虚拟机。因为当初部署服务器时做了虚拟机备份，所以就复制了一个备份的虚拟机。可是新虚拟机启动之后无法在本地网络上找到新虚拟机的
IP 地址（本地网络采用 DHCP 分配 IP
地址）！因为服务器是远程控制的，当然新虚拟机也就无法使用了。

为了查找原因，笔者把虚拟机复制到本地主机上，用正常方法开启。启动过程及登录都很正常，于是检查网卡状况：

$ ifconfig

可是却只有显示 lo 信息！ 怪了，eth0 呢？只有 lo
当然是没有办法同网络通讯的。于是查找一下启动信息：

$ dmesg | grep eth

发现如下信息：

udev: renamed network interface eth0 to eth1

原来 eth0 已经没有了，被命名为 eth1, 再看网卡配置

$ cat /etc/network/interfaces  
auto eth0  
iface eth0 inet dhcp

至此事情水落石出，原来 KVM 是在启动时传递 mac
参数的，如笔者是用下面命令启动 KVM 虚拟机：

$ sudo kvm -m 256 -hda /data/kvm/mail.img -net
nic,vlan=0,macaddr=52-54-00-12-30-05 -net
tap,vlan=0,ifname=tap5,script=no -boot c -smp 2 -daemonize -nographic &

注意上面的 macaddr=52-54-00-12-30-05，这就是虚拟机启动后的网卡
mac，因为网络内不可以有相同的 mac，所以启动每个虚拟机的 mac
都要改。可是当换了新的 mac
后，虚拟机里的系统就认为换了新网卡，所以系统改变 eth0 为
eth1，而在网卡设置里面却只设置了 eth0， 所以虚拟机启动之后并没有启动新的
eth1 网卡，当然就连不上网络了。原因找到了之后问题的解决也就非常简单:

$ vi /etc/network/interfaces

增加以下内容：

auto eth1  
iface eth1 inet dhcp

再重新启动网络:

$ /etc/init.d/networking restart

至此问题应该就完全解决了。不过有个问题还要注意，如果有多次用不同的 mac
启动虚拟机，可能你的虚拟机里已经有了 eth2， eth3 甚至是 10
都是有可能的，因为你每用一个新的 mac
去启动虚拟机，系统就会增加一个网卡。可以修改下面这个文件：

$ vi /etc/udev/rules.d/70-persistent-net.rules

删除所有的的 ethX 行，重启虚拟机即可。

{ Thanks 逸飞. }
