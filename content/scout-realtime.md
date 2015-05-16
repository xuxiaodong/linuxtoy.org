Title: Scout Realtime: 实时监视服务器资源
Date: 2014-03-18 14:44
Author: toy
Category: Apps
Slug: scout-realtime

[Scout Realtime][s] 是由 Scout 所开发的一个实时服务器度量工具，  
通过它，你可以直接在网络浏览器中观察到服务器资源的实时变化情况，  
包括 CPU 和内存的占用率、磁盘的利用率、网络流量、以及 top 进程  
等重要信息。Realtime 使用曲线图来加以展示，看起来非常直观。

[![Realtime](/img/2014/03/realtime-thumb.png)](/img/2014/03/realtime.png)

在通过 `gem install scout\_realtime` 安装 Realtime 后，可以执行  
以下命令来启动它：

scout\_realtime start

然后，在浏览器中打开 `http://:5555` 便可以访问  
并看到结果了。

[s]: https://github.com/scoutapp/scout\_realtime
