Title: 使用 UNIX 的 10 个良好习惯
Date: 2007-01-15 08:56
Author: toy
Category: Tutorials
Slug: learn-10-good-unix-usage-habits

*The Linux Cookbook* 一书的作者 Michael Stutz 凭借自己多年使用 UNIX
的经验，总结了 10 个良好习惯，个人认为真的很受用，现摘要如下与大家分享。

1.  建立层级目录：使用 mkdir 的 -p 选项，如 `mkdir -p tmp/a/b/c`。
2.  解包到指定的目录：使用 tar 的 -C 选项，如
    `tar xvf newarc.tar.gz -C tmp/a/b/c`。
3.  联合命令：使用 ;、&&、|| 等控制运算符，如
    `cd tmp/a/b/c && tar xvf ~/archive.tar`。
4.  小心使用变量：把变量放到 "" 中，如  

    ` ~ $ ls tmp/ a b ~ $ VAR="tmp/*" ~ $ echo $VAR tmp/a tmp/b ~ $ echo "$VAR" tmp/* ~ $ echo $VARa`

    ~ $ echo "$VARa"

    ~ $ echo "${VAR}a"  
    tmp/*a  
    ~ $ echo ${VAR}a  
    tmp/a  
    ~ $  

5.  长命令的输入：使用 \\ 分行折断，如  

    ` ~ $ cd tmp/a/b/c || \ > mkdir -p tmp/a/b/c && \ > tar xvf -C tmp/a/b/c ~/archive.tar`
6.  分组命令：使用 ()、{} 来分组命令，如  

    ` ~ $ ( cd tmp/a/b/c/ || mkdir -p tmp/a/b/c && \ > VAR=$PWD; cd ~; tar xvf -C $VAR archive.tar ) \ > | mailx admin -S "Archive contents"`
7.  使用 xargs：可以过滤输出，如  

    ` ~/tmp $ ls -l | xargs -rw-r--r-- 7 joe joe 12043 Jan 27 20:36 December_Report.pdf -rw-r--r-- 1 \ root root 238 Dec 03 08:19 README drwxr-xr-x 38 joe joe 354082 Nov 02 \ 16:07 a -rw-r--r-- 3 joe joe 5096 Dec 14 14:26 archive.tar -rwxr-xr-x 1 \ joe joe 3239 Sep 30 12:40 mkdirhier.sh ~/tmp $`
8.  使用 grep 的 -c 选项可以计算输出的行数，它比使用管道的 wc -l
    更快，如  
    ` ~ $ time grep and tmp/a/longfile.txt | wc -l 2811`

    real 0m0.097s  
    user 0m0.006s  
    sys 0m0.032s  
    ~ $ time grep -c and tmp/a/longfile.txt  
    2811

    real 0m0.013s  
    user 0m0.006s  
    sys 0m0.005s  
    ~ $  

9.  匹配输出的字段：使用 awk，如  

    ` ~/tmp $ ls -l | awk '$6 == "Dec"' -rw-r--r--  3 joe joe   5096 Dec 14 14:26 archive.tar -rw-r--r--  1 root root  238 Dec 03 08:19 README ~/tmp $`
10. 停用 cat 的管道输出：可用 grep 代替，如  
    ` ~ $ time cat tmp/a/longfile.txt | grep and 2811`

    real 0m0.015s  
    user 0m0.003s  
    sys 0m0.013s  
    ~ $ time grep and tmp/a/longfile.txt  
    2811

    real 0m0.010s  
    user 0m0.006s  
    sys 0m0.004s  
    ~ $  

(via
[IBM](http://www-128.ibm.com/developerworks/aix/library/au-badunixhabits.html),
thanks!)
