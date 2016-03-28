Title: Termux 0.32：终端模拟器及 Linux 环境
Author: lovenemesis
Date: 2016-03-28
Category: Embedded
Tags: android, termux
Slug: termux-032
Summary: 若想在非 Root Android 手机上体验 Linux 的话，除了本站先前介绍过的 [GNURoot](https://linuxtoy.org/archives/install-debian-and-r-on-android.html) 方式以外，还可以尝试一个更轻量级但更适合移动需求的方案：Termux。

Termux 的特点有：

* 相比 GNURoot 的 200M+ 大小，它的安装包小巧很多，安装后的精简系统只有 10M 左右
* 提供与 Debian 类似 apt/dpkg 的软件包管理方式
* 自 0.32 开始提供对于 ARMv8 aarch64 架构的原生支持，提供 64 位软件仓库
* 提供**新版本**的 `git`, `zsh`, `vim`, `python`, `ruby`, `openjdk`, `gcc`, `clang`, `openssh` 等众多生产力工具
* 支持多个会话同时运行
* 贴心的快捷键设计，适配虚拟及实体键盘
* 支持 Android 5.0 引入的权限管理体系，支持写入外置 SD 卡
* 灵活的扩展组件：自定义风格，悬浮式终端，甚至可以访问手机联系人的系统API接口 

说了这么多优点，那么相比 GNURoot 及其后续的 GNUDebian 有何不足呢？

* 并非单纯 Debian 的移植，于是在软件包方面并不二进制兼容
* 不具备 X 服务，无法运行 Linux 图形应用
* 社区类似一个小众的发行版，跟 Debian ARM 的社区不能比
* 软件仓库数量远不如 Debian，缺乏小众应用
* 仅支持 Android 5.0+

Termux 以 [GPLv3 协议](https://termux.com/source-code.html)发布，可从 [Play Store](https://play.google.com/store/apps/details?id=com.termux) 或者 [F-Droid.org](https://f-droid.org/repository/browse/?fdid=com.termux) 下载。

**友情提示**：使用前一定要[阅读帮助文档](https://termux.com/help.html)哦！
