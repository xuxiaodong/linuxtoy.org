Title: ps、kill 使用备查
Date: 2006-09-12 10:48
Author: toy
Category: Cli
Slug: ps_and_kill

-   ps－查看当前正在运行的进程，示例：$ ps
-   kill {PID}－通过 PID 来停止任意进程，示例：$ kill 1012
-   killall {Process-name}－通过名称来停止任意进程，示例：$ killall
    httpd
-   ps -ag－获取所有正在运行进程的信息，示例：$ ps -ag
-   kill 0－停止所有的进程（你的 shell 除外），示例：$ kill 0
-   linux-command &－后台执行进程，示例：$ ls / -R | wc -l &
-   ps aux－显示进程的所有者，示例：$ ps aux
-   ps ax | grep process-U-want-to see－查看某个特定的进程，示例：$ ps
    ax | grep httpd
-   top－查看当前正运行的进程、内存及 CPU 占用率，示例： $ top

[via [NDS
Engineers](http://www.ndsengineers.com/reference/353314-linux-commands-identify-kill-running-process.html)]
