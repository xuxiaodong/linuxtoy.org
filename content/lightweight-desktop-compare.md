Title: 很轻很强大：轻量级桌面环境比较
Date: 2008-12-02 11:28
Author: lovenemesis
Category: Featured
Tags: enlightenment, lxde, Xfce
Slug: lightweight-desktop-compare

这天你终于下定决心购买了一台流行的 Netbook
，与往常装机一样，直接安装心爱的 Linux
发行版。好不容易安装完成了，却发现平日启动飞快的应用程序在 Netbook
上怎么都跑不快。怎么办呢？
与往常一样，你上网寻求帮助，发现了很多“轻量级桌面环境”。面对如此多的选择，到底哪个才是适合你的呢？  

如上所述，本文主要是对由于 Netbook
风行而火爆起来的几款轻量级桌面环境进行一个比较，希望能对使用 Netbook
或者电脑配置较古老的朋友有所帮助。  
有个小小的问题是，本人没有 Netbook，只能让自己的 12寸本本“山寨”一下了……

*测试环境*

    AMD Turion 64 X2 TL-58 1.9G / DDR2 800 2GB*2 / nVidia GeForce 8400M G 128M
    Fedora 10 2.6.27.5-117.fc10.i686.PAE / X.org 1.5.3

*测试项目*

1.  OpenOffice.org 3.0 Writer 第一次启动用时（所谓“冷启动”）；
2.  OpenOffice.org 3.0 Writer 第二次启动用时；
3.  GIMP 2.6.2 第一次启动用时；
4.  GIMP 2.6.2 第二次启动用时；
5.  Mozilla Firefox 3.0.4 第一次启动用时；
6.  Mozilla Firefox 3.0.4 第二次启动用时；
7.  OpenOffice.org 3.0 Writer + GIMP 2.6.2 + Mozilla Firefox 3.0.4 +
    默认文件管理器 + 默认终端模拟器 情况下总已用内存。

*测试方法*

为每个桌面环境建立全新的独立的用户帐户，在首次登录后进行以上测试。在一个桌面环境中的测试结束之后，关闭计算机，等待五分钟后再开机，进行下一个桌面环境中的测试。  

本人水平有限，不清楚如何精确计算启动用时，只好手机的秒表，精确到毫秒。注意！人对视觉刺激是存在反应时，所以该时间仅作粗略比较。  
总已用内存选取使用当前桌面环境下默认终端模拟器中 htop
所显示已用内存值。

**[LXDE](http://lxde.org/)** *Let's speed up your desktop!*

LXDE，是 Lightweight X11 Desktop Environment
的缩写，它特别为低配置环境下的电脑设置，如
Netbook、MID或者是较老的电脑设计。该桌面环境还为 Netbook
等设备设计了标签式的 lxlauncher，方便快速调用程序（个人觉得这种 launcher
借鉴了 PalmOS 上的很多 Launcher 的设计）。  
LXDE 是一个相对较新的项目，随着 Netbook 的兴起而产生。我是在今年 OOoCon
2008 上遇见了 LXDE 的 [Mario Behling](http://perspektive89.com)
先生后才产生兴趣的。Mario 用一台原装 Xandros 的 eeePC 和一台安装了
Pud-LXDE 的 eeePC 做比较，LXDE 下 OOo 2.4
出色的启动速度给我留下了深刻的印象。

*Fedora 10 安装：* `yum groupinstall LXDE`  
  
*测试版本：* lxde-common 0.3.2.1  
  
*默认文件管理器：* PCManFM  
  
*默认终端模拟器：* lxterminal

**[Xfce](http://www.xfce.org/?lang=zh_CN)** *... and everything goes
faster!*

Xfce 是一款适用于多种 *NIX
系统的轻量级桌面环境。它被设计用来提高您的效率，在节省系统资源的同时，能够快速加载和执行应用程序。 -
Olivier Fourdan, Xfce 创始人  
Xfce 是一个有很长历史的的桌面环境项目了，在很多U盘 Linux
中可以见到它的身影。另外，Xfce
也是本次测试的轻量级桌面环境中唯一一个支持窗口透明特效的。

*Fedora 10 安装：* `yum groupinstall XFCE`  
  
*测试版本：* 4.4.3  
  
*默认文件管理器：* Thunar  
  
*默认终端模拟器：* xterm

**[Enlightenment](http://www.enlightenment.org/)** *Beauty at your
fingertips!*

Enlightenment 是窗口管理器，Enlightenment
是桌面外壳，Enlightenment是创建漂亮应用程序的材料，Enlightenment，或者简单的一个
*e*，代表着一群尝试创造次世代应用程序的人们。  
相比以上两款轻量级桌面环境，Enlightenment
在亚洲地区不是那么出名，可能是由于本地化比较欠缺的缘故。本人了解它还是从
Yellowdog Linux 开始的。Enlightenment
在追求轻量级的同时也十分注重美观，它的控件悬停特效绝对让人过目不忘～

*Fedora 10 安装：* `yum install enlightenment efreet eterm`  
  
*测试版本：* 0.16.999.043  
  
*默认文件管理器：* 不知道名字……  
  
*默认终端模拟器：* eterm

好了，参赛选手介绍完毕。为了更好的反应这些轻量级桌面环境的性能，测试中也加入了
GNOME 2.24，方便比较。

**测试结果：**

    LXDE        XFCE        Enlightenment        GNOME

    22.88      24.29         24.40                          22.84       OOo 1st(ms)
    3.87         4.52           4.02                            5.13         OOo 2nd(ms)
    17.06       18.54        19.63                          19.59       GIMP 1st(ms)
    5.82         5.54           5.64                            5.82         GIMP 2nd(ms)
    13.85      14.99         14.03                          12.64       FF3 1st(ms)
    3.49         3.38           3.03                            3.38         FF3 2nd(ms)
    237          250            195*                           288         UsedMem (MB)

*eterm 启动失败，以 Xterm 代替。

**结果分析**

从上表的结果看来，在应用程序启动时间上，各个桌面环境的差异并没有预想中的那么大，最快的与最慢的差别都在2s内（全距），对于用户来讲差别并不是十分明显。另外，非轻量级
GNOME
的性能也算对得起观众。在内存使用方面，各个桌面环境还是有不小差别的，最低的
195M 与最高的 288M 相差 93M（全距）。造成这种结果的原因是什么呢？

本次测试所用平台性能比 Netbook
要高很多，尤其在内存方面；同时除了桌面环境以外的其他所有软件都是一致的。在这种条件下，可以认为差异只是由于桌面环境本身的性能所致，与硬件和其他软件无关。桌面环境对应用程序的影响体现在与X
server
的沟通速度和自身占用内存上。而结果中相近应用程序启动速度，反映了在同一个
X server
下，窗口管理器的性能优化空间实际上相当的小。于是轻量级桌面环境的优势更多的体现在自身占用内存较小，可以留给应用程序更多的内存上。

早期的 Netbook (比如一代 eeePC )或者老的本本都只 256M
内存，还要分给显示8M左右。在这种总内存不够用的条件下， LXDE 和
Enlightenment 由于无需访问交换分区，就会比 XFCE 和 GNOME
体现出更快的应用程序启动速度。但是一旦拥有较充足的内存（新一代的 Netbook
都拥有 512M
内存），同样都无需访问交换分区，这种差异就变得不是那么明显了。

**结论：**

由于各个轻量级桌面环境本身性能上差异不大，所以你决定根据自己的喜好去选择。如果注重功能，推荐具有标签式
Launcher 的 LXDE；如果注重外观，推荐华丽的
Enlightenment；如果希望与传统的桌面环境在使用习惯上保持一致，推荐 Xfce。

**PS:关于使用测试平台的对结果的影响的补充说明**

很感谢诸位朋友的下面的评论，看到很多朋友说到测试平台对结果的影响问题，觉得有必要补充说明下。  
很显然，最理想的情况应该是找一台 Netbook
来测试，现实是我没有……（下面会有此句话的修订版～）

测试的目的是考察桌面环境这个**软件**本身的性能，采用这个硬件性能充足的平台可以最大限度降低硬件条件对它影响。固然这些桌面环境是为低内存配置的机子设计的，但是**没有任何证据表明轻量级桌面环境在大内存条件下的表现下与在低内存下的表现会有显著差异**。再说用来参考的GNOME，根据GNOME项目的推荐512M内存来看，256M内存显然会对
GNOME 这个**软件**的表现有影响。于是：  
  

`低内存配置下LXDE的表现=高内存配置下LXDE的表现（以LXDE为例，其他类似）； 低内存配置下GNOME的表现<高内存配置下GNOME的表现；`  
  

本着公平竞争的原则，结合考虑测试目的是考察**软件**本身，只能选择高内存配置的平台以照顾
GNOME，也只有这样最终结果才具有比较性。  
  
于是上面的话应该修订为：  
  
很显然，最理想的情况应该是找一台 Netbook 来测试(当不考虑和 GNOME
比较的情况下)，现实是我没有……

Ubuntu 和 Xubuntu
毕竟是两个发行版，系统启动时默认载入的服务都不一样(印象中前者默认启用蓝牙而后者不)，如果要比较的话，可以在
Ubuntu 下安装 XFCE，或者在 Xubuntu 下安装 GNOME，这样比较较好些。

*个人观点，仅供参考！  
  
欢迎使用其他发行版的朋友提供更多比较数据！！！*
