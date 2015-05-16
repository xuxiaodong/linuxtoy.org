Title: DocBook 傻瓜包
Date: 2008-10-21 19:56
Author: toy
Category: Apps
Tags: docbook
Slug: docbook-package

读者 [Fisherss](http://fisherss.linuxtoy.net/) 制作了一个 DocBook
傻瓜包，其中整合了 libxml、libxslt、jre，能够用 fop 处理 PDF，xsltproc
处理 HTML。PDF 输出基本完美，中文书签和断行没问题。这个 DocBook
傻瓜包可以为你省却安装、配置 DocBook
的麻烦。有需要的同学可从以下地址下载，体积为 58M。

<http://fisherss.googlecode.com/files/docbook_template-0.7.tar.bz2aa>  
<http://fisherss.googlecode.com/files/docbook_template-0.7.tar.bz2ab>  
<http://fisherss.googlecode.com/files/docbook_template-0.7.tar.bz2ac>  
<http://fisherss.googlecode.com/files/docbook_template-0.7.tar.bz2ad>

此 DocBook 傻瓜包的使用方法为：

> 1. 先合包:
>
> cat docbook\_template-0.7.tar.bz2aa docbook\_template-0.7.tar.bz2ab
> docbook\_template-0.7.tar.bz2ac docbook\_template-0.7.tar.bz2ad >
> docbook\_template-0.7.tar.bz2
>
> 2. source ./init
>
> 3. make pdf-chs || make html-chs || make pdf || make html

详细说明可参见包中的 README 文件。

[via [Fisherss’ Personal Blog](http://fisherss.linuxtoy.net/?p=195)]
