Title: IEs 4 Linux 新版支持 IE 7
Date: 2006-10-23 19:19
Author: toy
Category: Apps
Slug: ies_4_linux_support_ie_7

[IEs 4 Linux](http://www.tatanka.com.br/ies4linux/index-en.html)
可以让在 Linux 上安装 IE 变成一件十分简单和惬意的事。昨天发布的 [IEs 4
Linux 2.1
beta2](http://www.tatanka.com.br/ies4linux/downloads/ies4linux-2.1beta2.tar.gz)
版开始支持安装 IE 7 了。不过，需要使用 --beta-install-ie7
的命令行选项来激活。据作者称，在 Linux 安装的 IE 7，虽然窗口外观与 IE 6
并无二致，但其核心已经是 IE 7 的引擎。

另外，新的 IEs 4 Linux
还包括了一个图形化的安装界面，想来使用上要容易得多了。值得注意的是，可能是作者的粗心所致，lib/ui.sh
文件中的 dev/null 前面少了一个 /，即正确的应该为
/dev/null，所以请在使用之前，自行更正。
