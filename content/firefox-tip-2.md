Title: 小技巧: 改善 Firefox 性能
Date: 2009-07-13 17:56
Author: toy
Category: Tips
Tags: Firefox
Slug: firefox-tip-2

使用 Firefox 日久，让人不免既爱又恨起来。爱的是它具有丰富的
Add-ons，可让人随心所欲的扩展其现有功能；恨的是它似乎总是容易遭遇性能瓶颈，时间一长便慢了下来。最近，我看到一则小技巧，通过尝试，对于改善
Firefox 的性能还挺有效的，现介绍给同好分享。

Firefox 从 3.0 开始将书签、历史等信息存储到了 SQLite
数据库中，所以我们可以通过优化 SQLite 数据库来达到改善 Firefox
性能的目的。以下是操作步骤：

1. 转到 Firefox 的 profile 目录，默认位于
~/.mozilla/firefox/xxxxxxxx..default/；  
2. 若是针对单个的 SQLite 文件（如 places.sqlite）执行优化，则运行
`sqlite3 places.sqlite vacuum`。你也可以通过下列命令来对所有的 SQLite
文件执行优化：

for s in *.sqlite; { sqlite3 $s vacuum; }

注意：如果在你的 Linux 系统上找不到
sqlite3，则需要先行安装。另外，在执行优化时，你也要关闭 Firefox。

{via
[MozillaLinks](http://feedproxy.google.com/~r/MozillaLinks/~3/J3xBykOOZfw/)}
