Title: PCMan File Manager 将要重写
Date: 2009-09-28 16:51
Author: toy
Category: News
Tags: Pcmanfm
Slug: pcman-file-manager-to-rewrite

{ 编译/guest }

由于原有 PCManFM 的一些限制和无法解决的 bug，洪任諭 (Hong Jen Yee)  
决定重新设计并重写整个程序。若没有重大的 bug，原有的 0.5.1  
版本近期将不再更新。

下一代 PCMan File Manager 的目标（个人理解为将会新增的特性）：

1. 在支持 glib/gio 和 gvfs
的同时仍保持原有的性能和内存占用（作者接下来做了一段说明）我知道很多人不相信这个，认为使用来自
GNOME 的 glib/gio gvfs 会让程序更慢更重量级，当然很多使用 gio/gvfs/GNOME
的程序都很慢，但是相信我，PCManFM 不会成为其中之一。很多人认为基于 GTK+
的程序很慢，也不是轻量级，但是如你所知，PCManFM 已经证明这是错误的。  
2. 无缝访问远程文件系统 sftp、smb、ftp（gvfs 提供功能）  
3. 支持回收站（gvfs 提供功能）  
4. 将程序核心功能分离为独立的 libfm  
5. 更好的 DnD 支持，支持 XDS (X Direct Save，详见  
)  
6. 更小代码量，更好的组织结构  
7. 与其他程序更好的兼容性 (因使用 glib/gio)  
8. 使用新版 GTK+ 的新特性  
9. 更好的桌面和卷管理  
10. 使用 LD\\\_PRELOAD 加载 libfm，这样可以使得 libfm 提供的 file
manager widgets 替代 GTK+ 中的默认 file dialogs

如果没什么意外，下一代 PCManFM 将于 09 年末或 10 年 Q1 发布。

来自 PCManFM 主页，仅作简单翻译。参考原网页 。

{ Thanks guest. }
