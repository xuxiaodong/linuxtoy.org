Title: Bespin-被KDE4遗忘的主题
Date: 2009-08-29 15:31
Author: gmsh
Category: Apps, News
Tags: Bespin, KDE
Slug: into-to-bespin-kde-qt-style

Bespin 是一款 KDE4/Qt 的主题风格，它前卫、时尚。事实上，如果 thomas
Lübking 没有离开 Oxygen 团队的话，没准人们用的 KDE4 就会默认是这个样子。

  
*转自 <http://blog.gmsh.pp.ru/2009/08/into-to-bespin-kde-qt-style/>  
（Gmsh's Blog）*

### Bespin 预览

[![despin\_hacked\_amarok](http://i.linuxtoy.org/images/2009/08/despin_hacked_amarok.jpeg)](http://i.linuxtoy.org/images/2009/08/despin_hacked_amarok.jpeg)

despin.hacked.amarok

[![gnome.apps.xbar展示 感谢 Wang Hoi
的开发](http://i.linuxtoy.org/images/2009/08/gnome.jpeg)](http://i.linuxtoy.org/images/2009/08/gnome.jpeg)

gnome.apps.xbar展示 感谢 Wang Hoi 的开发

[![bespin.setting](http://i.linuxtoy.org/images/2009/08/bespinsetting-400x223.jpg)](http://i.linuxtoy.org/images/2009/08/bespinsetting.jpeg)

bespin.setting

[![qt.apps.xbar展示](http://i.linuxtoy.org/images/2009/08/opera-400x253.jpg)](http://i.linuxtoy.org/images/2009/08/opera.jpeg)

qt.apps.xbar展示

### Bespin 特点

最大的特点就是它支持全局菜单（见上图），这是 Mac OS
观感的特点之一。Bespin 是 KDE4
下第一款，也是目前唯一一款支持全局菜单的主题风格。全局菜单（Global
menu），使窗口大方简洁明快。这款主题借助 Xbar 实现了 KDE4/Qt
程序的全局菜单，而 Wang Hoi 开发了将 Gnome 的全局菜单集成到 Xbar
的后端的软件 globalmenu-gnome。Bespin 还支持对
某个程序特别定制外观，上图中的 amaroK 外观便是 John Smith 通过 Bespin
设置文件 hack
而成的。它的窗口装饰还支持鼠标滚轮对按钮的操作，感兴趣的朋友可以试试。还有动态图标。  
从外观上看 Bespin 时尚前卫，大方有致

### Bespin 的趣事

这要从 KDE 3 时代讲起。在当年 KDE 中存在着模仿 Mac 的风潮，而 thomas
Lübking 开发的 Baghira 主题便是其中的佼佼者。Baghira 主题是 Bespin
主题的前身。thomas Lübking 参与了 Oxygen
设计团队，并贡献了不少代码，但被 Oxygen
设计团队的某些成员所排斥，被指控所写的代码是臃肿的，不利维护的，最终被清除代码。thomas
Lübking 毅然离开了 Oxygen 设计团队，并启动了 Bespin 项目。John Smith
觉得这不过是艺术设计风格之间的碰撞，不过 thomas Lübking
性格确实很倔强，它曾经开发了一款软件去掉 Plasma
右上的那个腰果图标，仅仅因为他讨厌腰果，在开发 Baghira
的时候，它也因个人喜好拒绝开发 Qt4 版。没办法，这就是 thomas Lübking
，一个有个性的开发者，开发了这么一款有个性的主题引擎。现在的 Bespin
主题已经成为了  
社区最火的主题之一，也是 John Smith
最喜欢的主题。以上预览只是展示了Bespin的一个小侧面，Bespin
更强大的功能在于它的可定制性，不同人眼中有不同的哈姆雷特，不同的人手下也有不同的
Bespin，这涉及个人品位。

### 那么，从哪里可以得到 Bespin 呢？

`svn co https://cloudcity.svn.sourceforge.net/svnroot/cloudcity`

不少发行版的包管理器中可以搜到，搜索 Bespin 即可

### PS

关于集成 Gnome-globalmenu：

1.安装gnome2-globalmenu

2.然后从kdesvn检出 trunk/playground/base/plasma/globalmenu，编译安装。

3.在~/.bashrc中加入export GTK\_MODULES=globalmenu-gnome。重新登录。

关于演示图内容

今天是[John
Smith](http://linuxtoy.org/archives/author/gmsh/)喜爱的歌手MJ的诞辰，小小的致敬一下。

Xbar原理简析

[John
Smith](http://linuxtoy.org/archives/author/gmsh/)简单看了一下，Xbar 是
C/S 模型，Server 是 org.kde.XBar（Xbar向 D-Bus注册自身）; Client 是
org.kde.XBar-，有兴趣可以研究一下。

### 参考资料

http://code.google.com/p/gnome2-globalmenu/

http://cloudcity.sourceforge.net/

http://frinring.wordpress.com/2009/01/29/mac-style-menubar-for-kde-4-and-others/

http://forum.kdecn.org/thread-141-page-1.html

http://qiacat.blogspot.com/2009/03/gnome-global-menu-in-kde4.html
