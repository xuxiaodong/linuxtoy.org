Title: 在 Ubuntu 中安装 JDK 6
Date: 2006-12-20 21:49
Author: toy
Category: Tutorials
Slug: install_jdk_6_in_ubuntu

对于 Linux 用户来说，Java 1.6 有两项新特性特别引人注目：一是支持 GTK
图形主题，这样 Java
应用程序的外观与系统的默认外观看起来很一致；二是内嵌新的字体渲染引擎会应用系统默认的字体配置，使
Java 应用程序的效果看起来很好，如果是 LCD 屏幕，则更佳。

如果你需要更快的享受到 Java 的新特性，那么可以遵照以下步骤来执行 JDK 6
在 Ubuntu 中的安装过程。

1.  从 Java 的官方网站上[下载 JDK
    6](http://java.sun.com/javase/downloads/index.jsp)
    备用，注意下载的文件为 jdk-6-linux-i586.bin。
2.  到本站下载
    [java-package\_0.28ubuntu1\_all.deb](http://linuxtoy.org/deb/)，并使用
    `sudo dpkg -i java-package_0.28ubuntu1_all.deb` 安装。
3.  准备 fakeroot 工具，如果没有，则使用 `sudo apt-get install fakeroot`
    来安装。
4.  使用 `fakeroot make-jpkg jdk-6-linux-i586.bin` 来制作 deb
    包，生成的文件名为 sun-j2sdk1.6\_1.6.0\_i386.deb。
5.  安装 JDK 6，执行指令 `sudo dpkg -i sun-j2sdk1.6_1.6.0_i386.deb`
    即可。

在安装完成之后，可以执行 `java -version` 来查看当前所用的 Java
的版本。另外，如果你的系统中含有其他 Java 版本，可以使用
`sudo update-alternatives --config java` 来选择最新的版本。

我对 Java 程序截了一幅图，可以看看效果：

![Java App](http://i.linuxtoy.org/i/2006/12/java_app.jpg)
