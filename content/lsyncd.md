Title: Lsyncd: 实时同步
Date: 2014-06-10 16:49
Author: toy
Category: Apps
Slug: lsyncd

[Lsyncd][l] 通过 inotify 或 fsevents 来监视本机目录树，并将其实时  
同步 (mirror) 到远端的目标机器上。

Lsyncd 默认使用 rsync，采用 Lua 开发而成，比较轻量级，效果  
不错。

**安装 Lsyncd**

在 Debian 上，可通过以下指令安装 Lsyncd：

(root) # apt-get install lsyncd

**Lsyncd 用法**

要看看 Lsyncd 实时同步的效果，不妨执行：

$ lsyncd -nodaemon -rsync ~/tmp vu2:tmp

该命令将本机的 `~/tmp` 目录同步到远端机器 vu2 的 tmp 目录。

使用 Lsyncd 的更好方式是定义配置文件，具体可以参考[官方手册][m]。

[l]: https://github.com/axkibe/lsyncd  
[m]:
https://github.com/axkibe/lsyncd/wiki/Lsyncd%202.1.x%20%E2%80%96%20The%20Configuration%20File
