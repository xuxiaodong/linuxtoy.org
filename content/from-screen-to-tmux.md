Title: 从 screen 切换到 tmux
Date: 2011-04-15 21:26
Author: toy
Category: Tips
Tags: tmux
Slug: from-screen-to-tmux

在我的 Linux 生活中，我曾做过几次重要的切换。我先是从 Archlinux 切换到  
Gentoo，后来又从 bash 切换到了 zsh。现在，我又从 screen 切换到  
tmux。对于各个终端控来说，screen  
是几乎每天都会使用的好工具，抛开确实不易。但有了更加好用的  
tmux，我为什么不切换？

[![Tmux
thumb](http://linuxtoy.org/img/2011/04/tmux-thumb.png)](http://linuxtoy.org/img/2011/04/tmux.png)

### 我为什么要从 screen 切换到 tmux

对我来说，从 screen 切换到 tmux
不是平白无故的，自然有其充分的理由。我感觉使用  
tmux 更加方便、灵活和高效。我非常喜欢 tmux 的这些方面：

+ 垂直分割窗口，当然水平也是可以的  
+ vi 或 emacs 按键绑定模式  
+ 有多个粘贴缓冲，可完全由按键进行选取、复制、以及粘贴操作  
+ 配置很容易，尤其是状态行  
+ 脚本化，通过脚本可以方便的控制 tmux 会话  
+ 有预设布局，可搜索窗口，自动命名窗口名称  
+ 文档清晰、详尽

### 更改默认按键前缀

从 screen 切换到 tmux 十分平滑，tmux 的按键设置与 screen  
大都相同，只是其默认按键前缀为 Ctrl-b。为了延续在 screen  
中的使用习惯，我将其更改为 Ctrl-a。将下列内容加到 $HOME/.tmux.conf
中即可：

set -g prefix ^a  
unbind ^b  
bind a send-prefix

### 按键绑定

我还在 .tmux.conf 中定义了以下按键绑定：

+ 水平或垂直分割窗口

unbind '"'  
bind - splitw -v # 分割成上下两个窗口  
unbind %  
bind | splitw -h # 分割成左右两个窗口

+ 选择分割的窗格

bind k selectp -U # 选择上窗格  
bind j selectp -D # 选择下窗格  
bind h selectp -L # 选择左窗格  
bind l selectp -R # 选择右窗格

+ 重新调整窗格的大小

bind ^k resizep -U 10 # 跟选择窗格的设置相同，只是多加 Ctrl（Ctrl-k）  
bind ^j resizep -D 10 # 同上  
bind ^h resizep -L 10 # ...  
bind ^l resizep -R 10 # ...

+ 交换两个窗格

bind ^u swapp -U # 与上窗格交换 Ctrl-u  
bind ^d swapp -D # 与下窗格交换 Ctrl-d

+ 执行命令，比如看 Manpage、查 Perl 函数

bind m command-prompt "splitw -h 'exec man %%'"  
bind @ command-prompt "splitw -h 'exec perldoc -f %%'"

### 定制状态行

状态行左边默认就很好了，我对右边定制了一下，显示 uptime 和 loadavg：

set -g status-right "#[fg=green]#(uptime.pl)#[default] •
#[fg=green]#(cut -d ' ' -f 1-3 /proc/loadavg)#[default]"

下面两行设置状态行的背景和前景色:

set -g status-bg black  
set -g status-fg yellow

### 默认启动应用

当 tmux 启动时，可以默认启动一些应用：

new -s work mutt # 新建名为 work 的会话，并启动 mutt  
neww rtorrent # 启动 rtorrent  
neww vim # 启动 vim  
neww zsh  
selectw -t 3 # 默认选择标号为 3 的窗口

### 复制与粘贴操作

1. 按 C-a [ 进入复制模式，如果有设置 `setw -g mode-keys vi` 的话，可按
vi  
的按键模式操作。移动至待复制的文本处，按一下空格，结合 vi  
移动命令开始选择，选好后按回车确认。

2. 按 C-a ] 粘贴已复制的内容。

### 参考

tmux 的官方主页:  
我的 [.tmux.conf][t]

[t]: https://bitbucket.org/xuxiaodong/dotman/src
