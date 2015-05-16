Title: 基于浏览器的匿名 P2P 文件分享服务
Date: 2011-11-09 17:39
Author: lovenemesis
Category: Web App
Tags: P2P
Slug: web-based-anonymous-p2p-sharing

FileTea 是一个使用 HTML5 技术编写的试验性 P2P
文件分享站点，只需要启动浏览器即可上传和下载文件。[转载自 shellex
的部落格](http://shellex.info/filetea-an-anonymous-web-based-file-sharing-server/)

发现一个很好玩的东西，[FileTea](https://filetea.me/)

看上去就是个普通的Web介面的文件分享服务，其实伊很有意思：

1.
它是做P2P分享的，服务器不存储文件内容。因此除了正在传输的数据，仅仅保持和上传者、下载者的浏览器会话信息。

2.
依赖HTML5的文件API来提供文件上传。也就是说，一旦浏览器关闭，那么该分享就失效。

当然了，这种东西必须是开源的，在debian SID里可以直接 apt-get install
filetea安装。

近年来Web碉堡了以后，果然所有能被重写的桌面程序都会被重写一遍。Google搞Chrome真是碉堡了。

Update：作者 [Eduardo
Lima](http://www.igalia.com/nc/igalia-247/igalian/item/elima/)
是Linux和Javascript达人啊

**为方便作者回复请前往[原文留言](http://shellex.info/filetea-an-anonymous-web-based-file-sharing-server/)**
