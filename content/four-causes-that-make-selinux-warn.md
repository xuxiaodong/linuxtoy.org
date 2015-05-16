Title: 导致 SELinux 警告的四个常见原因
Date: 2012-11-14 14:26
Author: lovenemesis
Category: Featured, Security
Tags: Apache, selinux
Slug: four-causes-that-make-selinux-warn

上次的 [SELinux
的入门](http://linuxtoy.org/archives/selinux-introduction.html)评论中，有童鞋表示
SELinux 警告看不懂。这次就来介绍下四个导致警告产生的原因以及解决方案。

**原因一：出现标注错误**

SELinux
的核心概念就是标注，无论是文件系统、目录、文件、文件启动描述符、端口、消息接口还是网络接口，**所有的一切都需要标签，并且仅且仅能按照标签所赋予的权限执行**。即使运行的
Apache 进程被黑客入侵且取得了 `uid=0 root`
权限，它依然无法访问某个用户主目录下的文件。因为标注为 `httpd_t` 的
Apache 进程所持有的无法访问标注为 `user_home_t` 的内容。

因此，如果标注有问题的话，SELinux
就会弹出警告。如何处理此类，可以参看[本站前文](http://linuxtoy.org/archives/selinux-introduction.html)中关于
`semanage fcontext` 和 `restorecon` 命令的使用。当然也可以按照图形化的
SELinux 除错工具中的提示解决。

**原因二：自定义了程序运行设置**

经过多年的发展，SELinux
已经积累了大量的策略文件时，对于绝大多数应用程序的默认运行请求都有记录，可以赋予合适的最小权限予以执行。不过若是您自定义了一些运行配置或者有特殊的应用需求，则需要调整部分
SELinux 设置。

对于大多数常见的自定义需求，SELinux
采取布尔值的方式进行控制，可以参看[本站前文](http://linuxtoy.org/archives/selinux-introduction.html)中关于
`setsebool` 命令的使用。若想了解全部可调整的 SELinux 布尔值，使用
`semanage boolean ­-l` 命令。这可以通过图形化的 SELinux
除错工具解决，也可以通过图形化的 `system-config-selinux` 解决。

**原因三：SELinux 策略或应用程序配置有问题**

若是您并未特别修改配置却依然收到 SELinux 警告，原因可能就在 SELinux
策略或者应用程序本身了。此时建议首先在 SELinux
除错工具的帮助下提交错误报告，然后再依据情况进行处理。若是已经被报告过，通常在错误报告的评论中会详细解决方案。

此时若是想忽略 SELinux 警告依然运行应用程序，则有如下几种方式：

-   将 SELinux 设为允许模式，仅记录警告但不阻止运行：`setenforce 0`。
-   将某单一标注进程设置为允许模式，而非整个系统，例如仅想以允许模式运行
    Apache: `semange permissive -a httpd_t`
-   参照 SELinux
    除错工具的建议创建并加载自定义策略。具体过程依情况而异，SELinux
    除错工具内会有详细的说明。

**原因四：程序已被入侵**

SELinux 并非入侵检测系统，所以目前 SELinux
除错工具无法主动的甄别出入侵企图，不过当您发现警告内容包含有如下特征时，很有可能对应进程已被黑客攻破了：

-   尝试关闭 SELinux (/etc/selinux) 或者设定某个 SELinux 布尔值。
-   尝试载入内核模块、写入内核目录或者引导器镜像。
-   尝试读取 shadow\_t 标识的文件，那里通常包含了加密的账户信息。
-   尝试覆盖写入日志文件。
-   尝试连接不需要的随机端口或者邮件端口。

至此四种常见警告原因介绍完毕，希望您下次遇到 SELinux
警告时可以安全有效的处理。顺便说下，绝大部分 SELinux
除错工具的本地化问题已经解决，使用简中的童鞋们将可以在 Fedora 18
看到简中的警告内容了。

本文摘译自 [Daniel Walsh
博文](http://drupalwatchdog.com/2/2/apache-selinux)及[演讲
PDF](http://people.fedoraproject.org/~dwalsh/SELinux/Presentations/selinux_four_things.pdf)。
