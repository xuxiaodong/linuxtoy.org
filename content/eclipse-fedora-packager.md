Title: Eclipse Fedora Packager
Date: 2010-10-21 23:50
Author: lovenemesis
Category: Development
Tags: Eclipse, Fedora, packager
Slug: eclipse-fedora-packager

Eclipse Fedora Packager 是一款为 Fedora 打包者特别设计的 Eclipse
插件，满足全方位的 Fedora 打包需要。

Eclipse Fedora Packager 目前实现如下功能：

-   方便的 Git 克隆和分支切换。
-   包含语法高亮、自动补全、更新日志完善的 **RPM Spec 文件编辑器**。
-   **下载代码包**以及上传新代码包。
-   **准备本地编译**（执行 %prep 部分）。
-   按照当前 Spec **生成 SRPM 包**。
-   执行本地编译。
-   推送至 **Fedora Koji** 编译系统。
-   创建 **Mock** 编译环境。
-   推送至 **Fedora Bodhi** 更新系统。
-   Eclipse **Git 支持**。

Eclipse Fedora Packager 的目标设计人群是：

-   相对于命令行，更加**偏好 GUI 工具**；
-   **已经熟悉 Eclipse** 或者其他 IDE 环境；
-   几乎天天使用 Eclipse；
-   从来没有为 Fedora 打包过，但是**准备尝试**；
-   并不清楚软件是怎样进入 Fedora 的但是**需要为软件打包**；
-   主要**目标是为软件打包**并进入 Fedora 而不是花费精力学习大量工具。

在 Fedora 14 系统上安装 Eclipse Fedora Packager 只需要运行：

`pkcon install eclipse-fedorapackager`

早先的发布（比如 F13）步骤要稍复杂些：

1.  安装依赖关系：`pkcon install eclipse eclipse-changelog eclipse-rpm-editor fedora-release-rawhide fedora-packager`
2.  从 rawhide
    中安装：`su -c 'yum install --enablerepo=rawhide eclipse-fedorapackger'`

目前最新版本是 rawhide 中的 [0.1.8
版本](https://koji.fedoraproject.org/koji/buildinfo?buildID=201275)。

[发布公告及更早的版本安装方法（邮件列表）](http://lists.fedoraproject.org/pipermail/devel/2010-October/144570.html)

[详细用户指南](https://fedoraproject.org/wiki/Eclipse_Fedora_Packager_User_Guide)

**[详细用户指南中文版](https://fedoraproject.org/wiki/Eclipse_Fedora_Packager_User_Guide/zh)**
