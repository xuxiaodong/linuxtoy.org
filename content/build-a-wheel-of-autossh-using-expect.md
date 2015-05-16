Title: Build a wheel of autossh using expect
Date: 2010-09-15 08:29
Author: toy
Category: Tips
Tags: SSH
Slug: build-a-wheel-of-autossh-using-expect

{ 撰文/[ivan\_wl](http://ivsays.appspot.com) }

首先，感谢国家。我能写出这么一篇技术文，全靠国家所赐。

题目的意思是，用expect给autossh再造一个轮子。为什么又要造轮子呢？我们先从autossh说起。

autossh是个很方便的管理ssh连接的工具。但是出于安全性的考虑，ssh连接一段时间后没有活动，就会自动断开。对于我们这些把ssh主要用做穿墙代理工具的同学，无疑是很不方便的。所以很多人都使用autossh这个工具。autossh会运行一个ssh子进程，并每隔一段时间检测ssh连接的状态，当ssh进程意外退出或连接断开时，autossh会重启ssh进程。如果你的ssh服务器使用的是密钥认证的方式，autossh可以很完美的工作。但问题来了，如果你不得不使用密码认证的方式呢？当你用autossh登陆ssh服务器，输入密码，连接建立了，可以穿墙了！过了一会儿，ssh连接超时，自动断开。autossh也意识到了这一点，于是它重启了一个ssh进程，连接上服务器，接下来 -
输入密码…
autossh可是不会帮你再输入密码的。所以，在密码认证的情况下，autossh基本算是废了。这也就是我们要再造一个autossh的轮子的原因，而且要比它更圆，能自动输入密码。

我的方案是使用expect这个工具。expect可以读取程序的输出，分析输出的内容，与期望的输出进行对比，并模拟输入。如果你玩什么基于文本的MUD游戏，就可以用它来来自动完成枯燥的练级过程。我们首先很自然的就想到，用expect脚本来给autossh输入密码。在我们的这个情景中，我们希望autossh作为expect脚本的子进程，当脚本结束时，autossh也跟着结束。否则再次运行expect脚本，由于autossh还在后台，就会出现错误，除非你手动结束它。但是经过实践，发现autossh有一个问题，当autossh的父进程被结束时，其自身并不会跟着结束，而是变成孤儿进程，被init收养（Mac
OS下是launchd）。这在应用中就比较麻烦了。所以我们跳过autossh，直接用expect来控制ssh，实现autossh的功能，也就是给autossh再造一个轮子。

实现的expect脚本如下，或直接[点击下载](http://ivsays.appspot.com/media/agZpdnNheXNyDAsSBU1lZGlhGMllDA/autossh.sh?a=download)：

#!/usr/bin/expect --  
#!/bin/sh  
#  
# autossh.sh  
# SimpleSSHProxy  
#  
# Created by ivan on 10-9-10.  
# http://twitter.com/ivan\_wl  
#  
# This is another wheel of autossh built using expect.  
# If you have to use ssh password authorizing,  
# use this instead of autossh.  
#  
# WARNING: This script is NOT SAFE for your password,  
# DON'T USE THIS IF YOU HAVE SECURITY CONCERNS!  
#  
# Usage: autossh.sh [foo] [foo] [bindingIP:port] [foo] [username]
[remoteHost] [password]

# get arguments  
set IPandPort [lrange $argv 2 2]  
set username [lrange $argv 4 4]  
set remoteHost [lrange $argv 5 5]  
set password [lrange $argv 6 6]

while (1) {  
set connectedFlag 0;  
spawn /usr/bin/ssh -D $IPandPort $username@$remoteHost;  
match\_max 100000;  
set timeout 60;  
expect {  
"?sh: Error*"  
{ puts "CONNECTION\_ERROR"; exit; }  
"*yes/no*"  
{ send "yes\\r"; exp\_continue; }  
"*?assword:*" {  
send "$password\\r"; set timeout 4;  
expect "*?assword:*" { puts "WRONG\_PASSWORD"; exit; }  
set connectedFlag 1;  
}  
# if no password  
"*~*"  
{ send "echo hello\\r"; set connectedFlag 1; }  
}  
if { $connectedFlag == 0 } {  
close;  
puts "SSH server unavailable, retrying...";  
continue;  
}

while (1) {  
set conAliveFlag 0;  
interact {  
# time interval for checking connection  
timeout 60 {  
set timeout 10;  
send "echo hello\\r";  
expect "*hello*" { set conAliveFlag 1; }  
if { $conAliveFlag == 1 } {  
# connection is alive  
continue;  
} else { break; }  
}  
}  
}

close;  
puts "SSH connection failed, restarting...";  
}

将上面的代码保存为一个文本文件，如autossh.sh，chmod加上x属性，使用方法为：

autossh.sh [foo] [foo] [bindingIP:port] [foo] [username] [remoteHost]
[password]

其中的 foo
参数并无实际意义，可以用任何字符串代替，保留其的目的是使此脚本与autossh的参数调用方法兼容。

这个脚本可以自动输入ssh密码，并且实现autossh的主要功能，即ssh连接的断线检测和重连，但是无法实现ssh进程意外退出时重生ssh进程。当ssh进程意外退出（比如你手动杀掉）脚本进程也就退出了。不过这种情况实在比较难以遇到，所以也算是合格。如果实在需要ssh进程的重生，可以考虑这么一种思路：再用一层expect脚本来包裹这个脚本进程，在外层脚本中实现进程的重生功能，（这个用while循环和wait命令是非常容易实现的）这个问题就留给有心的读者自己研究吧。

{ Thanks ivan\_wl. }
