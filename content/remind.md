Title: Remind: 命令行的 calendar 及 todo list
Date: 2009-03-11 14:17
Author: toy
Category: Apps
Tags: Calendar, Remind, Todo list
Slug: remind

[撰文/逸飞]

用 vi 习惯了后，做什么都想 vi 化。用过各种各样的任务管事软件，先是
Outlook、KOrganiser、Evolution，试过本站推荐的
[todo.txt](http://linuxtoy.org/archives/todotxt.html)、[Dev
Todo](http://linuxtoy.org/archives/dev-todo.html)，还试用了一周的
tdl，都不能如意（tdl
相对比较不错的说，可惜有个问题我怎么也找不到答案，就是无法查看指定日期的日程安排，有知道的同学指点一下，感激不尽）。后来抱着试一试的心情，试用了一下食古不化同学推荐的
Remind，顿有相见恨晚之感，在此强烈推荐！

上面讲到 vi，Remind 就是一款可以用 vi 来编辑你的 todo list
的工具。我最喜欢 Remind
的特点是它的数据库就是文本文件，简单易懂，但是功能强大，应用灵活！这也符合
Linux 的精神。

下面讲一下我的独特应用。Remind 是一个 calendar 工具，不是 todo
工具（讲得不对请指正，我也是刚用不久，还有很多东西要发掘）。它的日期指定方式多种多样，能设定各种特定的时间。但是好象没有管理
todo 事项的功能，其实只要稍作变通就可以实现。

我的方法是专门建一个文件夹，取名 rem，然后在该文件夹下建若干个 .rem
文件（Remind 的数据文件），如
birthdays.rem、item1.rem、item2.rem、todos.rem。.rem
文件是文本文件，可以用 vi、Emacs 建立编辑。

todo.rem 是一般日常事务，item1、item2
代表特定项目，项目完成后把该文件移走或删除就好了。然后用命令：

`$ remind .`

可以处理本文件夹下所有符合条件的项目。

下面讲怎样管理 todo 事项。Remind 命令格式如下：

`REM Mar 11 2009 MSG feed friend's dog.`

那到了 2009 年 3 月 11 日这天这就会提示“feed friend's
dog."，但是喂好了狗，怎样隐藏提示呢？用 vi
在这句话说面加一个＃号就可以了，＃被 Remind 理解为注释。

如果你忘了喂狗，Remind
在第二天并不会提醒你，那朋友的狗就要饿死了，可以写成：

`REM Mar 11 2009 *1 MSG feed friend's dog.`

那从 3 月 11 日起，Remind 会天天提醒你，直到你把它注释掉。

如果要连续喂 3 天，可以写成：

`REM Mar 11 2009 *1 UNTIL Mar 13 2009 MSG feed friend's dog.`

如果在 4 天内隔天喂一次，可以写成：

`REM Mar 11 2009 *2 UNTIL Mar 14 2009 MSG feed friend's dog.`

Remind 可以在[这里下载](http://www.roaringpenguin.com/products/remind)。
