Title: ibus-table 1.8.3 发布
Date: 2014-07-04 11:30
Author: lovenemesis
Category: Input Method
Tags: Fedora, ibus
Slug: ibus-table-1-8-3-released

ibus-table 1.8.3 已经发布，简化了数据库格式并支持与 GNOME 3
集成。*感谢发布者 Wu Peng 来稿*

新特性有:

-   简化的 sqlite 数据库格式，减小了文件体积;
-   通配符支持，可在对话框中设置;
-   更多配置选项，gnome 3 集成;
-   改进候选词的排列顺序;
-   修正了输入时的光标移动;
-   错误修正;

更新 ibus-table, 需要重新构建相关的软件包, 如 `ibus-table-chinese`,
`ibus-table-others` 等。

欢迎大家使用 ibus-table 1.8.3, 预祝使用愉快。

[英文更新摘要](https://raw.githubusercontent.com/mike-fabian/ibus-table/master/NEWS)

**PS:** 此更新已经进入Fedora 19/20 updates-testing repo。

可以使用如下 yum 命令在Fedora 19/20 上升级 ibus-table:

`#su -c 'yum upgrade --enablerepo=updates-testing "ibus-table*"'`
