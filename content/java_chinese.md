Title: 解决 Java 应用程序的中文显示及中文输入问题
Date: 2006-08-01 15:13
Author: toy
Category: Tutorials
Slug: java_chinese

经过近两天时间的奋战，终于解决了 Java
应用程序的中文显示及中文输入问题，现整理如下，供有兴趣的朋友参考。

一、中文显示问题的解决

问题描述：Java 应用程序的中文无法显示，呈现方块状。

原因分析：Java 应用程序无法找到可供显示中文的字体。

解决方案：首先，确保系统里安装了 [JDK
1.5.0\_06](http://java.sun.com/j2se/1.5.0/download.jsp)，如果安装的是
JRE 1.5.0\_06，那么卸掉 JRE，再安装 JDK。然后下载 [fireflysung
1.3.0](http://cle.linux.org.tw/fonts/FireFly/fireflysung-1.3.0.tar.gz)，解压后将其中的
ttf 文件丢到系统字体目录，我是放到 ~/.fonts 字体目录的，再用
fc-cache -f -v 跑一遍，让系统知道这个字体。最后，就是转到 JDK 安装目录的
/usr/lib/j2sdk1.5-sun/jre/lib/fonts 中，使用下面的命令来完成。

` 　　sudo mkdir fallback 　　cd fallback 　　sudo ln -s ~/.fonts/fireflysung.ttf 　　sudo mkfontdir 　　sudo mkfontscale 　　`

二、中文输入问题的解决

问题描述：使用 Ctrl+Space 无法呼出 scim，因此无法在 Java
应用程序中输入中文。

原因分析：1.可能是由于该 Java 应用程序将 Ctrl+Space
定义成了快捷键，所以与 scim 存在冲突。2.由于 scim XIM
支持模块没能自动加载，故导致在 Java 应用程序中无法呼出 scim。

解决方案：针对第一种原因，只要修改 scim 的呼出热键，或者修改 Java
应用程序中的快捷键，即可解决问题。

而第二种原因可以按如下方法处理：

1.检查 XMODIFIER 的设置

`export | grep XMODIFIER | grep "@im=SCIM" | wc -l`

输出应该为1。如果不是，则检查系统配置，推荐使用 utf-8 区域。

2.如果上一步输出无误，则输入下列命令：

`ps aux | grep "scim-launcher.*-f x11" | grep -v grep | wc -l`

此输出应该大于或等于1。如果不是，如我的输出为0，则说明 scim XIM
支持模块没有自动载入。你可以手动载入它：

`scim -d -c socket -f x11 -e socket`

此时，我启动 Java 应用程序，试了试
scim，已经可以输入中文了。但如果每次都手动加载还是比较麻烦，所以我们考虑让系统自动加载它。

在/etc/X11/Xsession.d中创建 75custom-scim\_init 文件，包括如下内容：

` 　　export XMODIFIERS="@im=SCIM" 　　export GTK_IM_MODULE="scim" 　　export XIM_PROGRAM="scim -d" 　　`

转到 System->Preferences->Sessions，选择 Startup Programs，添加
scim -d，并保留顺序为50。

登录 root 终端，输入下列命令：

`gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules`

重新启动系统，一切正常，cool!

参考：

[最简单的对 JDK
1.5的中文乱码处理方法](http://forum.ubuntu.org.cn/viewtopic.php?t=6338)
中 kdekid 网友的方法，既保险又简单，感谢。  
　　[Why XIM apps does not
work?](http://www.scim-im.org/wiki/faq/general/why_xim_apps_does_not_work)
scim 的官方文档，遇到问题查找官方文档不失为一种解决之道啊。
