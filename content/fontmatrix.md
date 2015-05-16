Title: Fontmatrix: Linux 下的字体管理器
Date: 2007-12-10 11:01
Author: toy
Category: Apps
Slug: fontmatrix

在 Linux
平台上一直都比较缺乏字体管理器，不过这种状况可能要成为过去了。最近所出现的
[Fontmatrix](http://www.fontmatrix.net/)
算是一个较为实用的字体管理程序。使用
Fontmatrix，你可以激活或停用系统中的字体，也可以预览字体，并让你了解字体的全面信息。此外，Fontmatrix
还允许你给字体贴 Tag、生成 fontbook 等。

[![Fontmatrix
截图](http://i.linuxtoy.org/i/2007/12/fontmatrix-thumb.png)](http://i.linuxtoy.org/i/2007/12/fontmatrix.png)  
*Fontmatrix 屏幕截图*

目前，Fontmatrix 仍然在开发之中，不过已经有公开发布的 0.2svn
版可用。从我的试用情况来看，程序还算稳定。Fontmatrix 仅提供有 rpm
包和源码包，其中 rpm 包可用于 Fedora 8 和 openSUSE 10.3。使用其他 Linux
发行版的朋友需要自己编译。

简单说一说 Fontmatrix 的编译过程，首先需要准备依赖：Qt 4.3 和
Freetype2，它们的开发包要先安装好。另外，如果要从 svn
获取源代码的话，那么还要安装 Subversion。

接着获取 Fontmatrix
的源代码，可以下载作者的[存档](http://www.fontmatrix.net/archives)，也可以直接通过
svn 获取，我们使用后者。

`svn checkout http://svn.gna.org/svn/undertype/branches/fontmatrix002`

这将创建 fontmatrix002 目录，下一步执行编译过程：  
` cd fontmatrix002/ qmake -o Makefile typotek.pro make`

现在进入其中的 bin 目录，就可以运行 Fontmatrix 了：  
` cd bin/ ./fontmatrix`
