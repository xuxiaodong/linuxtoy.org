Title: makeself 制作自解压压缩包
Date: 2009-01-06 14:42
Author: hmy
Category: Apps, Cli
Tags: makeself shell
Slug: makeself

Google Earth for Linux 就是利用该软件制作的自解压包。假如你手上有 Nginx
的源代码包 nginx.tgz，你想做成类似 Google Earth
那种一次执行就自动安装的包，那么利用 makeself 可以轻松实现。

建立一个临时目录 nginx，把 nginx.tgz 放在里面，然后在该目录里面写一个
shell，名为 init.sh，内容如下：  

` #!/bin/bash tar zxpf nginx.tgz -C /tmp/ cd /tmp/nginx ./configure --prefix=/tmp/nginxtest make make install`

然后在 nginx 目录上层目录执行下面的命令：

`# makeself nginx nginx.bin nginx ./init.sh`

那么就会把 nginx 目录打包成 nginx.bin。执行 nginx.bin
会自己把自己解压到一个临时目录，然后自动执行
init.sh。有兴趣的同学自己去试吧！

[makeself](http://megastep.org/makeself/)
