Title: bash 使用技巧
Date: 2006-08-01 14:45
Author: toy
Category: Tutorials
Slug: bash_tip

1.编辑/etc/bash.bashrc，启用下面3行：  

　　` 　　if [ -f /etc/bash_completion ]; then 　　    . /etc/bash_completion 　　fi 　　`

2.载入/etc/bash\_completion

`xxd@locdev:~$ . /etc/bash_completion`

你会发现在 shell 中按 Tab 键的不同的，如试一试：sudo
apt-g[Tab]，发现了什么？它已经帮你自动补完了。
