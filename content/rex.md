Title: (R)?ex: 部署及配置管理工具
Date: 2013-06-13 22:51
Author: toy
Category: Apps
Slug: rex

很高兴从同事那里认识了 [(R)?ex][r] 这个好工具。Rex 允许你通过 SSH
在远端服务器执行命令，不仅可用于快速部署各种服务，而且能够进行配置管理。Rex
的自动化处理的确给人一种方便省时的感觉。

![Rex](http://lt-file.b0.upaiyun.com/files/2013/06/rex.png)

Rex 纯由 Perl 所打造，不必担心的是，你只需了解一点 Perl
便可快速上手。Rex 除了能够从命令行执行操作外，还支持将相关任务放入
Rexfile 文件。

Rex 可通过如下单行进行安装：

$ curl -L get.rexify.org | perl - --sudo -n Rex

同时也针对 Debian、Ubuntu、Gentoo、CentOS、openSUSE、Mageia、Fedora
等发行版提供有安装包，详情可参考 [Rex 的官方获取页面][g]。

[r]: http://rexify.org/  
[g]: http://rexify.org/get/index.html
