Title: Web 测试与浏览自动化
Date: 2009-04-27 11:06
Author: toy
Category: Reviews
Slug: web-test-and-browser-automation

{撰文/zhichyu}

一直对网络机器人之类的东西比较感兴趣。可以实现定时登录某站点捞积分，还可以提高测试
Web 站点效率（虽然我目前不做这一块）。我目前了解的有以下几个实现途径：

**(1) JavaScript**

所有主流浏览器对嵌入 JavaScript 的支持比较一致，对 JavaScript 暴露了 DOM
访问 API 以及浏览器操作 API。所以“JavaScript”这条路比较好走。但由于
JavaScript
不能访问本地文件（安全性考虑）等限制，我无法做“登录某站点后下载某文件”之类的操作。JavaScript
相关的 Web 自动化工具有：

*
[zope.testrecorder](http://pypi.python.org/pypi/zope.testrecorder)：一个跨浏览器
(IE, Firefox, Safari) JavaScript 程序，记录浏览器事件 (点击和输入文字等)
以及测试断言
(这个文本框应包含这个文字，那个复选框应不应被勾选等)。必须安装 Zope 这个
Web Server，再访问 zope.testrocoder 这个组件，然后输入任意 URL
开始记录测试。但是安装和配置 Zope 太麻烦了。需要配合
[Selenium](http://www.openqa.org/selenium/)（一个开源的 Web 测试框架）或
zope.testbrowser（见下文）使用。  
* [JsUnit](http://www.jsunit.net/)：设计为测试静态或生成的 HTML
文档，不能与实际的 Web Server 交互。

**(2) 控制浏览器**

IE 和 Firefox 都提供了编程接口以便外部程序控制其行为。

* [MSDN](http://msdn.microsoft.com/en-us/library/aa752084(VS.85).aspx)
给出了 IE 的 COM 接口以及 VB 控制 IE 的例子。pywin32 以 Python 包装了
COM 等机制，所以用 [Python 操作 IE
也是可行的](http://www.evilbitz.com/2006/10/22/python-ie-automation-thorough-tutorial/)。[PAMIE](http://pamie.sourceforge.net/)
对 pywin32 进一步包装，控制 IE 更加方便。关于 Python 的 COM
编程，请参考《Python Programming on Win32》一书。另外该书的 Chapter 21.
Active Scripting 还描述了怎样把 Python 嵌入 IE（受限于安全性，嵌入
Python 不允许导入任何模块，所以并不能提供比 JavaScript
更多的功能）。另外注意： IE 7 及以上版本默认不允许 COM
控制，这样打开：Tools --> Internet Options --> Security --> Security
for this zone 修改为"Medium"。  
*
[XPCOM](https://developer.mozilla.org/en/Creating\_XPCOM\_Components)
是访问 Gecko 库、嵌入或扩展 Gecko
的方法。[PyXPCOM](https://developer.mozilla.org/en/PyXPCOM) 包装了 XPCOM
机制。FireFox 等以 Gecko 作为 Web 排版引擎，所以可以通过 XPCOM
来控制它们。这方面资料较少，我至今还没有在 Google 上发现通过 PyXPCOM
控制 Firefox 的例子。

**(3) 模拟浏览器**

浏览器的重定向、表单和 Cookie 等行为比较好模拟，但 Frame、DOM
访问、JavaScript 和 JavaApplet
等就越来越难模拟了。以下按照模拟能力降序排列：

* [HttpUnit](http://httpunit.sourceforge.net/)（Java 实现，配合
JUnit）：支持基本 HTTP 认证、简单的 JavaScript。  
* [zope.testbrowser](http://pypi.python.org/pypi/zope.testbrowser)
是一个 Zope 组件但可脱离 Zope 单独使用。支持简单 DOM
(含表单)、Cookie、定制 HTTP 请求。  
* [WebUnit](http://webunit.sourceforge.net/)（Python 实现，配合
PyUnit）：DOM 方面仅支持表单，其他能力与 zope.testbrowser 相当。  
* [twill](http://twill.idyll.org/)（Python 实现）：模拟能力与 WebUnit
相当。  
* Python 3 标准模块 urllib（基于更底层的 http.client 模块）和
http.cookiejar 等配合起来支持基本的定制 HTTP 请求、Cookie。标准模块
html.parser 解析 HTML，可能需要 python-utidylib 做 HTML 整理。（《Python
Cookbook》第 14 章 Web Programming 还提到控制 IE、使用 HTTPS 等技巧。）

**(4) 宏记录鼠标点击坐标和时间然后重放**

这个方法受 Web
页变化影响很大，且测试逻辑不明确，所以这方式的测试用例几乎无法维护。许多商业的
Web 测试软件就是这一类。
