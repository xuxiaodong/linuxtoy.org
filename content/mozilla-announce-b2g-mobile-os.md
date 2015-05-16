Title: Mozilla 正式宣布 B2G 手机系统
Date: 2012-02-29 13:38
Author: lovenemesis
Category: Embedded
Tags: b2g, Mozilla
Slug: mozilla-announce-b2g-mobile-os

本站[先前介绍的 Mozilla Boot-to-Gecko
智能手机系统](http://linuxtoy.org/archives/mozilla-boot-to-gecko-os.html)正式面世，硬件合作厂商业已确定。

Mozilla 在巴塞罗那举行 Mobile World Congress 2012 上[对外正式宣布
Boot-to-Gecko
项目](http://blog.mozilla.com/blog/2012/02/27/mozilla-in-mobile-the-web-is-the-platform/)，并在刷新固件
Samsung Galaxy S II 设备上展示的雏形：

[MWC 2012 B2G
样机试玩视频](http://www.youtube.com/watch?v=OAaH5vikEOM)（[天朝镜像](http://v.youku.com/v_show/id_XMzU3Nzc4MjE2.html)）

[Engadget 6
分钟试玩视频](http://www.engadget.com/2012/02/28/mozilla-boot-to-gecko-hands-on-video/)（注意
3：42 时展示 Keyboard
配置，从中可以看到**具备繁体中文注音输入法和简体中文拼音输入法**）

想要在桌面上体验 B2G？只需要下载实现了新 Mobile HTML5 API 的 [Firefox
Nightly](http://nightly.mozilla.org/) 和 [Gaia UI
源代码](https://github.com/andreasgal/gaia)，然后打开其中的
`homescreen.html` 文件即可。

此外 Mozilla 还宣布其业界合作伙伴 Adobe 及 Qualcomm 将加入到 B2G
项目中来协作开发首部原型机，运营商 Telefónica 也在发布会上表达了将在
2012 年合作发布首台平台参考机的意图。可以预见的是该平台参考机会和当前的
Galaxy S II 有较大差异。

配合 B2G 项目，Mozilla 在过去的时间里首先宣布了[无需密码的身份认证系统
BrowserID](https://wiki.mozilla.org/Identity/BrowserID) 从 Mozilla Labs
毕业，并[改名为 Mozilla
Persona](http://identity.mozilla.com/post/18038609895/introducing-mozilla-persona)，原先[无需重启的主题
Personas
将会有一个新名字](http://blog.mozilla.com/addons/2012/02/02/renaming-personas/)。

其次，[操作系统及运行设备中立的网页程序商店 Mozilla
Marketplace](https://marketplace.mozilla.org/en-US/login?to=/en-US/developers/)
进入[开发软件提交阶段](http://hacks.mozilla.org/2012/02/mozillamarketplace-open-for-app-submissions/)。相比其他现有的软件商店，Mozilla
Marketplace 有如下特点：

-   允许作者将网页程序放置在指定的第三方站点。
-   允许用户为免费程序进行捐助。
-   使用价格区间的方式而非实时兑换的方式处理不同地区的支付货币。
-   将使用 [PayPal
    做为支付手段](https://developer.mozilla.org/en/Apps/Marketplace_Payments)。

[更多桌面运行截图](http://arstechnica.com/business/news/2012/02/first-look-mozillas-boot2gecko-mobile-platform-and-gaia-ui.ars)

[本站先前报道](http://linuxtoy.org/archives/mozilla-boot-to-gecko-os.html)

[B2G 主页](http://www.mozilla.org/en-US/b2g/)

[B2G 系统源代码](https://github.com/andreasgal/b2g)

[Gaia UI 源代码](https://github.com/andreasgal/gaia)

**FAQ**

**这个和 Open webOS 有什么不同呢？**

webOS 使用 Enyo 固然也是基于 HTML5 + JavaScript
实现的，具有一定的跨平台跨浏览器功能，但是对于设备特殊功能（比如拨号、蓝牙传输等）的访问是通过自定义的
API 实现的，并未标准化。意味着若是 Web
程序使用了这些特殊功能的话，将只能在 webOS 设备上运行。而 Mozilla 则和
W3C 紧密合作推进
[WebAPI](http://linuxtoy.org/archives/mozilla-webapi.html)的，意味着针对
B2G 编写的 Web 程序将可以运行在包括 Firefox for Mobile
在内的任何浏览器和手持设备上。

此外一个区别就是 webOS 使用 WebKit 做为网页渲染引擎而 B2G 使用的是
Gecko。

**是不是意味着即将能看到 Firefox Phone？**

不是，值得注意的是这是一个项目，而不是产品。B2G 是**为推动 HTML5
在移动设备特定 API 发展的前瞻性项目**，希望能借此为 Web
开发者创建和原生程序开发者一样拥有大量 API
的开放式、标准化开发平台，扩展 Web 程序的适用范围。B2G 取得的成果将通过
W3C 的标准化过程用于其他各种浏览器和移动操作系统上。

**对于普通用户 B2G 有什么意义？**

对于普通用户来讲 B2G
代表未来与设备和平台无关的移动互联网体验，购买的一个 Web
程序，将可以在任何通过 Persona
授权的设备上运行，不再会因为更换手机操作系统而不得不购买新平台的相同程序。

*消息来源：*[Mozilla
Hacks](https://twitter.com/#!/mozhacks/status/174485168113979392)
