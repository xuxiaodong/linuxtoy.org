Title: Mozilla Labs Jetpack 介绍
Date: 2010-01-12 08:21
Author: lovenemesis
Category: Firefox Extension
Tags: jetpack, Mozilla
Slug: mozilla-labs-jetpack-introduction

即将正式发布的 [Mozilla Firefox
3.6](http://www.mozilla.com/en-US/firefox/all-rc.html/) 内置了 Mozilla
Labs 孵化项目之一 [Personas](https://mozillalabs.com/personas/)；
[Prism](https://mozillalabs.com/prism/) 项目在本站也多次介绍
。今天介绍另一个 Mozilla Labs 正在孵化的项目：
[Jetpack](https://jetpack.mozillalabs.com/) 。

目前的 Extension
附件组件框架固然无比灵活，但是存在的一些弊端，诸如：对浏览器启动速度和安全性的影响；修改扩展之后必需的重启；每次版本更新时扩展的兼容性。这些因素促使
Mozilla
构思一套全新的附加组件框架，期望在未来部分取代当下的扩展体系，Jetpack
就因此而诞生。Jetpack 可以显著简化当前的 Firefox
附件组件开发，只需要懂基本的 HTML、CSS 和 JavaScript 即可开发出实用的
Firefox 附件组件。

大致浏览了下项目主页上的演示视频和
Demos，实现诸如广告过滤、图像编辑和视频过滤等功能变的十分简单（区区20行代码），同时控件的风格也和
Firefox 整体得到统一。用户可以随时安装、更新、启用/禁用 Jetpack
扩展而无需重启 Firefox。

项目主页上提供了[教程](https://jetpack.mozillalabs.com/tutorial.html)、[范例](https://jetpack.mozillalabs.com/demos.html#)和
[API](https://developer.mozilla.org/en/Jetpack/)，感兴趣的朋友可以开始琢磨了。关联库方面目前仅有
Twitter 。

目前 Jetpack
以扩展方式实现（[点此下载](https://jetpack.mozillalabs.com/install.html)，支持
Win32、Linux、Mac OS X），何时并入 Firefox 本身未知。

消息来源：[The
Register](http://www.theregister.co.uk/2010/01/11/mozilla_extensions_future/)
