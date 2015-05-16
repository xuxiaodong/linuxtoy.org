Title: GNOME Activity Journal 初赏
Date: 2010-04-29 17:49
Author: lovenemesis
Category: Featured, File Manager
Tags: GNOME, Zeitgeist
Slug: gnome-activity-journal-preview

提起 GNOME 3.0 ，或许绝大多数人想到的是 [GNOME
Shell](http://linuxtoy.org/archives/fedora-12-beta-gnome-shell-preview.html)
， 这次给大家展示下另外一个新组件： GNOME Activity Journal

与通常的桌面搜索根据内容索引不同，GNOME Activity Journal
的主要功能是提供按照时间的文件索引，为用户提供 Nautilus
结构式之外的另外一种检索文件方式。用户在打开电脑后并不需要知道昨天工作的文件名是什么，通过
GNOME Activity Journal
就可以按照类型轻易的找到昨天工作的文件。后台的引擎是
[Zeitgeist](http://live.gnome.org/Zeitgeist) 。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-01-300x182.png)](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-01.png)

这个便是主界面，从鼠标指向位置可以看到可以将常用文件标记上，这样便会一直出现。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-02-300x182.png)](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-02.png)

可以对 PDF 文档格式生成预览。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-03-300x181.png)](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-03.png)

对于视频文件也可以做到预览。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-04-300x182.png)](http://i.linuxtoy.org/images/2010/04/screenshot-activity-journal-04.png)

对于同一类型的文件，可以做到自动归类。

**使用体验：**

1.  与桌面搜索不同， Activity Journal
    不需要花时间建立索引，安装好之后立即就可以使用；
2.  几乎所有的文件都可以做到预览，而且比在 Nautilus 中快很多；
3.  按照功能说明，似乎应该还可以自己添加 Tag
    和评级的，但是没有找到或者当前版本尚未实现。

Fedora 13 用户要尝试它很简单，在终端运行以下命令即可：

`su -c 'yum install gnome-activity-journal'`

[项目主页](http://live.gnome.org/GnomeActivityJournal)
