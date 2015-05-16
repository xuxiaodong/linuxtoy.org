Title: LibPinYin 0.3
Date: 2011-12-22 00:00
Author: lovenemesis
Category: Input Method
Tags: libpinyin
Slug: libpinyin-03

经过一年多的开发，[开源拼音输入法的整合
LibPinYin](http://linuxtoy.org/archives/libpinyin-%E5%BC%80%E6%BA%90%E6%8B%BC%E9%9F%B3%E8%BE%93%E5%85%A5%E6%B3%95%E7%A4%BE%E5%8C%BA%E5%A4%A7%E8%9E%8D%E5%90%88.html)
发布了 0.3 版本，进入公开测试阶段。

目前 ibus-pinyin 已经可以使用新的 LibPinYin 后端，提供了如下新功能：

-   智能整句引擎；
-   i 模式: 支持lua script 扩展；
-   v 模式: 快速键入英文。

Fedora 16 上安装方法：

`su -c 'yum --enablerepo=updates-testing upgrade ibus-pinyin'`

然后在 ibus 中会出现名叫 "Intelligent Pinyin(Beta)" 的新拼音引擎。

[LibPinYin 0.3
源代码包下载](https://github.com/downloads/libpinyin/libpinyin/libpinyin-0.3.0.tar.gz)

[项目 Github 首页](https://github.com/libpinyin/libpinyin)

*消息来源：*[Fedora
中文邮件列表](http://lists.fedoraproject.org/pipermail/chinese/2011-December/008777.html)
