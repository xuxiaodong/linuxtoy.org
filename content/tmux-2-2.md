Title: tmux 2.2 添加 hooks 及 24 位色支持
Date: 2016-04-11 20:42:51
Authors: toy
Category: News
Tags: tmux
Slug: tmux-2-2

与 screen 类似的终端多路复用器 [tmux]({filename}/tmux.md) 已经发布了新的 2.2 版本。

<!-- PELICAN_END_SUMMARY --> 

tmux 是我每天都在使用的好工具，看其 [CHANGES][c] 文件此版本主要新增了一些诸如 `#{scroll_position}`、`#{socket_path}` 之类的格式，实现了 client-attached、pane-exited 等 hooks，以及 RGB 24 位色支持。

值得注意的是，该版本也包含一些不兼容的更改，比如移除了 TMPDIR、mouse-utf8/utf8
选项、及某些格式化字符串等，详情可查看变更文件。

tmux 2.2 的源码包可从 [GitHub 获取][g]。

[c]: https://raw.githubusercontent.com/tmux/tmux/master/CHANGES
[g]: https://github.com/tmux/tmux/releases
