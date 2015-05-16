Title: FileZilla 3.0.5 RC1 发布
Date: 2008-01-02 08:00
Author: toy
Category: Apps
Slug: filezilla-305-rc1-released

开源、跨平台的 FTP 软件
[FileZilla](http://linuxtoy.org/search/filezilla) 在昨天发布了 3.0.5 RC1
版。该版本主要添加了目录列表比较、打开/编辑本地文件、使用默认的系统语言选项等新特性。同时，FileZilla
3.0.5 RC1 也包含针对发送及接收指示器的新美工设计。

![FileZilla](http://i.linuxtoy.org/i/2007/09/filezilla-logo.png)

**FileZilla 3.0.5 RC1 更改日志**

New features:  
+ Directory listing comparison  
+ Ability to open and edit local files  
+ Add option to use default system language. Note: Language selection
will be reset to default if updating to this version.  
+ New artwork for send and recv indicators

Fixed bugs:  
- Fix crash with keepalive timer  
- nix: Use proper locale initialization, happened too late in FZ's
startup sequence in previous versions.  
- Fix issue with proxies in combination with nonstandard ports  
- Fix timezone offset detection if user has specified a custom offset  
- MSW: Cancel remote renaming of files if listing changes  
- Fix prefix search in file listings not working with all keys  
- Internal engine state could get confused on failed transfers  
- Fix visual refresh problem in queue  
- Fix several glitches with right-to-left languages  
- Write errors during downloads are now critical, as they usually
require user interaction (e.g. disk full)  
- Calculate proper filesize on VMS servers  
- Remote directory tree did not display all known directories  
- Don't display error messages if some local directories are not
accessible during auto-completion in local view header or if if they are
parent of an accessible directory in the local tree view.

你可以从这里[下载适用于 Linux 系统的 FileZilla 3.0.5
RC1](http://sourceforge.net/project/showfiles.php?group_id=21558&package_id=206762&release_id=565102)。
