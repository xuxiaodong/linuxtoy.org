Title: Cockpit：基于 Web 的图形化服务管理工具
Date: 2014-02-13 11:26
Author: lovenemesis
Category: Productivity, Server
Tags: cockpit
Slug: cockpit-web-based-gui-service-managment-tool

Cockpit
是红帽开发的网页版图像化服务管理工具，优点是无需中间层，且可以管理多种服务。

根据其项目主站描述，Cockpit 有如下特点：

-   从[易用性考虑设计](http://blogs.gnome.org/uraeus/2014/02/10/excited-about-cockpit/)，方便管理人员使用，而不是仅仅的终端命令按钮化。
-   不会打乱已有终端或脚本服务配置，通过 Cockpit
    启用的服务可以在终端停止，脚本运行的错误亦会被 Cockpit 捕获。
-   支持一次性管理多个服务，实现自动化和批处理。

**[一张图说明 Cockpit
工作方式](https://raw.github.com/cockpit-project/cockpit/master/doc/cockpit-transport.png)**

注意目前 Cockpit 还处于早期开发阶段，**不建议在生产环境使用**！

[官方项目站点](http://cockpit-project.org/)
