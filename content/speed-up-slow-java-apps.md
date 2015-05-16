Title: Linux 下 Java 开启 OpenGL 技巧
Date: 2009-04-22 10:56
Author: toy
Category: Tips
Tags: Java
Slug: speed-up-slow-java-apps

在我的系统上每次使用 Java 应用程序时，我都感觉特别慢。对于一些比较大的
Java
应用程序而言，这种感觉尤其明显。最近，我学到了一招技巧，提速的效果还不错。如果你也有类似的烦恼，那么赶紧来试试吧。

要使用该技巧，你必须满足以下条件：

1. 开启 OpenGL 3D 加速的显卡  
2. Sun Java version 5 及更高版本

说来也简单，你只需在 Java 应用程序的启动命令中加入如下选项即可：

-Dsun.java2d.opengl=true

这样，该 Java 应用程序就会使用 OpenGL 硬件加速来进行渲染。

以 FreeMind 为例，通过编辑其安装目录下的 freemind.sh
启动脚本，可以加入上面的选项（大约在 209 行左右）。

{ via [Ubuntu Forums](http://ubuntuforums.org/showthread.php?t=1129187)
}
