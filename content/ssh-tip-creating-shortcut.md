Title: SSH 使用技巧一则: 创建快捷方式
Date: 2009-04-15 11:58
Author: toy
Category: Cli
Tags: SSH
Slug: ssh-tip-creating-shortcut

在管理服务器时，我通常选择使用 SSH 方式。以下是一则 SSH
使用技巧，希望对你有用。

**创建快捷方式**

当你在执行 ssh
命令登录服务器时，有没有被需要输入命令后面的一长串参数感到厌烦呢？比如，名为
serveradmin@domain.com 的用户要登录到 example.com 主机上，需执行：

ssh serveradmin@domain.com@example.com

你当然可以使用 alias，但 SSH
本身也提供有相应的解决方案──你可以为需要经常访问的远程主机创建快捷方式。

1. 找找看你的用户主目录下是否有 .ssh，若没有，则使用 mkdir 创建一个；

2. 使用你喜欢的文本编辑器（如 Vim）来创建 config 配置文件：

vim ~/.ssh/config

3. 仍以前面的例子来说明，假设我要创建的快捷方式名为
lt，则加入下面的内容，其中 HostName 为主机名，User 为用户名：

Host lt

HostName example.com  
User serveradmin@domain.com

4. 保存编辑。

现在，你只要执行 `ssh lt` 就可以了。
