Title: 试用  Deluge 的 Web 界面
Date: 2007-10-18 08:35
Author: toy
Category: Apps, BitTorrent Client, Featured
Slug: trying-out-deluge-web-interface

[Deluge](http://linuxtoy.org/search/deluge) 是我一直在推荐的 BitTorrent
下载软件。正如[之前我提到的](http://linuxtoy.org/archives/deluge-web-interface.html)一样，在昨天发布的
[Deluge 0.5.6 RC
1](http://deluge-torrent.org/2007/10/16/056rc1-version-05595-released/)
中已经包含了 Web 界面插件。该插件不仅为 Deluge 提供了另外一种 BitTorrent
下载界面，而且能够通过 Web 浏览器从远程控制 BitTorrent 下载。这对 Deluge
来说，的确是起到了扩展功能的作用。

要使用 Deluge 的 Web 界面，首先需要启用这个 Web 界面插件。这可以通过点击
**Edit → Plugins** 菜单命令，并选中 **Web User Interface** 插件来完成。

在正式使用之前，还需对其加以配置。除了必须设置密码之外，其他选项可以保持默认。

![Deluge Web UI Config](http://i.linuxtoy.org/i/deluge/webui-config.png)

现在打开 Web 浏览器，如 Firefox，在地址栏输入下列内容可以进入 Deluge 的
Web 界面：

`http://localhost:8112/`

如果是远程登录 Deluge 的 Web 界面，可以将 localhost 换成该机的 IP 地址。

按照提示，输入密码，即可登录 Deluge 的 Web 界面。

[![Deluge Web
UI](http://i.linuxtoy.org/i/deluge/deluge-webui01-thumb.png)](http://i.linuxtoy.org/i/deluge/deluge-webui01.png)

目前，该 Web 界面的功能包括：可以从本机或 url 添加
torrent，能够设置刷新间隔，可以全部暂停或恢复 torrent 列表，等等。

[![Deluge Web
UI](http://i.linuxtoy.org/i/deluge/deluge-webui02-thumb.png)](http://i.linuxtoy.org/i/deluge/deluge-webui02.png)

[![Deluge Web
UI](http://i.linuxtoy.org/i/deluge/deluge-webui03-thumb.png)](http://i.linuxtoy.org/i/deluge/deluge-webui03.png)

[![Deluge Web
UI](http://i.linuxtoy.org/i/deluge/deluge-webui04-thumb.png)](http://i.linuxtoy.org/i/deluge/deluge-webui04.png)

如果能够提供更灵活、更强大的 BitTorrent 下载操控能力，相信 Deluge 的 Web
界面将变得更加实用。
