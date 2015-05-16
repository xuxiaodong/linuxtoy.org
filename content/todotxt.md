Title: Todo.txt: bash打造的待做事项管理
Date: 2008-07-29 21:04
Author: lwl
Category: Cli
Slug: todotxt

[Todo.txt](http://todotxt.com/)是[lifehacker](http://www.lifehacker.com)的[Gina
Trapani](http://www.ginatrapani.org/)使用bash编写的一个todo列表管理器。你可以在命令行对待做事宜进行添加、删除、修改优先级，以及其他各种操作。所有内容都保存在文本文件中。

例如 （假设你已经*ln -s /path/to/todo.sh ~/bin/t*）：

-   *t add @shopping 买苹果* <span style="#999999;"><span
    style="#999999;">#添加买苹果</span></span>
-   *t ls @home* <span style="#999999;"><span
    style="#999999;">#列出在家里要做的事情</span></span>
-   *t pri 12 a* <span style="#999999;"><span
    style="#999999;">#将编号12的待做事项优先级设置为a</span></span>

还有更多，请用*t -h*观看帮助,
还可以观看youtube[录像](http://lifehacker.com/software/todo%27txt/todotxt-in-action-183429.php)。

Todo.txt在[google
code](http://code.google.com/p/todotxt/)也有镜像，其中包括Shane
Koste用python改写的一个版本，它提供了更多功能。例如任务A依赖于任务B,
你可以将B设置为A的子任务，只有你完成A之后，B才会出现。

太简单？这是[KISS](http://en.wikipedia.org/wiki/KISS_principle)的一个体现，你也可以让事情复杂起来，例如：

-   在本机架设一个[AIM](http://todotxt.com/library/todobot.pl/)或者[Jabber](http://todotxt.com/library/todo_jabber_bot/)机器人，你就可以在其他任何有网络的地方通过这个机器人管理待做事宜了。你当然也可以ssh进去查询。
-   导出到[iPod](http://groups.yahoo.com/group/todotxt/message/108)、PDA或者任何能读文本文件的播放器。
-   我个人比较喜欢用[conky](http://conky.sourceforge.net/)来监视系统状况，也就顺便把高优先级和已经完成的任务在桌面上显示出来。注意conky要设置中文字体才能正确显示中文。Windoz上也可以[显示在桌面](http://lifehacker.com/398997/todo-embeds-the-contents-of-todotxt-onto-your-desktop)上。mac
    osx上自然也不会缺少。
-   通过cron把每天所作的事情发到自己的信箱，再利用gmail的tag功能，把这些[time
    log](http://www.gtdlife.cn/2008/834/download-software-of-time-log/)放到一个类别里面。
-   如果你每天第一件事是看电子邮件，可以设置在凌晨自动把高优先级的事项发到信箱，如果配合[gcalcli](http://code.google.com/p/gcalcli/),
    更是如虎添翼阿。

todo.txt输入输出都是文本，简单而又强大。它的开放性使得如何使用todo.txt依赖于你的想象力，有什么好点子和大家分享么？

[Todo.txt](http://todotxt.com/)
