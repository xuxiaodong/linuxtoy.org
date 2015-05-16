Title: Mozilla Weave 1.0 Beta3 发布
Date: 2009-12-14 06:34
Author: lovenemesis
Category: Firefox Extension
Tags: Firefox, weave
Slug: mozilla-weave-10b3-released

Mozilla 实验室最近发布了 Firefox 浏览器书签及设置同步软件 Weave 1.0 Beta
3 版本，该版本很有可能成为在不久后发布的 1.0 RC 版本。

Mozilla Weave
扩展不仅可以同步书签，还包括历史记录、保存密码、偏好设置和**打开标签页**，这一切都通过加密的方式传输并保存在
Mozilla 的服务器上，只需要免费注册一个 Weave 帐号即可。

保存打开标签页功能十分适合在多处使用 Firefox 的朋友。在安装 Weave 扩展的
Firefox 选择“退出并保存标签页”之后，就可以在任意安装了 Weave 扩展的
Firefox 恢复之前保存的标签页。

另外， Weave 也支持最近发布的 [Firefox Mobile for
Maemo](http://www.mozilla.com/en-US/mobile/) 版本，使用 N900
的朋友们有福了～

[![](http://i.linuxtoy.org/images/2009/12/weave.png)](http://i.linuxtoy.org/images/2009/12/weave.png)

[官方博客发布日志](http://mozillalabs.com/weave/2009/12/11/weave-1-0-beta-3-released/)

[安装 Mozilla Weave 扩展（需要 Firefox 3.5
以上）](https://addons.mozilla.org/services/install.php?addon_id=weave)

**安全警告：** Fedora 的用户可能会得到 SELinux
错误提示说需要文本重定向，诡异的是按照错误提示的解决方法给 Weave
库赋予重定向标签并不能解决问题（提示文件错误，似乎是路径转义符导致的，望
SELinux
高手指教），暂时只好使用以下命令允许全局文本重定向（安全性降低！）：

`su -c 'setsebool -P allow_execmod on'`

PS: 继续期待 Firefox Mobile for Android 中……
