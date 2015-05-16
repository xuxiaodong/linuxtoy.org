Title: 修复 Firefox 2.0 的小 bug
Date: 2006-12-21 20:11
Author: toy
Category: Tutorials
Slug: fix_firefox_bug

当使用 Firefox 2.0
浏览网页时，我发现无法用“Backspace”这个快捷键来返回刚刚访问的页面。也许这算得上是
Firefox 2.0 的一个小 bug。该 bug
会对惯用快捷键的用户带来不便。不过，我们可以通过以下方法来修复这个 bug。

1.  在 Firefox 地址栏输入“about:config”，并回车；
2.  在 Filter 中输入“browser.backspace\_action”，将其值由“1”修改为“0”；
3.  重启 Firefox。

由于我还没有更新到 Firefox
2.0.0.1，所以不能确定该版本中的“Backspace”是否有效。欢迎使用该版本的朋友反馈。
