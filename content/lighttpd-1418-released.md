Title: Lighttpd 1.4.18 发布
Date: 2007-09-10 10:20
Author: toy
Category: Apps
Slug: lighttpd-1418-released

[Lighttpd](http://www.lighttpd.net/)
是一个安全、快速、符合规范、以及具有弹性的 Web 服务器。目前有为数不少的
Web 2.0 网站都在使用它。最近，Lighttpd 发布了 1.4.18 版。这是一个 bug
修订版，其中修正了一些安全方面的问题。如果你还在使用 Lighttpd
的旧版本，那么应尽快加以更新。

![lighttpd](http://i.linuxtoy.org/i/lighttpd.png)

在 Lighttpd 1.4.18 中主要修正的问题如下：

- fixed compile error on IRIX 6.5.x on prctl()  
- fixed forwarding a SIGINT and SIGHUP when using max-workers  
- fixed FastCGI header overrun in mod\_fastcgi  
- fixed hanging redirects with keep-alive due to missing
"Content-Length: 0" headers  
- fixed crashing when using undefined environment variables in the
config  
- fixed compilation of mod\_mysql\_vhost on irix

你可以从这里[下载 Lighttpd
1.4.18](http://www.lighttpd.net/download/lighttpd-1.4.18.tar.gz)。
