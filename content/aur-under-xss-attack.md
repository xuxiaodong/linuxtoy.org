Title: AUR 遭受 XSS 攻击
Date: 2012-02-19 12:05
Author: cheer_xiao
Category: News
Tags: Archlinux
Slug: aur-under-xss-attack

有用户通过向包名字段注入 JavaScript 脚本的方式对 Archlinux 的社区包仓库
AUR (Archlinux User Repository, [主页](https://aur.archlinux.org)和
[Archlinux wiki
相关页面](https://wiki.archlinux.org/index.php/Arch_User_Repository))
进行了 XSS([cross-site
scripting](http://en.wikipedia.org/wiki/Cross-site_scripting)，跨站脚本)
攻击。 **Update**: 北京时间 2012-2-19 下午 3:08，AUR 已经恢复正常。

攻击者注入的 JavaScript 脚本将相关包的页面重定向到
[ubuntu.com](http://www.ubuntu.com)。因为 AUR
主页会展示最近提交和改动的包，而且未对相关字段做过滤处理，因此 AUR
主页也受到了影响。

目前整个 AUR 已经下线检修，在 Archlinux 的 bug tracker
里面也已经有相关[条目](https://bugs.archlinux.org/task/28515)追踪此问题。

PS. 就目前的情况来看，在下认为此事可能和 Ubuntu
并无瓜葛，只是提醒网站维护者 AUR 存在 XSS
漏洞，应及早修复，以免造成更严重后果。攻击者是否利用 XSS
漏洞作了其它恶意破坏，还得等开发人员检查完毕方能定论。
