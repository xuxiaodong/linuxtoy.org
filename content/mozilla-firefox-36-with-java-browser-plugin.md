Title: Mozilla Firefox 3.6 下使用 Java 浏览器插件
Date: 2009-11-21 22:59
Author: lovenemesis
Category: Tutorials
Tags: Firefox, Java
Slug: mozilla-firefox-36-with-java-browser-plugin

即将发布的 Mozilla Firefox 3.6 系列将不再支持以前 OJI (Open Java Virtual
Machine Integration)架构 Java 浏览器插件，需要使用 Java 6 Updates 10
及以后提供的符合 NPAPI 标准的新版本浏览器插件。本文介绍如何在 Mozilla
Firefox 3.6 下配置 Java 浏览器插件。

下文以从 Mozilla 官方下载的 Mozilla Firefox 3.6 Beta 4 i686 Linux
版本为例，介绍如何在 Fedora 12 下为其添加 Java 支持。

***方法一*：使用 Sun Java**

由于 Fedora 12 默认提供的 OpenJDK 6 并未包含新的 NPAPI
标准的插件，所以可以使用 **Sun 的 Java** 解决。

**1.** 从 [Java.com](http://www.java.com) 网站上下载 Java
运行时环境。这里使用 Linux (self-extracting file) 版本。

**2.** 将下载好的文件拷贝到希望安装 Java
的目录下，为其添加可执行权限并运行，
`chmod +x jre*.bin && ./jre*.bin `，按照提示安装即可。

**3.** 在 Java 安装目录中找到名为 **libnpjp2.so**
文件，`find . -name libnpjp2.so` 。

**4.** 为其创建一个符号连接到 Mozilla Firefox 3.6 的安装目录下的 plugins
目录即可。

如果你的 **Java 和 Mozilla Firefox
安装在同一个目录**下（比如像我都安装到 $HOME/Apps
下），那么下面这条命令可以自动完成上面的两步：
`ln -vs $PWD/$(find . -name libnpjp2.so) ./firefox/plugins/libnpjp2.so`

**重新启动 Mozilla Firefox** 即可使用这个新版本的 Java 插件了~

***方法二*：使用 Fedora 13 Rawhide 中的 OpenJDK plugin**

最近 OpenJDK Build17 增加了 Alpha 版本 NPAPI 插件，该插件在 Fedora 13
Rawhide 的 OpenJDK 中可用。

**1.** 将 OpenJDK 更新至 Fedora 13 版本。

`su -c 'yum --enablerepo=rawhide update java-1.6.0-openjdk-plugin'`

**2.** 更改默认的 libjavaplugin.so 指向。

`su -c 'alternatives --config libjavaplugin.so'`

之后输入 2 选择 IcedTeaNPPlugin.so 并按回车确定。

**3.** 重新启动浏览器。经简单测试 Citrix 的 Java 客户端和 RuneScape
可用。

使用 M$ 系统的朋友可以参考 Sun
的[这篇教程](http://www.java.com/en/download/help/new_plugin.xml)进行设置。

[mozillaZine
论坛原帖](http://forums.mozillazine.org/viewtopic.php?f=23&t=1576825)

[FedoraForum
论坛原帖](http://forums.fedoraforum.org/showthread.php?p=1333555)
