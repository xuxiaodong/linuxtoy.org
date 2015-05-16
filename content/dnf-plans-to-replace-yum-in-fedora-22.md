Title: DNF 预期于 Fedora 22 取代 Yum
Date: 2014-06-13 12:31
Author: lovenemesis
Category: Tools
Tags: dnf, Fedora, yum
Slug: dnf-plans-to-replace-yum-in-fedora-22

尽管 Fedora 21 还要到 10 月份才能发布，关于 Fedora 22
的功能提议已经开始，其中一个亮点既是用 DNF 替代 Yum 成为默认包管理工具。

DNF 从 Yum 分支出来，使用专注于性能的 C 语言库
[hawkey](https://github.com/akozumpl/hawkey)
进行依赖关系解析工作，大幅度提升包管理操作效率并降低内存消耗。此外 DNF
还支持 Python 3。

要替换 Yum 成为默认包管理工具，还需要实现的有：

-   修改 Anaconda 安装器使其默认使用 DNF。
-   重新实现当下 yum-utils 里的工具。
-   提供 yum 到 dnf 的命令重定向方便用户迁移。
-   该变化对于使用图形化安装工具的用户来说是透明，现阶段 PackageKit
    已经支持 dnf 可以随时切换(?)。

[DNF 文档首页](http://akozumpl.github.io/dnf/)

[替换项目 Wiki
页](https://fedoraproject.org/wiki/Changes/ReplaceYumWithDNF)

**PS:** 凑巧的是，本人昨日刚刚完成了 [DNF
的简体中文本地化](https://www.transifex.com/projects/p/dnf/language/zh_CN/)工作，欢迎进行审阅并提出意见！
