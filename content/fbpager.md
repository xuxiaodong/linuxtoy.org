Title: Fluxbox 的小配件——FbPager
Date: 2006-09-04 20:14
Author: toy
Category: Tutorials
Slug: fbpager

[FbPager](http://www.fluxbox.org/fbpager/) 是 Fluxbox
中一个相当酷的小配件。之所以这样说，原因有二：

1.  FbPager 与 Fluxbox
    一样，支持透明特性，这样能够与其融合在一起，非常之漂亮。
2.  FbPager 支持鼠标操作，你可以在每个 Pager
    中随意拖动某个窗口，相当之好玩。

说到这儿，可能你有点想知道这个 FbPager 究竟是什么东东了吧？其实，FbPager
就像是扩展的工作区。它除了具备工作区的功能之外，还带来了以上一些好玩的特性。先来看个图：

![FbPager](http://i.linuxtoy.org/i/fbpager.png)

假如你想在自己的 Fluxbox 中尝试它，可以按以下步骤进行：

1.  安装：`sudo apt-get install fbpager`。
2.  启动：在终端中输入 fbpager 即可。
    第一次启动由于程序不能找到 ~/.fluxbox/fbpager
    配置文件可能会报错，没关系，我们稍后建立一个就是了。
3.  配置：对于 FbPager 的控制就是通过上面的 ~/.fluxbox/fbpager
    文件进行的。

    示例 1：如果要让 FbPager 具有透明效果，只需在该文件中加入
    `fbpager.alpha: 64`。

    示例 2：在默认情况下，FbPager
    是水平排列工作区的，如果要让其垂直排列，那么在文件中加入
    `fbpager.workspacesPerRow: 1`。

    除此之外，你还可以从很多方面对 FbPager
    进行配置，如更改工作区的大小、颜色等。详细参阅下面的内容：

    [php]  
    fbpager.alpha: 255  
    fbpager.x: 0  
    fbpager.y: 0  
    fbpager.workspace.width: 64  
    fbpager.workspace.height: 64  
    fbpager.workspacesPerRow: 6400  
    fbpager.followDrag: false  
    fbpager.followMove: false  
    fbpager.changeWorkspaceButton: 11  
    fbpager.raiseWindowButton: 2  
    fbpager.lowerWindowButton: 3  
    fbpager.closeWindowButton: 3 3 1  
    fbpager.exitButton: 1 3 3  
    fbpager.nextWorkspaceButton: 4  
    fbpager.prevWorkspaceButton: 5  
    fbpager.moveInWorkspaceButton: 1  
    fbpager.dragToWorkspaceButton: 2  
    fbpager.align: LeftToRight  
    fbpager.color: white  
    fbpager.windowColor: white  
    fbpager.focusedWindowColor: white  
    fbpager.windowBorderColor: black  
    fbpager.backgroundColor: darkgray  
    fbpager.currentBackgroundColor: lightgray  
    fbpager.multiClickTime: 250  
    fbpager.icons: false  
    fbpager.windowBorderWidth: 1  
    [/php]

4.  提示：你不需要每次手动启动 FbPager，可以考虑让其开机便自动运行，将
    `[startup] {fbpager}` 加入到 apps 文件中即可解决。
    另外，直接在 Pager
    中拖动小矩形，便可以定位程序窗口在桌面的位置。而且，使用鼠标滚轮可以切换每个
    Pager。

