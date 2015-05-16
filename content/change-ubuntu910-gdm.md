Title: 小小更改 Ubuntu 9.10 的不和谐的 GDM 登录界面
Date: 2010-01-01 12:15
Author: ihipop
Category: Tips
Slug: change-ubuntu910-gdm

{ 撰文/[ihipop](http://ihipop.gicp.net/)}  
  
怎么说呢，小小的抱怨下

9.10
的某些改进太过极端了，构建变化太大，多，升级过度不平滑，而且还有那么多的
BUG，不知道是不是为了 Gnome 3 做准备

（个人感觉，大家别拍板砖(*^\_\_^*)。。。），，，，，，，，，，，

举例来说，这个新的 GDM，暂时不能更换主题，如果你用默认的
Xsplash，还好，看的过去，但是若果你更换了
Xsplash，尤其是换成了那种明快色调的，那个黑布垃圾的东西，太不和谐了

下面就小小微微调整下  

1.  注销当前用户，退出到 GDM 登录界面
2.  Ctrl+Alt+F1，切换到命令行下面，并且正常登录
3.  设定环境变量(是数字0，不是字幕O)  <span style="blue;">export
    DISPLAY=:0.0</span>
4.  运行下列命令 <span style="blue;">sudo -u gdm
    gnome-control-center</span>
5.  Ctrl+Alt+F7，切换到 X 下面，你会看到按照用户 gdm 权限运行的
    gnome-control-center
6.  切换到 appearance 外观选项卡，在这里设置和你当前主题匹配的 GDM
    登录主题，配色，和字体，完成后关闭即可
7.  所有设置，立竿见影～看图吧～(*^\_\_^*) ……

[](http://i.linuxtoy.org/images/2010/01/0101_104821.jpg)  

[![login](http://i.linuxtoy.org/images/2010/01/0101_104806-400x300.jpg)](http://i.linuxtoy.org/images/2010/01/0101_104806.jpg)[![login-detail](http://i.linuxtoy.org/images/2010/01/0101_104821-400x300.jpg)](http://i.linuxtoy.org/images/2010/01/0101_104821.jpg)
