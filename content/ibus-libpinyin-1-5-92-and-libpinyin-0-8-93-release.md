Title: ibus-libpinyin 1.5.92 和 libpinyin 0.8.93 发布
Date: 2013-03-22 15:24
Author: lovenemesis
Category: News
Tags: ibus, libpinyin
Slug: ibus-libpinyin-1-5-92-and-libpinyin-0-8-93-release

ibus-libpinyin 1.5.92 和 libpinyin 0.8.93
已经发布，**新增专业词库及第三方词库导入支持**。*感谢作者 Peng Wu 来稿*

此版本包括以下新特性:

-   新增十大专业词库，可在首选项中配置;
-   可在首选项中, 编辑用户的lua script扩展;
-   可以导入第三方词库, 词库格式参见首选项下方的说明;

安装 ibus-libpinyin 后，在 ibus 中会出现名叫 "Intelligent Pinyin"
的新拼音引擎和 "Intelligent Bopomofo" 的新注音引擎。

欢迎大家使用 "Intelligent Pinyin" 和 "Intelligent Bopomofo"。 ^\_^

PS: 此更新已经进入 Fedora 18 updates-testing repo。

可以使用如下 yum 命令在 Fedora 18 上升级 ibus-libpinyin:

`$ su -c 'yum upgrade --enablerepo=updates-testing "ibus-libpinyin" "libpinyin*" "opencc*"'`
