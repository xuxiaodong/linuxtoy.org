Title: 观点：Linux 上的杀毒软件
Date: 2015-02-13 17:23
Author: lovenemesis
Category: Featured
Tags: antivirus
Slug: opinion-antivirus-in-linux

刚刚进入二月，在[360安全卫士 for
Linux](https://linuxtoy.org/archives/360-for-linux.html)瞬间更名为[360安全卫士国产系统专版](http://chinaossafe.360.cn/)。紧接着不久，[Dr.Web
宣布发现一款可能源自 ChinaZ 的 Linux
系统的后门程序](http://news.drweb.com/show/?i=9272&lng=en&c=5)。加之又被朝内媒体炒作起来的
OpenSSL 基金会事宜，不由得思绪飘溢，再看看 Linux 平台上的杀毒软件。

### 开源尚存 商业已死

如果您是本站的老读者的话，或许还记得这篇发表在 2008 年的文章：[三款
Linux
下的免费桌面级杀毒软件](https://linuxtoy.org/archives/3\_free\_antivirus\_under\_linux.html)。既然是回顾，就从那里开始好了。

* [小红伞 Avira 已经全线停止了对 Linux
平台的支持](https://www.avira.com/en/support-for-home-knowledgebase-detail/kbid/1491)，其中现有的付费企业用户支持将于
2016 年结束。网站上已经找不到其面向个人用户的免费版本了。

* **Avast! 亦停止了对 Linux 桌面版的支持**，在其网站上仅能找到[针对
Linux
企业用户的支持](https://www.avast.com/en-us/linux-server-antivirus)，适用于家庭用户的免费版本不见踪影了。

* 开源方案[ClamAV](http://www.clamav.net/index.html) 及其[图形前端
ClamTK](https://bitbucket.org/dave\_theunsub/clamtk/)
当然还活着，开发还相当活跃。

略微惊讶中，有查找了其他面对个人用户的**商业免费方案**：

* AVG for Linux 不见踪影，从主页的下载区域完全消失。

*
[F-PROT](http://www.f-prot.com/download/home\_user/download\_fplinux.html)仍在下载中心里提供一个基本的
32
位命令行扫描工具。不过通过一般的主页浏览产品时已经看不到了，恐怕也是近乎停滞的状态。

* [Comodo Antivirus for
Linux](https://www.comodo.com/home/internet-security/antivirus-for-linux.php)貌似还活着，提供了针对不同发行版的
32 位及 64
位版本二进制包。不过貌似主程序已经停止更新一段时间了，需要借助[社区修改的驱动模块](https://forums.comodo.com/comodo-antivirus-for-linux-cavl/comodo-antivirus-on-fedora-21-64bit-t109166.0.html)才能在新近内核上正常启动全部服务。

针对**桌面用户的付费方案**中：

* [Panda DesktopSecure for
Linux](http://www.pandasecurity.com/japan/homeusers/solutions/desktopsecure/)貌似还在提供免费
Beta 试用，但是购买链接已经失效。

* [ESET®
NOD32®](http://www.eset.com/int/home/products/antivirus-linux/)至少还存活着，借助其在[中国区的淘宝店铺](http://eset-nod32.taobao.com/?spm=a1z10.1-c.0.0.oo8zIV)，应该还可以在短暂的试用期结束后使用序列号激活，228
软妹币可用三年六个月。遗憾的是，它依然[要求禁用
SELinux](http://kb.eset.com/esetkb/index?page=content&id=SOLN2701&actp=search&viewlocale=en\_US&searchid=1423808183549)。

* [Bitdefender
在商业用户类型中](http://www.bitdefender.com/business/antivirus-for-unices.html)中提供包含
GUI 的 Linux
版本，允许申请个人免费试用。根据其[尚能访问的软件仓库](http://download.bitdefender.com/repos/)来看，最后一次主程序更新是
2010 年。

除了开源软件以外，商业解决方案处于衰败状态。

### 危险将至 盾在何方

毫无疑问，继承自 Unix 系的用户权限管理体系使得 Linux
在用于桌面环境加权不少。由于权限的限定，就算单一用户被感染了，也不会影响其他用户或者系统的工作。

此外，还有诸如 SELinux 和 AppArmor 等强制访问控制机制，启用后系统在面对
0-day
安全漏洞时也可以做到比较有效的风险控制，增加了借助单一服务安全漏洞渗透整个系统的难度。

针对 Linux 桌面的杀毒软件方案的衰落，难道就意味着 Linux
桌面安全无比了么？

个人看法：**完全不是**。

用户权限设计和 MAC
访问控制机制的设计初衷都是**保护操作系统及其上服务的安全性**，用户群体是系统管理员，降低系统及服务重新配置的工作量。

但是对于普通桌面用户来讲，重要的不是搭载系统的 `/`
根分区，而是**搭载用户数据的 `$HOME`**。  
而这方面，恰好是系统内建管理机制和访问控制系统做不到的地方。

此外相比收过训练的系统管理员，普通桌面用户安全意识更低，容易受到定向攻击。简单一个假想例子：

1. 一个用户态的 Bash 脚本，其中混杂了一句 `rm-rf
$XDG\_PICTURES\_DIR`  
2. 在面向诸如麒麟、Deepin
等用户的发行版论坛上，以热点问题发布“教学贴”，比如“CrossOver
注册机，亲试有效”  
3. 在“教学贴”中指导用户如何下载，如何给点击 Bash
脚本时增加可执行权限，如何执行云云

之后用户默认存放照片的目录就没了……系统照样运作，没有越权，不会触发警报……

更复杂的些，上面这个方法还可以针对浏览器配置文件目录进行注入，配合“教学贴”让初学用户忽略浏览器自身的完整性警告或者插件安全提醒。之后能干的事情就多了……

以上能成功，其实就是利用了当前的三个现状：

1.
由于推行所谓的国产操作系统，大量初学用户涌入，信息及知识上的不对等，会导致不经筛选的相信所谓的高手。  
2. Linux 系统已有的安全机制侧重于保护系统及服务，而非用户数据。  
3. 从 Win
平台迁移来的用户，太过于依赖安全软件的“一揽子”式安全保护，本身安全意识异常薄弱。

可惜的是，似乎当下 Linux 平台的杀毒软件似乎没有哪个能做到类似 Windows
下同类产品的“一揽子”式保护。普通 Linux 桌面用户，风险犹存。

### 有市场吗？

在之前查询 Linux 商业免费杀毒软件时，注意到几乎这些商业软件都提供了针对
OS X 平台的产品。由于个人并未使用过近期的 OS X
产品，不过似乎水果厂对于安全也是做了不少改善，包括限定软件安装来源等。不过其中有多少方案可以在崇尚开源且自由的
Linux 桌面借鉴，不好说。而这波针对 OS X 的杀毒软件，是不是也是类似当年
Linux 桌面的昙花一现，暂且观望吧。

不过 Linux 桌面在安全方面也不是停滞不前，基于
KDBUS、Wayland、SELinux、cgroups 等的 [GNOME Sandbox
应用](https://wiki.gnome.org/Projects/SandboxedApps)正在开发，能不能实现期望中的更安全的应用、更简便的开发，在[接下来的
GNOME 3.16
版本](http://blogs.gnome.org/mclasen/2015/01/21/sandboxed-applications-for-gnome/)，就有可能初步体验下了。

至少我来看，市场是有的，就看是谁来填了。
