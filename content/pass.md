Title: pass: 以 Unix 之道来管理密码
Date: 2014-04-01 10:49
Author: toy
Category: Cli
Slug: pass

pass 是一个遵循 [Unix 哲学][u]开发而成的密码管理工具。使用 pass，你可以添加、移除、生成、检索、以及同步密码。密码通过 GPG 加密保存，并能够根据个人的需要有条理地进行组织。

<!-- PELICAN_END_SUMMARY -->

**安装 pass**

pass 已被包含到大多数 Linux 发行版的包仓库中，因此可直接通过包管理器安装：

    % sudo apt-get install pass # Debian/Ubuntu  
    % sudo yum install pass # Fedora/RHEL  
    # emerge -av pass # Gentoo  
    # pacman -S pass # Arch Linux

当安装完毕后，Debian/Ubuntu、Fedora/RHEL、Arch Linux 用户可将 pass 的 bash 补全文件添加到配置中：

    % echo "source /etc/bash_completion.d/password-store" >> ~/.bashrc

Gentoo 用户需执行以下命令来启用 bash 补全：

    # eselect bashcomp enable --global pass

**初始化密码存储**

首先，你需要执行下面的命令来初始化密码存储：

    % pass init E4C5E99A

其中，你应将 `E4C5E99A` 换成你的 GPG key ID。执行该命令后，pass 将在你的用户主目录下创建 .password-store 目录及 .gpg-id 文件。

如果你打算将密码存储通过 Git 进行管理，那么也可在此时初始化 Git 仓库：

    % pass git init

这样，你的每次操作 pass 都会自动提交到 Git 仓库中。

**生成密码**

要使用 pass 生成密码，可执行：

    % pass generate im/irc 10  
    [master 5e62671] Added generated password for im/irc to store.  
    1 file changed, 0 insertions(+), 0 deletions(-)  
    create mode 100644 im/irc.gpg  
    The generated password to im/irc is:  
    T4$urI145B

在此，我们为 im 类目下的 irc 生成了 10 位的随机密码。

**添加密码**

对于已有的密码，可通过下列命令将其添加到 pass 的密码存储中：

    % pass insert website/linuxtoy.org  
    Enter password for website/linuxtoy.org:  
    Retype password for website/linuxtoy.org:  
    [master 20910f5] Added given password for website/linuxtoy.org to store.  
    1 file changed, 0 insertions(+), 0 deletions(-)  
    create mode 100644 website/linuxtoy.org.gpg

这里，我为 website 类目的 linuxtoy.org 站点加入密码，根据 pass 的提示输入即可。

**编辑密码**

如果后来对密码进行了修改，那么我们对已存储在 pass 中的密码就有必要进行同步更新了。这可通过 `pass edit` 命令来完成：

    % pass edit im/qq  
    [master a688254] Edited password for im/qq using editor.  
    1 file changed, 0 insertions(+), 0 deletions(-)

在授权通过后，pass 将调用默认的文本编辑器来让你对密码进行修改，完成后直接保存即可。

**删除密码**

对不想再保留的密码，可将其从 pass 的密码存储中移除：

    % pass rm im/irc  
    Are you sure you would like to delete im/irc? [y/N] y  
    removed ‘/home/xiaodong/.password-store/im/irc.gpg’  
    [master 3f2ae10] Removed im/irc from store.  
    1 file changed, 0 insertions(+), 0 deletions(-)  
    delete mode 100644 im/irc.gpg

从命令输出可以看到，删除密码需要得到你的确认。

**查看密码**

其实，我们最关心的是如何使用这些已经保存的密码。为此，pass 提供了查看并将其拷贝到剪贴板的接口：

    % pass show -c website/linuxtoy.org  
    Copied website/linuxtoy.org to clipboard. Will clear in 45 seconds.

此处，我们查看了 linuxtoy.org 的密码，并复制到了剪贴板中，这样我们就可以直接用来登录了。

值得注意的是，为了安全，复制到剪贴板中的密码只会保存 45 秒。

使用 Firefox 的朋友也可以配合 [passff][f] 这个插件来直接从 pass 检索密码，并自动填充及提交表单。

**参考**

* [pass 官方网站](http://www.zx2c4.com/projects/password-store/)  
* [pass Manpage](http://git.zx2c4.com/password-store/about/)

[u]: http://en.wikipedia.org/wiki/Unix_philosophy  
[f]: https://github.com/jvenant/passff
