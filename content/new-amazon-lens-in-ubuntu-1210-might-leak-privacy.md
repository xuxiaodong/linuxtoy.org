Title: Ubuntu 12.10 新增 Amazon 搜索可能泄露隐私
Date: 2012-10-31 17:47
Author: lovenemesis
Category: News
Tags: eff, privacy, Ubuntu
Slug: new-amazon-lens-in-ubuntu-1210-might-leak-privacy

根据 Electric Frontier Foundation 的研究，Ubuntu 12.10 新增的 Amazon
搜索可能会导致隐私泄露。

[几天前发布的 Ubuntu
12.10](http://linuxtoy.org/archives/ubuntu-12-10.html)搭载了一个 Amazon
购物搜索的 Lens。当用户在 Dash 中进行搜索时，也会默认获得来自 Amazon
购物网站的信息。通过这种方式，Canonical 可以从 Amazon 获得一部分收入。

这个行为在开发时就收到了来自社区的不少反对声，因为这样子意味着在告知全世界你在计算机上搜索了什么。对此
Canonical 的创始人 [Mark Shuttleworth 撰文表示搜索是由 Ubuntu 代为用户向
Amazon
发起的](http://www.markshuttleworth.com/archives/1182)，希望用户相信他们。

然而 Mark Shuttleworth 并没有告诉完整的故事。

搜索关键词和 IP 的确是通过 HTTPS 加密发送到 Ubuntu 的服务器然后再转发给
Amazon 的，但是**从 Amazon 返回的数据结果确是通过 HTTP
直接发送给用户的**。这意味着：

1.  若是接入的是公共网络，HTTP
    非加密方式传输可以让其他人通过返回结果窃取到你的搜索内容。
2.  由于是不经过 Ubuntu 代理直接返回给用户，Amazon
    方面依然可以在服务器端记录用户的搜索关键词和 IP。

目前[第一点已经得到改善](http://blog.canonical.com/2012/10/12/searching-in-the-dash-in-ubuntu-12-10-an-update/)，改为使用
HTTPS 的方式返回搜索结果了。

相比之下，另一个问题可能更严重。**在默认情况下，Canonical 会将加密发送到
Ubuntu 服务器的搜索关键词和 IP
信息储存起来，并转发给第三方合作伙伴，包括 Facebook, Twitter, BBC 和
Amazon**。这个隐私声明可以在 Dash 中点击 `i` 图标查看。

[Canonical
的第三方程序隐私列表](http://www.ubuntu.com/aboutus/privacypolicy/thirdparties)上列出了它的第三方合作伙伴，但是**并没有回答诸如来自用户的搜索关键词和
IP 会保留多久，会以何种方式交给第三方等问题**。

实际上这种搜集用户操作并给第三方的行为很常见，各种闭源操作系统中诸如 Win
和 OS X
已经这么干很多年了（黑日白月注：还有朝内的某卫士和某毒霸等）。不过这样子的行为在
Linux 发行版中还是首次出现，且默认启用。

如果你对此有所顾虑的话，可以用以下命令删除 Amazon Lens：

`sudo apt-get remove unity-lens-shopping`

再到隐私程序中**禁止 Dash 搜索互联网内容**。

更多详情欢迎阅读[EFF
原文](https://www.eff.org/deeplinks/2012/10/privacy-ubuntu-1210-amazon-ads-and-data-leaks)

*消息来源：*[Ars
Technica](http://arstechnica.com/security/2012/10/eff-calls-ubuntus-amazon-search-result-feature-major-privacy-problem/?comments=1#comments-bar)
