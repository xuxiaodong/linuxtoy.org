Title: Ubuntu Mir 及 Unity Next
Date: 2013-03-05 09:36
Author: lovenemesis
Category: News
Tags: canonical, Ubuntu
Slug: ubuntu-mir-and-unity-next

Canonical 宣布将在 2014 的 Ubuntu 中使用自己的显示服务器 Mir ，不再使用
X 或者 Wayland。

Canonical 表示**现在的 X 以及未来的 Wayland
无法满足未来横跨桌面、手机、平板和电视的发展策略**。Ubuntu 社区经理 Jono
Bacon 认为这两者都包含了太多 Ubuntu 策略中用不到的功能。于是 Canonical
决定开发自己的显示服务器 Mir。

和新生的 Wayland 的一样，**Mir 也面临厂商的闭源驱动支持问题**。Canonical
表示希望能“劝说”闭源驱动厂商实现围绕 EGL
的驱动开发模式，简化针对不同显示服务器的支持。

目前 Mir 仅能在开源驱动下使用，且依赖 Canonical fork
出来，**未提及也未打算合并至上游 Mesa 的 EGL DRI2 代码**。

和新生的 Wayland 不一样的地方是 **Mir 目前没有任何工具集支持**。当下
Wayland 已经得到 GTK3 及 Qt5
的明确支持，上游桌面环境及应用程序的迁移正在逐步进行。在 Qt/QML 之外 Mir
将面临应用支持的问题。

此外 Canonical 表示 **Mir 将助力未来自家使用 QT/QML 技术构建桌面环境
Unity Next**。

[Mir 技术细节 Wiki](https://wiki.ubuntu.com/MirSpec)

[Mir PPA](https://launchpad.net/~mir-team/+archive/staging)

[Mir 源代码](https://code.launchpad.net/~mir-team/mir/trunk)

[来自 Canonical 和 Phoronix 的视频
Demo](http://www.phoronix.com/scan.php?page=news_item&px=MTMxODQ)

*友情提醒：*和 Canonical 的其他开源项目一样，Mir 的开发需要签署
CLA，意味着[贡献的代码和内容版权将完全归属于
Canonical](http://linuxtoy.org/archives/cla-fpca-cca.html)。

*消息来源*：[OMG
Ubuntu](http://www.omgubuntu.co.uk/2013/03/canonical-announce-custom-display-server-mir-not-wayland-not-x#content)
[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTMxNzY)

**PS** 和先前预计的不符，Ubuntu for Touch 并不是 Mir
的首次大规模公开见面，[测试报告](http://linuxtoy.org/archives/ubuntu-12-10-touch-preview.html)指出它依然使用
Android 的 SurfaceFlinger 。
