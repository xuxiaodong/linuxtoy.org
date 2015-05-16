Title: lynis 1.3.0
Date: 2013-04-15 11:21
Author: lovenemesis
Category: Security
Tags: lynis
Slug: lynis-1-3-0

[lynis](http://www.rootkit.nl/projects/lynis.html) 是一款用于检测 Linux
系统健壮性的脚本，方便管理员找出系统中的易受攻击的安全隐患。

[lynis](http://www.rootkit.nl/projects/lynis.html)
会检测系统中的安全框架、数据库、各类常见服务、文件系统、防火墙、日志、打印系统等各个部分的配置安全情况，内容比较全面。

[官方下载](http://www.rootkit.nl/projects/lynis.html)

**注意：**由于需要执行对 `/var/log` 和 `/tmp`
的写入操作，需要以**管理员权限**运行：

`sudo ./lynis -cQ `

之后即可在屏幕上看到详尽的检测结果，最终报告也会被写入
`/var/log/lynis.log` 中。

**Fedora 下安装（尚未更新至 1.3.0 版本）**：

`pkcon install lynis`

[消息原文](http://xmodulo.com/2013/04/how-to-scan-linux-for-vulnerabilities.html)

[消息来源](https://plus.google.com/116280387570477878143/posts/6e7thHnoRor)
