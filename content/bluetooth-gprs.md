Title: Linux 下通过蓝牙连手机 GPRS 拨号上网
Date: 2009-10-29 10:46
Author: hmy
Category: Tips
Slug: bluetooth-gprs

现在的智能手机一般都有“猫”的功能。因此可以把你的手机当做一个无线猫来用。  
如果你的手机开通了 GPRS
流量包月，那么你拨号上网的流量也是算在这个里面的。  
因此还是很不错，上海 5 元包月有 30M 流量。

我是通过蓝牙连接手机，然后利用 PPP 拨号。手机是 Blackberry  
8820，操作系统是 Debian Etch。笔记本是 Lenovo r61i。  
说一下设置的要点。

首先在 Debian 里面安装 bluez-utils 和 pppoe 软件，  
然后在硬件上打开你的蓝牙（一般笔记本有开关）。  
启动 `/etc/init.d/buletooth` 服务，  
运行 `hciconfig` 命令，看看是否找到了蓝牙设备。

打开手机的蓝牙，然后在电脑上执行 `hcitool scan`  
命令，搜索你的手机，看看手机的蓝牙的 Mac
地址是多少。然后记下这个地址。配置到  
/etc/bluetooth/rfcomm.conf 文件里面。重启电脑的蓝牙服务。

然后是配置 PPP 拨号。  
在 /etc/ppp/peers 里面建立文件 gprs，内容如下：

/dev/rfcomm0 115200

connect '/usr/sbin/chat -v -f /etc/ppp/peers/chat-gprs'  
crtscts  
modem -detach  
noccp  
defaultroute  
usepeerdns  
noauth  
ipcp-accept-remote  
ipcp-accept-local  
noipdefault

建立 /etc/ppp/peers/chat-gprs 文件，内容如下：

'' ATZ OK  
AT+CGDCONT=1,"IP","cmnet"  
OK "ATD*99***1#"  
CONNECT ''

建立好以后，执行 `pon gprs` 就能连上网络了。  
时间比较仓促，没精力慢慢写一个详细教程，有兴趣的人可以看看  

[这里](http://www.howtoforge.com/linux\_internet\_access\_gprs\_edge\_via\_bluetooth\_gsm\_phone)，  
有什么问题可以留言里面讨论。
