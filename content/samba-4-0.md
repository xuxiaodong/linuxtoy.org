Title: Samba 4.0 添加兼容的 Active Directory 支持
Date: 2012-12-12 11:36
Author: toy
Category: News
Tags: Samba
Slug: samba-4-0

Samba 开发团队已发布 [Samba 4.0][s] 版本。Samba 4.0 是该项目诞生 21
年（与 Linux 内核同岁）后推出的一个具有重要里程碑意义的版本。Samba 针对
M$ Windows
系统提供文件、打印、以及认证服务。本次发布的版本引入的最主要特性是实现了兼容的
M$ Active Directory（活动目录）协议。

在 Active Directory 支持方面，Samba 4.0 包含 LDAP 目录服务器、Heimdal
Kerberos 认证服务器、安全的动态 DNS
服务器、以及实现了所有必要的远程过程调用。目前，Samba 4.0 的 Active
Directory 域控制器支持 M$ Windows 客户端的所有版本，包括 Windows
8；它提供诸如组策略、Roaming Profiles、Windows 管理工具、与 M$ Exchange
和 OpenChange 集成等特性支持，并允许互相加入到各自的 Active Directory
域。

此外，Samba 4.0 还引入了 SMB 2.1 文件服务支持、初步实现了 SMB
3、整合了集群
SMB2/SMB/CIFS文件服务、更易集成到现有的目录服务、改进了稳定性/安全性/性能、模块化的
Virtual File System（VFS）允许 OEM 厂商定制 Samba 等功能。

Samba 4.0 的源代码可至其官方主页[下载][d]。

[s]: https://www.samba.org/samba/news/releases/4.0.0.html  
[d]: https://www.samba.org/

{ via [LWN](https://lwn.net/Articles/528797/) }
