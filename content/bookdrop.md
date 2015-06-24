Title: BookDrop: 通过 Dropbox 接收 Kindle 电子书
Date: 2015-06-24 22:11:31
Authors: toy
Category: Apps
Tags: dropbox, kindle
Slug: bookdrop

如果我想在 Kindle 上阅读通过其他渠道购买的电子书，那么有两种选择：要么连线直接拷贝，要么将书作为附件发送到 Kindle 的个人文档服务。而通过 BookDrop 则可合二为一，只要将书存储于 Dropbox 的文件夹，它就会在后台完成格式转换，并自动传送到 Kindle。

<!-- PELICAN_END_SUMMARY -->

![BookDrop](http://linuxtoy.org/images/2015/06/bookdrop.png)

除了 Amazon 本身所支持的 mobi、azw、pdf、txt、doc(x)、htm(l)、png、jp(e)g 等格式之外，BookDrop 还特别针对 epub、cbr、cbz 等格式提供了支持。唯一比较遗憾的是，文件大小需限制到 25MB 以下。

要使用 BookDrop，只需执行以下 3 步即可：

1. 连接 Dropbox，这将会创建 `Apps/book-drop` 目录，稍后将书存储于此；

2. 将链接拖到浏览器的书签栏；

3. 登录 Amazon.com 网站，进入管理 Kindle 设备页面，执行上一步的书签链接，并按提示操作。

若是你在 Kindle 上收到 wecome to bookdrop 的文档，则说明设置成功。

&mdash; [BookDrop](https://getbookdrop.com/)
