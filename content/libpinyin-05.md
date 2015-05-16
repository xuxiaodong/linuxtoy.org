Title: LibPinYin 0.5
Date: 2012-02-06 14:27
Author: lovenemesis
Category: Input Method
Tags: libpinyin
Slug: libpinyin-05

[开源拼音输入法大融合](http://linuxtoy.org/archives/libpinyin-%E5%BC%80%E6%BA%90%E6%8B%BC%E9%9F%B3%E8%BE%93%E5%85%A5%E6%B3%95%E7%A4%BE%E5%8C%BA%E5%A4%A7%E8%9E%8D%E5%90%88.html)
LibPinYin 0.5 发布，带来全新的注音解析引擎。*感谢 Peng Wu 来稿*

以下内容[转载自 Fedora
中文邮件列表](http://lists.fedoraproject.org/pipermail/chinese/2012-February/009068.html)

适用于 ibus-pinyin 的 libpinyin 后端有如下的新功能:

-   全新的全拼/双拼/注音解析器;
-   增强的模糊拼音支持，比如:启用了 an/ang 的模糊音，会自动启用 uan/uang
    的模糊音;;
-   改进了自学习部分;

请用以下命令在 Fedora 16 上安装:

`su -c 'yum --enablerepo=updates-testing upgrade "ibus-pinyin*"'`

然后在 ibus 中会出现名叫 `"Intelligent Pinyin(Beta)"` 的新拼音引擎和
`"Intelligent Bopomofo(Beta)"` 的**新注音引擎**。

如果有问题，欢迎报 bug 到
[Bugzilla](https://bugzilla.redhat.com)，组件请选择 `ibus-pinyin` 或
`libpinyin`。

祝大家使用愉快。
