Title: Phoronix Test Suite 0.3.0 发布
Date: 2008-04-19 11:28
Author: lovenemesis
Category: Apps
Tags: Phoronix Test Suite, Releases
Slug: phoronix-test-suite-030-released

基于 Linux 平台的硬件测评工具 [Phoronix Test
Suite](http://linuxtoy.org/archives/phoronix-test-suite.html) 0.3.0
版本昨天发布了。这个版本引入了以下新功能，目前该套件共有 25 个预置文件和
9 个测试集：

-   SPECViewPerf：面向图形工作站的 OpenGL 的测评。
-   IOzone：一个流行开放源代码的硬盘 IO 测评。
-   增强了软硬件检测：现在结果汇报中可以看到在测试期间所占用的磁盘空间和可能影响测试成绩的软件如
    Firefox 和 Compiz。
-   屏蔽屏幕保护：在测试期间自动关闭屏幕保护功能并在测试结束后自动恢复，GNOME
    下是通过 GConf，其他是通过 xdg-screensaver。
-   引入自动化模式：通过编辑一个 XML 文件可以实现无人职守批量化测试。

另外，针对 Fedora 和 Ubuntu 引入了依赖性检测，在这两个发行版上运行 Test
Suite 时可以检测测试必需软件是否已经安装。

Phoronix Test Suite 0.3.0 可从 [Phoronix
网站下载](http://www.phoronix.com/scan.php?page=article&item=pts_030#=1)。

**更新**

昨天发布的 Phoronix Test Suite 0.3.0 在今天发布了一个修正版，修正了
0.3.0 版本中一个由于错误调用 GCC 导致系统死机的 Bug。

同时，这个修正版还包括了两个新的测试预置文件：

-   一个是用来测试基于 WINE 的 Direct3D 9 实现能力的。
-   另一个是用来测试 X RENDER 表现能力的。

另外，该修正版本还对部分预置文件做了修整。详见[这里](http://www.phoronix.com/scan.php?page=news_item&px=NjQzOQ)。

[撰文/黑日白月]
