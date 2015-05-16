Title: SunPinYin 2.0.3
Date: 2011-02-18 21:41
Author: lovenemesis
Category: Desktop Stuff
Tags: sunpinyin
Slug: sunpinyin-203

智能整句输入法 SunPinYin 发布 2.0.3 正式版本。

**编译：**

-   正确识别 CFLAGS, CXXFLAGS 和 LDFLAGS
-   Scons 会记录 configure.conf 中的配置参数。
-   支持 ARMEL 架构
-   可以在 FreeBSD 上编译了。

**libsunpinyin:**

-   新的 LOGO!
-   历史纪录缓存更侧重最近的提交。
-   支持 --libdir 和 --libdatadir 配置参数。
-   混拼(Hunpin)支持(感谢 Hanjie Xu 贡献)。
-   修正历史纪录为单个字时的奇怪行为。
-   修正可能的候选词排序问题

**ibus-sunpinyin:**

-   支持 --libdir, --datadir, --execdir 编译参数。
-   使用 `Alt+num` 为候选词删除按键。
-   支持对于 IBus-1.4 的编译

**xsunpinyin:**

-   版本同步 xsunpinyin 和 libsunpinyin。
-   修复空白目录可能导致的崩溃问题。
-   修复在多屏幕时的位置问题。
-   修复导致历史记录丢失的退出崩溃问题。
-   修复当拼音过长的时候文字重叠问题。
-   修复双拼设置的忽视问题。
-   修复切换到英文时的怪异问题。

**scim-sunpinyin:**

-   添加对于 scim 的支持(感谢 liangguo)。

[官方网站下载及更新日志原文](http://code.google.com/p/sunpinyin/)
