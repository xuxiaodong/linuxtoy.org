Title: FileZilla 更新到 3.0.3 版
Date: 2007-11-08 09:00
Author: toy
Category: Apps
Slug: filezilla-updated-to-303

开源、好用、跨平台的 FTP 客户端
[FileZilla](http://filezilla-project.org/) 于昨日更新到了 3.0.3
版。此版本添加了自动检测服务器时区、保留文件时间戳的选项、传输类型选择菜单、以及安装一些默认的过滤器等改进。另外，FileZilla
3.0.3 也修正了一些 bug。推荐大家升级。

![FileZilla](http://i.linuxtoy.org/i/2007/09/filezilla-logo.png)

以下引用自 FileZilla 3.0.3 的更新日志，供大家参考：

+ Install some default filters if filters.xml missing in user's settings
directory  
- OS X: Fix remote file viewing/editing  
- Additional fixes for SFTP servers with nonstandard filename
encodings  
+ Automatic server timezone detection. Custom offset in the Site
Manager may need to be adjusted. FTP only.  
+ Option to preserve file timestamps on downloads (all protocols)  
+ Option to preserve file timestamps on uploads on FTP servers
supporting the MFMT command  
+ Add transfer type (ascii/binary/auto) selection to transfer menu  
- Shorten very long filenames on file exists dialog  
- Attempt at working around broken routers and firewalls disconnecting
the control connection of the transfer session on transfers  
- Deleting directories containing lots of files should be faster now  
- Disallow settings/site import from files located in the settings
storage directory  
- Fix nullpointer dereference on non-UTF8 enabled SFTP servers  
- *nix: Fix button height inconsistencies on dialogs with certain
artwork (e.g. Ubuntu 7.10)

- [下载 FileZilla
3.0.3](http://sourceforge.net/project/showfiles.php?group_id=21558&package_id=15149&release_id=552373)
