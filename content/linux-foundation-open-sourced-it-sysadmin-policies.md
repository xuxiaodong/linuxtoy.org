Title: Linux 基金会 IT 系统管理策略文档
Author: lovenemesis
Date: 2015-09-09
Category: Books
Tags: sysadmin
Slug: linux-foundation-open-sourced-it-sysadmin-policies
Summary: Linux 基金会近日将其 IT 部门的系统管理策略文档开源出来，其中有不少十分有益的要点值得系统管理员们借鉴。

秉承开源合作共享的理念，Linux 基金会将多年来 IT 部门系统管理策略的文档开放出来。目前有两篇，分别是[《Linux 工作站安全检查清单》](https://github.com/lfit/itpol/blob/master/linux-workstation-security.md)和[《构建安全团队通信清单》](https://github.com/lfit/itpol/blob/master/trusted-team-communication.md)。

第一份文档比较长，一些有趣的要点有：

* UEFI 及其 Secure Boot 对于 Linux 系统安全是有益的
* Thunderblot、Firewire、ExpressCard 是安全隐患
* 建议选择支持 SELinux/AppArmor/GrSecurity 等 MAC/RBAC 的发行版
* 全盘加密是必须，包括交换分区
* 备份也要加密，云端备份选择无特征（Zero Knowledge）的
* 对于工作和一般网页浏览分开使用两个浏览器
* 不要待机，每天关机或睡眠

[Useful IT Policies](https://github.com/lfit/itpol)

[Linux 基金会原文](http://www.linux.com/news/featured-blogs/167-amanda-mcpherson/850607-linux-foundation-sysadmins-open-source-their-it-policies)