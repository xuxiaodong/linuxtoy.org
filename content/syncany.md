Title: Syncany
Date: 2011-05-26 16:23
Author: lovenemesis
Category: Cloud
Tags: syncany
Slug: syncany

Syncany 是一款开源的云端存储和文件分享软件，支持在包括 FTP、Amazon S3
等多种环境下备份和分享文件数据。

Syncany 相比 Dropbox 等服务具有以下优势：

-   本地加密：文件经过本地加密后才发送至云端。
-   混合存储：通过插件方式支持多种远程存储媒体。
-   完整版本控制

它支持的远端存储包括：

-   本地文件夹：包括挂载的磁盘、NFS 或者其他任何通过 VFS
    虚拟文件系统实现的文件夹。
-   FTP
-   **IMAP:**使用一个 IMAP 文件夹，文件在分块后作为邮件附件存在。
-   Google Storage
-   Amazon S3
-   Rackspace Cloud Files
-   WebDAV
-   **Picasa：**将文件分块后伪装为图片保存。
-   Windows Share (NetBIOS/CIFS)

目前 Syncany
刚刚发布第一部分代码，速度还比较慢，不过从它的特性来看还是十分值得期待的。

[源代码](https://launchpad.net/syncany/trunk)

[编译指南](http://bazaar.launchpad.net/~binwiederhier/syncany/trunk/view/head:/syncany/DEVELOPMENT)
