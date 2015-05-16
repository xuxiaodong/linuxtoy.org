Title: aptitude 使用快速参考
Date: 2006-11-25 11:16
Author: toy
Category: Tutorials
Slug: aptitude_quick_reference

aptitude 与 apt-get 一样，是 Debian
及其衍生系统中功能极其强大的包管理工具。与 apt-get 不同的是，aptitude
在处理依赖问题上更佳一些。举例来说，aptitude
在删除一个包时，会同时删除本身所依赖的包。这样，系统中不会残留无用的包，整个系统更为干净。以下是笔者总结的一些常用
aptitude 命令，仅供参考。

命令

作用

aptitude update

更新可用的包列表

aptitude upgrade

升级可用的包

aptitude dist-upgrade

将系统升级到新的发行版

aptitude install pkgname

安装包

aptitude remove pkgname

删除包

aptitude purge pkgname

删除包及其配置文件

aptitude search string

搜索包

aptitude show pkgname

显示包的详细信息

aptitude clean

删除下载的包文件

aptitude autoclean

仅删除过期的包文件

当然，你也可以在文本界面模式中使用 aptitude。
