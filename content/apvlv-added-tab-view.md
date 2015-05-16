Title: Apvlv 增添分页浏览功能
Date: 2009-03-01 13:14
Author: toy
Category: Apps
Tags: Apvlv, PDF, Vim
Slug: apvlv-added-tab-view

各位还记得笔者去年为大家介绍的 Vim 化的 PDF 阅览工具
[Apvlv](http://linuxtoy.org/archives/apvlv.html) 吗？最近，Apvlv
增添了两项不错的新特性：一是类似 Firefox
的分页浏览功能（如下图所示）；二是，现在 Apvlv 支持 PDF
书签了。喜欢的朋友赶紧去升级吧。

![Apvlv](http://i.linuxtoy.org/images/2009/02/apvlv-tab.png)

这里着重说一说 Apvlv 的分页浏览功能。通过 :tabnew 可以开新的标签，再配合
gt、gT、以及 ngt 就可以在各个标签之间切换了。

目前，笔者已将 Apvlv 作为主要的 PDF 阅览工具使用，但 Apvlv
还缺少一项重要功能，即对带密码保护的 PDF 提供支持。期待作者在 Apvlv
后续版本中能够加入。

由于作者目前还没有准备新的 tarball
包，所以要尝试这些新功能的话，你需要通过 svn 获取其源代码并自行编译。

[Apvlv](http://code.google.com/p/apvlv/source/checkout)
