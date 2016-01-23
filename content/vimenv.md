Title: Vimenv：我的 Vim 环境我作主
Date: 2012-04-17 23:39
Author: toy
Category: Tips
Tags: Vim
Slug: vimenv

相信每位使用 [Vim][v] 的朋友都有一套自己的环境配置。我自然也不例外。最近，我对自己的 Vim 环境进行了审视，深感具有不少问题，仍有改进之必要。  

**现有问题**

细究起来，我的 Vim 环境配置目前主要存在下面两个问题：

1. 管理不便。这里所说的管理主要针对 Vim Scripts 而言，包括插件、配色方案、工具等等。它们的安装、删除、升级若是纯粹通过手工来完成的话，的确显得麻烦，且耗费时间。

2. 移植性差。我总是会在不同的电脑上使用 Vim。当将 Vim 配置从一台电脑迁移到另一台电脑时，既不够顺畅，又需要做额外的工作。

**Pathogen + Git submodules 来拯救**

要解决上述问题，其实只要 [Pathogen][p] 和 [Git submodules][g] 就可以完美达成。其中，Pathogen 这个 Vim 插件能对 Vim 的 runtimepath 做到轻松管理。这样，Vim 的各式插件、配色方案、以及工具可以分别归属于自己单独的位置。而 Git submodules 则使添加、升级 Vim 插件更加方便。这使我的 Vim 环境配置具有非常好的灵活性。

**Vimenv：更加趁手**

为了使这套方案用起来更加趁手，我用 Ruby 编写了 [Vimenv][e] 这个简单的脚本。其用途包括：初始化 Vim 环境、添加/移除/列出/更新 Vim 插件、编辑 Vim 配置等。

Vimenv 用法如下：

    % git clone git://github.com/xuxiaodong/vimenv.git  
    % cd vimenv  
    % ./vimenv -i # 初始化 Vim 配置，默认使用同目录下的 \_vimrc 及 \_vim  
    % ./vimenv -u # 更新插件  
    % ./vimenv -a majutsushi/tagbar # 添加 tagbar 插件，即去除 https://github.com/ 之后的部分  
    % ./vimenv -r gist # 移除 gist 插件  
    % ./vimenv -l # 列出已安装的 Vim 插件

如果你使用我的 Vim 环境，只需执行前 4 步即可。另外，其下的 \_vimrc 可换成你自己的，但别忘了在其中添加下面几行以使 Pathogen 使用正常：

    " Pathogen  
    runtime bundle/pathogen/autoload/pathogen.vim  
    call pathogen#infect()  
    call pathogen#helptags()

欢迎 fork :)

[v]: http://www.vim.org  
[p]: https://github.com/tpope/vim-pathogen  
[g]: https://help.github.com/submodules/  
[e]: https://github.com/xuxiaodong/vimenv
