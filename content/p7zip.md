Title: P7ZIP－Linux 中的 7-Zip
Date: 2006-09-21 21:08
Author: toy
Category: Apps
Slug: p7zip

7-Zip 是一种高压缩比存档格式 7z 的管理器，不过用于 Win 平台。如果是
Linux 用户，则可以使用 [P7ZIP](http://p7zip.sourceforge.net) 来代替。

-   P7ZIP 的安装
    在 Debian/Ubuntu 系统，可通过 sudo apt-get install p7zip 进行安装。
-   P7ZIP 的使用
    -   创建压缩包：7za a -t7z
        test.7z *，此命令将目录中的所有文件压缩到 test.7z 中。
    -   解开压缩包：7za X test.7z，此命令用于将 test.7z
        中的文件提取出来。可使用 -t 来指明压缩格式。
    -   更多信息：7za –help。

（Via [Every Flavour
Beans](http://beans.seartipy.com/2006/09/21/7-zip-compression-format-support-on-gnulinux-using-p7zip/),
thanks!）
