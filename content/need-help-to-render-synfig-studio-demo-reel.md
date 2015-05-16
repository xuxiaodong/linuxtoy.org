Title: Synfig Studio Demo Reel 动画渲染求助
Date: 2011-12-01 15:55
Author: lovenemesis
Category: AskLinuxtoy
Tags: synfig
Slug: need-help-to-render-synfig-studio-demo-reel

[Synfig Studio](http://www.synfig.org/cms/) 是一款免费且开源的 2D
动画制作软件，近期社区计划制作第二款宣传视频，需要诸位朋友协助完成渲染工作。*感谢
jcome 来稿*

Synfig Studio Demo Reel 是 Synfig 社区用来演示 Synfig Studio
软件功能的视频，其中挑选收录由 synfig 社区艺术家用 Synfig Studio
制作的精彩的动画视频。[第一个版本的 demo
reel](http://www.synfig.org/cms/en/gallery/animation/synfig-studio-demo-reel/)
是在多年前制作的，现在显得有些过时了。因为自从这个版本的 demo reel
之后，Syfnig Studio
发布了多个版本，带来了不少的新功能，而且动画艺术家们也制作了更多的更精彩动画作品，为了让便于大家能直观了解当前的
Synfig Studio 和 Synfig 社区，我们正在**着手准备第二个 Demo Reel
的制作**，因为软件渲染需要大量的 cpu 资源，我们请求童鞋们伸出援助之手。

我们以一个蜘蛛的动画片段作为开始，第一次的任务是渲染这个动画的第
5941～6162 帧的长度，共 222 帧画面。

[![](http://linuxtoy.org/img/2011/12/synfig-dem-reel-2.png "synfig-dem-reel-2")](http://linuxtoy.org/img/2011/12/synfig-dem-reel-2.png)

图：动画第 6000 帧的截屏

**基本要求：**

有安装 Synfig Studio的系统（推荐 Linux 发行版）安装[最新版本的 synfig
studio](http://www.synfig.org/cms/en/download/stable) ：

-   多数 Linux 发行版官方仓库都有 Synfig
    Studio，但是可能不是最新的稳定版；
-   在上面链接中是最新的稳定版，有 rpm, deb 以及免安装的 bin 格式。

[32 位 RPM 朝内镜像下载](http://dl.dbank.com/c0nwwd0gd7)  
[64 位 RPM 朝内镜像下载](http://dl.dbank.com/c0k8dxrk91)  
[32 位 DEB 朝内镜像下载](http://dl.dbank.com/c0cub0wvvu)  
[64 位 DEB 朝内镜像下载](http://dl.dbank.com/c0wbae3lm1)

**动画源文件：**

蜘蛛动画的其中一个片段，因为是矢量的所以非常的小才 2.9MB 大小，

**渲染方式（以渲染第5941～5951共10帧为例）：**

-   命令：`$ synfig spiderboat.sifz --start-time 5941f --end-time 5951f -w 1920 -h 1080 -o render/spiderboat.png`
-   渲染的结果是PNG图片序列，每个图片在1.8MB左右，幅面时 1920 x
    1080，文件名字是自动带帧数，如 spiderboat.5941.png；
-   渲染是帧为单位的，是可以随时中断再继续的。

**用时参考：**

-   在 MacbookPro 2.66 GHz Intel Core 2 Duo, 8GB 133 DDR3 Fedora16 x64
    的平台上的渲染速度是：15~20分钟/帧；
-   这个阶段的 222 帧动画分解成多个小任务，以20帧为一个认领单位。

感兴趣的朋友请直接回复说明联系方式或者电邮 jcomee at gmail
