Title: WebQQ 桌面化（更新最终效果图）
Date: 2009-11-17 00:26
Author: lovenemesis
Category: Instant Messenger, Tips, Tutorials
Tags: alltray, Prism, webqq
Slug: webqq-desktop-integration

WebQQ
做为腾讯今年全新推出的产品，由于它跨平台的特性，从内测起就得到在下的关注。本文将阐述如何用两个小软件将
WebQQ 更好的与 Linux 桌面整合起来。

所谓桌面化，个人理解就是将网络应用与现有桌面本地应用结合到一起，脱离浏览器运行。本文分两步，第一步首先是将其拨离浏览器，创建桌面快捷方式；第二步是增加最小化系统托盘及新消息提示功能。

**创建桌面图标**

目前将网络应用扩展到桌面是一个趋势，存在着很多解决方案，本文以 Mozilla
Prism 为例，类似的方法同样适用于 Google Chrome 。

**1.** 到 [Mozilla Prism](http://prism.mozilla.com/) 的网站上下载
Prism，点击 Download Now 之后会提示有两种，一种是以 Mozilla Firefox
扩展的方式，适合已经安装有 Firefox
的朋友；一种是以独立程序的方式，适合尚未安装或不需要 Firefox
浏览器的朋友。

这里选择第一种。下载后重新启动 Firefox 以完成安装。

**2.** 打开 [WebQQ](http://web.qq.com/) 的页面，点击 Firefox
菜单栏上的“工具”-“Convert Website to
Application...”，弹出一个对话框，如下图：

[![](http://i.linuxtoy.org/images/2009/11/screenshot-prism-mozilla-labs-280x300.png)](http://i.linuxtoy.org/images/2009/11/screenshot-prism-mozilla-labs.png)

只需要在 Name 一栏填写想要的程序名，比如 "WebQQ"；在 Create Shortcuts
下面记得勾选 Desktop，确认创建桌面快捷方式，点击 OK 即可。

此时桌面上应该已经出现了名为 Webb.desktop
的文件，双及它会提示是否要运行该来源不明软件，点击 Mark as
Trusted。之后图标会变成 WebQQ
的样子，此时再次双击，就会以一个独立进程打开 WebQQ
页面，登陆即可。如下图：

[![](http://i.linuxtoy.org/images/2009/11/screenshot-webqq-389x300.png)](http://i.linuxtoy.org/images/2009/11/screenshot-webqq.png)

**注意：**这一步出现问题的童鞋（比如总是打开固定的某个页面而不是 WebQQ
页面），请手动编辑 .desktop 文件，将其中的 firefox 替换成
xulrunner。详情参考文末解释。

**创建系统托盘提示**

大多数即时通讯软件都具有最小化到系统托盘的功能，并且新消息到来的时候会有弹出提示。接下来要将通过
[AllTray](http://linuxtoy.org/archives/alltray.html) 这款小软件将 WebQQ
也赋予这个实用功能。

**1.** 首先当然要安装
alltray，它已经被包含到绝大多数发行版的软件仓库里。 Fedora
里在终端运行如下命令即可：

`su -c 'yum install alltray'`

**2.** 安装完成后，可以在“应用程序”-“附件”
里找到它，点击后会产生一个小窗口，提示“点击需要最小化到系统托盘的窗口”，照它所说的做，点击下
WebQQ 的窗口，立刻就最小化到系统托盘了~

怎么样？很方便吧？但是每次启动后还要启动 Alltray
点一下，有些麻烦。而且别忘记我们还需要有新消息提示。

**3.** 这里就需要 alltray 的第二种运行方式了: `alltray [程序名] [选项]`

通过 man 手册得知组合以下几种选项可以达到托盘区新消息提示的效果：

`-s ` 在首次启动时不隐藏主窗口。正是我们想要的，总需要输入QQ号和密码吧……

`-i ` 使用一个 PNG 文件做为托盘区图标，*后接 PNG
文件路径*。看来这里需要知道 WebQQ
的图标位置，用任意文本编辑器打开桌面上先前创建的 .desktop
文件，查看` Icon=` 一行即可得知。

`-l ` 使用较大图标，当图标尺寸大于 24*24 时使用。

`-st ` 允许在所有可见工作区显示。也是我们想要的。

`-t `
当窗口标题变化时显示提示，*后接提示显示时间，单位秒*。通过这个选项可以实现来新消息时的弹出提示，因为
WebQQ 会在有新消息时改变窗口标题。

**4.** 了解完 Alltray 的第二种模式，开始动手修改 WebQQ.desktop
文件。用任意文本编辑器打开桌面上的 WebQQ.desktop
文件，在` Exec= `这行的已有内容的前面添加 `"/usr/bin/alltray"`
，用空格和已有内容隔开；再在已有内容的最后添加上面讨论的那些选项。比如我的` Exec= `行经过修改后变为：

`Exec="/usr/bin/alltray" "/home/lvp/Apps/firefox/firefox" -app "/home/lvp/.mozilla/firefox/hnvzquts.default/extensions/refractor@developer.mozilla.org/prism/application.ini" -override "/home/lvp/.webapps/webqq@prism.app/override.ini" -webapp webqq@prism.app -i "/home/lvp/.webapps/webqq@prism.app/icons/default/webapp.png" -t 5 -s -st`

其中斜体部分是我添加的内容。 -i 后是用做托盘区图标的 PNG
文件地址，用下面 `Icon=` 一行的地址即可；-t 5 代表当标题变动时显示5
秒钟的提示；-s 代表首次运行时不隐藏窗口，这样我可以输入号码和密码；-st
代表在所有工作区可见。保存并退出。

最终效果图1：

[![](http://i.linuxtoy.org/images/2009/11/webqq-message-400x84.png)](http://i.linuxtoy.org/images/2009/11/webqq-message.png)

最终效果图2：

[![](http://i.linuxtoy.org/images/2009/11/webqq-qun-400x91.png)](http://i.linuxtoy.org/images/2009/11/webqq-qun.png)

**完成**

此番设置之后，双击桌面上的 WebQQ 即可直接连接至 WebQQ
页面。点击窗口关闭按钮会最小化到系统托盘区。当有新消息时会有弹出提示，持续5秒钟。需要退出
WebQQ 时，右键点击系统托盘区图标选择 Exit
即可。所有的操作同本地安装的即时通讯软件一样，完全整合到现有桌面环境中了~

**PS:** 有朋友说用 Prism 看不了 Flash，这个肯定是可以的，下图为证。

[![](http://i.linuxtoy.org/images/2009/11/screenshot-youtube-ian-brown-stellify-389x300.png)](http://i.linuxtoy.org/images/2009/11/screenshot-youtube-ian-brown-stellify.png)

出现问题可能是跟 Flash 插件的安装位置位置有关，一般将其放置到
`/usr/lib/mozilla/plugins` 这个位置大多数软件都可以识别。

**PS2:** 有些朋友使用发行版提供（比如 Ubuntu 或者 Fedora 预装的）的
Firefox 时会遇到无法正常启动 Prism
创建网页窗口的情况，表现为总是打开一个固定的主页。此时需要修改创建的
.desktop 文件，**将其中的 firefox 替换成 xulrunner** ，如下：

`Exec="/usr/bin/alltray" "/usr/bin/xulrunner" -app "/home/lvp/.mozilla/firefox/hnvzquts.default/extensions/refractor@developer.mozilla.org/prism/application.ini" -override "/home/lvp/.webapps/webqq@prism.app/override.ini" -webapp webqq@prism.app -i "/home/lvp/.webapps/webqq@prism.app/icons/default/webapp.png" -t 5 -s -st`
