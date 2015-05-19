Title: Sysdig: 系统故障排查利器
Date: 2015-01-15 11:36
Author: toy
Category: Apps
Slug: sysdig

[Sysdig][s] 在操作系统层面进行监听，并将系统调用及系统事件等系统活动捕获下来，这使得它看起来极像面向系统的 tcpdump 或 Wireshark。如果你打算对系统中的异常故障进行排查，那么 Sysdig 将成为你解决问题得心应手的利器。

在 Linux 上，可使用以下命令来安装 Sysdig：

    :::bash
    curl -s https://s3.amazonaws.com/download.draios.com/stable/install-sysdig | sudo bash

这将把 Sysdig 安装到 rpm 或 deb 系的 Linux 系统。

**捕获系统活动**

实时捕获，结果打印到标准输出：

    :::bash
    sysdig

将捕获结果保存到文件 system.scap，方便稍后分析：

    :::bash
    sysdig -w system.scap

捕获指定的事件数 200 并保存到文件：

    :::bash
    sysdig -n 200 -w system.scap

读取已捕获的文件：

    :::bash
    sysdig -r system.scap

**捕获结果解释**

    :::bash
    (1) (2) (3) (4) (5) (6) (7) (8)  
    1 10:54:50.462463956 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    2 10:54:50.462603110 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    3 10:54:50.462729565 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    4 10:54:50.462859521 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    5 10:54:50.463206317 0 sysdig (29043) > switch next=0 pgft_maj=0
    pgft_min=1790 vm_size=35748 vm_rss=7164 vm_swap=0  
    6 10:54:50.464246835 0 (0) > switch next=7 pgft_maj=0 pgft_min=0
    vm_size=0 vm_rss=0 vm_swap=0  
    7 10:54:50.464249707 2 (0) > switch next=8374 pgft_maj=0 pgft_min=0
    vm_size=0 vm_rss=0 vm_swap=0  
    8 10:54:50.464255940 0 (7) > switch next=0 pgft_maj=0 pgft_min=0
    vm_size=0 vm_rss=0 vm_swap=0  
    9 10:54:50.464264256 2 (8374) > switch next=0 pgft_maj=0 pgft_min=0
    vm_size=0 vm_rss=0 vm_swap=0  
    10 10:54:50.464358113 2 (0) > switch next=854(mlnet) pgft_maj=0
    pgft_min=0 vm_size=0 vm_rss=0 vm_swap=0  
    11 10:54:50.464370099 2 mlnet (854) < poll res=0 fds=  
    12 10:54:50.464378193 2 mlnet (854) > poll fds= timeout=5  
    13 10:54:50.464385400 2 mlnet (854) > switch next=0 pgft_maj=216
    pgft_min=3386 vm_size=162608 vm_rss=12196 vm_swap=2716  
    14 10:54:50.464950541 0 (0) > switch next=1105(memcached) pgft_maj=0
    pgft_min=0 vm_size=0 vm_rss=0 vm_swap=0  
    15 10:54:50.464954692 0 memcached (1105) < epoll_wait res=0  
    16 10:54:50.464976007 0 memcached (1105) > epoll_wait maxevents=32  
    17 10:54:50.464984030 0 memcached (1105) > switch next=0 pgft_maj=3
    pgft_min=247 vm_size=327412 vm_rss=1860 vm_swap=468  
    18 10:54:50.465256687 2 (0) > switch next=2181(plugin-containe)
    pgft_maj=0 pgft_min=0 vm_size=0 vm_rss=0 vm_swap=0  
    19 10:54:50.465261465 2 plugin-containe (2181) < poll res=0 fds=  
    20 10:54:50.465297692 2 plugin-containe (2181) > getrlimit
    resource=3(RLIMIT_STACK)

通过 Sysdig 捕获的结果如上所示，每列的意思分别为：

1. 事件编号  
2. 时间戳  
3. CPU 编号  
4. 进程名  
5. 线程 ID  
6. 事件方向，> 为进入事件，< 为退出事件  
7. 事件类型，比如 open、read 等  
8. 事件参数列表

**过滤捕获结果**

在默认情况下，Sysdig 捕获的信息非常多，要从中找到我们感兴趣的信息，这就需要类似 grep 的过滤功能。

按字段类别进行过滤：

    :::bash
    sysdig -r system.scap proc.name=sysdig

这条命令过滤出进程名为 sysdig 的系统事件，结果为：

    :::bash
    1 10:54:50.462463956 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    2 10:54:50.462603110 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    3 10:54:50.462729565 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    4 10:54:50.462859521 0 sysdig (29043) > sysdigevent event_type=1
    event_data=0  
    5 10:54:50.463206317 0 sysdig (29043) > switch next=0 pgft_maj=0
    pgft_min=1790 vm_size=35748 vm_rss=7164 vm_swap=0

Sysdig 提供包括 fd、process、evt、user、group、syslog 等字段类别，可通过 `sysdig -l` 查询。

除 = 外，Sysdig 的过滤表达式还支持 g=、<、<=、>、>= 及 contains 等比较操作符。

同时，也可以使用 and、or、not 等布尔操作符。例如：

    :::bash
    sysdig -r system.scap proc.name=sysdig and evt.type=switch

**Chisels**

在 Sysdig 中，chisels 是通过 Lua 编写的脚本，可以用来扩展 Sysdig 的过滤功能。

比如我们想看读写磁盘文件最频繁的进程，可以使用 topprocs_file 这个 chisels：

    :::bash
    sysdig -c topprocs_file

结果为：

    :::bash
    Bytes Process  
    ------------------------------  
    448.36KB mozStorage  
    220.38KB perl  
    1.69KB tmux  
    1.62KB sh  
    1.59KB Xorg  
    1.30KB urxvtd

更多 chisels，可通过 `sysdig -cl` 了解。当然，如果你熟悉 Lua，那么也可以编写自己的 chisels。

[s]: http://www.sysdig.org
