Title: tmuxomatic：管理 tmux 会话
Date: 2016-04-29 15:41:16
Authors: toy
Category: Cli
Tags: tmux
Slug: tmuxomatic
Via: tmuxomatic|https://github.com/oxidane/tmuxomatic

随着 [tmux][t] 的流行，其周边工具也开始逐步多了起来。tmuxomatic 以一种称为 windowgram 的方式来安排 [tmux][t] 窗口会话，一旦经过组织并保存到文件，便可多次重复使用。与手工操作比较起来，感觉着实要省事不少。

<!-- PELICAN_END_SUMMARY -->

tmuxomatic 要求 Python 3 及 tmux 1.8 以上版本，可通过如下指令安装：

    pip install tmuxomatic

值得注意的是，此方法安装的 tmuxomatic 2.18 存在一个 bug。如果设置了 tmux 的 `pane-base-index` 不为 0，tmuxomatic 将报找不到 `pane 0` 的错误。不过，tmuxomatic 的 git 版本已经对此进行了修正。

初次使用 tmuxomatic，我们执行 `tmuxomatic -f demo_session` 来绘制 windowgram。

1. 在 tmuxomatic 的 flex 命令提示符下输入 `new cli` 新建一个名为 cli 的窗口。此时，屏幕上会显示数字 1 作为标识。

2. 为了便于后续操作，将 `1` 放大到 30 个字符宽和 10 个字符高：

        scale 30x10

3. 目前只有 1 个窗格，我们接着在右边再添加一个窗格，其宽度与 1 一样：

        add right 100%

4. 现在我们有了两个窗格 0 和 1，如果需要更多窗格，那么还可以使用 `break` 或 `split` 指令。这里我们使用 `split` 来将 0 进行分拆：

        split 0 bottom 5 2

    这样我们将窗格 0 变成 0 和 2，且高度一样。

5. 如果不再需要其他操作，可以执行 `done`。之后，tmuxomatic 将为我们创建此会话。执行 `exit` 则只保存结果。

在 windowgram 绘制完毕后，我们还可以根据需要来为窗格添加别的操作，比如执行程序、转到某个目录、聚焦。

```
1 run vim
0 dir ~/code/linuxtoy.org
2 foc
```

窗格 1 执行 Vim，0 转到 `~/code/linuxtoy.org` 目录，并聚焦窗格 2。

通过 `cat demo_session` 看看最终的样子：

```
##------------------------------------------------------------------------------
##
## Session file created by tmuxomatic flex 2.19-dev
##
##------------------------------------------------------------------------------

## Window added by tmuxomatic flex 2.19-dev

window cli

111111111111111111111111111111000000000000000000000000000000
111111111111111111111111111111000000000000000000000000000000
111111111111111111111111111111000000000000000000000000000000
111111111111111111111111111111000000000000000000000000000000
111111111111111111111111111111000000000000000000000000000000
111111111111111111111111111111222222222222222222222222222222
111111111111111111111111111111222222222222222222222222222222
111111111111111111111111111111222222222222222222222222222222
111111111111111111111111111111222222222222222222222222222222
111111111111111111111111111111222222222222222222222222222222

1 run vim
0 dir ~/code/linuxtoy.org
2 foc
```

要创建 tmux 会话，只需执行 `tmuxomatic demo_session` 即可。

[t]: https://linuxtoy.org/tag/tmux.html
