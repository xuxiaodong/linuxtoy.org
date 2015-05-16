Title: Vimpress：使用 Vim 发布 WordPress 网志
Date: 2008-02-22 17:30
Author: toy
Category: Apps
Slug: vimpress

如果你是一位 Vim 使用者，而碰巧又在通过 WordPress
发布网志的话，那么，一定不要错过
[Vimpress](http://www.friggeri.net/projets/vimpress/)。Vimpress 是一个
Vim 插件，利用该插件，你可以直接从 Vim 发布或编辑网志。

![Vimpress](http://i.linuxtoy.org/i/2008/02/vimpress.png)

目前，Vimpress 具有下列功能：

> * 获得文章列表  
>  * 写新文章  
>  * 编辑文章  
>  * 现场保存 (yeah, no kidding)  
>  * 支持分类  
>  * 支持标签

要安装 Vimpress，你只需将所下载的 tar.gz 文件提取到 ~/.vim 目录，并编辑
plugin 下的 blog.vim (在 Settings 部分)：

-   blog\_username：你的 WordPress 帐号名
-   blog\_password：该帐号的密码
-   blog\_url：xmlrpc.php 文件的 URL

另外，如果你要使用 Tag，可以将 enable\_tags 设置为 1，且 UTW tag
支持需要安装额外的[插件](http://blog.circlesixdesign.com/download/utw-rpc-autotag/)。

现在，你可以通过 :BlogNew 命令来写新的文章，完成后可以使用 :BlogSend
发布。如果你需要编辑已经发布的文章，可以使用 :BlogOpen id。此外，使用
:BlogList 命令可以列出已发布的所有文章，如果文章过多的话，反应会很慢。

**更新**

weakish 网友介绍了另一种[在 Vim 中写 WordPress
的方法](http://millenniumdark.blog.ubuntu.org.cn/2007/11/26/%e7%94%a8vim%e5%af%ab%e7%8f%ad%e5%9c%96%e4%b8%ad%e6%96%87%e7%b6%b2%e5%bf%97/)
(通过 vimblog.vim)，值得一试。

P.S. 本文即以 Vimpress 发布。

[via [某人的栖息地](http://www.ooso.net/index.php/archives/278)]
