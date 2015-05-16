Title: X 系统的相关命令
Date: 2009-12-02 14:01
Author: hmy
Category: Cli
Slug: x-commands

X 系统提供了一些丰富的命令，利用这些命令可以方便的完成某些有用的工作。  
xset 设置 X 系统的方方面面，  
比如设置 bell
响玲的声音大小，设置键盘的重复率，绿色能源控制，字体路径，键盘  
led 灯的状态，  
鼠标的左右手习惯，设置屏幕保护参数等。

例如我在开机的时候执行下面命令来设置鼠标的灵敏度：

xset m 4/2 4

用下面的命令来让屏幕关闭：

xset dpms force off

再配合 slock 命令，这样就完全黑屏锁住了屏幕，而且消耗资源最少。

另外还有一个 xmodmap
命令，可以对键盘映射进行重新布局。比如用下面的命令把 Windows 键转换成
Ctrl 键来用。


    remove mod4 = Super_L
    add Control = Super_L

另外还有 xsetroot，xhost 等很多命令，希望能抛砖引玉，番茄鸡蛋也可。
