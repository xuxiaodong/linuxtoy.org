Title: Phoronix Test Suite 0.6.0 发布
Date: 2008-05-11 20:31
Author: lovenemesis
Category: Apps
Tags: phoronix
Slug: phoronix-test-suite-060-%e5%8f%91%e5%b8%83

5月10日，Phoronix 论坛发布了旗下的基于 Linux 的硬件测试套件 Phoronix
Test Suite 0.6.0 ，该版本相对既有版本有48项更新。
该版本的发布标志着朝预期6月初发布的1.0正式版本迈进了一步。

该版本有如下更新：

-   增加了 *make-download-cache*
    参数。使用该参数将把测试所必需文件下载到
    *~/.phoronix-test-suite/download-cache/*.
    目录下，之后可以将其中内容加以备份或拷贝其他电脑上直接使用而无需再重新下载，这样可以节省部分流量。
-   增加了 *sensors*
    参数，可以即时返回当前温度探测器结果并生成相应表格。
-   增加了新的基于 X-Plane 9 的测试。X-Plane 9
    是一个得到FAA认证的模拟现实飞行软件。本测试套件里包括的版本经过精简，远小于其官方网站上的400M版本。
-   增加了新的基于 GROMACS 的测试。 GROMACS
    是一个模拟计算分子运动状态的软件，尤其适合于反应当下多核多线程环境下系统的科学运算能力。
-   通过HAL，现在可以正确显示主板的型号和厂家了。
-   可以通过在*phoronix-test-suite/* 根目录下使用 *php
    pts/etc/scripts/package-build-deb.php*
    来创建相应的的deb安装包。并且，Phoronix Test Suite 将从Ubuntu 8.10
    起成为Universe资源仓库中的一员。

下载（包括deb安装包）及更新说明见[这里](http://www.phoronix-test-suite.com/)。
