Title: man 使用技巧两则
Date: 2007-09-08 11:10
Author: toy
Category: Tips
Slug: man-tricks

记得我初学 Linux 使用时，首先了解的就是如何在 Linux
系统中获得帮助的课程。当然，这其中少不了 man 命令的介绍。今天，在
Linux.com 网站读到一篇介绍 man
使用技巧的文章，个人感觉很受用，现介绍给大家分享。

1.  **使用书签**

    ![man tricks](http://i.linuxtoy.org/i/2007/09/man-trick1.png)

    man 其实是调用 less
    来显示手册页的。因此，在阅读内容比较长的页面时，可以使用书签来标记需要重复阅读的重要内容。标记的方法为：先按
    **m** 键，然后在 mark: 后输入标记字母，如
    a。需要说明的是，标记符是区分大小写的，也就是说 a 与 A
    是两个不同的标记符。

    当你需要返回先前设置的书签时，可以按 **'** 键（单引号）。此时会显示
    goto mark:，输入你设置的标记符即可。

2.  **测试命令**

    ![man tricks](http://i.linuxtoy.org/i/2007/09/man-trick2.png)

    当你在阅读 man 手册页时想要对命令的用法进行尝试的话，那么可以使用
    **!**。这让你不必打开新的终端，也不用离开 man 手册的阅读页面。在按下
    **!**
    之后，你就可以自由输入所要测试的命令了。完成后，按回车键将返回到 man
    手册的阅读页面。

- *[Secrets of the man command by Shashank
Sharma](http://www.linux.com/feature/119031)* [Linux.com]
