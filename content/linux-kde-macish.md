Title: Linux KDE Macish — Linux 仿 Mac 之 KDE 篇
Date: 2010-01-14 17:47
Author: Yunkwan
Category: Tips
Tags: KDE
Slug: linux-kde-macish

{ 撰文/[Yunkwan](http://yunkwan.wordpress.com) }

我是 KDE  
Fans。所以，可能以下会出现非常主观的观点。但是，我承认我不极端~

Linux 下的文章一大堆都是 GNOME 下模仿
Mac，但是怎样模仿都感觉不同，毕竟不同就是不同~

不如不要一味地抄了~ 相似也可以啊~ 这样既有特色又有美感~

除了 GNOME 下的 Mac4Lin 还有很不错的 Elemetary。这两个都是常见的 GNOME
仿 Mac 的 theme。但是看着看着会很容易看腻~

但是别忘了我们还有疯狂崛起的 KDE 哦~

有不少人说 KDE 很像 Windows Vista 7

这当然，默认的 Air 透明主题和 Single panel 还有那个大大一片的 Kick off
菜单~ 确实有几分和 Vista 相似~

但是，你打开 Dolphin 看看 Colums View Mode 这是效仿 Mac 的~

[![Dolphin](http://i.linuxtoy.org/images/2010/01/thumb\_dolphin\_colums\_view.png)](http://i.linuxtoy.org/images/2010/01/dolphin\_colums\_view.png)

然后再试试 System setting (有些发行版叫 personal setting，比如
openSUSE)，搜索 比如 “keyboard” 不相关的项目变成灰色~ 这也是非常
Machish。

[![System
setting](http://i.linuxtoy.org/images/2010/01/thumb\_system\_setting\_search.png)](http://i.linuxtoy.org/images/2010/01/system\_setting\_search.png)

[![System
setting](http://i.linuxtoy.org/images/2010/01/thumb\_system\_setting\_search2.png)](http://i.linuxtoy.org/images/2010/01/system\_setting\_search2.png)

其实，本身 KDE 就非常地 Macish 哦!

当然，这些功能性上的 Macish 不能满足我们喜欢 Mac-like 的人啦~

尽管 Oxygen 本身就颇为美观，但是很容易看腻~ 让人激动激动的是 KDE SC 4.4
的 Oxygen 窗口主题有了很大的改进，好看非常多了~

令我开心和陶醉的是 Title Bar 的按钮好看了很多，多了 no border
的效果，不再像以往的 Oxygen 那样占了那么多位置~ 还加了 outline
color，令窗口更加好看~

当然，这还是不够 Macish 的，毕竟 KDE 要做出 KDE 的特色嘛~ 要
Oxygen-like 到底~

这是就要提及不少人已经知道的 [Bespin
主题](http://cloudcity.sourceforge.net)啦!

Bespin 就是 KDE 下另一个漂亮的主题啦!! 而且这个主题是非常非常 Macish
的哦!

BTW，我也是一个 Kubuntu Fans

Kubuntu 下安装 Bespin:

sudo aptitude install kde-style-bespin kde4-style-bespin
kwin-style-bespin kwin4-style-bespin

当然，除了窗口 Macish，还有那个那个 Global menu 哦!

不用担心，我们有 Xbar 这个 Plasmoid-widget。

部分发行版的 Xbar 在安装 Bespin 的包时候已经安装了~ 比如 openSUSE
安装了 Bespin 主题就直接有 Xbar 了~

Kubuntu 下安装 Xbar:

sudo aptitude install plasma-widget-xbar

既然，所有东西都安装齐了~ 那么就开始动工吧!

Bespin 的可定义性非常高~  

这里附上一个我自己的[配置文件](http://dl.dropbox.com/u/2438732/kde\_macish/yunkwan\_bespin.bespin)。

打开 System setting，选 Apperance (外观)项目~ 然后，Style
(不知道中文是不是样式，基本没怎用过中文环境~)。

选择 Bespin，然后 config 设置，导入刚才的配置文件。然后选定导入好的配置
然后点击 load (载入/加载)，点确定。

[![Bespin](http://i.linuxtoy.org/images/2010/01/thumb\_bespin\_config2.png)](http://i.linuxtoy.org/images/2010/01/bespin\_config2.png)

[![Bespin](http://i.linuxtoy.org/images/2010/01/thumb\_bespin\_config.png)](http://i.linuxtoy.org/images/2010/01/bespin\_config.png)

如果你像我一样不喜欢工具按钮旁边有文字的，就在 Fine Tuning 这个页面选上
不显示文字/只显示图标 再应用就 OK 了~

[![Bespin](http://i.linuxtoy.org/images/2010/01/thumb\_bespin\_config1.png)](http://i.linuxtoy.org/images/2010/01/bespin\_config1.png)

然后到 Windows (窗口) 设置，其实就是标题栏和外框~ 要用 Bespin 的就用
Bespin 的，虽然不是很 Macish 但是也很好看~ 但是 Bespin
的标题栏有时会出现奇怪的情况~ 而且在 Kubuntu 下要在设置后 logout
一下才能看到 bespin 标题栏真正的效果~ 如果有 KDE 4.4 就直接选用 Oxygen
的 no border，这样更加 Macish。在隔壁一个页面 按钮 可以自定义排列 标题栏
按钮的位置~

[![Bespin](http://i.linuxtoy.org/images/2010/01/thumb\_bespin\_config3.png)](http://i.linuxtoy.org/images/2010/01/bespin\_config3.png)

完成了这些，已经非常 Macish 了!

如果还要 Global menu 就接着看吧~

在桌面新建一个 Panle (面板)，移到顶部~ 然后添加 Xbar 这个 widget
到这个  
Panel。

[![Xbar](http://i.linuxtoy.org/images/2010/01/thumb\_xbar.png)](http://i.linuxtoy.org/images/2010/01/xbar.png)

调整一下 Panel 的宽度，合适就可以了~

可能在加入 Xbar 后，Xbar 的位置再 Panel 不是正确的~ logout 一下就可以~

就是这样了~ 既 Macish 又不是全抄袭的感觉~

至于 Dock 嘛~ 我个人喜欢~ Docky2，很流畅~

还有 3D mode 和 Glass theme，非常 Macish!

Kubuntu 下安装 Docky2:

加入这个 PPA 源就可以

deb http://ppa.launchpad.net/docky-core/ppa/ubuntu karmic main  
deb-src http://ppa.launchpad.net/docky-core/ppa/ubuntu karmic main

sudo aptitude install docky

虽然 Docky2 这个源是测试版 daily
build，正式版还没有发布，但是已经相当稳定了~  
当然，在 KDE 下很多 Docky2 的附加功能都用不上啦~ 毕竟那些是针对
GNOME的。

这里我没有提及换 Mac 的图标~ 因为，我觉得 KDE 本身的 Oxygen
图标已经很好了~ 而且，Oxygen 的图标是考虑上了 Usability 的~
所以，默认的图标除了美观之外还顾及到可用性~
很容易通过看图标就知道用途~

{
[Source](http://yunkwan.wordpress.com/2010/01/12/linux-kde-macish-linux%e4%bb%bfmac%e4%b9%8bkde%e7%af%87/).
Thanks Yunkwan. }
