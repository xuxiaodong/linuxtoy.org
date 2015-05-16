Title: 用Cpulimit和脚本自动控制CPU使用率
Date: 2010-09-25 19:52
Author: Petty
Category: News
Tags: cpulimit
Slug: cpulimit-2

[Cpulimit](http://cpulimit.sourceforge.net/)
是一款用于控制CPU使用率的工具
（本站之前[介绍](http://linuxtoy.org/archives/cpulimit.html)），这里介绍的是一套用它来自动控制CPU使用率的脚本，原出
[Ubuntu
Forum](http://ubuntuforums.org/showthread.php?t=992706)。它可以用于防止CPU超载，也可以用黑名单/白名单的方法对某些特殊应用放行，对于服务器是一套有用的工具。

首先安装 *cpulimit* 和 *gawk*

`sudo apt-get install cpulimit gawk`

脚本在[此处](http://dl.dropbox.com/u/6864546/cpulimit.tar.gz)下载，其中包含
**cpulimit\_daemon.sh** 和 **cpulimit**
两个文件。可用编辑器修改前者实现自定义配置，如下图：  

![cpulimit-daemon](http://images.maketecheasier.com/2010/09/cpulimit-edit-daemon.png)

红框部分:  
CPU\_LIMIT: 这是每个程序能使用的最大CPU资源。默认值为 20%。

DAEMON\_INTERVAL: 这是脚本检查CPU情况的间隔时间，默认值为3秒。

BLACK\_ PROCESS\_ LIST:
这是指定只监视某些特定进程时用的黑名单。有多个进程的话，可以用 "|"
隔开。 例如， "mysql|firefox|gedit"。

WHITE\_ PROCESSES\_ LIST: 这是指定某些特定进程不用监视时用的白名单。
用法同上。

**注意**: *黑名单和白名单至少要有一个为空白——不能同时使用这两者。*

**安装：**

将 cpulimit\_daemon.sh 文件拷贝至 /usr/bin/ ，并修改其访问权限。

`sudo cp ~/cpulimit/cpulimit_daemon.sh /usr/bin`

` `

`sudo chmod 700 /usr/bin/cpulimit_daemon.sh`

将 cpulimit 文件拷贝至 /etc/init.d/ ，修改其访问权限并使其开机自启动。

`sudo cp ~/cpulimit/cpulimit /etc/init.d/`

`sudo chown root:root /etc/init.d/cpulimit`

`sudo chmod +x /etc/init.d/cpulimit`

` `

`sudo update-rc.d cpulimit defaults`

重启系统，守护进程会自动启动。可以在终端中查看和控制状态：

`sudo service cpulimit status`

检查守护进程是否已启动。 如果没有，用以下命令启动。

`sudo service cpulimit start`

相反可以用以下命令终止：

`sudo service cpulimit stop`

**卸载：**

卸载可参考以下步骤：

1、停止守护进程

`sudo service cpulimit stop` # 会终止 cpulimit 守护进程和一切受
cpulimit 控制的进程。

2、移除开机自启动

`sudo update-rc.d -f cpulimit remove` # 移除符号链接

3、删除自启动脚本

`sudo rm /etc/init.d/cpulimit`

4、删除 cpulimit daemon 文件

`sudo rm /usr/bin/cpulimit_daemon.sh`

5、卸载 cpulimit 程序

`sudo apt-get remove cpulimit`

删除 gawk 与否看情况。

`sudo apt-get remove gawk`

[原文链接](http://maketecheasier.com/limit-cpu-usage-of-any-process-in-linux/2010/09/22)
