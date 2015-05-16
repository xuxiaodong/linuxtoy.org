Title: cpulimit: 限制进程的 CPU 占用率
Date: 2010-02-27 10:23
Author: toy
Category: Apps
Tags: CPU, cpulimit
Slug: cpulimit

cpulimit 是一个简单而有用的小程序，通过它你可以限制一个进程的 CPU  
占用率。如果善加利用，必将成为系统管理员的得力助手。

![cpulimit](http://i.linuxtoy.org/images/2010/02/cpulimit.png)

cpulimit 的用法也很简单，如上图所示，通过 -e
选项指定需控制的进程名（或 -p  
选项指定 pid），-l 选项指定 CPU 的占用百分比即可。这里，我将 Chrome 的
CPU  
占用率限制到 25%。

cpulimit
可从其[项目主页](http://cpulimit.sourceforge.net/)下载，或通过你所用的  
Linux 发行版包管理器安装。
