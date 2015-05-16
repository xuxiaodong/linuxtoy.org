Title: Ubuntu 升级：从 Edgy 到 Feisty
Date: 2007-01-26 22:39
Author: toy
Category: Tutorials
Slug: ubuntu-upgrade-from-edgy-to-feisty

Ubuntu 的最新开发版 7.04（Feisty）目前已经发布了两个 Alpha
版，其中不仅搭配了眼下各种软件的最新版本，而且添加了一些不错的新特性。在
Ubuntu Feisty Herd 2 推出后，我便想将现在使用的 Edgy
升级，但无奈受海底光缆损坏影响，无法获得较为理想的下载速度，所以只好作罢。直到今天，我的系统终于实现了从
Edgy 到 Feisty 的升级过程。

[![Control
Center](http://i.linuxtoy.org/i/2007/01/control_center_s.jpg)](http://i.linuxtoy.org/i/2007/01/control_center.jpg)

我把自己的升级过程写下来，希望对需要升级的朋友有些帮助。在此，要说明的是，Ubuntu
Feisty
尚未正式发布，可能会存在一些潜在的不稳定性问题。所以仅供测试之用，不要用于工作的平台。

从 Edgy 到 Feisty 的升级步骤为：

1.  修改 sources.list 文件。该文件位于 /etc/apt/
    目录下，你可以使用任何文本编辑器来修改它。你只需将该文件中的 `edgy`
    替换为 `feisty`
    并保存即可。要注意的是，如果你在该文件中添加了第三方软件的源的话，请根据实际情况酌情修改。
2.  更新源。在终端中执行 `sudo apt-get update` 指令。
3.  升级系统。你需要执行 `sudo apt-get dist-upgrade`
    命令。根据你的机器性能、网络速度、以及现有的系统情况，此过程需耗费较长的时间。从下载到完成安装，在我的机器上大约花了两个多小时。

一般来说，执行以上三步便可完成整个升级过程，但还是有可能出现一些问题。我的实际情况是第三步完成后，有两个包无法正常安装。这时，可以执行
`sudo apt-get -f install` 来解决问题。

在成功升级后，使用 ` cat /etc/issue` 可以看到现有系统的版本已经变成了
Ubuntu feisty (development branch) 字样。目前，Ubuntu Feisty 的 GNOME
已经更新到了 2.17.90，还有其他许多软件的更新。另外，在 System
菜单中原有的系统选项设置和管理工具已被 Control Center
所取代。至于更多细节方面的更新，则需要慢慢去发掘。
