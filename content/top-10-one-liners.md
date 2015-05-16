Title: 10 个最酷的 Linux 单行命令
Date: 2010-03-19 21:13
Author: toy
Category: Cli
Tags: Commandline
Slug: top-10-one-liners

下面是来自 [Commandlinefu](http://commandlinefu.com)
网站由用户投票决出的 10  
个最酷的 Linux 单行命令，希望对你有用。

1. `sudo !!`

以 root 帐户执行上一条命令。

2. `python -m SimpleHTTPServer`

利用 Python 搭建一个简单的 Web 服务器，可通过 http://$HOSTNAME:8000
访问。

3. `:w !sudo tee %`

在 Vim 中无需权限保存编辑的文件。

4. `cd -`

更改到上一次访问的目录。

5. `^foo^bar`

将上一条命令中的 foo 替换为 bar，并执行。

6. `cp filename{,.bak}`

快速备份或复制文件。

7. `mtr google.com`

traceroute + ping。

8. `!whatever:p`

搜索命令历史，但不执行。

9. `$ssh-copy-id user@host`

将 ssh keys 复制到 user@host 以启用无密码 SSH 登录。

10. `ffmpeg -f x11grab -s wxga -r 25 -i :0.0 -sameq /tmp/out.mpg`

把 Linux 桌面录制为视频。

关于  

[Commandlinefu](http://linuxtoy.org/archives/command-line-fu.html)，本站去年曾作介绍，不熟悉的朋友可点击查看。
