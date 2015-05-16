Title: Firefox 36 Beta
Date: 2015-01-16 11:06
Author: lovenemesis
Category: News
Tags: Firefox, Mozilla
Slug: firefox-36-beta

在波澜不经的 Firefox 35 之后（新添加的分享按钮其实还不错），Mozilla
如约将 Firefox 36 推送入 Beta
频道，将首选项改为标签页形式，且重新设计了平板下的界面，并部分实现了 MSE
扩展 API

**桌面版**的变化有：

* 现在可以同步在新标签页上固定的网页  
* 在 Beta 期间的前半阶段，将使用**标签页形式的首选项设计**  
* 移除 `-remote` 选项  
* 如果可能的话不再接受不安全的 RC4 加密  
*
[扩展兼容性做出改变](https://blog.mozilla.org/addons/2015/01/13/compatibility-for-firefox-36/)，为即将到来的[多进程
Firefox
](https://developer.mozilla.org/en-US/Add-ons/Working\_with\_multiprocess\_Firefox)做准备  
* 支持 [ECMAScript 6
Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Symbol)  
* 实现 [unicode-range CSS
描述符](https://developer.mozilla.org/en-US/docs/Web/CSS/unicode-range)、[object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
及
[object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position)、[isolation
CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/isolation)属性、CSS3
[will-change
属性](https://developer.mozilla.org/en-US/docs/Web/CSS/will-change)。  
* 实现 `CSSOM-View` 的滚动行为，允许不使用第三方库的平缓滚动  
* 提升了 ES6 generators 的性能，达到原先的 2 倍  
* 修改了 `const` 的语法，更好的符合 [ES6
规范](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)  
* 实现了部分 Media Source Extensions (MSE) API，可以**在 YouTube
实现原生 HTML5 播放付费内容**，完整支持即将到来  
* 支持 DOM Promises 探查  
* Inspector 的 Markup
视图增加[更多粘贴选项](https://developer.mozilla.org/en-US/docs/Tools/Page\_Inspector#Element\_popup\_menu\_2)  
* CSS 渐变可以在预先相乘的颜色上工作

[英文发布摘要](https://www.mozilla.org/en-US/firefox/36.0beta/releasenotes/)

[官方全平台多语言下载](https://www.mozilla.org/en-US/firefox/beta/all/)

**Android 版本**的变化有：

* **全新设计**的[平板界面风格](http://lucasr.org/2014/12/03/new-tablet-ui-for-firefox-on-android/)  
* 如果可能的话不再接受不安全的 RC4 加密  
*
[扩展兼容性做出改变](https://blog.mozilla.org/addons/2015/01/13/compatibility-for-firefox-36/)，为即将到来的[多进程
Firefox
](https://developer.mozilla.org/en-US/Add-ons/Working\_with\_multiprocess\_Firefox)做准备  
* 支持 [ECMAScript 6
Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Symbol)  
* 实现 [unicode-range CSS
描述符](https://developer.mozilla.org/en-US/docs/Web/CSS/unicode-range)、[object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
及
[object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position)、[isolation
CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/isolation)属性、CSS3
[will-change
属性](https://developer.mozilla.org/en-US/docs/Web/CSS/will-change)。  
* 提升了 ES6 generators 的性能，达到原先的 2 倍  
* 修改了 `const` 的语法，更好的符合 [ES6
规范](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)  
* 实现了部分 Media Source Extensions (MSE) API，可以**在 YouTube
实现原生 HTML5 播放付费内容**，完整支持即将到来  
* CSS 渐变可以在预先相乘的颜色上工作  
* 修复在使用 VPN 或切换网络时的 DNS 解析问题

[英文发布摘要](https://www.mozilla.org/en-US/mobile/36.0beta/releasenotes/)

[官方 Play Store
下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox\_beta&referrer=utm\_source%3Dmozilla%26utm\_medium%3DReferral%26utm\_campaign%3Dmozilla-org)
