Title: 重装上阵：Battle Tanks 0.8
Date: 2008-09-11 22:49
Author: lovenemesis
Category: Games
Tags: btanks
Slug: battle-tanks-08

Battle Tanks
是一款有趣的桌面游戏。你可以从三种不同的重型载具里选择其一，然后用五花八门的武器将你对手轰出战场！
原创的卡通风格图像，动感劲爆的音乐，多样化风格的AI，以及免费的互联网死亡竞赛，无限乐趣尽在
Battle Tanks～

**特点**

-   *多人游戏* “Battle Tanks”
    从一开始就为多人游戏而设计。局域网联机、互联网联机以及分屏对战，以及独特的混合模式：在两个人使用分屏模式游戏的同时，还可以邀请其他人通过局域网加入一起对战！提供了四种流行的对战模式：死亡竞赛，组队死亡竞赛，夺旗赛及协作赛。
-   *跨平台* “Battle Tanks” 是一款跨平台游戏。不管你是来自 Windows,
    Linux 还是 Mac 的玩家，战场上可不管什么操作系统，只认武器。
-   *免费分发及源代码开放* 多人游戏版本是在 GNU GPL
    协议下发布的。第一，这意味着你可以免费下载并与你的朋友们分享，而没有任何限制和花费。其次，完整的游戏源代码可以免费获得。这意味着任何懂得
    C++
    的人都可以修补不足，或许还可以发现开发者专为好奇的玩家准备的惊喜～
-   *怀旧情调* “Battle Tanks”
    的开发者们喜欢上个世纪那些好玩的街机游戏，所以他们会十分努力的去再铸这些儿时经典的辉煌。

**出彩的特征**

-   *三种载具，每种都有不同的特殊能力*：坦克、Shilka防空装甲车和火箭炮。
-   *大量的武器*: 四种弹药、六种火箭弹、空中打击、地雷等等。
-   *13张多人对战地图*：9张死亡竞赛，4张协作模式，覆盖了包括城市、乡村、森林、沙漠等等场景。
-   *充满交互游戏世界*：道路上有交通车辆，建筑物也可以被摧毁，以及变化的天气……
-   *多种战争对象*: 步兵、载具、直升机等等。
-   *支持键盘和手柄*

[![](http://i.linuxtoy.org/i/2008/09/scr0001-big-300x224.jpg)](http://i.linuxtoy.org/i/2008/09/scr0001-big.jpg)

[![](http://i.linuxtoy.org/i/2008/09/scr0011-big-300x224.jpg)](http://i.linuxtoy.org/i/2008/09/scr0011-big.jpg)

[![](http://i.linuxtoy.org/i/2008/09/scr0018-big-300x225.jpg)](http://i.linuxtoy.org/i/2008/09/scr0018-big.jpg)

**官方网站及下载地址**见[这里](http://btanks.sourceforge.net/blog/)。

**PS:**这个是其中Shilka防空装甲车的真实图片，来自维基百科。

[![](http://i.linuxtoy.org/i/2008/09/300px-zsu-23-4_shilka_togliatti_russia-2.jpg)](http://i.linuxtoy.org/i/2008/09/300px-zsu-23-4_shilka_togliatti_russia-2.jpg)

**附： Fedora 9 i686 编译方法**

-   首先，从上面下载源代码包，用 tar xf 解包后进入生成的目录。
-   安装必要的依赖包。 打开一个终端，输入 su -c ' yum install SDL-devel
    scons expat-devel lua-devel smpeg-devel SDL\_image-devel
    libogg-devel libvorbis-devel'，输入管理员密码后下载安装。
-   在源代码目录下输入 scons prefix="/usr" 开始编译。
-   如果编译无错误，输入 su -c 'scons install‘ 安装。之后输入 btanks
    就可以开始游戏了。

