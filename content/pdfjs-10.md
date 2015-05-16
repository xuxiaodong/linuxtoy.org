Title: pdf.js 1.0
Date: 2011-10-29 11:22
Author: lovenemesis
Category: Firefox Extension
Tags: html5, PDF
Slug: pdfjs-10

之前介绍的 HTML5 技术的 PDF 解析器 pdf.js 升级至 1.0
版本，并且将成为未来 Firefox 内嵌的 PDF 阅读器。

和 Google Chrome 使用的**源自 Foxit 的闭源 PDF 浏览插件**不同，PDF.js
是**基于开放的 HTML5 及 JavaScript 技术实现的开源产品**。

[源代码仓库访问](https://wiki.mozilla.org/PDF.js#Milestone:.C2.A0PDF.js_Firefox_extension_1.0)

[免重启测试版扩展安装](http://andreasgal.github.com/pdf.js/extensions/firefox/pdf.js.xpi)

下面是在 Fedora 16 预装的 Firefox 7.0.1 上使用该扩展浏览 [UEFI Secure
Boot Impact on Linux
白皮书](http://ozlabs.org/docs/uefi-secure-boot-impact-on-linux.pdf)的样子：

[![](http://linuxtoy.org/img/2011/10/pdfjs10.png "pdfjs10")](http://linuxtoy.org/img/2011/10/pdfjs10.png)

从结果中可以看到常见的 PDF 阅读功能一应俱全，渲染速度上也已经和本地的
PDF 阅读插件无异。

毫无疑问 pdf.js 将被整合入 Gecko 成为 Firefox 的内嵌 PDF
阅读器，但是具体整合时间表尚未确定。

[消息来源](http://identi.ca/notice/84752021)：[Geek](http://www.geek.com/articles/news/this-is-what-firefoxs-built-in-pdf-reader-looks-like-20111027/)
