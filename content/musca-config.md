Title: 最小主义: 我的 Musca 桌面环境
Date: 2009-11-09 16:14
Author: jiqingwu
Category: Tips
Tags: Musca, WM
Slug: musca-config

{ 撰文/[吴吉庆](http://hi.baidu.com/jiqing0925) }

我现在有一个非常简单实用的桌面环境了：Musca + Conky + Trayer。

当然 Musca 运行时需要 dmenu，其实也不是非 dmenu不可，据说 Dzen 也不错。  
我现在用的是 dmenu。

先放一张我的桌面截图吧。

[![Musca](http://i.linuxtoy.org/images/2009/11/musca\_config-thumb.jpg)](http://i.linuxtoy.org/images/2009/11/musca\_config.jpg)

**我的 Musca 配置**

[Musca](http://linuxtoy.org/archives/musca.html)  

是我最近发现的非常喜欢的平铺式窗口管理器。对于它的安装和使用我已经在[这里](http://linuxtoy.org/archives/musca.html)做了介绍。今天主要介绍一下它的配置，也就是在  
.musca\\\_start 中写了哪些让 Musca 启动后执行的命令：

#!bash  
# 告诉musca不要管理conky和trayer的窗口  
manage off trayer  
manage off Conky

# 启动conky和trayer  
exec conky  
# 为了方便在网页中显示，我把trayer的命令拆为3行，  
# 请复制后拼接为一行  
exec trayer --edge top --align right --widthtype request  
--height 20 --SetDockType true --transparent true  
--alpha 255 --tint 0x00ff00

# 设定聚焦帧的边框颜色为橘黄，我喜欢的颜色  
set border\_focus Orange  
# 如果有空帧，则新启动的程序会自动在空帧中打开，这点很方便  
set window\_open\_frame empty  
# 不需要单击，鼠标经过的时候窗口就聚焦  
set focus\_follow\_mouse 1  
# 设置dmenu的启动命令，我用的是自己编译的支持xft的dmenu  
set dmenu /usr/local/bin/dmenu -i -b -fa Sans-12 -p $

# 因为我没有xterm，所以重新绑定Mod4+t启动系统的默认终端  
bind off Mod4+t  
bind on Mod4+t exec x-terminal-emulator  
# 按Mod4+q退出musca，不知道为什么不管用  
bind on Mod4+q quit  
# 按Mod1(我这里是Alt) + 方向键移动选定的窗口  
bind on Mod1+Left slide left  
bind on Mod1+Right slide right  
bind on Mod1+Up slide up  
bind on Mod1+Down slide down

# 按Mod4 + 数字键快速地切换工作组  
bind on Mod4+1 use 0  
bind on Mod4+2 use 1  
bind on Mod4+3 use 2  
bind on Mod4+4 use 3  
bind on Mod4+5 use 4

# 确定每个工作组的活跃范围，屏幕上留出20像素给conky和trayer  
pad 0 0 20 0  
hook on ^add pad 0 0 20 0  
# 添加一个叫web的工作组，并加载我导出的窗口布局，上网用  
add web  
load .mweb  
# 切换到原来第一个工作组  
use 0  
load .mdefault

**配合 Musca 的 Conky 配置**

大家可以看到我的 Conky 中显示了当前工作组的窗口列表，这个怎么实现的呢？
Conky自己能通过 ${exec cmd} 显示 cmd 的输出。而我们能通过 musca -c
'show windows'
输出当前组的窗口列表，但是输出的格式是每个窗口一行，这不是我们想要的，我们可以通过
awk，对这个字符串处理一下。综合起来是： ${exec musca -c 'show
windows'|awk '{printf " | %s",$0}'}

为了方便大家参考，我将我整个的 Conky 配置文件贴在下面。

#!bash  
# jiqing's conky configuration

# set to yes if you want Conky to be forked in the background  
background no

# 使用xft字体  
use\_xft yes  
# 默认的xft字体  
xftfont Sans:size=10  
# Text alpha when using Xft  
xftalpha 1.0

# 每8秒更新一次  
update\_interval 8.0

# 更新的次数，设为0是永远更新  
total\_run\_times 0

# 使用桌面，不用自己的窗口  
own\_window no

# If own\_window is yes, you may use type normal, desktop or override  
own\_window\_type desktop  
# Use pseudo transparency with own\_window?  
own\_window\_transparent yes  
# If own\_window\_transparent is set to no, you can set the background
colour here  
own\_window\_colour black

# If own\_window is yes, these window manager hints may be used  
#own\_window\_hints undecorated,below,sticky,skip\_taskbar,skip\_pager

# 使用双缓冲，避免闪烁  
double\_buffer yes

# Minimum size of text area  
minimum\_size 500 18  
maximum\_width 1340

# Draw shades?  
draw\_shades no  
# Draw outlines?  
draw\_outline no

# 让conky有边框，我觉得这样酷一点  
draw\_borders yes

# Draw borders around graphs  
draw\_graph\_borders no

# 边框用实线，不用点画线  
stippled\_borders no

# border margins  
border\_margin 3

# border width  
border\_width 1

# 定义一些颜色  
color0 white  
color1 yellow  
default\_color gray73  
default\_shade\_color black  
default\_outline\_color black

# Text alignment, other possible values are commented  
alignment top\_left

# Gap between borders of screen and text  
# same thing as passing -x at command line  
gap\_x 0  
gap\_y 2

# Subtract file system buffers from used memory?  
no\_buffers yes

# set to yes if you want all text to be in uppercase  
uppercase no

# number of cpu samples to average  
# set to 1 to disable averaging  
cpu\_avg\_samples 2

# number of net samples to average  
# set to 1 to disable averaging  
net\_avg\_samples 2

# Force UTF8? note that UTF8 support required XFT  
override\_utf8\_locale yes

# Add spaces to keep things from moving about? This only affects
certain objects.  
#use\_spacer none  
use\_spacer left

# Maximum size of buffer for user text, i.e. below TEXT line.  
#max\_user\_text 16384

# Allow for the creation of at least this number of port monitors (if 0
or not set, default is 16)  
#min\_port\_monitors 16

# Allow each port monitor to track at least this many connections (if 0
or not set, default is 256)  
#min\_port\_monitor\_connections 256

# variable is given either in format $variable or in ${variable}.
Latter  
# allows characters right after the variable and must be used in
network  
# stuff because of an argument

# stuff after 'TEXT' will be formatted on screen  
# 为了方便在网页中显示，我把conky输出的内容分为多行，  
# 如果你想像我一样在一行中显示，请把TEXT后的内容拼为一行

TEXT  
${font Bistream Vera Sans Mono:size=10:bold}${color green}  
${time %Y年%m月%d日 %H:%M}$font $color  
|$color0 开机时间:$color1 $uptime\_short $color  
|$color0 CPU:$color1 $cpu% $color  
|$color0 内存:$color1 $mem/$memmax  
${font Sans:size=9}${color pink}  
${exec musca -c 'show windows'|awk '{printf " | %s",$0}'}

最后，说一点心得，其实手动平铺式窗口管理器并不是很难用，大多数情况你都不需要使用浮动窗口模式，只要你合理安排窗口布局，GIMP
你都能用得很舒服。

{
[Source](http://hi.baidu.com/jiqing0925/blog/item/42e150f7db590728720eecbc.html).
Thanks jiqing. }
