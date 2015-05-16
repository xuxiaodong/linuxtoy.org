Title: Cherokee：最快的 Web 服务器
Date: 2008-12-01 19:30
Author: toy
Category: Apps
Tags: Cherokee, Web server
Slug: cherokee

Cherokee 号称是目前最快的 Web 服务器软件，在性能上，甚至比 Nginx
还略胜一筹。与 Apache、Lighttpd、Nginx
等其他同类软件的对比，大家不妨看看这个[测试页面](http://www.cherokee-project.com/benchmarks.html)。我在本机安装了
Cherokee，一番使用下来，Cherokee 给我的感觉是，其易用性做得也很不错。

![Cherokee](http://i.linuxtoy.org/images/2008/12/cherokee.png)

Cherokee 的功能包括支持 FastCGI、SCGI、PHP、CGI、TLS 及 SSL
加密连接，虚拟主机，授权认证，实时编码，载入均衡，与 Apache 兼容的 log
文件等等。

Cherokee 内含一个名为 cherokee-admin
的工具，执行后，允许管理员直接通过浏览器进入 <http://localhost:9090/>
对其进行管理和配置。比如，开启或关闭服务器，进行一般选项的设定，配置虚拟服务器、信息源、图标、Mime
类型等项目。

感兴趣的同学可进入 [Cherokee
的官方主页](http://www.cherokee-project.com/)作进一步的了解，或者[下载其最新版本的源代码](http://www.cherokee-project.com/downloads.html)。
