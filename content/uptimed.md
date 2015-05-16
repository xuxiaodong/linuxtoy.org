Title: Uptimed: 记录 Linux 系统的 uptime
Date: 2012-04-09 22:45
Author: toy
Category: Cli
Slug: uptimed

[Uptimed][u] 堪称 uptime 命令的守护程序版本，利用它你可以将 Linux
系统每次的 uptime  
记录起来，并根据时间长短进行排名。

以下为在我的 Funtoo 上安装 Uptimed 后并执行 `uprecords` 的结果：

# Uptime | System Boot up  
----------------------------+---------------------------------------------------  
1 10 days, 04:46:13 | Linux 3.0.7-gentoo Thu Mar 29 19:42:47 2012  
-> 2 0 days, 02:21:53 | Linux 3.0.7-gentoo Mon Apr 9 20:11:30 2012  
----------------------------+---------------------------------------------------  
no1 in 10 days, 02:24:21 | at Fri Apr 20 00:57:42 2012  
up 10 days, 07:08:06 | since Thu Mar 29 19:42:47 2012  
down 0 days, 19:42:30 | since Thu Mar 29 19:42:47 2012  
%up 92.614 | since Thu Mar 29 19:42:47 2012

目前，我最好的成绩是 10 days，你的 Linux
有多少天呢？欢迎大家在评论中告诉我 :)

[u]: http://podgorny.cz/moin/Uptimed
