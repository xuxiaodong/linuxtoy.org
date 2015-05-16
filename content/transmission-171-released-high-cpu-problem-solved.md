Title: Transmission 1.71 发布，高 CPU 占有率问题解决
Date: 2009-06-14 22:11
Author: lovenemesis
Category: BitTorrent Client
Tags: Transmission
Slug: transmission-171-released-high-cpu-problem-solved

近日， Transmission 发布了 1.7 系列的首个修订版 1.71，针对 1.70 引入的
DHT 支持做了修正，显著降低了 CPU 占有率。

主要更新：

-   修正 1.70 在 high-peer 群中 CPU 占有率偏高的 Bug；
-   修正 DHT 和 libevent 在 1.70 中的 Bug。

[英文官方网站及完整更新日志](http://www.transmissionbt.com/)

[源代码下载](http://mirrors.m0k.org/transmission/files/transmission-1.71.tar.bz2)

[Fedora 11 i586平台 RPM
下载](http://files.getdropbox.com/u/464139/Transmission/transmission-1.71-1.fc11.i386.rpm)

[Fedora 系 SRPM
下载](http://files.getdropbox.com/u/464139/Transmission/transmission-1.71-1.fc11.src.rpm)

**PS:**

晚了这么几天才公布是因为要编译以上的 RPM，见谅～  
1.70 版本的 DHT CPU 占有率高到不可用，该版本改善很多。
根据搜集的信息来看 DHT 的 UDP 端口号与就是对应 TCP 端口的一致。
