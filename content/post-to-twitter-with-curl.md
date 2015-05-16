Title: 小技巧：从命令行发布 Twitter 消息
Date: 2008-03-09 10:35
Author: toy
Category: Tips
Slug: post-to-twitter-with-curl

你用什么方式发布 [Twitter](http://twitter.com/) 消息？从 Twitter
网站，还是 [Twitter
客户端](http://linuxtoy.org/archives/twitux.html)？Download Squad
介绍了一个从命令行发布 Twitter
消息的实用技巧，想必惯用命令行的朋友会喜欢。要使用该技巧，我们需要一个名为
[curl](http://curl.haxx.se/) 的命令行工具。如果在你的 Linux
系统中无法找到 curl，可通过包管理工具搜索并安装它。

![Curl](http://i.linuxtoy.org/i/2008/03/curl.png)

当你需要从命令行发布 Twitter 消息时，只需按如下格式输入即可：

`curl -u 帐号:密码 -d status="要发布的消息" http://twitter.com/statuses/update.xml`

[via [Download
Squad](http://www.downloadsquad.com/2008/03/07/post-to-twitter-using-the-command-line/)]
