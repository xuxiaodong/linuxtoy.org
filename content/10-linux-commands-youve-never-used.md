Title: 你从未用过的 10 条 Linux 命令？
Date: 2007-02-28 09:34
Author: toy
Category: Tutorials
Slug: 10-linux-commands-youve-never-used

Brock 老兄写了一篇文章《[你从未用过的 10 条 Linux 命令（10 Linux commands you've never used）](http://bashcurescancer.com/10-linux-commands-youve-never-used.html)》，虽然标题有点过于绝对和主观，不过文章还是不错的。其实，无论你是否听说过或者使用过这些命令，都值得我们再来重温一遍。不是吗？

这 10 条 Linux 命令依次是：

1.  pgrep：比如，你可以使用 `pgrep -u root` 来代替 `ps -ef | egrep '^root ' | awk '{print $2}'`，以便抓取属于 root 的 PID。
2.  pstree：我觉得这个命令很酷，它可以直接列出进程树，或者换句话说是按照树状结构来列出进程。
3.  bc：这个命令在我的系统中没有找到，可能需要安装。这是用来执行计算的一个命令，如使用它来开平方根。
4.  split：这是一个很有用的命令，它可以将一个大文件分割成几个小的部分。比如：`split -b 2m largefile LF_` 会将 largefile 分割成带有 LF 文件名前缀且大小为 2 MB 的小文件。
5.  nl：能够显示行号的命令。在阅读脚本或代码时，这个命令应该非常有用。如：`nl wireless.h | head`。
6.  mkfifo：作者说这是他最喜欢的命令。该命令使得其他命令能够通过一个命名的管道进行通信。嗯，听起来有点空洞。举例说明，先创建一个管道并写入内容： ` mkfifo ive-been-piped ls -al split/* | head > ive-been-piped`，然后就可以读取了：`head ive-been-piped`。
7.  ldd：其作用是输出指定文件依赖的动态链接库。比如，通过 `ldd /usr/java/jre1.5.0_11/bin/java` 可以了解~~哪些线程库链接到了~~ java 依赖（动态链接）了哪些库。（感谢 NetSnail 的指正。）
8.  col：可以将 man 手册页保存为无格式的文本文件。如：` PAGER=cat man less | col -b > less.txt`
9.  xmlwf：能够检测 XML 文档是否良好。比如：` curl -s 'http://bashcurescancer.com' > bcc.html xmlwf bcc.html perl -i -pe 's@<br/>@<br>@g' bcc.html xmlwf bcc.html bcc.html:104:2: mismatched tag`
10. lsof：列出打开的文件。如：通过 `lsof | grep TCP` 可以找到打开的端口。

这 10 条 Linux 命令，有些的确比较鲜为人知。我个人也只用过其中很少的几个命令，像 col、split、lsof 等等。当然，有些大牛们可能全部都用过。通过引荐本文，希望我们能够更加重视 Linux 命令的使用。

([via](http://bashcurescancer.com/10-linux-commands-youve-never-used.html), thanks!)
