Title: LFTP 3.5.15 & 3.6.0 发布
Date: 2007-10-21 09:01
Author: toy
Category: Apps
Slug: lftp-3515-and-360-released

[LFTP](http://lftp.yar.ru/) 是一个非常经典的命令行 FTP
客户端程序。最近，LFTP 不仅发布了一个 bug 修订版
3.5.15，而且同时也发布了包含新增特性的版本 3.6.0。在 LFTP 3.5.15
中的超时处理问题及关闭代理服务器设置时所产生的 bug 已经修复。LFTP 3.6.0
对程序的主要代码进行了清理，并添加了一些新的设置、命令以及选项。

[![LFTP](http://i.linuxtoy.org/i/2007/10/lftp_s.png)](http://i.linuxtoy.org/i/2007/10/lftp.png)

LFTP 3.6.0 的详细更新记录为：

- major code cleanup.  
- new setting ftp:use-stat-for-list allows faster directory listing.  
- new command `eval' with -f option allows complex aliases.  
- send encoded parts of ftp URLs untranslated to ftp server.  
- new mirror
options --on-change, --depth-first, --no-empty-dirs, --ascii.  
- new mirror option --only-existing (Damon Harper).  
- new setting xfer:log, log successful transfers if true to
~/.lftp/tarnsfer\_log.  
- new setting ssl:check-hostname.  
- fixed cls exit code in case of an error.

- [Download LFTP 3.5.15 & 3.6.0](http://lftp.yar.ru/get.html)
