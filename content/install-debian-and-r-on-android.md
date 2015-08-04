Title: 在 Android 系统上安装 Debian Linux 与 R （更新 RStudio Server 安装）
Author: lovenemesis
Date: 2015-08-04
Category: Tutorial
Tags: android, debian, R
Slug: install-debian-and-r-on-android
Summary: 要说最近为啥没更新，原因很多，不过真相只有一个：在折腾新购入的平板。这里就描述下如何在 Android 平板上安装原生 Linux 系统以及用于统计及和机器学习的 R 语言环境。

其实在 Android 平板上通过第三方软件，已经可以提供很多类似一般桌面 Linux 系统的工具了。常用的 [Firefox](https://play.google.com/store/apps/details?id=org.mozilla.firefox&hl=en)、[VLC](https://play.google.com/store/apps/details?id=org.videolan.vlc&hl=en)、 [LibreOffice](https://play.google.com/store/apps/details?id=org.documentfoundation.libreoffice&hl=en) 以及[终端模拟器](https://play.google.com/store/apps/details?id=jackpal.androidterm&hl=en)都有 Android 版本，结合 Busybox 也能拥有大部分 coreutils 工具，甚至还有诸如 [Terminal IDE](https://play.google.com/store/apps/details?id=com.spartacusrex.spartacuside&hl=en)这种一站式的开发工具方案（不过不支持 Android 5.0+）。若是想要接近桌面级别的体验的话，比如像在下希望使用的 R 语言环境，还是安装一个完整的 Linux 环境比较好。

在 Android 手机或平板上，若是 Unlock Bootloader 且获取了 root 权限，那么多种的方法可以将亦或完整亦或深度定制各种的 Linux 环境安装上去，网上教程也有不少，不再赘述。本文描述的方法则具有如下特点：

1. **无需 root**，无需修改系统分区或者 Bootloader；
2. 安装的是正常的 Debian Linux ARM 版本，可从官方仓库获得更新，兼容第三方 backport 仓库；
3. 允许**多个 Linux 发行版共存**，非常方便的删除或重建，无需担心在系统或者 SD 卡上有异样残留；
4. 像普通 Android 应用一样运行 Linux 系统，可与其他 Android 应用之间自由切换；
5. Linux 系统服从 Android 系统的电源管理策略（读作：省电）。 

首先请出主角 [GNURoot](https://play.google.com/store/apps/details?id=champion.gnuroot&hl=en) 及 [GNURoot Wheezy](https://play.google.com/store/apps/details?id=champion.gnuroot.wheezy&hl=en)。前者在应用程序级别提供一个虚拟根文件系统，允许在其上运行为其微调的桌面 Linux 发行版；后者则显而易见的是为其打造的 Debian Wheezy 版本。

GNURoot 本身支持多个不同的 Linux 发行版，在下常用的 Fedora 亦在其中。不过由于打包的是古老亦不再维护的 Fedora 17，实在是不推荐使用。至于那个 Debian WheezyX 版本，稍候说明。

GNURoot 的使用方法相当直观。第一步选择要创建的根文件系统，若是没有安装上面提到的 Wheezy 的话，在选择后跳转到 Play Store 提示安装。稍事片刻创建完成后，就可以在第二步选择启动了，记得勾上 "Launch As Fake Root" 的选项。第三个选项则是删除根文件系统，点击后选中的根文件系统就会干净的删除，估计您不会想现在就点击它吧…

不过在点击启动之前，最好确认下您已经准备好了合适的输入设备，因为即将迎接您的仅仅是一个终端模拟器，而安装 R 的操作需要有不少终端的操作。若是有蓝牙键盘最好，没有的话推荐使用这款名为 [Hacker's Keyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=en) 的虚拟键盘，可以提供很多终端下常用的按键。

Debian Wheezy 这个根文件系统生成时间稍早，所以当然一上来是通过 `apt-get` 升级到最新版本了。除此之外，诸如 `less`、`vim` 之类的工具也还是装上才感觉完整了。有几点需要注意的：

1. 默认登录即是 root 账户；
2. 主机的内置存储和 SD 记忆卡等设备被挂载到 `/storage` 下；
3. 由于 Android 系统权限限定，仅能写入内置存储，不能写入外置 SD 卡；
4. 包括 GNURoot 及 GNURoot Wheezy 在内的程序都无法移动到 SD 卡，因为 SD 卡上没有可执行权限的概念。

由于 Debian 针对 Stable 的管理策略，要想用上最新的 R 必须使用 backport 的仓库。根据[Debian Package for R Software](https://mirrors.ustc.edu.cn/CRAN/bin/linux/debian/README.html#debian_wheezy_oldstable)的描述，需要将如下仓库信息添加到 `/etc/apt/sources.list` 文件末尾：

`deb http://<favorite-cran-mirror>/bin/linux/debian wheezy-cran3/`

对于在下的网络来说，既是以下地址：

`deb http://mirrors.ustc.edu.cn/CRAN/bin/linux/debian wheezy-cran3/`

通过 `echo` 加重定向的方式可以非常方便的将其添加到文件末尾。

然后添加加密公钥到：

`apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480`

再下来就是安装了：

`apt-get update`
`apt-get install r-base r-base-dev`

这个过程比较漫长（约200M），一方面是 Debian FTP 的访问速度所限，另一方面则是安装及解包时间了。在耐心等待或者睡一觉之后，就可以开心的在平板上使用 R 语言啦！

对于已经习惯使用图形化 IDE Rstudio 的在下来说，R 终端还是需要熟悉下的：

1. 运行脚本需要使用 `Rscript`，而非 `R CMD BATCH`。
2. 使用 help.start() 可以启动 HTML 的帮助手册页面，可以在 Android 系统环境下的浏览器中查看。
3. 类似的，图形绘制及表格之类的，也可以通过嵌套在 Shiny 的方式输出到 Web 页面，之后在 Android 系统浏览器中查看。

最后说说同一个作者出品的 [WheezyX](https://play.google.com/store/apps/details?id=champion.gnuroot.wheezyx) 和[GNURoot Debian](https://play.google.com/store/apps/details?id=com.gnuroot.debian)。前者是在启动时初始化一个 vnc 服务，使得可以使用本地或远程的 VNC 客户端看到 X 图形化界面。在下尝试了在其基础上安装 LXDE 桌面环境，在极度漫长的安装过程（包含依赖关系近 700M）后失败，无法启动 LXDE。后者则是该名作者的新作品，按照其说明是新的结合及未来的趋势，不过根据评论来看似乎还有不少问题需要处理。

经过这么一番折腾，感觉 Android 平板还是有不少可以把玩和折腾的地方，特别是对 Linux 用户来说。若是您有更多折腾的经历或心得，不妨来稿或者在评论中分享。

### 7 月 22 日更新

在本文发布第三天，GNURoot Debian 发布了新版本 0.2，这两天再次体（zhe）验（teng）了下：

* 与 GNURoot 完全不同，无法延用之前创建的根文件系统，且仅支持 Debian
* 升级到 Debian Jessie 8.1 Stable 版本，且架构支持硬浮点 `armhf`
* 挂载以及和系统交互的方式变化不少，$HOME 分区可以直接在 Android 系统下访问，还有一些奇怪的 `mount` 输出没看懂
* 附带的 Jessie 特别精简，连 `vi` 都没有，创建根分区之后要安装的常用工具不少…
* CRAN Backport 里的 R 貌似只有针对 `armel` 的，而 Jessie Backport 里的版本太老，于是想了想，干脆自己动手编译了 R 3.2.1 版本，总共用时两个半小时，还好
* 至少在我使用的 Z4 Tablet 上，安装部分应用（比如 git, openssh-client）会提示 `Cannot open audit interface`，谷歌说可能跟内核或者挂载有关，已经提交 Issue Report 等反馈…
* 理论上讲 RStudio Server 也可以编译，但是至少需要解决上述的问题才能安装必要的依赖关系。

### 8 月 4 日更新

上个周末 GNURoot Debian 发布了 0.26 版本，解决了之前[反馈的问题](https://github.com/corbinlc/GNURootDebian/issues/5)，意味着可以编译 RStudio Server 了！

* 首先前往 [RStudio 官网](https://www.rstudio.com/products/rstudio/download-server/)下载源代码包。
* 解压到某处之后，**仔细阅读**其中的 INSTALL 说明。
* RStudio 需要 R 的共享库，如果之前手动编译 R 的过程中没加上 `--enable-R-shlib` 选项的话（竟然不是默认启用），重编译先吧…
* 根据说明，可以借助 `dependencies/linux/install-dependency-debian` 文件的内容处理编译 RStudio 的依赖关系。由于 GNURoot Debian 默认没有配置 `sudo`，这里建议还是**手动安装各个依赖**比较好
* 几点需要提醒的：
  1. 没必要特别安装 OpenJDK 6，在编译 R 的时候所用的 OpenJDK 7 即可
  2. 无需担心 AppArmor、Qt SDK 的依赖，Server 版本用不上
* 解决完 debian 文件所描述的后，参照 `common/install-common` 里的内容进一步处理依赖关系，同样还是建议参考，但是手动处理，其实也就是手动执行同目录下的其他以 install 开头的脚本。当然在上一步 debian 脚本中通过仓库解决的就不需要了，比如 boost 和 pandoc
* 此时可以参考 [RStudio 论坛](https://support.rstudio.com/hc/communities/public/questions/200656557-Building-RStudio-on-Ubuntu-Linux-on-ARM)上的解答，包括下载最新版本的 Closure Complier 来替换 `src/gwt/tools`目录中的老版本，已经创建空的 pandoc 目录，都是值得应用的。它还提到了使用 Oracle JDK 8 来加快 GWT 构建，这点我没有尝试，有兴趣也可以用 OpenJDK 8 看看。这篇文档较早，新版本还需要一些 clang 的头文件，也是使用 install 脚本处理就好。
* 全部依赖关系处理结束之后，返回源代码顶层目录，按照 INSTALL 文档的说明，创建 build 目录并调用 cmake 创建编译配置文件，
* 若一切正常，就可以使用 `make install` 开始编译了（没看错，没有 `make` 步骤）。在 Z4 Tablet 上，GWT 构建果真使用了 90 分钟，而 C++ 代码部分的编译用了 6 至 8 小时（具体时间未知，因为中途睡着了…）
* 结束之后，继续按照 INSTALL 文档的说明，创建服务所用的运行账户、添加 init.d 配置文件、创建管理脚本符号链接、创建运行时所必要的目录
* 之后就可以通过 `rstudio-server start` 启动，然后在系统浏览器中输入 ｀127.0.0.1:8787｀，其中 8787 是 rstudio-server 的默认端口号，就能看到熟悉的 RStduio 登录界面啦！
* 不过，别高兴的太早…你会发现 root 账户登录不能，提示需要密码，设置密码后还是不行，创建个全新的普通用户，问题依旧，提示 `Error occurred during transmission`…网上搜到的解决方案提示根分区满了，呃，好像不相关啊…
* 尝试换用 systemd 的启动脚本时收到提示说 dbus 不可用，不知道这个会不会是原因？

所以，RStudio Server 的确可以在 Andriod/GNURoot Debian 环境下正常编译（尽管时间比较长），但是其正常工作，似乎还需要一些研究。
