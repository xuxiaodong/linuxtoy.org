Title: SELinux 入门
Date: 2011-05-31 13:41
Author: lovenemesis
Category: Featured, Security
Tags: selinux
Slug: selinux-introduction

几乎可以肯定每个人都听说过 SELinux
(更准确的说，尝试关闭过)，甚至某些过往的经验让您对 SELinux
产生了偏见。不过随着日益增长的 0-day
安全漏洞，或许现在是时候去了解下这个在 Linux
内核中已经有8年历史的强制性访问控制系统(MAC)了。

**SELinux 与强制访问控制系统**

SELinux 全称 Security Enhanced Linux (安全强化 Linux)，是 MAC (Mandatory
Access
Control，强制访问控制系统)的一个实现，目的在于**明确的指明某个进程可以访问哪些资源(文件、网络端口等)**。

强制访问控制系统的用途在于**增强系统抵御 0-Day
攻击(利用尚未公开的漏洞实现的攻击行为)的能力**。所以**它不是网络防火墙或
ACL 的替代品，在用途上也不重复**。

举例来说，系统上的 Apache
被发现存在一个漏洞，使得某远程用户可以访问系统上的敏感文件(比如
`/etc/passwd` 来获得系统已存在用户)，而修复该安全漏洞的 Apache
更新补丁尚未释出。此时 **SELinux 可以起到弥补该漏洞的缓和方案**。因为
/etc/passwd 不具有 Apache 的访问标签，所以 Apache 对于 `/etc/passwd`
的访问会被 SELinux 阻止。

相比其他强制性访问控制系统，SELinux 有如下优势：

-   控制策略是可查询而非程序不可见的。
-   可以**热更改策略**而无需重启或者停止服务。
-   可以从进程初始化、继承和程序执行三个方面通过策略进行控制。
-   控制范围**覆盖文件系统、目录、文件、文件启动描述符、端口、消息接口和网络接口**。

那么 SELinux 对于系统性能有什么样的影响呢？根据 [Phoronix 在 2009 年使用
Fedora 11
所做的横向比较](http://www.phoronix.com/scan.php?page=article&item=fedora_debug_selinux#=1)来看，**开启
SELinux 仅在少数情况下导致系统性能约 5% 的降低**。

SELinux 是不是会十分影响一般桌面应用及程序开发呢？原先是，因为 SELinux
的策略主要针对服务器环境。但随着 SELinux 8年来的广泛应用，目前 **SELinux
策略在一般桌面及程序开发环境下依然可以同时满足安全性及便利性的要求**。以刚刚发布的
Fedora 15 为例，笔者在搭建完整的娱乐(包含多款第三方原生 Linux 游戏及
Wine 游戏)及开发环境(Android SDK + Eclipse)过程中，只有 Wine
程序的首次运行时受到 SELinux 默认策略的阻拦，在图形化的“SELinux
故障排除程序”帮助下，点击一下按钮就解决了。

**了解和配置 SELinux**

*1. 获取当前 SELinux 运行状态*

`getenforce`

可能返回结果有三种：`Enforcing`、`Permissive` 和 `Disabled`。Disabled
代表 SELinux 被禁用，**Permissive
代表仅记录安全警告但不阻止可疑行为**，Enforcing
代表记录警告且阻止可疑行为。

目前常见发行版中，RHEL 和 Fedora 默认设置为 Enforcing，其余的如 openSUSE
等为 Permissive。

*2. 改变 SELinux 运行状态*

`setenforce [ Enforcing | Permissive | 1 | 0 ]`

该命令可以立刻改变 SELinux 运行状态，在 Enforcing 和 Permissive
之间切换，结果保持至关机。一个典型的用途是看看到底是不是 SELinux
导致某个服务或者程序无法运行。**若是在 setenforce 0
之后服务或者程序依然无法运行，那么就可以肯定不是 SELinux 导致的。**

若是想要**永久变更系统 SELinux 运行环境，可以通过更改配置文件
`/etc/sysconfig/selinux` 实现**。注意当从 Disabled 切换到 Permissive
或者 Enforcing
模式后需要重启计算机并为整个文件系统重新创建安全标签(`touch /.autorelabel && reboot`)。

*3. SELinux 运行策略*

配置文件 `/etc/sysconfig/selinux` 还包含了 SELinux
运行策略的信息，通过改变变量 `SELINUXTYPE`
的值实现，该值有两种可能：`targeted`
代表仅针对预制的几种网络服务和访问请求使用 SELinux 保护，`strict`
代表所有网络服务和访问请求都要经过 SELinux。

RHEL 和 Fedora 默认设置为 `targeted`，包含了对几乎所有常见网络服务的
SELinux 策略配置，已经默认安装并且可以无需修改直接使用。

若是想自己编辑 SELinux 策略，也提供了命令行下的策略编辑器 `seedit` 以及
Eclipse 下的编辑插件 `eclipse-slide` 。

*4. coreutils 工具的 SELinux 模式*

常见的属于 coreutils 的工具如 `ps`、`ls` 等等，可以通过增加 `Z`
选项的方式获知 SELinux 方面的信息。

如 `ps auxZ | grep lldpad`

`system\_u:system\_r:initrc\_t:s0 root 1000 8.9 0.0 3040 668 ? Ss 21:01
6:08 /usr/sbin/lldpad -d`

如 `ls -Z /usr/lib/xulrunner-2/libmozjs.so`

`-rwxr-xr-x. root root system\_u:object\_r:lib\_t:s0
/usr/lib/xulrunner-2/libmozjs.so`

以此类推，`Z` 选项可以应用在几乎全部 `coreutils` 工具里。

**Apache SELinux 配置实例**

*1. 让 Apache 可以访问位于非默认目录下的网站文件*

首先，用 `semanage fcontext -l | grep '/var/www'` 获知默认 `/var/www`
目录的 SELinux 上下文：

`/var/www(/.*)? all files
system\_u:object\_r:httpd\_sys\_content\_t:s0`

从中可以看到 Apache 只能访问包含 `httpd\_sys\_content\_t` 标签的文件。

假设希望 Apache 使用 `/srv/www`
作为网站文件目录，那么就需要给这个目录下的文件增加
`httpd\_sys\_content\_t` 标签，分两步实现。

首先为 /srv/www 这个目录下的文件添加默认标签类型：`semanage
fcontext -a -t httpd\_sys\_content\_t '/srv/www(/.*)?'`  
然后用新的标签类型标注已有文件：`restorecon -Rv /srv/www`  
之后 Apache 就可以使用该目录下的文件构建网站了。

其中 `restorecon `在 SELinux
管理中很常见，起到恢复文件默认标签的作用。比如当从用户主目录下将某个文件复制到
Apache 网站目录下时，Apache
默认是无法访问，因为用户主目录的下的文件标签是
`user\_home\_t`。此时就需要 `restorecon `将其恢复为可被 Apache 访问的
`httpd\_sys\_content\_t` 类型：

`restorecon -v /srv/www/foo.com/html/file.html`

`restorecon reset /srv/www/foo.com/html/file.html context
unconfined\_u:object\_r:user\_home\_t:s0->system\_u:object\_r:httpd\_sys\_content\_t:s0`

*2. 让 Apache 侦听非标准端口*

默认情况下 Apache 只侦听 80 和 443 两个端口，若是直接指定其侦听 888
端口的话，会在 `service httpd restart` 的时候报错：

`Starting httpd: (13)Permission denied: make\_sock: could not bind to
address [::]:888`

`(13)Permission denied: make\_sock: could not bind to address
0.0.0.0:888`

`no listening sockets available, shutting down`

`Unable to open logs`

这个时候，若是在桌面环境下 **SELinux
故障排除工具**应该已经弹出来报错了。若是在终端下，可以通过查看
**/var/log/messages** 日志然后用 **sealert -l**
加编号的方式查看，或者直接使用 `sealert -b`
浏览。无论哪种方式，内容和以下会比较类似：

`SELinux is preventing /usr/sbin/httpd from name\_bind access on the
tcp\_socket port 888.`

`***** Plugin bind\_ports (92.2 confidence)
suggests *************************`

`If you want to allow /usr/sbin/httpd to bind to network port 888`

`Then you need to modify the port type.`

`Do`

`# semanage port -a -t PORT\_TYPE -p tcp 888`

`where PORT\_TYPE is one of the following: ntop\_port\_t,
http\_cache\_port\_t, http\_port\_t.`

`***** Plugin catchall\_boolean (7.83 confidence)
suggests *******************`

`If you want to allow system to run with NIS`

`Then you must tell SELinux about this by enabling the 'allow\_ypbind'
boolean.`

`Do`

`setsebool -P allow\_ypbind 1`

`***** Plugin catchall (1.41 confidence)
suggests ***************************`

`If you believe that httpd should be allowed name\_bind access on the
port 888 tcp\_socket by default.`

`Then you should report this as a bug.`

`You can generate a local policy module to allow this access.`

`Do`

`allow this access for now by executing:`

`# grep httpd /var/log/audit/audit.log | audit2allow -M mypol`

`# semodule -i mypol.pp`

可以看出 SELinux
根据三种不同情况分别给出了对应的解决方法。在这里，第一种情况是我们想要的，于是按照其建议输入：

`semanage port -a -t http\_port\_t -p tcp 888`

之后再次启动 Apache 服务就不会有问题了。

这里又可以见到 `semanage` 这个 SELinux
管理配置工具。它第一个选项代表要更改的类型，然后紧跟所要进行操作。详细内容参考
[Man 手册](http://linux.die.net/man/8/semanage)

*3. 允许 Apache 访问创建私人网站*

若是希望用户可以通过在 `~/public_html/`
放置文件的方式创建自己的个人网站的话，那么需要在 Apache
策略中允许该操作执行。使用：

`setsebool httpd\_enable\_homedirs 1`

`setsebool` 是用来切换由布尔值控制的 SELinux
策略的，当前布尔值策略的状态可以通过 `getsebool` 来获知。

默认情况下 setsebool
的设置只保留到下一次重启之前，若是想永久生效的话，需要添加 `-P`
参数，比如：

`setsebool -P httpd\_enable\_homedirs 1`

**总结**

希望通过这一个简短的教程，扫除您对 SELinux
的误解甚至恐惧，个人感觉它并不比 iptables
策略复杂。如果希望您的服务器能有效抵挡 0-day 攻击时，那么 SELinux
或许就是一个值得考虑的缓和方案。

**致谢**

本文大量参考自 Vincent Danen 发表在 TechRepublic 上的 SELinux
系列教程[1](http://www.techrepublic.com/blog/opensource/introduction-to-selinux-dont-let-complexity-scare-you-off/2447)，[2](http://www.techrepublic.com/blog/opensource/practical-selinux-for-the-beginner-contexts-and-labels/2458)，[3](http://www.techrepublic.com/blog/opensource/practical-selinux-port-contexts-and-handling-access-alerts/2463)。在此向
Vincent Danen 致敬。
