Title: Oracle + Sun 产品战略
Date: 2010-01-29 12:17
Author: toy
Category: News
Tags: Oracle, Sun
Slug: oracle-sun-product-strategy

{ 撰文/[Terry Wang](http://terrywang.net) }

今日乘着上班的空隙和下班后的一点时间，基本看完了 Oracle + Sun 产品战略
Webcast  
和 Presentation 中的绝大部分，并在 Twitter  
上做了中文的”推播”，整理于此，希望能对此次合并感兴趣的朋友有所帮助。

**操作系统**

OS 方面，埃里森大叔说：我们有世界上最好的 Linux 和
Unix，任君挑选。个人觉得在 Linux 前面加上企业级更为妥当，要说 RHEL/OEL
是世界上最好的 Linux，有几人会同意？这个问题根本就没有的答案。

以下是直接来自 Presentation 的内容，我就不翻译了：

> Solaris And Linux Advantage

> With Solaris and Linux, Oracle provides the industry’s most complete
and open operating systems offering in the industry.

> + With Solaris, Oracle offers industry-leading scalability,
reliability, security and performance through superior technical
innovation

> + With Linux, Oracle delivers world-class support and technology
leadership for the most widely deployed open source operating system

不知何时 Solaris 已经是 Oracle Solaris Operating System
了，定位就像猜测的那样，高端企业级用户。Webcast 里着重讲
ZFS，内置虚拟化技术，安全性，DTrace
和自我恢复能力（原地复活？）。这样的话 Oracle 就拥有了最好的 Unix
操作系统和一个不错的企业级 Linux 发行版本。

目前 [Solaris
主页](http://www.sun.com/software/solaris/10/index.jsp)还残留着一点 Sun
的印记，相信很快就会被彻底抹去，换上白底大红字。大家再最后看几眼吧，时日无多了。

Linux 方面，Oracle 也将继续对 Linux
社区贡献代码。例如现在已被我们所熟知的，并已被认为是主流，被引入 Linux
内核的 Btrfs，Oracle Cluster File System 2（OCFS2）。

更多的详见：

**虚拟化**

Oracle VM 和 VirtualBox 将会被整合，外加 Solaris  

中已有的虚拟化技术，组成了从桌面到数据中心，一个完整虚拟化解决方案。VirtualBox  
将会被重新命名为 Oracle VM  
VirtualBox，专注于桌面虚拟化领域和新特性的引入，扮演类似于 VMware  
Workstation，VMware Fusion（Mac）的角色。事实上在技术上，VirtualBox  
已经大有超越 VMware Workstation，后来居上之势，尤其是 3.x 引入
[Teleportation  

实时迁移特性](http://linuxtoy.org/archives/virtualbox-teleportation.html)之后，非常看好之。

Oracle VM 将是战略性产品，除了原有的 x86/x86\_64 架构支持之外，SPARC  
架构支持很快会被加入。注意 Oracle VM Server for x86 和 Oracle VM Server
for  
SPARC 是不同的，具体的可以参考  

[Presentation](http://www.oracle.com/ocom/groups/public/@ocom/documents/webcontent/044521.pdf)
16 页。

谈到 Oracle VM 的优势时，Edward Screven – Chief Corporate Architect
主要提到了如下几点：

+ 无许可证费用

包含实时迁移和高可用特性，当然需要支持的得付费。

+ 完整的产品组合

从桌面到数据中心，架构支持 x86/x86\\\_64 和 SPARC。而 VMware 仅支持
x86/x86\_64。

+ 易于部署和管理

有 Oralce VM template 简化虚拟机的创建，Oracle VM Manager 和 Enterprise
Manager 进行监控和管理。

+ 高性能，低资源消耗/开支（overhead）

运行 Oracle 数据库和企业级应用，搭建高可用集群的最佳选择。而 VMware
解决方案在负载过高时性能表现不佳。

说到 VMware 的解决方案的时候，提到 VMware
过于专注在虚拟化技术层面本身，而没有考虑到企业级应用中实际会遇到的各种问题。并说用
VMware 的解决方案相当于额外引入了一个虚拟化层，相对于 Oracle VM
来说，增加了IT基础架构的复杂性。

**办公套件**

OpenOffice.org 将被作为一个独立的（开源）全球业务部门来管理。Oracle
将保留 Sun 的开发和支持团队，继续开发和支持
OpenOffice.org，以便和现有的产品线整合。用户还将看到
StarOffice，StarSuite 改名以融入 Oracle 产品线，Oracle 将专注于 OOo 与
BI 和 Content Management 系统的整合。

此外还将会有一个基于 Web 的 Cloud  
办公套件诞生，跨平台，可以在任何浏览器（包括移动设备）上使用，将使用
ODF 格式。

**Java Virtual Machine (JVM)**

Sun HotSpot JVM 和 BEA JRockit JVM 都是 strategic  
JVM，两者将会被整合起来。但不知道整合起来的 JVM 叫什么，也如何定位。

**Java 应用服务器**

目前 Oracle 拥有 4 个 Java 应用服务器，毫无疑问 WebLogic Server
是其中的王中之王，也是业界企业级应用服务器的标杆。

GlassFish 还将继续是 Java EE
的参考实现，也将会成为新技术和新标准的试验田，类似于 Fedora 和 Red Hat
Enterprise Linux 的关系。

Sun Java System Web Server 和 Oracle Application Server
则将功成身退，归隐山林。不过应该会继续对现有的用户提供支持，Lifetime
support policy 放在那里。

**Java IDE**

JDeveloper 是 Oracle 的 Strategic
开发工具。不过我个人不是很喜欢这个东西，也不适应 ADF，可能是 Eclipse
用多了，习惯问题。

NetBeans 则将继续作为 Java 开发者首选之轻量级开发工具，专注于 Java
EE6，Java ME，添加更多动态脚本语言支持。

Eclipse 方面，Oracle 还将继续是该项目 Strategic
Member，会继续向其贡献代码。也会继续更新 Oracle Enterprise Pack for
Eclipse（OEPE），这是 BEA WebLogic Workshop（Oracle Workshop for
WebLogic）和 BEA Workshop Studio 的替代品。

**Portal**

Portal 又多了一个，达到了前所未有的 5 个。WebCenter Suite 是 Strategic
产品，WebCenter Interaction（Plumtree/ALUI）目前是作为 WebCenter Suite
的一部分来卖，和 WebLogic Portal 一起都会继续被开发并整合到 WebCenter
大家族中。Oracle Portal 和 Glassfish WebSpace
Server，基本上是等着退休了。

**大家最关心的 MySQL 之命运**

MySQL
将作为独立的（开源）全球业务部门运作，有独立的开发和销售团队，MySQL
将被继续开发和支持，就像 InnoDB 那样，并和 Oracle
数据库的管理工具整合。按照 Oracle 的承诺来看，MySQL
应该会变得更好，拭目以待。

还有一些不是很重要的产品，在 Webcast 里都没有提及，比如那个 Sun Java
System Directory Server（LDAP）等等，也就没太关注。

此外，来爆一下料。曾经的 Sun 有 8000 左右的 Mac
用户，使用不同的硬件，包括 Macbook/MacBook Pro，Mac Pro，不排除还有 mini
和 Server 的可能。他们将给 Oracle IT 部门带来什么问题和挑战？将得到来自
IT
的何种程度的支持？他们使用哪些软件办公？暂时都还是疑问。处理得当的话将来有没有可能会被当成案例呢？其他的我所知不多，Sun
内部使用的办公套件标准肯定不会是微软的 Office 套件，StarOffice/StarSuite
才是 Sun 的标准办公套件。

暂时就写这么多，还比较乱。来日再编辑整理加入更多内容，欢迎留言交流，提出你的看法和反馈，当然也可以用
Twitter 直接 @ 我，谢谢;-)

**内容来源**

+ [Oracle + Sun Webcast and
Presentation](http://www.oracle.com/us/sun/044498)  
+ [Oracle + Sun Product Strategy Webcast
Series](http://www.oracle.com/events/productstrategy/index.html)

{ [Source](http://terrywang.net/archives/940). Thanks Terry Wang. }
