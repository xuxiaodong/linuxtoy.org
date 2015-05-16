Title: Systemd 落选 Fedora 14 的详细原因
Date: 2010-09-19 14:50
Author: liangsuilong
Category: Distros
Tags: Fedora, systemd
Slug: the-detail-of-dropping-systemd-in-fedora-14

前几天的 FESCO 会议决定 systemd 将会被推迟到下一个开发周期，即 Fedora
15。Systemd 在最后时刻落选成为 Fedora 14
默认进程管理器，引发了一大堆争议问题。尤其是 Lennart
的不满，认为不应该在这个时候才决定放弃 systemd。  

随后 nirik 在网志上发表了一篇文章，详细解释了为什么 FESCO 会在 Fedora 14
的周期内放弃 systemd。这篇文章在一定程度上代表了 FESCO
的立场。他提到了四个最主要的原因：

1.  Systemd 的文档还没有完全准备好，而且 systemctl
    这个用于开启和关闭的原生 systemd
    服务的软件没有图形化前端，命令行模式又没有完整的文档指导用户操作。</li>
2.  chkconfig 和 system-config-services 还不能处理原生的 systemd 服务。
3.  软件包打包指引还没有被 systemd
    单元文件的指引所取代。现在的说法是准许大部分软件包发布 sysvinit
    脚本。但我们需要确保这些脚本能够正常的运行。当我们有指引以后，我们不再会回头重新做这些工作。
4.  现在有一种感觉是必须要尽快完成
    systemd，并且必须让它成为默认的进程管理器。整个团队必须要赶着达到这个目的。但是在这种自信的情绪下，开发团队也必须认清
    systemd 是数以百万用户在使用它，因为要保证它能够稳定地运行。

nirik 认为推迟 systemd
是一个正确的主意，他在后面会详尽解释为什么。他认为他们已经犯下了错误，现在应该是继续前进并且寻找出一个办法避免同类时间再次发生。他也为这个失误道歉了。

推迟 systemd 的这个议题早在几个星期的 FESCO
的会议上就已经纳入到议程了。然而 systemd
的测试日活动却是在继续进行中。所以 nirik
就觉得他应该在得到更多的测试数据以后再做出决定，所以就花费了更多时间在测试上获得数据。nirik
承认这是他的责任。他认为当时他们即使没有得到数据的前提下也可以开展尝试和讨论。至少他们可以讨论他们当时已经得到的数据。

-   回复特性的程序（或者是决定回滚特性）应该要被额外提出来。什么时候应该做这件事情？是否需要通过
    FESCO
    的大多数人投票同意等？他觉得我们应该增加这一点到处理新特性的规则里面。当我们决定确认
    systemd
    作为一个新特性的时候，有一部分人向我们施加了压力，要求我们认真审阅
    systemd
    或者决定在下一个周期才列它为默认进程管理器。在这个会议上，有一部分成员认为
    systemd 在 Fedora 14 是可行的，但不足够 5 个选票，当时 nirik
    认为缺乏足够的支持确认 systemd。在 systemd 这个特性上，nirik
    感觉很糟糕因为这好像他们很紧急地发明一样东西，而且这个东西是很糟糕的。
-   nirik 认为他本来可以跟特性的拥有者沟通得更加好。所有会议的提议都会
    CC 给 Lennart。所以他应该知道 systemd 将会被讨论，但是我们本来应该把
    Lennart 拉入到讨论之中，但是 nirik 没有做到。他表示歉意。
-   nirik 他在 2010 年 9 月 8日的时候在 trac 发了一个 提议，请求所有
    FESCO 的成员投票这个问题。FESCO 中的
    三个成员参与了投票了，并且留下了建议。nirik
    认为需要有更好的办法处理那些紧急的无法举行会议讨论的主题。特别会议？主题线显示我们需要投票？如果你发现你无法参与投票或者参与会议，你是时候退出会议了。

nirik 在这里提到了几个他认为做得十分出色的地方：

-   Lennart 已经在修复 Bug 和令 systemd
    正常运作做了很多出色的工作。所以他坚信 systemd 在 Fedora 15
    会回到轨道上面。</li>
-   QA 团队也在测试和寻找 Bug 中作出巨大贡献。
-   Bill Nottingham 为了 systemd 在调整 initscripts/upstart
    等软件包方面也做了大量工作， 令 systemd 可以顺利进行测试。

最后他相信 systemd 会在 Fedora 15 的时候顺利成为默认的进程管理器。

原文地址：<http://scrye.com/wordpress-mu/nirik/2010/09/15/fesco-features-and-systemd/>

原始中文翻译：<http://www.isspy.com/the-detail-of-systemd-was-dropped-in-fedora-14/>

翻译不好，有怪莫怪。
