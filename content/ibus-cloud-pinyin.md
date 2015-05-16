Title: iBus的云输入法后端
Date: 2010-08-01 20:36
Author: lovenemesis
Category: News
Tags: cloud, ibus, Input Method
Slug: ibus-cloud-pinyin

[ibus-cloud-pinyin](http://code.google.com/p/ibus-cloud-pinyin/) 使用
[Sogou](http://pinyin.sogou.com/cloud/) 和 [QQ](http://py.qq.com/web/)
的云输入法为后端，目前正在开发中，已基本可用，可在其项目主页上下载源码编译安装。*感谢
Petty 来稿！*

据其主页上的描述，该项目具有如下特点：

-   在线、离线输入，并可快速切换
    -   双拼（包含[微软拼音、搜狗拼音、智能 ABC、拼音加加、UCDOS 6
        智能双拼、自然码方案）](http://code.google.com/p/ibus-cloud-pinyin/wiki/DoublePinyinScheme)及全拼，支持已有的和未来的双拼布局以及全拼的拼音分隔符
    -   独创 Tab
        键进入纠正模式，对刚选定汉字片段或正在编辑的拼音进行纠正
    -   独创 jkl;asdf 键选词（纠正模式中）
    -   简繁体转换（需要
        [opencc](http://code.google.com/p/open-chinese-convert/)）
-   在线输入
    -   多个云拼音引擎同时使用
    -   未完成的部分在后台异步完成，输入过程无阻塞（普通 Web
        输入法会阻塞）
-   离线输入
    -   支持用户自造词，动态调整词频
    -   支持直接导入 scel 词库
    -   支持南方模糊音
-   灵活的 Lua 脚本作为配置文件
    -   可自定义复杂功能，譬如就地 Google Translate 选定内容
-   DBus 接口

它替代了[本站之前介绍过](http://linuxtoy.org/archives/kimpanel-and-sougou-cloud-ime.html)的
[ibus-sogoupycc](http://code.google.com/p/ibus-sogoupycc/)
。值得注意的是，[该项目使用了](http://code.google.com/p/ibus-cloud-pinyin/source/browse/#svn/trunk/src)由[GNOME
提出的](http://live.gnome.org/Vala)类似 C#
的[Vala](http://en.wikipedia.org/wiki/Vala_%28programming_language%29)
语言。
