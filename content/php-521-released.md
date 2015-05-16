Title: PHP 5.2.1
Date: 2007-02-09 10:19
Author: toy
Category: Apps
Slug: php-521-released

[PHP](http://www.php.net/) 开发团队已经于早些时候宣布了 PHP 5.2.1
可用的消息，据悉，本次发布主要是增强了 5.x 分支的稳定性和安全性。PHP
官方建议使用者升级到最新版。

在 PHP 5.2.1 发布公告中所列出的安全增强和修正有：

> * Fixed a possible safe\_mode & open\_basedir bypasses inside the
> session extension.  
>  * Prevent search engine from indexing the phpinfo() page.  
>  * Fixed a number of input processing bugs inside the filter
> extension.  
>  * Fixed unserialize() abuse on 64 bit systems with certain input
> strings.  
>  * Fixed possible overflows and stack corruptions in the session
> extension.  
>  * Fixed an underflow inside the internal sapi\_header\_op()
> function.  
>  * Fixed allocation bugs caused by attempts to allocate negative
> values in some code paths.  
>  * Fixed possible stack overflows inside zip, imap & sqlite
> extensions.  
>  * Fixed several possible buffer overflows inside the stream
> filters.  
>  * Fixed non-validated resource destruction inside the shmop
> extension.  
>  * Fixed a possible overflow in the str\_replace() function.  
>  * Fixed possible clobbering of super-globals in several code paths.  
>  * Fixed a possible information disclosure inside the wddx
> extension.  
>  * Fixed a possible string format vulnerability in *print()
> functions on 64 bit systems.  
>  * Fixed a possible buffer overflow inside mail() and
> ibase\_{delete,add,modify}\_user() functions.  
>  * Fixed a string format vulnerability inside the odbc\_result\_all()
> function.  
>  * Memory limit is now enabled by default.  
>  * Added internal heap protection.  
>  * Extended filter extension support for $\_SERVER IN cgi AND
> apache2 SAPIs.

你可以从下面的链接下载到 PHP 的最新版，其中包括完整的源码包和用于
Windows 平台的二进制包。

Download [PHP 5.2.1](http://www.php.net/downloads.php)
