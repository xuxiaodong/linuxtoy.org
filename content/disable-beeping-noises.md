Title: 禁用 beep
Date: 2011-07-24 13:50
Author: shuge.lee
Category: Tips
Tags: Bash, beep, Shell
Slug: disable-beeping-noises

禁用各种环境下的 beep 。

### 禁用 bash shell 环境下的 beep

编辑 /etc/.inputrc, 添加一下设置，保存。

set bell-style none

### 禁用 VIM 的 beep

编辑 ~/.vimrc ，添加一下设置，保存。

set noerrorbells  
set visualbells  
set t\_vb=

### 禁用 MinGW/msysgit 环境下的 beep

临时禁用

net stop beep

永久禁用

sc config beep start= disabled

### 参考链接

[disable beeping noises on WinXP/Linux/VI  

](http://my.opera.com/allbits/blog/2007/04/25/disable-beeping-noises-on-winxp-workstations-windows)

（完）
