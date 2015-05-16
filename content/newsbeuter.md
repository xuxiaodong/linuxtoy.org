Title: Newsbeuter：在控制台下读 RSS 新闻
Date: 2008-08-27 08:00
Author: toy
Category: Apps, Cli
Tags: Newsbeuter, RSS
Slug: newsbeuter

RSS 是如今比较流行的新闻获取方式。如果你打算在 Linux 的控制台下阅读 RSS
新闻，Newsbeuter 可以满足你的要求。Newsbeuter
是一款专门为文本终端界面而设计的 RSS 阅读工具。目前，它支持 RSS
0.9x/1.0/2.0 和 Atom 格式的 feed。除却对 feed 规范和 opml
导入/输出的支持外，Newsbeuter 还包括快捷键、给 feed 打 tag、能够下载
podcast、可定制外观等功能。

![Newsbeuter](http://i.linuxtoy.org/i/2008/08/newsbeuter.png)

你可以参照这里的介绍[从源代码编译安装
Newsbeuter](http://www.newsbeuter.org/doc/newsbeuter.html#id2494856)。需要注意的是，Newsbeuter
要求 STFL、SQLite 3、libcurl 等依赖。

**导入 OPML 文件**

如果你使用过其他的 RSS 阅读工具，那么可以将自己积累的 feed 输出为 opml
文件以供 Newsbeuter 使用。要将 opml 文件导入
Newsbeuter，只需执行下列命令即可：

`newsbeuter -i feeds.opml`

注意将 feeds 替换为你的 opml 文件名称。

**添加 feed**

要把 feed 添加到 Newsbeuter，你可以使用任何文本编辑器向
$HOME/.newsbeuter/urls 文件（如不存在，可自行建立该文件）追加 feed
地址即可。例如，添加 LinuxTOY 的 feed 地址：

<http://linuxtoy.org/feed/>

只要保证每个 feed 地址占用一行即可。

**阅读 RSS 新闻**

执行 newsbeuter 命令后即启动了 Newsbeuter 阅读程序，首先可以按 R
键来获得更新，使用 Enter 键进入阅读。更多的快捷键用法建议通过按 ?
来获得帮助。

另一个[终端下的 RSS 阅读工具
Snownews](http://linuxtoy.org/archives/snownews.html)。

[Newsbeuter](http://www.newsbeuter.org)
