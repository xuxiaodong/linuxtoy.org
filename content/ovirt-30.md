Title: oVirt 3.0
Date: 2012-02-11 13:15
Author: lovenemesis
Category: Productivity
Tags: Fedora, oVirt
Slug: ovirt-30

oVirt 项目发布首个正式版本 3.0。

本次发布包括三个组件，SDK，引擎和节点。

[Engine
3.0](http://ovirt.org/releases/stable/src/ovirt-engine-3.0.0_0001.tar.gz)：提供功能丰富的虚拟化管理系统，提供以
Jboss AS7 为基础的应用服务器，支持进程优先级管理。

[SDK
1.3](http://ovirt.org/releases/stable/src/ovirt-engine-sdk-1.3.tar.gz)：利用
Python 针对引擎暴露的 API 进行应用程序开发，REST 风格。

[Node
2.2.2](http://ovirt.org/releases/stable/src/ovirt-node-2.2.2.tar.gz)：提供最小化的
Linux 镜像，作为虚拟化的主机，并提供了 oVirt 引擎链接的功能，使用了部分
Fedora 16 中的组件

[oVirt](http://www.ovirt.org/) 由 Canonical, Cisco, IBM, Intel, NetApp,
Red Hat, SUSE 合作开发，该项目于 2008 年由 Red Hat
发起，皆在建立一套开放的虚拟化解决方案。

在 Fedora 16 下安装 oVirt 引擎：

`sudo wget http://www.ovirt.org/releases/stable/fedora/16/ovirt-engine.repo -P /etc/yum.repos.d`

`sudo yum install -y ovirt-engine`

之后的内容请参照[安装配置手册](http://www.ovirt.org/w/images/a/a9/OVirt-3.0-Installation_Guide-en-US.pdf)

如果**对 oVirt 相关技术感兴趣**的话，欢迎参加[今年 3 月 21 日在北京 IBM
Campus 举行的 oVirt
工作坊活动](http://www.ovirt.org/news-and-events/workshop/)。

[英文邮件列表发布公告](http://lists.ovirt.org/pipermail/announce/2012-February/000019.html)
