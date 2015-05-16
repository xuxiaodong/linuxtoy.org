Title: 还原 Ubuntu 6.10 的默认 Shell
Date: 2006-11-06 18:18
Author: toy
Category: Tutorials
Slug: restore_ubuntu_edgy_shell

Ubuntu 6.10 已将先前默认的 [bash](http://www.gnu.org/software/bash/)
shell 更换为了
[dash](http://gondor.apana.org.au/~herbert/dash/)。其表现是 `/bin/sh`
链接到了 `/bin/dash` 而不是传统的 `/bin/bash`。

Ubuntu Edgy 是第一个将 dash 作为默认 shell 的发行，这似乎是受了 Debian
的影响。在 Ubuntu Wiki
上可以了解到更换的[相关原因](https://wiki.ubuntu.com/DashAsBinSh)，dash
更小，且运行更快，还与 POSIX 兼容。

但问题是目前网上有大片的用户由于 shell
的更换而致使脚本出错，毕竟现有的很多脚本都不是 100% POSIX
兼容。如需将默认的 shell 改回 bash，可以在执行
`sudo dpkg-reconfigure dash` 后，选择 no。

（非常感谢朋友 hui 的细心发现）
