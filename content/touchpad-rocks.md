Title: Touchpad rocks
Date: 2008-01-22 10:15
Author: toy
Category: Tips
Slug: touchpad-rocks

本来想写英文的 blog，可考虑到好像还没有特别详细的介绍配置 触摸板
的中文文章，还是用中文算了，一是可以给我 so poor
的英文语法遮羞，二来可以丰富一下中文的 Linux 资源，三来一会还要继续我的
LaTex work，节省点查字典的时间。

不知道是不是大家都像我一样忽略了配置笔记本的触摸板，我似乎这些年都一直在用笔记本工作，学习，娱乐，一直都额外再配个鼠标，一直忽略了强大的触摸板。最近看了
Apple 刚出的 Macbook Air 的多功能触摸板，心血来潮，研究了一下 Linux 下面
X
的触摸板的驱动的配置，发现其强大无比，如果你早知道了，莫要笑话我，哈哈，let's
go。

如果你装的是 Ubuntu 发行版，那么基本上你的 X 的配置文件 (xorg.conf)
里面已经设置好了相关的驱动，是默认设置，你只需要添加些相关的参数就 ok
了。下面是 Ubuntu 默认的触摸板的配置：

    Section "InputDevice"
        Identifier "Synaptics Touchpad"
        Driver "synaptics"
        Option "SendCoreEvents" "true"
        Option "Device" "/dev/psaux"
        Option "Protocol" "auto-dev"
        Option "HorizScrollDelta" "0"
    EndSection

先让我们来使我们之后的修改不需要重启 X 就能生效，在上面的里面添加：

`Option "SHMConfig" "on"`

然后重启一下 X，这样你就可以动态的通过 synclient
命令来修改你的触摸板的参数，当然也有 Gui 的程序，比如
qsynaptics。看你习惯吧，推荐用
synclient，只有命令行才最强大，不是么，哈。比如 synclient Var1=value1
Var2=value2 ....

因为各位的显示器的分辨率都不一样，所以默认的设置可能会让你觉得使用触摸板移动指针太慢了，没关系，let's
correct this：  

` Option "MinSpeed" "0.9" Option "MaxSpeed" "1.5" Option "AccelFactor" "0.0750"`

这是我的设置，我的分辨率是 1920 x 1200， 所以你们酌情修改……一般来讲
MinSpeed 0.5、MaxSpeed 0.9、AccelFactor 0.0350 就 OK 了。

很多电脑上面的触摸板下面只有两个 Pads， 没有中键这怎么办？ok，这么办：

`Option "RBCornerButton" "3"`

现在你点击你的触摸板的右上角就是中键了，帅吧。
一般触摸板的右下角是右键，右上角是中键，然后右面边缘是上下 scroll，
下面边缘是左右 scroll，这些是默认设置，可以通过 synclient -l
来查看你机器上面的默认设置。

如果上面的一些和边边角角有关的设置不起作用的话，肯定是默认的 edge
的设置不对，你可以设置一下 LeftEdge，RightEdge，TopEdge，BottomEdge
来适应你的需要。

如果你的触摸板支持多点的话，你也可以设置成类似 MacBook 那样用两只手指
scroll 哦。

最后再推荐一个小程序，可以模拟测试你的输入设备的行为，xev。

还有很多微调的参数，man synaptics 自己去研究吧。

[撰文 /
[Jay](http://jay-notes.blogspot.com/2008/01/touchpad-rocks.html)]
