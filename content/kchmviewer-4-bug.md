Title: 修正 KchmViewer 4 的两个 Bug
Date: 2009-05-24 18:31
Author: toy
Category: Tips
Tags: KchmViewer
Slug: kchmviewer-4-bug

{撰文/john}

**index 显示不全 bug 的解决**

KchmViewer 4 有一个 bug ，就是看一些 chm 文档时，index 会显示不全（有
Python 的 chm 格式文档的可以试一下，python261.chm 的 index 在 KchmViewer
4 下大概能显示到字母 n 的样子）。昨天调试了一下，改正了这个 bug
。修改方法为：

下载源代码（官网上下），在 lib/libchmfile 目录下，找到 libchmfile.cpp
文件，修改函数 bool LCHMFile::parseIndex( QVector<
LCHMParsedEntry > * indexes ) const，将其从：

return m\_impl->parseBinaryIndex( indexes )  
|| m\_impl->parseFileAndFillArray( m\_impl->m\_indexFile, indexes,
true );

改为：

return m\_impl->parseFileAndFillArray( m\_impl->m\_indexFile, indexes,
true )  
||m\_impl->parseBinaryIndex( indexes );

然后编译，这样得到的程序就能正确的显示 index
了。具体原因的分析，请查看我写的日志：。

**中文路径 bug 的解决**

解决方法是：

在源码目录下找到 kchmmainwindow.cpp 下找到 parseCmdLineArgs()
函数，找到如下行：

filename = args->arg(0); （在文件的520行）

和

filename = qApp->argv()[i]; （在文件的547行）

分别改为：

filename = QString::fromLocal8Bit(args->arg(0));

和

filename = QString::fromLocal8Bit(qApp->argv()[i]);

然后保存编译，大功告成！

具体分析见我的日志 。
