Title: Google Reader 与 Vimperator 快捷键冲突的解决之道
Date: 2008-10-05 09:31
Author: toy
Category: Tips
Tags: Google Reader, Vimperator
Slug: google-reader-and-vimperator

在转到 Google Reader
之后，其强大的快捷键功能我一直用得很爽。不过有一点，Google Reader
的快捷键与我喜欢的 Firefox 扩展
[Vimperator](http://linuxtoy.org/archives/vimperator.html)
有冲突。虽然可以通过临时禁用 Vimperator 来解决，但毕竟需要按一次 Ctrl +
z，还是有点不爽。某天，翻阅 [Vimperator 的
Wiki](http://vimperator.cutup.org/index.php?title=Tips_and_Tricks#Useful_autocommands)，于是这个问题得到了完美的解决。

具体的解决办法是，向 ~/.vimperatorrc 文件加入下列内容即可：

[code='bash']autocmd LocationChange .* :js modes.passAllKeys =
/mail.google.com/.test(buffer.URL) ||
/google.com\\/reader\\//.test(buffer.URL)[/code]

当使用 Google Reader 阅读新闻时，就会自动进入 Vimperator 的 PASS THROUGH
状态，而要正常使用 Google Reader 快捷键也没有什么问题了。

BTW：这项内容对于 Gmail 也是有效的。
