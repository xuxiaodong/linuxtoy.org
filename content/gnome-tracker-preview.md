Title: GNOME Tracker 初赏
Date: 2010-04-30 02:16
Author: lovenemesis
Category: Desktop Stuff, Featured
Tags: GNOME, tracker
Slug: gnome-tracker-preview

相对于 [GNOME Activity
Journal](http://linuxtoy.org/archives/gnome-activity-journal-preview.html)
独特的时间索引， GNOME 3.0 的另一个组件 GNOME Tracker
则注重将传统的桌面搜索功能进一步发扬光大。

与 KDE4 引入的桌面搜索类似，GNOME Tracker 0.8 同样使用得到欧盟赞助的
[Nepomuk](http://nepomuk.semanticdesktop.org//)
拓扑模型，提供了全文搜索。此外实时更新保证了可以无需等待即可搜索新增或更改的文件，搜索关键词类推测保证包含关键词的单复数和不同词性的文件都得到搜索。

安装完成后，注销重登录即可在系统托盘区看到 Tracker
的小图标，默认该图标仅在进行索引时出现。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-tracker-status.png)](http://i.linuxtoy.org/images/2010/04/screenshot-tracker-status.png)

如图，左键点击显示索引进度，似乎目前邮件搜索被暂时禁用了。点击右键或者输入
tracker-preferences 即可出现首选项对话框。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-indexing-preferences-01-249x250.png)](http://i.linuxtoy.org/images/2010/04/screenshot-indexing-preferences-01.png)

在首选项的 Indexing
标签页下可以调整索引选项，对于挂载设备点和可移动介质也可以做到即时索引。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-indexing-preferences-02-249x250.png)](http://i.linuxtoy.org/images/2010/04/screenshot-indexing-preferences-02.png)

在 Location 标签页可以设定监视的文件夹，递归和非递归检索的分类很贴心。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-indexing-preferences-03-249x250.png)](http://i.linuxtoy.org/images/2010/04/screenshot-indexing-preferences-03.png)

在 Ignore Content 标签页中预设很多不索引的文件类型，当然也可以自己添加。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-tracker-search-tool-01-300x233.png)](http://i.linuxtoy.org/images/2010/04/screenshot-tracker-search-tool-01.png)

支持各类常见文档的全文搜索，包括 M$ Office 类文档。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-tracker-search-tool-02-300x233.png)](http://i.linuxtoy.org/images/2010/04/screenshot-tracker-search-tool-02.png)

支持各类常见多媒体文件元数据索引，包括 MP3 。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-nautilus-tags-180x250.png)](http://i.linuxtoy.org/images/2010/04/screenshot-nautilus-tags.png)

另外，在安装完 Tracker 之后， Nautilus
中文件右键属性菜单中就会出现对应的 Notes 和 Tags
标签页，输入在这里的内容也是会被 Tracker 检索的。

[![](http://i.linuxtoy.org/images/2010/04/screenshot-database-size-180x250.png)](http://i.linuxtoy.org/images/2010/04/screenshot-database-size.png)

Tracker 生成的数据库相当的苗条，相对于 Google Desktop Linux 的近 300M
，检索同样目录的 Tracker 只有 33M 。

**使用体验：**

1.  原来 GNOME Activity Journal 的 Tags 信息是需要安装 Tracker
    才能实现的。
2.  Tracker 0.8 重置了后台引擎，目前速度飞快，本人 300+G
    的各种资料只用了不到10分钟索引，检索的时候也是即时显现结果。
3.  目前和 GNOME 2.X 系列的整合还很有限， Panel Applet
    和热键搜索框都没有。

**Fedora 13 下安装：**

`su -c 'yum install tracker tracker-search-tool'`

[项目主页](http://projects.gnome.org/tracker/features.html)
