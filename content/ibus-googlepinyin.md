Title: IBus-GooglePinYin
Date: 2011-09-03 12:31
Author: lovenemesis
Category: Input Method
Tags: Fedora, googlepinyin, ibus
Slug: ibus-googlepinyin

[Shellexy 童鞋](http://twitter.com/shellexy)将Android 平台的 Google
Pinyin 输入法移植到 IBus 输入法框架下了。

注意该程序并非 Google 官方出品，是将爱好者自行将 Android
平台版本迁移过来。

Fedora 15 下编译安装：

1.  下载并安装必要编译组件：

        pkcon install cmake ccache gcc-c++ opencc-devel ibus-devel

2.  下载并解压[源代码包](http://code.google.com/p/libgooglepinyin/downloads/list)。
3.  进入源代码目录：

        cd libgooglepinyin-*

4.  创建编译目录：

        mkdir build && cd build
            执行 CMake 编译脚本：cmake .. -DCMAKE_INSTALL_PREFIX=/usr

5.  编译：

        make -j3

6.  安装：

        su -c 'make install'

7.  之后在 IBus 中启用即可。

[项目代码托管首页](http://code.google.com/p/libgooglepinyin/)

[消息来源](https://twitter.com/#!/shellexy/status/109835784110092288)
