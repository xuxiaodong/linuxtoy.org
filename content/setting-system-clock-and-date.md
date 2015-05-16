Title: 设置系统时钟和日期
Date: 2007-07-20 18:27
Author: toy
Category: Tutorials
Slug: setting-system-clock-and-date

在 Linux 中除了使用 GUI 的方式设置系统时钟和日期之外，我们也可以通过 CLI
使用 date 命令来完成同样的事情。以下是使用 date
命令设置系统时钟和日期的详细过程。

你可以使用如下命令来设置系统时钟和日期：

`date mmddttttyyyy.ss`

其中，命令后跟参数的含义为：

-   mm：月
-   dd：日
-   tttt：时间，包括小时和分钟
-   yyyy：年
-   ss：秒

例如，假设你想要将当前系统的时钟和日期设置为 2007 年 7 月 17 日 11 时 15
分，那么可以执行下列指令：

`date 071711152007`

date 命令不加任何参数，则可以查看当前系统的时钟和日期。

[[via](http://linuxwave.blogspot.com/2007/07/setting-system-clock-and-date.html)]
