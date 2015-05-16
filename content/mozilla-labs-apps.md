Title: Mozilla Labs: Apps
Date: 2011-12-18 22:46
Author: lovenemesis
Category: Screenshots
Tags: html5, Mozilla
Slug: mozilla-labs-apps

Mozilla 试验室推出 Apps 项目，实现桌面浏览器和 Android 系统间无缝的
HTML5 应用程序生态圈。

Apps 项目提供：

-   横跨桌面浏览器、手机及平板设备等多种类型设备的富 HTML5 应用体验。
-   使用 HTML5, CSS 和 JavaScript 网页开放技术和资源。
-   提供具有选择性的，简化的应用程序分发方式。

简单来说，Apps 项目包含以下元素：

**应用描述文件(App Manifest)**

[![](http://linuxtoy.org/img/2011/12/manifest.png "manifest")](http://linuxtoy.org/img/2011/12/manifest.png)

JSON 格式的描述文件，和 W3C Widgets 和 Chrome Web Store
的格式类似，Mozilla 非常希望能标准化该类用途 JSON 文件的格式。

**MOZAPPS API**

引入一组位于 `navigator` 下的新 DOM API，实现：

-   允许网站发出应用程序安装请求。
-   允许用户明确授权的页面执行应用程序管理工作。

**HTML5 App 运行时环境**

所谓运行时环境，只是一个实现了上述 MOZAPPS API 的 JavaScript
脚本，可以**方便的部署到需要调用 MOZAPPS API
执行程序安装操作的网站上，比如你自己的私人博客**。当用户在使用了该运行时环境的网站上点击安装时，会触发如下对话框：

[![](http://linuxtoy.org/img/2011/12/html5.png "html5")](http://linuxtoy.org/img/2011/12/html5.png)

**调控面板(Dashboard)**

使用 icongrid 库撰写的应用程序管理面板，可以在这里完成重新启动 Web
程序，调整位置，删除等操作。

[![](http://linuxtoy.org/img/2011/12/dashboard.png "dashboard")](http://linuxtoy.org/img/2011/12/dashboard.png)

**桌面 Firefox 运行时环境**

如果使用桌面版 Firefox
的话，用户可以安装该扩展获得更佳的安装体验，如下图：

[![](http://linuxtoy.org/img/2011/12/runtime-firefox.png "runtime-firefox")](http://linuxtoy.org/img/2011/12/runtime-firefox.png)

此外，和先前的 [Prism](https://mozillalabs.com/prism/)
项目类似，它还将依据操作系统，创建对应的原生风格的启动器，比如 Dock
图标或者 EXE 文件等。

**Android 平台运行时环境**

Mozilla 希望用户选择了某个 Web
应用，不仅可以在桌面浏览器中使用它，在手机、平板电脑等移动设备上照样可以使用。该
Android 运行时环境是一个原生 Android 程序，允许用户安装、运行和管理
Mozilla Apps 应用。

[![](http://linuxtoy.org/img/2011/12/store-android.png "store-android")](http://linuxtoy.org/img/2011/12/store-android.png)

它将为每个安装的 Mozilla 应用创建对应的应用程序图标，和原生的 Android
程序一样，点击将在嵌入式 Web 环境中运行：

[![](http://linuxtoy.org/img/2011/12/roundball.png "roundball")](http://linuxtoy.org/img/2011/12/roundball.png)

**应用同步(AppSync)**

通过利用最新的[分布式认证系统
BrowserID](https://browserid.org/)，用户的应用程序将在关联的 Apps
运行时环境间**自动同步，无需手动重复安装**。

[![](http://linuxtoy.org/img/2011/12/appsync.png "appsync")](http://linuxtoy.org/img/2011/12/appsync.png)

**应用市场(App Marketplace)**

和 Mozilla 附加组件中心类似，Mozilla 提供了一个分发 HTML5 Web 应用的
[App Marketplace](http://apps-preview.mozilla.org/)，开发者只需要提交
Manifest 描述文件，用户就可以在这里实现查找、安装和评论等功能。

如果想要出售 Web 应用也是没有问题的，**Mozilla 正在和 PayPal
协商支持在各个国家和地区的购买**。因为使用的是同样的 MOZAPPS
API，开发者完全可以实现类似的分发平台和程序内账单系统。

**更多后台技术细节、代码及下一步计划，请见[详细英文介绍](http://kix.in/2011/12/15/behind-the-mozilla-apps-developer-preview/)**

[Mozilla Labs Apps 项目首页及视频介绍](https://apps.mozillalabs.com/)
