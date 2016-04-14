Title: Vim 8.0 即将来临
Date: 2016-04-14 09:55:16
Authors: toy
Category: News
Tags: vim
Slug: vim-8

日前，有网友在 [Hacker News][h] 上爆出了 Vim 8.0 的文档文件。看起来这是既 Vim 7.4 之后的又一个重大更新版本，其中新增了好些不错的功能，同时也修正了许多缺陷。该版本非常令人期待。

<!-- PELICAN_END_SUMMARY -->

个人认为，以下几点为 Vim 8.0 的亮点：

* 异步 I/O 支持及 channels

    这项特性允许 Vim 在后台与其它进程交换信息。

* 内置 JSON 支持

    如今 JSON 使用得越来越广泛，为此 Vim 8.0 添加了 `json_encode()` 和 `json_decode()`。

* Packages（插件包管理)

    Vim 有一个令人诟病的地方，其插件管理不甚方便。故此 Vim 社区出现了一些第三方插件管理工具。Vim 8.0 自带插件包管理功能，相信会使插件的使用更加方便。

* GTK+ 3 支持

    GTK+ 2 逐渐步入老旧之列，所以 Vim 8.0 带来了 GTK+ 3 支持。

* Jobs、Timers、Partials、Window ID 等

    Vim 8.0 不仅为用户，而且也为开发者添加了一些不错的特性。

&rarr; [Vim 8.0](https://github.com/vim/vim/blob/master/runtime/doc/version8.txt)

[h]: https://news.ycombinator.com/item?id=11486786
