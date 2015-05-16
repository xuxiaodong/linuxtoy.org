Title: 使 OpenOffice.org 运行更快的技巧
Date: 2007-06-23 22:01
Author: toy
Category: Tips
Slug: make-openofficeorg-run-faster

OpenOffice.org 是我目前在 Linux
下所用的主力办公软件，但它有一个令人诟病的地方：启动时总是慢吞吞的，这让人十分不爽。今天在
Zolved 上读到一篇可使 OpenOffice.org
提速的技巧文章，在试验后感觉效果很明显，特介绍给大家分享。

[![OpenOffice.org](http://i.linuxtoy.org/i/2007/06/ooo-speed_s.jpg)](http://i.linuxtoy.org/i/2007/06/ooo-speed.jpg)

首先，你需要启动 OpenOffice.org Writer，在设置后，其他的
Calc、Impress、Draw
等组件也会生效。接着，执行“工具->选项”菜单命令，选择左边的“内存”，设置要点如下：

-   在“撤销”选项，步骤数目建议设置为 20 或 30，总之应小于 100。
-   在“图形缓存”选项，OpenOffice.org 使用设置为
    128MB，每个对象的内存设置为 20MB。
-   在“插入对象缓存”选项，设置对象数为 20。
-   选中“启用快速启动”选项。

然后，再选择左边的“Java”，取消选择“使用 Java
运行环境”选项。最后点击“确定”保存你的设置。现在你可以关闭 OpenOffice.org
并再次启动它以感受速度的变化了。

[[via](http://www.zolved.com/synapse/view_content/28209/How_to_make_OpenOffice_run_faster_in_Ubuntu)]
