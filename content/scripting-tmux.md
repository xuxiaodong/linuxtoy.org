Title: 脚本化 tmux
Date: 2012-07-02 11:04
Author: toy
Category: Tips
Slug: scripting-tmux

昨天我在家试了下脚本化
[tmux][t]，其表现相当令人满意，只需稍加定制便可满足各种实际需要。这或许可以成为抛弃
GNU screen，改用 tmux 的又一个理由。

该脚本先判断一个名为 codefun 的 tmux
会话是否存在，如果不存在则创建它，否则就附加到此会话。接下来，在新建会话之后的动作包括：

* 创建窗口 1，并分为上下两个窗格，其中上窗格占 80% 空间，运行
Vim，下窗格占 20% 空间，运行 Pry  
* 创建窗口 2，运行 Mutt  
* 创建窗口 3，运行 Irssi  
* 创建窗口 4，运行 Cmus  
* 创建窗口 5，分左右两个窗格，各占 50% 空间，皆运行 Zsh

这些都是通过脚本自动完成的，我感觉用起来相当方便。其效果如下图所示：

[![tmux](http://linuxtoy.org/img/2012/07/tmux.png "tmux")](http://linuxtoy.org/img/2012/07/tmux.png)

有兴趣的同学可至我的 [GitHub][g] 页面围观 :)

[t]: http://linuxtoy.org/archives/from-screen-to-tmux.html  
[g]: https://github.com/xuxiaodong/tmuxen
