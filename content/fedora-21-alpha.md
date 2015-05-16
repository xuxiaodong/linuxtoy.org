Title: Fedora 21 Alpha
Date: 2014-09-24 09:27
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-21-alpha

经过多次延期之后，代表 Fedora.NEXT 系列改进的首个版本 Fedora 21 宣告了
Alpha
问世，将产品线分为**工作站、服务器及云计算**，分别作出特殊优化方便开箱即用。

###云计算###

* 模块化内核：云计算和内核小组协力将 Fedora 所用的 Linux
内核按照模块重新打包，拆分成适合云计算的最小化内核及其他通用用途的模块。

* 原子主机：首个实现 [Project Atomic](http://projectatomic.io/)
的产品，快速创建 Docker 容器，且支持更新回滚。

###服务器###

* 带来一系列新服务管理工具：

1.
[Rolekit](http://fedoramagazine.org/flock-2014-day-2-fedora-server-role-ing-along/)
：集约式服务部署工具，方便管理员在统一的界面下完成特定用途的服务的部署安装工作。

2.
[Cockpit](http://cockpit-project.org/)：可通过远程浏览器访问的服务配置及状态监控工具。

3. [OpenLMI](http://www.openlmi.org/)：基于
[DMTF-CIM](http://www.dmtf.org/standards/cim)
构建的远程管理系统，允许通过脚本管理多个远程服务器。

* 域控制器：随着
[Rolekit](http://fedoramagazine.org/flock-2014-day-2-fedora-server-role-ing-along/)
发布的首个特定服务角色既是域控制器，方便快速部署基于
[FreeIPA](http://freeipa.org/) 的 Linux/UNIX 身份验证及授权系统。

###工作站###

* 包含最新的即将发布 GNOME 3.14 预览版本

*
默认安装[开发助手工具](http://devassistant.org/)，方便快速配置应用开发环境。

[Fedora 21 Alpha 官方下载（包含 KDE、ARM
等各种定制版）](http://fedoraproject.org/zh\_CN/get-prerelease#overview)

[安装前请阅读常见 F21
Bug](https://fedoraproject.org/wiki/Common\_F21\_bugs)

*消息来源：*[Fedora
Magazine](http://fedoramagazine.org/fedora-21-alpha-released/)
