Title: tmux 1.7 发布
Date: 2012-10-15 10:06
Author: toy
Category: News
Slug: tmux-1-7

[tmux][t] 是类似 GNU screen 的终端复用器。最近，tmux 的开发者发布了 1.7
版本，该版本主要包含如下改进：

* 新增 `move-pane` 及 `choose-tree` 命令  
* 新的 `status-position` 选项允许将状态行配置到屏幕的顶部或底部  
* 配置文件现在可以使用
``（续行符）、`~`（用户主目录）、`.`（服务器启动目录）、`-`（会话启动目录及面板的工作目录）等符号  
* `send-keys`、`find-window`、`select-layout`
等命令支持新的选项  
* 支持 `bracketed-paste` 模式  
* 改善了 manpage

你可以从 tmux 的项目主页下载其[源代码][s]。

[t]: http://tmux.sourceforge.net  
[s]: http://sourceforge.net/projects/tmux/files/tmux/tmux-1.7/
