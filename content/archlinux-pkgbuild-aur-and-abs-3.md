Title: Archlinux 的灵魂──PKGBUILD、AUR 和 ABS (3)
Date: 2008-03-01 11:14
Author: toy
Category: Featured
Slug: archlinux-pkgbuild-aur-and-abs-3

在这一部分中，我们将简单介绍 Yaourt 的安装和使用。此部分上接 [PKGBUILD
和
makepkg](http://linuxtoy.org/archives/archlinux-pkgbuild-aur-and-abs.html)、[AUR
和
ABS](http://linuxtoy.org/archives/archlinux-pkgbuild-aur-and-abs-2.html)。

就一般情况而言，当 Archlinux 用户需要使用 AUR 中的包时，往往会执行到
[AUR
官方网站](http://aur.archlinux.org/packages.php)查找所需的包、下载该包的
Tarball 文件、在命令行下对 Tarball 文件解压、通过 makepkg
编译打包、最后使用 pacman
安装这样一个过程。仔细打量这个过程，你是否觉得稍微有些繁琐呢？有解决的方案吗？回答是肯定的。这就是我们今天将要介绍的主角──[Yaourt](http://archlinux.fr/yaourt-en)。

**Yaourt 简介**

Yaourt 是一个由 Julien Mischkowitz 所编写的 Bash 脚本，它是将 Pacman 与
AUR 这两者相结合的绝佳工具。通过 Yaourt 安装 AUR
中的包十分方便，它不仅简化了上述繁琐的过程，而且把这一过程半自动化，使用者只需在它的交互模式中简单的回答几个问题即可。此外，Yaourt
支持将结果以鲜亮的颜色输出，非常抢眼。

**安装 Yaourt**

除了在 Archlinux 的 AUR 中可以找到
[Yaourt](http://aur.archlinux.org/packages.php?do_Details=1&ID=5863)
外，archlinuxfr 这个源中也包含 Yaourt。我们采用后者来安装
Yaourt。首先，将下列内容添加到 /etc/pacman.conf 文件：  
` [archlinuxfr] Server = http://repo.archlinux.fr/i686`

如果你的系统是 64 位，那么可以使用：  
` [archlinuxfr] Server = http://repo.archlinux.fr/x86_64`

接着，我们可以执行下面的命令来安装 Yaourt：

`pacman -Sy yaourt`

另外，我们将 aurvote 和 customizepkg
这两个包也装上，前者用于对喜欢的包投票，而后者是定制 PKGBUILD 所需的：

`pacman -S aurvote customizepkg`

同时，你需要为 aurvote 建立一个配置文件 .aurvote (位于 ~/ 目录下)：  
` user=你的 AUR 帐号 pass=该帐号的密码`

如果你没有 AUR 帐号，可到 <http://aur.archlinux.org/account.php>
注册一个。

**Yaourt 实战**

为了说明 Yaourt 的使用，我们以一个实例来进行。譬如，我对
[Phatch](http://linuxtoy.org/archives/phatch.html)
这个批量图片处理程序非常喜欢，我希望在 Archlinux
中安装它。首先，我们来看一下，在 Archlinux 中是否存在 Phatch：

`yaourt phatch`

Yaourt 在搜索后返回如下结果：  

` 1 aur/phatch 0.1.bzr435-1     Phatch is a simple to use cross-platform GUI Photo Batch Processor. ==>  Enter n° (separated by blanks, or a range) of packages to be installed      Example:   '1 6 7 8 9'   or   '1 6-9' ==>   ----------------------------------------------`

从该结果我们可以断定，Phatch 在 Archlinux 的 AUR 中。现在，我们只需按 1
就可以安装它了。

在显示一些输出信息后，Yaourt 会让你作出第一个选择：是否编辑 PKGBUILD
文件。按 Y 回答并输入你喜欢的文本编辑器后，你可以针对 PKGBUILD
的内容进行修改。  

` ==>  Edit the PKGBUILD (recommended) ? [Y/n] ("A" to abort) ==>   ----------------------------------------------`

然后，Yaourt 会询问是否继续编译。我们的回答当然是 Y。  

` ==>  Continue the building of 'phatch'? [Y/n] ==>   ----------------------------------------------`

接着，Yaourt 询问是否安装已编译好的包，同样回答 Y 即可。  

` ==>  Continue installing 'phatch'? [Y/n] ==>  [v]iew package contents   [c]heck package with namcap ==>   ----------------------------------------------`

最后，Yaourt 将检查投票情况，并问你是否要投票，按 Y 选择投票，按 n
表示不投票。  

` ==> Checking for phatch's vote status You have already voted for phatch inclusion/keeping in [community]`

综观 Yaourt 的命令行选项，与 Pacman 非常相似。关于 Yaourt
的更加详细的用法，通过 man yaourt 可以获得参考。其实，除了从 AUR
安装包外，Yaourt 也可以从 Archlinux 的源安装包，此不赘述。
