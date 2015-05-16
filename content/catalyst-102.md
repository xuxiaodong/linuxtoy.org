Title: Catalyst 10.2 发布，加入 Direct2D 加速
Date: 2010-02-18 10:55
Author: toy
Category: Apps
Tags: Catalyst
Slug: catalyst-102

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

AMD 刚刚发布了 Catalyst 10.2 的 Linux 驱动。沮丧的是，Catalyst  
依然没有 X Server 1.7 的支持。

Phoronix 早前确认了 Catalyst 10.2 会有新的 2D 加速架构。但 AMD  
没有透露具体信息。在这次发布中， Catalyst 10.2  
的确做到了这一点。他们使用了 Direct2D。Direct2D 是微软在  
Windows Vista/7 用于 2D 和矢量图形处理的  
API。使用这种加速架构的办法是插入名为 Direct2DAccel  
的键值到存储配置数据库的 DDX 部分。这也是 AMD 第一次把  
Windows 2D 加速代码共享到 Linux 驱动上。Direct2D  
加速属于试验性质，当加速稳定以后，就会变成默认选项。AMD  
用这种办法改进 2D 加速的确令人感到奇怪。

另外，Phoronix 已经收到报告指出使用 KDE4 的 KWin  
依然会存在问题。

AMD 暂时还没有宣布发布 Catalyst  
10.2，因此还没有发行公告，但是下载链接已经提供。

Catalyst 10.2  

下载地址：[ati-driver-installer-10-2-x86.x86\_64.run](https://a248.e.akamai.net/f/674/9206/0/www2.ati.com/drivers/linux/ati-driver-installer-10-2-x86.x86\_64.run)

{ Thanks liangsuilong. }
