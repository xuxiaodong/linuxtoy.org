Title: LibreOffice for Android 开发进展
Date: 2012-07-16 20:45
Author: lovenemesis
Category: Embedded
Tags: Android, libreoffice
Slug: libreoffice-for-android-current-status

拜于 Google Summer of Code，现在 LibreOffice for Android 已经有了原型。

[Michael Meeks
在博客上](http://people.gnome.org/~michael/blog/2012-07-03-libreoffice-android.html)分享了他指导的学生
Iain Billet 在 LibreOffice for Android 上的进展，目前 LibreOffice for
Android 已经颇具雏形了，参见下图。

[![](http://linuxtoy.org/img/2012/07/2012-06-29-android-lame-ui.png "2012-06-29-android-lame-ui")](http://linuxtoy.org/img/2012/07/2012-06-29-android-lame-ui.png)

取得的进展有：

-   整个 LibreOffice 代码树现在支持针对 Android 和 iOS 的交叉编译。
-   初步完成了 VCL 图形库的 Android 原生渲染后端，并且可以捕捉输入事件。

正在开发 **为 Android
平台优化的查看器和文件管理器**，支持手势快速缩放、翻页效果等，如下图：

[![](http://linuxtoy.org/img/2012/07/2012-06-29-android-viewer.png "2012-06-29-android-viewer")](http://linuxtoy.org/img/2012/07/2012-06-29-android-viewer.png)

[![](http://linuxtoy.org/img/2012/07/2012-06-29-android-pagination.png "2012-06-29-android-pagination")](http://linuxtoy.org/img/2012/07/2012-06-29-android-pagination.png)

下一步：

-   使用 Mozilla 为 Firefox for Android
    开发的链接器，大幅度缩小实现链接库体积。
-   实现对 Android /Intel X86 平台的兼容。
-   通过合并链接库为单一共享库的方式实现进一步优化，该项措施不仅是 iOS
    版本的先决条件，而且还将使得桌面版本的性能得到改善。

*消息来源：*[Ars
Technica](http://arstechnica.com/information-technology/2012/07/libreoffice-for-android-advances-document-viewer-is-on-the-way/)
