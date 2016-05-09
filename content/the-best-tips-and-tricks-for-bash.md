Title: Bash 使用技巧大补贴
Date: 2007-03-28 22:03
Author: toy
Category: Tips
Slug: the-best-tips-and-tricks-for-bash

Bash 是我们经常与之打交道的 Shell 程序，本文针对其使用技巧进行了搜罗。相信在你看过这些内容之后，定会在 Bash 的世界里游刃有余。

<!-- PELICAN_END_SUMMARY -->

-   从历史中执行命令

    有时候，我们需要在 Bash 中重复执行先前的命令。你当然可以使用上方向键来查看之前曾经运行过的命令。但这里有一种更好的方式：你可以按 Ctrl + r 组合键进入历史搜索模式，一旦找到需要重复执行的命令，按回车键即可。

-   重复命令参数

    先来看一个例子：  

        mkdir /path/to/exampledir
        cd !$

    本例中，第一行命令将创建一个目录，而第二行的命令则转到刚创建的目录。这里，`!$` 的作用就是重复前一个命令的参数。事实上，不仅是命令的参数可以重复，命令的选项同样可以。另外，Esc + . 快捷键可以切换这些命令参数或选项。

-   用于编辑的快捷键

    -   Ctrl + a：将光标定位到命令的开头
    -   Ctrl + e：与上一个快捷键相反，将光标定位到命令的结尾
    -   Ctrl + u：剪切光标之前的内容
    -   Ctrl + k：与上一个快捷键相反，剪切光标之后的内容
    -   Ctrl + y：粘贴以上两个快捷键所剪切的内容
    -   Ctrl + t：交换光标之前两个字符的顺序
    -   Ctrl + w：删除光标左边的参数（选项）或内容
    -   Ctrl + l：清屏

-   处理作业

    首先，使用 Ctrl + z 快捷键可以让正在执行的命令挂起。如果要让该进程在后台执行，那么可以执行 bg 命令。而 fg 命令则可以让该进程重新回到前台来。使用 jobs 命令能够查看到哪些进程在后台执行。

    你也可以在 fg 或 bg 命令中使用作业 id，如：`fg %3`

    又如：`bg %7`

-   使用置换

    -   命令置换

        先看例子：
        
            du -h -a -c $(find . -name *.conf 2>&-)

        注意 `$()` 中的部分，这将告诉 Bash 运行 find 命令，然后把返回的结果作为 du 的参数。

    -   进程置换

        仍然先看例子：
        
            diff <(ps axo comm) <(ssh user@host ps axo comm)

        该命令将比较本地系统和远程系统中正在运行的进程。请注意 `<()` 中的部分。

    -   xargs

        看例：  

            find . -name *.conf -print0 | xargs -0 grep -l -Z mem_limit | xargs -0 -i cp {} {}.bak

        该命令将备份当前目录中的所有 .conf 文件。

-   使用管道

    下面是一个简单的使用管道的例子：  

        ps aux | grep init

    这里，`|` 操作符将 ps aux 的输出重定向给 grep init。

    下面还有两个稍微复杂点的例子：  

        ps aux | tee filename | grep init

    及：  

        ps aux | tee -a filename | grep init

-   将标准输出保存为文件

    你可以将命令的标准输出内容保存到一个文件中，举例如下：`ps aux > filename`

    注意其中的 `>` 符号。

    你也可以将这些输出内容追加到一个已存在的文件中：`ps aux >> filename`

    你还可以分割一个较长的行：  

        command1 | command2 | ... | commandN > tempfile1
        cat tempfile1 | command1 | command2 | ... | commandN > tempfile2

-   标准流：重定向与组合

    重定向流的例子：  

        ps aux 2>&1 | grep init

    这里的数字代表：

    -   0：stdin
    -   1：stdout
    -   2：sterr

    上面的命令中，`grep init` 不仅搜索 `ps aux` 的标准输出，而且搜索 sterr 输出。

[The best tips & tricks for bash, explained](http://www.linuxtutorialblog.com/post/tutorial-the-best-tips-tricks-for-bash) [Linux Tutorials Blog]

(Thanks to Rechosen!)
