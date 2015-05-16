Title: 将 locale 从 zh_CN.GB2312 转到 zh_CN.UTF-8 的一些问题和解决方法
Date: 2007-06-11 21:00
Author: toy
Category: Tips
Slug: convert-locale

一直想把自己的 Linux box 从 zh\_CN.GB2312 的 locale 设置迁移到
zh\_CN.UTF-8 上去，无奈之前的大量的实验中用到的文件都是 GB2312
编码的，所以，这个迁移直到最近因为要在一个工具上添加 UTF-8
编码的中文支持才得以完成。以下是我在这个迁移的过程碰到的一些和中文相关的问题以及我个人的解决方法，列此一来备忘，二来希望能给有相同需求的朋友做个参考。

提醒：以下提及的工具中的大部分会对你的原始文件进行"写"操作，也就是说，
转换出来的结果可能会产生错误或者偏差。如果你不是一个有经验的 Linux
用户，请在做这些操作的时候，注意先做好备份。并强烈建议你在使用某一个工具之
前，先仔细阅读该工具的 manual。("man program-name")

**0、支持 Unicode 的 Terminal 工具**

我选择 Terminal
工具的[原则](http://ihome.ust.hk/blogs/home/josephwu/GNU_slash_Linux/2006/03/23/Wanted-a-terminal-emulator-substitute.html)是：轻量（占用系统资源小）且强大。基于之前我的一个[简单评测](http://ihome.ust.hk/blogs/home/josephwu/GNU_slash_Linux/2006/03/24/Terminal-Emulator-Comparison.html)，我现在用的
Terminal 工具是
[rxvt-unicode](http://software.schmorp.de/pkg/rxvt-unicode.html) 加
[screen](http://www.gnu.org/software/screen/)。xterm 对 unicode
的支持可能是最差的，除此之外，mlterm、GNOME-terminal
等工具虽然都能很好的支持 unicode，不过 mlterm 的 multi tab
功能在我更习惯于使用"screen"来做 multi tab 这点上显得有点多余；而
gnome-terminal 则太过于耗资源。rxvt-unicode 则刚好合我的胃口，尤其是它的
server+client 的模式可以在开启多个 Terminal 的时候节省大量的系统资源。:)

**1、文件内容的编码检测及转换**

文件内容的编码转换可以结合 2 个工具来完成。

a.如果你不知道你所要转换的文件的编码格式，你可以通过
[enca](http://trific.ath.cx/software/enca/)
这个工具来检测编码。举例如下：

`joseph@PeT43: ~ > enca foo.txt`

`Universal transformation format 8 bits; UTF-8`

b.如果你事先已经知道了文件的编码或者通过检测知道了文件的编码，可以通过
GNU 的 [iconv](http://www.gnu.org/software/libiconv/)
来进行编码转换。以下是一个例子用来把文件的编码从 GB2312 转换成 UTF-8：

`joseph@PeT43: ~ > iconv -f gb2312 -t utf-8 foo.txt > foot.txt.utf-8`

提醒：iconv 的输出默认是直接输出到标准输出(standard
output)，通常就是你的屏幕上。所以，你需要使用">"的重定向符号来把输出转存到一个"新"的文件里面去。切不可在">"后面使用你的原始的输入文件名作为输出文件名，因为">"操作，会首先将其后面的文件清空，然后再运行
">"前面的操作。也就是说，除了原始的输入文件被清空之外，你什么也得不到。这是很多
Linux 新用户经常会犯的一个"致命"错误。特此提醒。

**2、文件名的编码转换**

上述的 2
个工具只能对文件的内容进行编码的检测和转换，如果需要对文件名进行编码转换，则需要
[convmv](http://j3e.de/linux/convmv/man/) 来完成。convmv 的用法大致和
iconv 相似，以下是一个例子用来将"music"这个目录下的所有以 GB2312
编码的文件名的文件和子目录下的文件，转换成以 UTF-8 编码的文件名：

`joseph@PeT43: ~ > convmv -f gb2312 -t utf-8 -notest -r music`

请注意这里的"-notest"选项：如果不提供这个选项，该命令只会做一个转换的测试，并不会真正的转换。因为这个命令有一定的"破坏性"，所以，当你用这个程序的时候，最好是先不用"-notest"这个选项来做一遍测试，根据程序运行输出的信息来确定是否有个别的文件需要手动进行调整。

**3、MP3 的 ID3 tag 编码转换**

一个比较扰人的问题是，MP3 里面的 ID3(v1/v2) Tag
信息不能象普通的文本文件那样来用 iconv 进行编码转换。好在这个问题 [Feng
Zhou](http://www.cs.berkeley.edu/~zf/) 也碰到了，他写了一个 java 的程序
[ID3iconv](http://www.cs.berkeley.edu/~zf/id3iconv/) 来处理这些 MP3
文件的 ID tag 编码转换。

略有不足的是，这个程序没有提供一个类似于上面提及的 convmv
的"-r"(recursive)的选项可以来对某一个目录下的所有文件和子目录下的文件进行递归的处理。当然，我们可以用万能的“find”命令来弥补这个缺陷，以下是一个例子，用来对"music"
目录里面的所有 mp3 文件（含子目录下的文件）进行 ID3 tag 的转换:

`joseph@PeT43: ~ > find . -name '*.mp3' -exec java -jar /usr/local/bin/id3iconv-0.2.1.jar -e gb2312 '{}' \;`

这个命令利用到了"find"命令的"-exec"选项来对所有找到的文件进行指定的操作，这里“指定的操作”就是对该文件调用
id3iconv 这个 java 的程序来进行 ID3 tag 的编码格式转换。详情请参考 find
的 manual (man find)。

**4、在 rxvt-unicode terminal 中实时改变 locale 设置**

我所碰到的一个比较扰人的问题是，虽然现在日常的操作多数是在 UTF-8 的
locale 下进行的，但是很多时候我又需要一个基于 GB2312 的 rxvt- unicode
来跑原来的一些实验。简单的在一个现有的 rxvt-unicode session
下通过"export LC\_CTYPE=zh\_CN.GB2312"其实并不奏效。因为那只是告诉你的
bash 程序，此后的 locale 变成了 zh\_CN.GB2312，而 rxvt-unicode
程序本身却依然工作在它启动时候的 zh\_CN.UTF-8 的 locale
下。所以，即使改变了 bash 的 locale 设置，但如果在该 rxvt-unicode 中用
cat 或者 more 这样的命令来查看一个以 zh\_CN.GB2312
的文件，依然看到是一堆乱码。

在这种情况下，一种不需要重新设置 X 系统的 locale，实时修改运行状态下的
rxvt-unicode 本身的 locale 设置的解决方案是使用 rxvt-unicode
内置的"escape sequence"来实现。

如下的 2 个命令组合，先更改 bash 的 locale 设置，然后通过"escape
sequence"通知 rxvt-unicode 程序，现在这个 session 的 locale
设置已经被改成了 zh\_CN.GB2312：

`joseph@PeT43: ~ > export LC_CTYPE=zh_CN.gb2312; printf "\33]701;$LC_CTYPE\007"`

这样，你就实时的得到一个 zh\_CN.GB2312 的环境，可以对 zh\_CN.GB2312
的文件进行正确的显式和操作了。

如果需要转回到 zh\_CN.UTF-8 的模式，则可以通过如下的命令来实现：

`joseph@PeT43: ~ > export LC_CTYPE=zh_CN.utf8; printf "\33]701;$LC_CTYPE\007"`

当然，每次敲这么长的命令挺烦人的，我用的方法是把上面的这 2
个命令集合分别存成 .bash.gb 和 .bash.utf-8 两个文件，放到我的 home
目录。

如果我需要实时得到一个 GB2312 的 rxvt-unicode session，我就运行：

`joseph@PeT43:  somewhere > source ~/.bash.gb`

如果我需要实时得到一个 UTF-8 的 rxvt-unicode session，我就运行：

`joseph@PeT43: somewhere > source  ~/.bash.utf-8`

这样就省却了很多敲键盘或者 copy/paste 的时间。:)

这个方法是从
[rxvt-unicode](http://software.schmorp.de/pkg/rxvt-unicode.html) 的
[FAQ](http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.html)
中学来的。这个"701"的 escape sequence 是 rxvt-unicode 对 xterm 的 escape
sequence 的扩展，只在 rxvt-unicode 中有效。

[在 GNOME Terminal 里面可以通过菜单里面的"Terminal|Set Character
Encoding"来实时更改 locale。]

**5、VIM 配置文件的更新**

我是一个 VIMmer，以下是一些我在 UTF-8 环境下的 vim 的配置：

`set encoding=utf-8 " set default encoding as UTF-8`

`set fileencodings=ucs-bom,utf-8,cp936,latin1 " fileconding detection order`

`set termencoding=utf-8 " support Chinese display in rxvt-unicode`

**6、Misc**

以下是一些小技巧，简单罗列在下面。

a. 在做编码转换的时候，如果你的源格式设定为 GB2312 的话，而且在转换成
UTF-8 的时候，发现程序会报“illegal input sequence at position
xxxx"的错误。这是由于你之前的做的假定有问题。[GB2312](http://zh.wikipedia.org/wiki/GB_2312)
是国标里面一个最小也是最早的中文编码标准。其中，只涵盖了 6,763
个汉字。所以你需要转换的文件的原始的格式可能并不是 GB2312
编码。这个时候，你可以用 GB18030
做为源格式来进行转换。[GB18030](http://zh.wikipedia.org/wiki/GB_18030)
是最新的国家标准，包含了 27,564 个汉字，而且向下兼容 GB2312 和 GBK。

b.另外，支持 Unicode 且 Free
的中文字库我推荐使用"[文泉驿](http://wqy.sourceforge.net/cgi-bin/index.cgi)"。这好像也是目前为止，唯一的一个以支持
Unicode 为出发点的 Free 的中文字库。

**7、一些有用的参考：**

a. [Markus Kuhn](http://www.cl.cam.ac.uk/~mgk25/) 的"[UTF-8 and Unicode
FAQ for
Unix/Linux](http://www.cl.cam.ac.uk/~mgk25/unicode.html)"。最为详尽的
FAQ。

b. [Unicode Home Page](http://www.unicode.org/)。Unicode 的官方网站。

c. [A Quick Primer On Unicode and Software Internationalization Under
Linux and UNIX](http://eyegene.ophthy.med.umich.edu/unicode/)。 [Ed
Trager](mailto:ehtrager@umich.edu) 提供的一个关于如何在 Linux 下使用
Unicode 的 tutorial，涵盖了一些我没有提及的内容。推荐阅读。

[撰文/[Zhaojun](http://ihome.ust.hk/blogs/home/josephwu/)]
