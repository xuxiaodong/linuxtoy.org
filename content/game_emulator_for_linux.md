Title: Linux 下的几个游戏模拟器
Date: 2006-12-26 09:52
Author: toy
Category: Apps
Slug: game_emulator_for_linux

前言：我们都是从那个游戏机时代过来的。蹲在地上，拿着手柄，玩着魂斗罗，超级玛丽……

最近想玩电视游戏了。所谓的电视游戏
，也就是小时候玩过的红白游戏机（任天堂游戏机）啦之类的。相信我们玩过魂斗罗或超级玛丽。于是找啊找，找了不少，不止
FC，其他的像是街机啦，SFC 啦（超级任天堂），PCE，PS
啦。看起来都不错，而且在 Linux 下玩比在 Win 下玩好多了。

**FC、任天堂红白机**

Linux 下的模拟器为 fceu（FCE Ultra），而在 Win 下则是 virtuaNES，虽说
fceu 的官方网站有源代码下载，但是因为控制键不方便所以我到
[Linuxfans](http://www.linuxfans.org) 里面下载了一个 fceu
控制键修改版，用着很好。

[![fceu](http://i.linuxtoy.org/i/2006/12/fceu_s.png)](http://i.linuxtoy.org/i/2006/12/fceu.png)

**SFC、超任**

这个模拟器我也是第一次使用，不过看起来很好用，在 Win 下和 Linux
下都有一个跨平台的模拟器：zsnes。

[![zsnes](http://i.linuxtoy.org/i/2006/12/zsnes_s.png)](http://i.linuxtoy.org/i/2006/12/zsnes.png)

[![zsnes](http://i.linuxtoy.org/i/2006/12/zsnes2_s.png)](http://i.linuxtoy.org/i/2006/12/zsnes2.png)

**PCE（PC Engine）**

这个我也没玩过，不过看起来就是比 FC
屏幕解析度更好的游戏机。因为有好多游戏和 FC 相同，并且解析度更高，Linux
下的模拟器为 hu-go!，虽然在 apt
源里有这个，但是不如到官方下载最新的，并且带有图形前端界面。

[![hugo](http://i.linuxtoy.org/i/2006/12/hugo.png)](http://i.linuxtoy.org/i/2006/12/hugo.png)

**PS**

鼎鼎大名的索尼 PS 游戏机，在 Linux 和 Win
下有个跨平台的模拟器，那就是著名的 epsxe。

[![epsxe](http://i.linuxtoy.org/i/2006/12/epsxe_s.png)](http://i.linuxtoy.org/i/2006/12/epsxe.png)

[![epsxe](http://i.linuxtoy.org/i/2006/12/epsxe2.png)](http://i.linuxtoy.org/i/2006/12/epsxe2.png)

**街机类**

因为我是一个超级忠实的 KOF
爱好者，于是少不了一个实用的模拟器，于是找到了这个：gngeo。这个模拟器是专门用来解码
neogeo 的游戏，虽然在 Win 下可以用 kawaks，但是实际上在 Win
下玩实在是有点卡（全屏幕，我的显卡为 savage 16 Mb），但是在 Linux
下却都不卡，并且带有 xgngeo 这个模拟器前端，很不错。几乎就可以和 kawaks
相媲美了（“几乎”的原因是有几个 roms 似乎不能读取）。

[![gngeo](http://i.linuxtoy.org/i/2006/12/gngeo_s.png)](http://i.linuxtoy.org/i/2006/12/gngeo.png)

[![xgngeo](http://i.linuxtoy.org/i/2006/12/xgngeo.png)](http://i.linuxtoy.org/i/2006/12/xgngeo.png)

另外的比方 GameBoy 啦之类的就没有玩了，因为那个实在是不感兴趣。

相关链接：

-   FCE Ultra: <http://fceultra.sourceforge.net>
-   ZSNES: <http://www.zsnes.com>
-   Hu-GO!: <http://freshmeat.net/projects/hu-go/>（官方网站
    <http://www.zeograd.com> 无法访问。）
-   ePSXe: <http://www.epsxe.com>
-   Gngeo: <http://gngeo.berlios.de>
-   XGngeo: <http://www.choplair.org/?XGngeo>

（撰文／[yang](http://yoyoliyang.blogspot.com/2006/12/linux_26.html)）
