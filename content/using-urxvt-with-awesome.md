Title: Using Urxvt with Awesome
Date: 2009-05-24 18:46
Author: vern
Category: Tips
Tags: Awesome, Urxvt
Slug: using-urxvt-with-awesome

{撰文/vern}

**准备工作**

你可以在 ~/.Xdefaults 或者 ~/.Xresources 或者其它地方配置
urxvt，确认以下配置项被定义。

URxvt.urgentOnBell: True

添加完以上配置项后，执行命令

xrdb ~/.Xdefaults

或者

xrdb ~/.Xresources

如果你不喜欢听 beep 声，你可以在 ~/.xinitrc 或者 ~/.Xsession
中关闭它，确认以下命令被执行。

/usr/bin/xset b off

**Mutt 新邮件提醒**

你可以在 ~/.muttrc 或者 ~/.mutt/muttrc 中配置 mutt，确认 beep\\\_new
被定义；check\\\_new 和 timeout 默认已定义，确认它们未被取消定义。

set beep\_new=yes  
set check\_new=yes  
set timeout=600

在某 tag 标签(假设为 tag4)里打开 urxvt 并运行 mutt，切换至其它 tag
标签做些你感兴趣的事。在你离开 tag4 超过 10 分钟后，一旦有新邮件，标签
tag4 会高亮显示。

**Weechat 私人/高亮消息提醒**

在 Weechat 官方网站 下载 beep 插件，保存至 ~/.weechat/perl/ 目录。

cd ~/.weechat/perl  
wget http://weechat.flashtux.org/scripts/beep.pl  
cd autoload  
ln -sf ../beep.pl .

在某 tag 标签(假设为 tag2)里打开 urxvt 并运行 weechat-curses，切换至其它
tag 标签做些你感兴趣的事。当你在 irc 频道中收到 private 或者 highlight
消息时，标签 tag2 会高亮显示。

**Shell Job 完成时提醒**

据我所知的两种 Shell(bash/zsh) 都支持在显示提示符 PS1
之前执行命令的功能，我们要做的就是在那个时刻简单的执行一条命令:

echo -ne '\\a'

* bash 通过环境变量 PROMPT\_COMMAND

export PROMPT\_COMMAND="echo -ne '\\a'"

* zsh 通过函数 precmd()

precmd() {  
# your commands  
# ...  
echo -ne '\\a'  
}

在某 tag 标签(假设为 tag1)里打开 urxvt 并运行一个比较耗时的命令(例如一次
configure 或者 make)，切换至其它 tag
标签做些你感兴趣的事。当你刚才那条命令执行完成时，标签 tag1 会高亮显示。

**最后**

默认快捷键 Mod+u 可以把当前焦点跳转至最后一次发生高亮事件的窗口。

**参考**

[Irssi tips](http://awesome.naquadah.org/wiki/index.php/Irssi\\\_tips)
