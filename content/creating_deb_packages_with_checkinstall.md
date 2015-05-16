Title: 使用 Checkinstall 创建 deb 安装包
Date: 2006-08-01 14:01
Author: toy
Category: Tutorials
Slug: creating_deb_packages_with_checkinstall

Checkinstall 用于创建简单的 deb
安装包的确十分方便。除了安装、卸载方便之外，你还可以与他人分享。而且，其创建过程也是非常容易。

首先，保证系统已经安装了 Checkinstall。如果没有，则
`sudo apt-get install checkinstall`。

其次，下载要制作 deb
包的程序源码，准备好依赖，解压，进入目录配置并编译。

最后，一句命令 `checkinstall -D make install`，按提示完成即可。

在编译的目录里可以找到创建好的 deb 包，使用 `dpkg -i` 或 `dpkg -r`
就可以方便地安装或是卸载了。
