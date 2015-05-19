Title: ThinkPad X201i 安装 Debian 7.5 杂记
Date: 2014-07-13 12:45
Author: toy
Category: Tips
Slug: installing-debian-7-5-on-thinkpad-x201i

从公司领了一台 ThinkPad X201i，遂为其安装 Debian 7.5。选择的是 netinst 安装 ISO，本想着安装镜像小巧，且通过优盘亦很方便。没想到一下子掉到两个坑里。

其一是，如果选择图形化方式，安装程序会检测光驱，而由于这台笔记本并没有光驱，所以导致安装程序通不过检测，不能继续进行安装。解决方法是选择文本模式进行安装，即可以规避此问题。

其二是这个 netinst 安装镜像中并不带这台笔记本的 WiFi 模块固件，再加上周围环境不允许网线接入，所以在安装过程中不能联网。好在安装仍然可以继续，这里就依常规的步骤安装完毕即可。

接下来详细谈谈如何为这台 X201i 安装 WiFi 模块固件及联网工具。在其他能联网的机器上，转到 页面，下载以下 deb 包：

* firmware-iwlwifi：WiFi 模块固件，从安装出错提示中获悉  
* wireless-tools 及其依赖：无线工具集  
* wpasupplicant 及其依赖：无线联网工具

在安装好这些包之后，并在 `/etc/network/interfaces` 中加入如下内容：

    :::bash
    auto wlan0  
    iface wlan0 inet dhcp  
    wpa-ssid  
    wpa-psk

保存后，再执行：

    :::bash
    ifup wlan0

即可正常连接无线网络了。
