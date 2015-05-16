Title: 借我一双写轮眼──Less 语法高亮
Date: 2009-01-08 10:45
Author: Kardinal
Category: Apps
Slug: less-highlight

less 是 Linux
平台下最常用全屏文件查看程序……（此处省略一万字）……可谓”人类的好朋友“
^\_^!!

但是 less 显示的内容总是灰头土脸的，很让人不爽

我无意中发现一个秘密，可以让 less 摇身一变，摩登又靓丽

首先安装 source-highlight  
（这个工具主要用途是将文件转换为语法高亮的 html
页面，有兴趣的话可以试一下）

在 shell 的配置文件中添加以下语句  
（如果是 bash 的话就是 .bashrc）  

` #less语法高亮。需要安装 source-highlight PAGER='less -X -M' export LESSOPEN="| /usr/bin/src-hilite-lesspipe.sh %s" export LESS=' -R '`

看看效果  
` source .bashrc less xxx`

/usr/share/source-highlight/default.lang 文件可以设置默认语言类型，添加  
` include "sh.lang"`  
然后 less .bashrc
