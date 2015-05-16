Title: 使用 WebRunner 运行 Web 应用程序
Date: 2007-10-15 09:26
Author: toy
Category: Apps
Slug: webrunner

使用 [WebRunner](http://wiki.mozilla.org/WebRunner) 运行 Web
应用程序就像运行系统中原生的独立桌面程序一样。与一般的 Web
浏览器相比，WebRunner 既没有菜单，也没有工具栏，仅保持最少的
UI。WebRunner 的优势包括可以很好的与当前桌面整合，比如你可以为 Web
应用程序创建快捷方式，可以当一个正常的桌面程序来使用它；使用独立的进程；能够跨平台运行等。

[![WebRunner](http://i.linuxtoy.org/i/2007/10/webrunner_s.png)](http://i.linuxtoy.org/i/2007/10/webrunner.png)  
*使用 WebRunner 运行 Gmail*

WebRunner 目前的最新版是
0.7，在[下载安装包](http://starkravingfinkle.org/projects/webrunner/webrunner-0.7-linux.tar.bz2)后解开即可执行。例如，你可以通过在终端中输入以下命令来执行
Gmail：

`webrunner -uri http://mail.google.com`

当然，更好的使用方式是为其创建一个快捷方式，这就跟使用一般的桌面程序无异了。
