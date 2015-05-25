Title: 给 Zsh 的 Vi 模式添加指示符
Date: 2015-05-25 22:09:46
Authors: toy
Category: Tips
Tags: zsh, vi
Slug: vi-mode-in-zsh-prompt

用久了 `zsh` 的 Vi 命令行编辑模式，有时候会恍惚自己到底在哪个模式。大家都知道，Vim 的状态行可以显示模式的指示，以此来说明是正常模式还是插入模式。如果我们能把 Vim 的这个特性移植到 `zsh` 身上，那就完美了。

<!-- PELICAN_END_SUMMARY -->

用 `man zshzle` 看了看文档，发现实现起来并不难，只需在 `.zshrc` 中添加如下内容即可：

```bash
VIMODE='-- INSERT --'
function zle-line-init zle-keymap-select {
    VIMODE="${${KEYMAP/vicmd/-- NORMAL --}/(main|viins)/-- INSERT --}"
    zle reset-prompt
}
zle -N zle-line-init 
zle -N zle-keymap-select

RPROMPT='%{$fg[green]%}${VIMODE}%{$reset_color%}'
```

稍微解释一下，首先我们设置 `VIMODE` 变量保存默认状态（插入），接着利用 `zle` 提供的两个 widgets 来对变量内容进行替换，并重绘提示符。然后执行 `zle` widgets，并设置 `RPROMPT` 使指示符显示在右边。效果如下图。

![zsh-vi-mode](/images/2015/05/zsh-vi-mode.png)
