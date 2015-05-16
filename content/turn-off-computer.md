Title: Linux 关机小技巧
Date: 2009-08-28 11:51
Author: toy
Category: Tips
Slug: turn-off-computer

{ 撰文/逸飞 }

在 Linux
下关机有多种选择，可以从菜单关机，也可以从命令行关机。方式多种多样，可以有关机（Power
off）、待机（Suspend）、休眠（Hibernate）。

你可以随时进入待机与休眠状态，无须将所有工作一个一个保存，并关闭一个又一个的应用软件。因为休眠所保存的是当前的“状态”，所有打开的程序、设置及窗口排列等都不会改变。另外开机和关机的过程速度快。在开机方面，以
Ubuntu 来说，如果 Power off
后再开机，每隔三差五的系统就要进行磁盘检查，很耗费时间。要注意待机与休眠的区别，待机（Suspend）是挂起到内存，关机后需要保持对内存供电，不能完全关闭电源，但是这种方式重启动的速度最快。休眠（Hibernate）是挂起到硬盘，可以完全关闭电源。推荐大家多用待机与休眠，好处是显而易见的，以我的系统为例，在我的系统上运行着两个
kvm daemon 及一个 emacs daemon，如果每次都 Power off，这种繁琐可想而知。

在 GNOME 下实现待机与休眠很简单，直接从菜单点就可以了。可是在
wmii、Awesome 及  
FVWM 等 Window Manager 下怎么办？关机的命令是 shudown，可是查看 man
并没有  
suspend 及 hibernate 选项。系统也没有 suspend 及 hibernate 命令。Google
了 N  
次也没有找到答案，只好每次都退出 Window  
Manager，到登录界面去休眠（Hibernate）。后来想到，既然是 GNOME  
登录菜单上的命令，那命令应该是跟 GNOME 有关的了。打开 GNOME
Terminal，输入  
gnome- 后 TAB 自动补全，果然发现一个命令：gnome-power-cmd，就是它了。

* 待机：`$ gnome-power-cmd suspend`  
* 休眠：`$ gnome-power-cmd hibernate`

问题：没有 GNOME 怎么办？
