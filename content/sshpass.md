Title: sshpass: 用于非交互的 ssh 密码验证
Date: 2009-01-13 10:16
Author: toy
Category: Apps
Tags: SSH, sshpass
Slug: sshpass

[撰文/Zhang Huangbin (michaelbibby AT gmail.com)]

OpenSSH 自带的 ssh 客户端程序（也就是 'ssh'
命令）默认不允许你以非交互的方式传递密码，如：

`ssh www.iredmail.org <<EOF ssh_password ls /var/ EOF`

Shell 里这样的输入重定向使用得非常普遍，而且通常都工作得很好。但是 ssh
不允许这样的方式来传递密码，所以需要远程连上服务器后进行的批处理就无法进行。

sshpass 的出现，解决了这一问题。它允许你用 -p
参数指定明文密码，然后直接登录远程服务器。例如：

`# sshpass -p 'ssh_password' ssh www.iredmail.org`

用 '-p' 指定了密码后，还需要在后面跟上标准的 ssh 连接命令。

用法就是这么简单。

**注意：**

我之前使用的 sshpass 是
1.0，在第一次连接服务器的时候，无法自动接受服务器的 Key
验证，也不会出现提示信息，所以第一次连接服务器请使用标准的 ssh
命令行客户端工具，接受了服务器的 key 之后再用 sshpass。

[sshpass](http://sourceforge.net/projects/sshpass/)
