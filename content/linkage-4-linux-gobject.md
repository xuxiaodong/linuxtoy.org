Title: 使用GObject完全重写的联创上网助手 4 linux
Date: 2010-10-18 10:20
Author: ihipop
Category: Apps
Tags: linkage
Slug: linkage-4-linux-gobject

联创上网助手是江苏高校普遍采用的一款上网客户端，此前虽有矿大版linkage4l和lknnu等分支，但是一直是在矿大版的基础上修修补补，没有改善CPU占用100%，必须root用户运行等问题。  

linkage-4-linux是[黑孩儿](https://www.heiher.info/1883.html)在离线环境下根据自己模拟的联创服务器和矿大版本的协议(lknnu)使用GObject重写的而成的，  

在徐州工业学院测试通过，同时提供GTK和CLI两个分支，采用相同的核心  

![](http://linkage-4-linux.googlecode.com/svn/trunk/sanpshot/linkage-gtk-view.png)

> 考虑各个系统连接网络的方式不同，程序中没有去调用DHCP客户端获取IP地址，由用户手动操作。认证并连接网络的流程大概是这样的。  
>   
>  1. 断开当前网络接口的连接  
>   
>  2. 启动认证管理器运行认证  
>   
>  3. 当提示验证成功时，连接当前网络接口运行获取IP  
>   
>  4. 获取到IP地址，网络连接成功。

deb包下载: <http://code.google.com/p/linkage-4-linux/downloads/list>

常见问题:<http://code.google.com/p/linkage-4-linux/wiki/FAQ>

ubuntu下测试通过！其他平台未测试。  

deb包在安装时候已经自动设置不同用户的权限，此软件可以直接用普通用户身份运行。  

原版仓库：<http://git.heiher.info/linkage-gtk.git>
