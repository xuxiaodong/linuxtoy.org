Title: 超酷的 Zsh prompt
Date: 2009-05-04 19:26
Author: vern
Category: Tips
Tags: Zsh
Slug: zsh-prompt

{撰文/[Vern](http://s5unty.blogspot.com/)}

不仅美观而且实用的 Zsh
提示符，除了常见的主机名、用户名、路径名等标识符，它还能

* jobs 提醒  
* 非 0 的 exit code 提示  
* 路径名右对齐

相关配置内容如下：

[bash]  
# get the colors  
autoload colors zsh/terminfo  
if [[ "$terminfo[colors]" -ge 8 ]]; then  
colors  
fi  
for color in RED GREEN YELLOW BLUE MAGENTA CYAN WHITE GREY; do  
eval C\_$color='%{$terminfo[bold]$fg[${(L)color}]%}'  
eval C\_L\_$color='%{$fg[${(L)color}]%}'  
done  
C\_OFF="%{$terminfo[sgr0]%}"

# set the prompt  
set\_prompt() {  
mypath="$C\_OFF$C\_L\_GREEN%~"  
myjobs=()  
for a (${(k)jobstates}) {  
j=$jobstates[$a];i="${${(@s,:,)j}[2]}"  
myjobs+=($a${i//[^+-]/})  
}  
myjobs=${(j:,:)myjobs}  
((MAXMID=$COLUMNS / 2)) # truncate to this value  
RPS1="$RPSL$C\_L\_GREEN%$MAXMID<...<$mypath$RPSR"  
rehash  
}  
RPSL=$'$C\_OFF'  
RPSR=$'$C\_OFF$C\_L\_RED%(0?.$C\_L\_GREEN. (%?%))$C\_OFF'  
RPS2='%^'

# load prompt functions  
setopt promptsubst  
unsetopt transient\_rprompt # leave the pwd

precmd() {  
set\_prompt  
print -Pn "\\e]0;%n@$\_\_IP:%l\\a"  
}  
PS1=$'$C\_L\_BLUE%(1j.[$myjobs]% $C\_OFF
.$C\_OFF)%m.%B%n%b$C\_OFF$C\_L\_RED%#$C\_OFF'  
[/bash]

注意：上面 22 行中的 `< ` 被自动转义成了 `<`，请自行替换。

{ via
[Miek.nl](http://www.miek.nl/blog/archives/2008/02/20/my\_zsh\_prompt\_setup/index.html)
}
