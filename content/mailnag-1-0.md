Title: Mailnag 1.0
Date: 2014-07-15 17:29
Author: lovenemesis
Category: Desktop Stuff
Tags: mailnag
Slug: mailnag-1-0

Mailnag 是一款和桌面环境深度整合的邮件提示程序，最近发布了 1.0
正式版本。

Mailnag 通过 POP3 或者 IMAP
协议访问邮箱监视新邮件到达，点击到达邮件后将可以使用独立邮件客户端或者
`gnome-gmail` 在浏览器中打开。

本次正式版本变化有：

-   在 GNOME 3 的基础上增加了更多桌面环境支持，包括 Unity、Cinnamon 和
    Pantheon。
-   重构了插件架构，提供了与桌面环境的无关的消息提示、音效、过滤等插件，方便自定义邮件提示。
-   分别为 GNOME 3 和 Unity
    的设置了提示插件，深度整合入环境消息提示系统。
-   新的 DBus 插件允许其他程序和 Mailnag 进行交互。

注意该版本的配置文件不兼容早先版本，强烈建议升级前备份现有配置文件。

Mailnag 已经被各大发行版软件仓库收录，使用各自的包管理工具安装即可。

[项目 Github 首页](https://github.com/pulb/mailnag)
