Title: GimpBox.py: 另一个单窗口 GIMP 外挂
Date: 2010-02-28 19:53
Author: toy
Category: Apps
Tags: GIMP
Slug: gimpbox

{ 撰文/[Shellexy](http://shellexy.info/blog/) }

GIMP 2.7 终于有了官方的单窗口模式，不过不知道什么原因，官方的单窗口  
GIMP 依然是老多问题， 而且 GIMP  
官方解决单窗口模式启动问题的方式依然是粗暴地让 GIMP  
退出时取消单窗口模式，以至下次启动还得手工选择单窗口模式。

于是利用 PyGtk 和 Wnck (Window Navigator Construction Kit) 写了个  
GimpBox.py 脚本，用来将零散的多个 GIMP 窗口拽进一个单一的  
GimpBox 窗口。

查看:

[GoogleCode  
上的源码](http://code.google.com/p/gimpbox/source/browse/gimpbox.py)

用法:

wget http://gimpbox.googlecode.com/hg/gimpbox.py  
python gimpbox.py

效果:

[![GimpBox](http://i.linuxtoy.org/images/2010/02/gimpbox-thumb.png)](http://i.linuxtoy.org/images/2010/02/gimpbox.png)

截图是 GimpBox.py 自己启动 GIMP， 并将 GIMP  
窗口拽进自己的效果，  
从窗口菜单和标签栏缩略图可以看出这跟 GIMP  
官方单窗口模式的差异。

{ Thanks Shellexy. }
