Title: 使用 localepurge 删除无用的区域配置文件
Date: 2006-11-24 11:47
Author: toy
Category: Tutorials
Slug: localepurge

许多 Linux
用户仅在某个固定的区域使用系统。比如，作为中国的用户通常会使用
zh\_CN，而对其他区域的配置并不会关心。对于这些用户来说，localepurge
将是一个非常有用的小工具。使用它可以在保留需要的区域配置的前提之下删除其他那些系统中存在的无用的区域配置文件，这样自然的就会为你腾出不少磁盘空间。

安装 localepurge 是十分简单的，只需执行
`sudo aptitude install localepurge`
命令就可以了。在安装的过程中，程序会提示你进入如下图所示的画面中进行配置。

[![localepurge](http://i.linuxtoy.org/i/2006/11/localepurge_s.jpg)](http://i.linuxtoy.org/i/2006/11/localepurge.jpg)  
*（localepurge 配置截图）*

使用空格键可以选择需要保留的区域配置，其他的则会被删除。当以后在安装程序时，此工具也会自动执行，勿需再次配置。
