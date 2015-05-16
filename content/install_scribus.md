Title: 3 步安装 Scribus 最新版
Date: 2006-12-13 20:42
Author: toy
Category: Tutorials
Slug: install_scribus

毫无疑问，[Scribus](http://www.scribus.net) 是开源阵营中一款极为出色的
DTP 软件。不过，旧版本所存在的 CJK 问题，对于中文用户来说很是头痛。虽然
Scribus 官方表示目前仍未正式支持
CJK，但是最新版本已经有了很大的改观，正常使用是没有问题的。如果你有使用
Scribus 的需求，那么不妨一试。

[![Scribus](http://i.linuxtoy.org/i/2006/12/scribus_s.jpg)](http://i.linuxtoy.org/i/2006/12/scribus.jpg)  
*Scribus 正常显示中文内容*

在 Ubuntu Edgy Eft 中，安装 Scribus 最新的 1.3.3.6 版，只需以下 3
个步骤即可。

第 1 步：  

` gpg --keyserver wwwkeys.eu.pgp.net --recv-keys DA286F326C5F196B gpg --armor --export DA286F326C5F196B | sudo apt-key add -`

第 2 步：  
` sudo vim /etc/apt/sources.list`

然后，添加下面两行：  

` deb http://debian.scribus.net/debian edgy main restricted deb-src http://debian.scribus.net/debian edgy main restricted`

第 3 步：  
` sudo apt-get update sudo apt-get install scribus-ng`

现在，使用 Scribus，可以在 Story Editor
中输入中文，能够正常使用中文字体来显示相应内容。但仍然有一些不足：

1.  当使用中文字体时，Scribus 载入会花很长的时间。
2.  在直接输出为 PDF 时，Scribus
    不能正常嵌入中文字体，这导致中文效果相当不好。不过，我们可以通过输出为
    EPS 文件来加以补救，这将获得较好的效果。

