Title: GameConqueror v2.0b 公测
Date: 2009-12-21 11:37
Author: toy
Category: Games
Tags: GameConqueror
Slug: gameconqueror-v20b

{ 撰文/[WangLu](http://coolwanglu.blogspot.com) }

之前也（一年多了吧，可能快两年了）写过一个早期版本，在 LinuxTOY  
上也发过[广告](http://linuxtoy.org/archives/gameconqueror.html)。  
后来不开发了，一个是够用了，另一个是 64/32bit 支持遇到了难题。  
后来发现了 scanmem，看了看代码觉得还不错，于是就给它搞了个前端。

目标基本就是 CheatEngine 了，另外 scanmem
的一个优点是自动检测类型，这个思想蛮不错的，虽然慢些，但是可以忍受。

目前支持 int/float/double 搜索，支持的命令是 n(任意数字) 》(增加) <
(减少)。  
可以锁定数值，仅支持 '=' flag，就是保持不变。  
比较麻烦的是搜索和锁定的时候只能输入整数。

建议用 shell 执行，因为错误信息会在那里显示，而不会弹出来。

目前最想实现的功能：memroy view/edit。

主页  

svn地址  
svn checkout http://scanmem.googlecode.com/svn/trunk/ scanmem-read-only

目前只能 svn，没有发布，需要自行 automake，依赖 PyGTK，make 以后执行  
gui/GameConqueror.py。

PPA:

我很想知道 32bit 下能否正常使用，欢迎反馈~

{ Thanks WangLu. }
