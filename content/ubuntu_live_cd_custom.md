Title: Ubuntu Live CD 个性化定制全程图解
Date: 2006-10-14 20:52
Author: toy
Category: Tutorials
Slug: ubuntu_live_cd_custom

个性化定制最为明显的好处就在于能够真正适合自己的需要。想要个性化定制
[Ubuntu](http://www.ubuntu.com) 的 Live CD 吗？想要体验 DIY
的乐趣吗？本文将以图解的方式全程为你提供指导与帮助。

选择工具

“工预善其事，必先利其器”。选择一款合适的定制工具，对于普通用户来说尤其重要。这儿有两种
Ubuntu Live CD 的定制工具：[UCK](http://uck.sourceforge.net) 和
[Reconstructor](http://reconstructor.aperantis.com)。前者可以增删 Live
CD 中的语言包和应用程序，后者能够提供从 GNOME
桌面到应用软件的多方面定制功能。本文选择 Reconstructor 作为 Ubuntu Live
CD 的定制工具，读者朋友也可以自行尝试 UCK。

前期准备

在正式定制之前，应该做好这些方面的准备工作：制作或收集需要用到的定制资源，如主题、壁纸、模块等等；Ubuntu
Live CD 的原始 ISO 映像（Reconstructor 支持 6.06 及 6.10）；从
Reconstructor 官方网站下载定制程序；安装 Reconstructor 的使用依赖，如
squashfs-tools、libbogl-dev、mkisofs 等（详见 readme.txt 文件）。

定制过程

-   执行程序  

    ` tar xvzj reconstructor-2.0.tar.gz cd reconstructor-2.0/ sudo python reconstructor.py`  
    Reconstructor
    在启动时会检查使用依赖，并提示用户安装未完成的依赖。接着会进入欢迎页面。
    [![reconstructor
    welcome](http://i.linuxtoy.org/i/reconstructor_welcome_s.png)](http://i.linuxtoy.org/i/reconstructor_welcome.png)
-   创建工作目录

    Reconstructor 默认会将工作目录创建于
    /home/username/reconstructor，另外分别创建 remaster、root、initrd
    三个子目录。工作目录仅在首次使用时才有必要创建，如果是再次使用，则无需创建。因为我们是初次使用，所以勾选其中的三个选项。然后，在
    Live CD ISO Filename 选择先前下载好的原始 Ubuntu Live CD ISO
    映像文件。

    [![reconstructor
    workingdirectory](http://i.linuxtoy.org/i/reconstructor_workingdirectory_s.png)](http://i.linuxtoy.org/i/reconstructor_workingdirectory.png)

-   定制引导屏幕

    引导屏幕这部分可以定制 Live CD Splash 图像、引导选项文字的颜色、以及
    Usplash 图像。需要注意是，Splash 图像要求是 pcx 格式，而 Usplash
    则是编译好的 so 文件（对于 Ubuntu 6.06，Reconstructor
    支持直接生成）。设置后，点击“Apply”按钮以便生效。

    [![reconstructor
    bootscreen](http://i.linuxtoy.org/i/reconstructor_bootscreen_s.png)](http://i.linuxtoy.org/i/reconstructor_bootscreen.png)

-   GNOME 桌面的定制

    GNOME
    桌面包括登录屏幕、桌面、主题三部分的定制。其中，在登录屏幕中可以设置
    GDM 主题、Splash
    屏幕、背景颜色；桌面部分能够定制壁纸和字体；在主题中可以选择 GNOME
    桌面所用的主题及图标。对于这些定制，用户既可以选择系统自带的，也可以使用自己的。从
    [GNOME LOOK](http://gnome-look.org) 上可以找到这方面的丰富资源。

    [![reconstructor
    gnome](http://i.linuxtoy.org/i/reconstructor_gnome_s.png)](http://i.linuxtoy.org/i/reconstructor_gnome.png)

-   定制 Apt 源

    通过定制 Apt 源，就能够直接在 Live CD
    中使用这些扩展的源，以便安装需要的应用程序。在你需要使用的源前打勾选择即可。对于其他的源，可以输入到下面的文本框中。

    [![reconstructor
    apt](http://i.linuxtoy.org/i/reconstructor_apt_s.png)](http://i.linuxtoy.org/i/reconstructor_apt.png)

-   优化启动及关机过程

    在启动部分，可以选择在系统启动时需要运行的守护进程，如
    ppp、laptop-mode 等。同时，Reconstructor 也能够对关机过程进行优化。

    [![reconstructor
    optimization](http://i.linuxtoy.org/i/reconstructor_optimization_s.png)](http://i.linuxtoy.org/i/reconstructor_optimization.png)

-   设置用户及口令

    切换到 Live CD 选项页，对在 Live CD
    中要用到的用户、口令及主机名进行设置。

    [![reconstructor
    livecd](http://i.linuxtoy.org/i/reconstructor_livecd_s.png)](http://i.linuxtoy.org/i/reconstructor_livecd.png)

-   定制应用程序

    Reconstructor
    的模块功能可以让用户按需定制应用程序，如安装程序、删除程序等。普通用户可以使用
    Reconstructor
    提供的现有模块：包括图像处理软件、生产力软件、多媒体软件、网络软件、服务器软件、及其他软件等。如果现有模块不能满足你的要求，那么可以通过输入安装或删除命令来实现对于软件的定制。

    [![reconstructor
    modules](http://i.linuxtoy.org/i/reconstructor_modules_s.png)](http://i.linuxtoy.org/i/reconstructor_modules.png)

-   构建选项

    注意以上每一个部分的定制都需要点击“Apply”按钮。现在按“Next”进入构建选项页。在此设置
    Ubuntu Live CD ISO
    文件的保存路径、名称、架构。如果所有的都没有问题，那么继续下一步吧。

    [![reconstructor
    build](http://i.linuxtoy.org/i/reconstructor_build_s.png)](http://i.linuxtoy.org/i/reconstructor_build.png)

-   定制结束

    此时，需耐心等候一阵，直到看到 Finished 页面。

    [![reconstructor
    finished](http://i.linuxtoy.org/i/reconstructor_finished_s.png)](http://i.linuxtoy.org/i/reconstructor_finished.png)

最后测试

在 Ubuntu Live CD
定制结束后，先不要忙着刻盘，在虚拟机中测试一下，如果确认没有问题，那么就烧录并与朋友分享吧。
