Title: Linux 下的三款 Flash 独立播放器
Date: 2009-02-20 21:30
Author: lovenemesis
Category: Movie Player
Tags: Flash, gnash, swfdec
Slug: 3-standalone-flash-player-under-linux

现在互联网上流传有不少以 SWF 形式发布的教学视频。如何在 Linux
下观看这些教学视频文件呢？

实际上，这些 SWF 格式的视频就是编译好的 Flash 字节码文件。与同样是以
Flash 传播的 FLV 格式文件不同，一般的视频播放器如 MPlayer 和 VLC Media
Player 是无法直接播放的。下面将介绍三款在 Linux 下 SWF 格式的 Flash
播放器。

1.**[swfdec](http://swfdec.freedesktop.org/wiki/)**

[![](http://i.linuxtoy.org/images/2009/02/screenshot-fw_atoninswf-300x194.png)](http://i.linuxtoy.org/images/2009/02/screenshot-fw_atoninswf.png)

swfdec 是最早的一个开源 Flash 实现方案，目前可以播放大多数 Flash 7
格式的视频，被包含在几乎所有发行版软件仓库中，有32和64位版本。

Fedora 10 下安装：

`su-c 'yum install swfdec-gnome'`

2.**[Gnash](http://www.gnu.org/software/gnash/)**

[![](http://i.linuxtoy.org/images/2009/02/screenshot-fw_dmcjxswf-300x194.png)](http://i.linuxtoy.org/images/2009/02/screenshot-fw_dmcjxswf.png)

Gnash 是新兴的开源 Flash 实现方案，目前也是仅可支持到 Flash 7
格式视频，在近两年的发行版中都能见到它的踪影，有32和64位版本。

Fedora 10 下安装：

`su-c 'yum install gnash'`

3.**[Adobe Flash Standalone Player for
Linux](http://www.adobe.com/support/flashplayer/downloads.html)**

[![](http://i.linuxtoy.org/images/2009/02/screenshot-adobe-flash-player-10-300x209.png)](http://i.linuxtoy.org/images/2009/02/screenshot-adobe-flash-player-10.png)

Adobe Flash Standalone Player 被包含在 Adobe 面向是 Flash Debugger
的软件包中，需要在 Adobe
网站上额外下载。由于版权原因，不被包含在绝大多数发行版软件仓库中，只有32位版本。由于是官方的，对于各种
SWF 的兼容效果也是最好的。

Fedora 10 下安装：

[Peguin.SWF](http://blogs.adobe.com/penguin.swf/) 网站上会及时更新 Flash
Linux 版本相关的资讯以及独立版本的下载，找 Debugger/Standalone 即可。

为了方便只需要独立 SWF
播放器的朋友的朋友下载，在这里提供从中提取的最新的独立版本 (2.6MB)
：[点此下载](http://dl.dropbox.com/u/464139/flashplayer.7z)。**更新至
10.0.42.34 版本**

下载并用 7-zip 解压即可。双击解压缩生成的 flashplayer 即可使用。

若要在 GNOME 下创建 SWF 播放关联的话，右键点击任一 SWF
文件，选择“属性”-“打开方式”-“添加”，找到并选中刚才解压的 flashplayer
，点击“确定”。之后再选择前面的单选框将其设置为默认的 SWF
播放器，最后点击“关闭”完成。

**总结**

个人用几个英语语法方面的 SWF 视频测试了下， Gnash
有时会出现音画不同步的现象， swfdec 播放良好，与 Adobe Flash Standalone
Player 差别不大。  
有些朋友提到新东方的 SWF 播放不能的问题，这是新东方故意使用非标准 SWF
格式导致的，除了新东方自己的播放器，目前没有完美解决方案。因手头没有新东方的
SWF，无法测试以上三款播放器的情况。

上面三款独立 Flash 播放器喜欢哪个呢？赶紧选一个去看 SWF 教学视频吧！

**0.任意网络浏览器+ Flash 插件**

如果只有很少几个 SWF 文件的话，折腾半天那些独立的 Flash
播放器未免太麻烦了。  
其实只需要打开任意启用了 Flash 的网络浏览器，将想要播放的 SWF
文件拖动到地址栏上，浏览器就会用 Flash 插件打开本地 SWF 文件了。
