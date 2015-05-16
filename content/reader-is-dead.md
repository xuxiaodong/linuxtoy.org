Title: Reader is Dead: 完整备份 Google Reader
Date: 2013-06-30 10:27
Author: toy
Category: Apps
Slug: reader-is-dead

Google Reader
很快就要关闭了，如果你还没有将它的数据备份下来的话，那么不妨来  
用用 [Reader is Dead][r]。Reader is Dead 是一组相当实用的工具，其中包  
括 reader\\\_archive、reader\\\_browser、以及
feed\\\_archive。它们的用途分别为：

* reader\\\_archive：完整备份 Google Reader 数据，比 Google 本身提供的
Takeout  

好用，它不光备份所有阅读条目，还包括所有星标条目、标签条目、分享条目、评论等等。

* reader\\\_browser：使你能够通过 `http://localhost:8071`  
在网络浏览器中访问已备份好的 Google Reader 内容。

* feed\\\_archive：允许你保存来自 Google Reader feed 存档的公开 feed
数据。

当使用 reader\\\_archive 备份 Google Reader 数据时，可执行以下命令：

./reader\_archive --output\_directory=~/greader\_archive

其中，`~/greader\_archive` 为保存 Google Reader
数据的目录。程序会要求授权，根据提示  
将浏览器窗口中的授权码复制到终端窗口即可。之后，reader\\\_archive
便会为你抓取数据了。

[r]: http://readerisdead.com/
