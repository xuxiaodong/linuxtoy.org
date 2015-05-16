Title: 如何在 Fedora 上使用 BOINC
Date: 2009-04-20 23:09
Author: lovenemesis
Category: Featured, News
Tags: boinc, Fedora
Slug: how-to-install-boinc-on-fedora

[BOINC](http://boinc.berkeley.edu/)
是由伯克利大学主导的开源跨平台分布式计算平台。借助它，个人用户可以将自己计算机空闲时间贡献给有意义的科学运算，为全人类的进步做出一份努力。本文将介绍如何在
Fedora 系统上安装并配置 BOINC 。

全文以 Fedora 10 i386 为例，大量参考了 [BOINC
维基](http://boinc.berkeley.edu/wiki/Installing_BOINC_on_Fedora)上提供的信息。

*安装*  
目前 BOINC 已经被收录进 Fedora 7 以后的官方软件仓库中，可以方便的使用
yum 安装。

`su -c 'yum install boinc-client boinc-manager'`

安装完之后会创建一个 boinc 用户组和一个 boinc-client
服务。所有项目相关内容被存放在 /var/lib/boinc 目录下。  
其中 boinc-client 是协调所有 boinc-client 的管理程序， boinc-manager
是它的图形化管理前端。

*配置*  
出于安全方面的考虑，只有 root 用户才可以访问 boinc
的管理目录。个人用户还需要一些设置才能在日常使用的帐户下使用
boinc-manager 管理 BOINC 项目。  
**假设常用用户名为 username，用您的实际用户名替换掉 username。**

首先，需要将自身添加进 boinc 用户组。

`su -c '/usr/sbin/usermod -G boinc -a username'`

接下来，赋予 boinc 对于 /var/lib/boinc 目录的访问权限。

`su -c 'chmod g+rw /var/lib/boinc'`

`su -c 'chmod g+rw /var/lib/boinc/*.*'`

在常用用户主目录下创建指向 /var/lib/boinc 下认证文件的符号链接

`su -c 'ln -s /var/lib/boinc/gui_rpc_auth.cfg /home/username/gui_rpc_auth.cfg'`

改变该符号链接的所有者

`su -c 'chown boinc:boinc /home/username/gui_rpc_auth.cfg'`

完成以上所有工作后，**需要注销并重新登录**才可生效。

*使用*  
使用“系统”-“管理”-“服务”，点击选择"boinc-client"，使用“开始”启动
boinc-client 服务，之后就可以在“应用程序”-“系统工具”中使用“BOINC
Manager” 管理 BOINC 项目了。若要想以后开机时自动启动 boinc
服务的话点击“启用”即可。

首先从 BOINC
官方网站上寻找中意的分布式计算项目，目前主要以天文和医学的居多，复制下有意加入的项目网址，然后使用
BOINC Manager
“工具”菜单中的“加入项目”，填入项目网址即可。如果是首次使用的话，依照提示创建一个帐号即可。  
强烈建议之后使用创建的帐号访问网页并加入 Team China
组，向世界显示华人的力量～

“高级”菜单中的“本地参数设置”也是一个值得调整的地方。在这里可以配置 BOINC
对于处理器、内存和硬盘的使用情况。  
强烈建议使用本本的用户在“处理器使用”的“其他选项”中将“最多使用 CPU
时间调整”为
50.00%，可以有效避免本本过热的情况。**如果看不见该选项的话，需要用鼠标在该对话框稍微扩大些。**

*使用 CUDA 加速计算*  
如果您使用的显卡为 nVidia Geforce 8 系列及以后并具有**至少 256 M
独立显存**的话，还可以在 SETI@HOME 和 GPUGRID（仅限64位 Linux）中通过
CUDA 使用 GPU 加速计算。

下面简述使用 CUDA 要点：

1. 首先要具有 libcudart.so 运行库。**rpmfusion 打包的 nVidia
驱动中并不包含**，需要单独下载 CUDA ，可以从 [nVidia CUDA
官网](http://www.nvidia.cn/object/cuda_home_cn.html)找到。使用 nVidia
官方安装包的已经默认安装，无需单独下载 CUDA 了。

2. 使用 locate libcudart.so 命令找到 libcudart.so
的位置，然后创建一个符号链接到 /var/lib/boinc 目录下。

3. 赋予 /dev/nvidia0 和 /dev/nvidiactl 其他用户访问权限，用

`su -c 'chown o+rw /dev/nvidia0'`

`su -c 'chown o+rw /dev/nvidiactl'`

4. 在“系统”-“管理”-“服务”中重启 "boinc-client" 服务。

如果一切正常的话，那么在 BOINC Manager 的“消息”标签页中就可以看到
Coprocessors 的信息了。

*个人感受*  
本人算是 BOINC 的老用户了，但是自从主计算机变为 12
寸的本本后由于散热问题就很少参与了。尽管设置 CPU 时间为 50%
热量大为减少，但是要在限定的时间内上报计算，对于我的 Turion 64 X2 TL-58
有些难度。而自己的 GeForce 8400M G 只有 128 M 独立显存，CUDA
也用不成。所以， BOINC 还是交给有强力独立显卡或多核 CPU 的台式机用户吧～
