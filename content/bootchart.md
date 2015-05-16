Title: 你的 Linux 系统启动快吗
Date: 2007-07-13 14:00
Author: toy
Category: Apps
Slug: bootchart

很多朋友抱怨自己的 Linux
系统启动速度太慢，但又苦于没有什么好途径进行分析，使之能够得到改进。如果你正受到这方面问题的困惑，那么有一个
[Bootchart](http://www.bootchart.org/) 小工具能够帮助你。

Bootchart
能够对系统的性能进行分析，并生成系统启动过程的图表，以便为你提供有价值的参考信息。综合所得的信息，你就可以进行相应的改进，从而加快你的
Linux 系统启动过程。

在安装 Bootchart 并重新启动系统后，你就可以在 /var/log/bootchart/
找到它生成的图片文件了。以下是我的系统所生成的启动过程图表，你可以参考一下。

[![Bootchart](http://i.linuxtoy.org/i/2007/07/bootchart_s.png)](http://i.linuxtoy.org/i/2007/07/bootchart.png)

Bootchart 已被包含到常见的 Linux
发行版中，你可以直接从自己所用的系统中加以安装。如果你对 Bootchart
的源代码感兴趣，也可从 [Bootchart
的下载页](http://www.bootchart.org/download.html)获取。
