Title: Subtle: 有趣的伪平铺式窗口管理器
Date: 2011-02-20 13:47
Author: jiqingwu
Category: Apps
Tags: Subtle, WM
Slug: subtle

本文向你介绍 Subtle 这个有趣的伪平铺式窗口管理器。

<div id="subtle" class="document">

Author:
吴吉庆
email:
<jiqingwu@gmail.com>
home:
<http://hi.baidu.com/jiqing0925>
create:
2011-02-19
update:
2011-02-20
<div id="id1" class="contents topic">

目录

-   <span id="id9">[安装subtle](#id4)</span>
-   <span id="id10">[views：虚拟桌面](#views)</span>
-   <span id="id11">[Grabs：键盘和鼠标行为的绑定](#grabs)</span>
-   <span id="id12">[subtle的特色所在：gravity](#subtle-gravity)</span>
    -   <span id="id13">[什么是gravity](#gravity)</span>
    -   <span id="id14">[如何平铺](#id6)</span>
    -   <span id="id15">[是不是真的平铺式窗口管理器](#id7)</span>
-   <span id="id16">[讨厌的Tags](#tags)</span>
-   <span id="id17">[其它特性](#id8)</span>

</div>

自从发现 [Musca](http://aerosuidae.net/musca/Musca_Window_Manager)
后，大部分时间都在用
[Musca](http://aerosuidae.net/musca/Musca_Window_Manager)
，用它可以方便地构建我  
的集成工作环境。可惜作者已经很久很久没有继续开发了，  
等我有时间了，要好好研究一下
[Musca](http://aerosuidae.net/musca/Musca_Window_Manager) 的代码。

在网上乱逛，偶然发现了一个窗口管理器的截图，它自称是手动平铺的窗  
口管理器，叫subtle。这个东西在我以前写的  

[《平铺式窗口管理器Musca初体验》](http://linuxtoy.org/archives/musca.html)  
一文中曾提了一下，但当时我也是道听途说。

这次，嘿嘿，又让我撞见它，我的手又痒了。于是我搜索到它的
[主页](http://subforge.org/projects/1/wiki/Subtle/) ，  
看见它的开发很活跃，于是想体验一下，看看它会不会比
[Musca](http://aerosuidae.net/musca/Musca_Window_Manager) 更好用。

体验的结果令我惊讶，subtle虽然也号称是手动平铺的管理器，但和  
[Musca](http://aerosuidae.net/musca/Musca_Window_Manager) 与
[ion](http://freshmeat.net/projects/ion/)
的思想完全不同，可以说是一款很有特色的窗口管理器。  
果然有点 **subtle** 的意思。如何有特色，且听我与诸位看官分解。

<div id="id4" class="section">

[安装subtle](#id9)
------------------

既然要体验，就先装一个吧。

subtle是C开发的，本身很小巧，不过它选用了ruby做配置和扩展语言。大  
概作者很喜欢ruby吧。不过，这绑定推广ruby的行为，让对 ruby  
不感冒的用户有点为难。而且要安装体积比较大的ruby1.9以上的版本。

好了，不再多愁善感了，开始行动。在
[这里](http://subforge.org/projects/subtle/files) 上下载一个源码包，  
我下载了最新的，解开后，第一步居然不是 `make`{.docutils .literal} 而是
`rake`{.docutils .literal} ，  
好吧，安装rake和ruby：:

``` {.literal-block}
sudo apt-get install rake ruby1.9.1
```

然后rape一下，哦，不对，是rake一下：:

``` {.literal-block}
rake
(in /home/jiqing/subtle-0.9.2573-lambda)
rake aborted!
no such file to load -- mkmf
/home/jiqing/subtle-0.9.2573-lambda/Rakefile:12:in `require'
(See full trace by running task with --trace)
```

google之，原来要ruby1.8-dev，真是得寸进尺：:

``` {.literal-block}
sudo apt-get install ruby1.8-dev
```

再rake：:

``` {.literal-block}
rake
(in /home/jiqing/subtle-0.9.2573-lambda)
rake aborted!
Ruby 1.9.0 or higher required
/home/jiqing/subtle-0.9.2573-lambda/Rakefile:176
(See full trace by running task with --trace)
```

真想rape之了，都装了ruby1.9.1还叫什么叫。:

``` {.literal-block}
ls -l /usr/bin/ruby
```

发现居然是到ruby1.8的符号链接。rape!

``` {.literal-block}
sudo ln -sf /usr/bin/ruby1.9.1 /usr/bin/ruby
```

然后你就可以顺利地rake它了。:

``` {.literal-block}
rake
sudo rake install
```

rake出来的执行文件除了subtle，还有：

-   subtler - 一个subtle的命令行接口，怎么用，man subtler吧。
-   subtlext - ruby扩展接口，读取subtle的配置文件就靠它了。

在你的 .xinitrc 中添加 `exec /usr/bin/subtle`{.docutils .literal}
，startx就进入了  
subtle。如果你使用某种登录管理器，要把subtle加入可选择的会话列表  
中，我不会，嘿嘿，欢迎会的同鞋补充吧。

</div>

<div id="views" class="section">

[views：虚拟桌面](#id10)
------------------------

进入subtle后，先别动，冷静观察，上面有个细长状态栏，其它就是一片  
广袤的黑色屏幕。

状态栏左边有四个标签，每一个标签代表一个view，其  
实就是工作区（虚拟桌面），你可以通过小键盘上的 + 切换到下一个  
view，通过小键盘上的 - 切换到上一个view。也可以通过Win+n  
切换到第n个view。

为了给大家直观的印象，先放张图片吧，不过这是我改了配置后的截图。

[![subtle.png](http://linuxtoy.org/img/2011/02/thumb-subtle.png)](http://linuxtoy.org/img/2011/02/subtle.png)

</div>

<div id="grabs" class="section">

[Grabs：键盘和鼠标行为的绑定](#id11)
------------------------------------

W+Enter，W表示windows键，会启动一个终端。:

``` {.literal-block}
cp /etc/xdg/subtle/subtle.rb ~/.config/subtle/
```

这就生成咱自己的subtle.rb配置文件了，用你喜欢的编辑器打开它，它是  
配置文件，同时也是咱的帮助。

``` {.literal-block}
vim ~/.config/subtle/subtle.rb
```

搜索 `== Grabs`{.docutils .literal} ，找到 Grabs
一节，这是绑定键盘和鼠标按键的部分  
，如何使用，有详细的解说。:

``` {.literal-block}
grab "W-Return", "urxvt"
```

这表示按  
Win+Enter，会打开一个urxvt的终端，如果你用的不是rxvt，就改成你的  
终端模拟器的名称，保存然后Win+Ctrl+r，让subtle重新载入配置。幸好  
我用的也是rxvt，不然按了Win+Enter还没反应。  
作者也太不考虑广大用户的感受了，如果把urxvt换成  
x-terminal-emulator ，不就能适用各种终端了吗。

现在默认的终端窗口是最大化的，跟我来体验一下：

-   按Win+KeyPad\_4（小键盘上的7），终端窗口占据了左半边屏幕；
-   按Win+KeyPad\_6（小键盘上的6），终端窗口占据了右半边屏幕；
-   按Win+KeyPad\_8（小键盘上的8），终端窗口占据了上半边屏幕；
-   按Win+KeyPad\_2（小键盘上的2），终端窗口占据了下半边屏幕；
-   按Win+KeyPad\_7（小键盘上的7），终端窗口占据了左上四分之一的屏幕；
-   按Win+KeyPad\_9（小键盘上的9），终端窗口占据了右上四分之一的屏幕；
-   按Win+KeyPad\_1（小键盘上的1），终端窗口占据了左下四分之一的屏幕；
-   按Win+KeyPad\_3（小键盘上的3），终端窗口占据了右下四分之一的屏幕；
-   按Win+KeyPad\_5（小键盘上的5），终端窗口又占据了整个屏幕。

聪明的你，早就发现了，小键盘上9个键直观地对应着9个方位。

接着按 Win+KeyPad\_5  
，发现终端窗口变小了，占据了屏幕中间某个区域；再接着按，发现终端  
窗口的大小又变了，不过还是在屏幕中间。再按的话，又变成最大化了。  
不只Win+KeyPad\_5，连续Win+其它的小键盘数字键，也会改变窗口的位置和大  
小，不过相对位置还是对应于小键盘数字键所在的方位。

这是怎么做到的，在subtle.rb的Grabs一节中有这样的键绑定：:

``` {.literal-block}
grab "W-KP_7", [ :top_left,     :top_left66,     :top_left33     ]
grab "W-KP_8", [ :top,          :top66,          :top33          ]
grab "W-KP_9", [ :top_right,    :top_right66,    :top_right33    ]
grab "W-KP_4", [ :left,         :left66,         :left33         ]
grab "W-KP_5", [ :center,       :center66,       :center33       ]
grab "W-KP_6", [ :right,        :right66,        :right33        ]
grab "W-KP_1", [ :bottom_left,  :bottom_left66,  :bottom_left33  ]
grab "W-KP_2", [ :bottom,       :bottom66,       :bottom33       ]
grab "W-KP_3", [ :bottom_right, :bottom_right66, :bottom_right33 ]
```

那里的 `:top`{.docutils .literal} ， `:top_left`{.docutils .literal}
都是什么玩意，哈哈，  
这就要提到subtle里很有特色的一个概念： *gravity* 。

</div>

<div id="subtle-gravity" class="section">

[subtle的特色所在：gravity](#id12)
----------------------------------

<div id="gravity" class="section">

### [什么是gravity](#id13)

什么是gravity，就是窗口的位置和大小。  
在subtle.rb中搜索 `== Gravities`{.docutils .literal}
，找到那一节，可以看到  
详细的说明。

往下看，就发现了那些 `:top`{.docutils .literal} 、 `:top_left`{.docutils
.literal} 之类的定义，以  
`:top`{.docutils .literal} 为例，:

``` {.literal-block}
gravity :top,            [   0,   0, 100,  50 ]
gravity :top66,          [   0,   0, 100,  66 ]
gravity :top33,          [   0,   0, 100,  34 ]
```

后面的四个值都不是像素值，而是比例，以  
`gravity :top, [   0,   0, 100,  50 ]`{.docutils .literal}  
为例，可以这样理解，窗口在最左边，最上边，宽度100%的屏幕，高度占  
50%的屏幕。

回头再看看，  
`grab "W-KP_8", [ :top, :top66, :top33 ]`{.docutils .literal}  
原来Win+KeyPad\_8对应了一个gravity的列表，难怪连续按会改变窗口的大  
小和位置呢。

</div>

<div id="id6" class="section">

### [如何平铺](#id14)

现在我们已经有一个终端窗口了，按Win+KeyPad\_4，让它靠左边呆着。  
按Win+Return，再打开一个终端窗口，按Win+KeyPad\_6，让它靠右边呆着  
。看，严丝合缝地平铺了吧。

你可以按Win+方向键遍历各个平铺在表面的窗口，  
如果窗口多了，被盖住的看不见的窗口你是遍历不了的，怎么办？  
对上层的窗口按Win+l，让它降到下一层，被盖住的窗口就上来了。

居然没有提供一个遍历当前工作区所有窗口的快捷键，多少有些可恶吧。

</div>

<div id="id7" class="section">

### [是不是真的平铺式窗口管理器](#id15)

对于平铺的两个终端窗口，我们聚焦在左边的终端窗口，再次按  
Win+KeyPad4，改变它的大小，它变大了，但右边的终端没有改变，这样右  
边终端的一部分区域就被盖住了。再按  
Win+KeyPad4，左边终端又变小了，屏幕中间空出一部分区域，右边的终端  
并没有变大来填充。

当一个窗口的大小改变时，有其它窗口的大小也会跟着改变，这才是平铺  
式窗口管理器的本质吧？而当一个窗口的位置和大小的改变独立于其它窗  
口时，它就是浮动式窗口管理器吧？  
我想这就是平铺与浮动的本质区别，  
从这个意义上看，subtle是真的平铺式窗口管理器吗？

subtle中也有浮动的概念，你对聚焦的窗口按Win+f，它就有了浮动的属性  
，但是有什么分别吗？即使被你平铺的窗口，你按住窗口键，用鼠标  
左键同样能自由地改变它的位置，用鼠标右键同样能改变它的大小。

要说subtle的特色，我看就在于它是一个提供了一组快捷键，能快速改变  
窗口布局的浮动式窗口管理器。

</div>

</div>

<div id="tags" class="section">

[讨厌的Tags](#id16)
-------------------

除了Grab和Gravity，还有一个Tag值得一提。  
Tag的主要作用是控制窗口放在哪个view中。  
看下面的例子：:

``` {.literal-block}
tag "terms" do
  match "xterm|[u]?rxvt"
  gravity :right
end

view "dev",   "terms"
```

这表示如果我启动rxvt，就会匹配到terms这个Tag，而匹配terms这个  
Tag的窗口都会放入dev这个view中。  
也就是说，不管我在哪个view中启动rxvt，都必定放入dev这个view中，  
这算什么。

文档中还说，每个应用程序的窗口必定关联到一个view，如果没有显式关联，  
就会关联到default view。如果你没有显式指定default view，第一个  
view就是default view。

也就是说，如果我没有把gvim匹配到某个tag，也没有关联到某个view，  
我想在第三个view中，启动gvim，结果gvim会被放入第一个view，  
我还得去第一个view找它。这算什么特性？

窗口又不能在view之间移动，只能通过Win+s，让它具有stick属性，从  
而在所有view中可见。这个……，俺非常不喜欢。

Tags这个特性，有些stupid，请作者看见不要生气，请心平气和地把这当  
作用户的反馈，认真对待吧。

</div>

<div id="id8" class="section">

[其它特性](#id17)
-----------------

除了Grab、Gravity、views、Tags，  
还有Hooks属性，用户可以通过这个定义subtle中的行为会触发一些什么事  
件。我却不知道如何在subtle启动时触发外部的程序（如conky等）启动，  
不知道有没有这个功能呢？

另外，依赖ruby也不是白依赖的，你可以安装用ruby写的sublets，  
加一些时钟、cpu利用率之类的插件，不过我没弄成功。  
我耳边不禁响起《色戒》中梁朝伟的声音：有这么难吗？  
有兴趣的朋友有时间玩玩看。

体验完，我又用回
[Musca](http://aerosuidae.net/musca/Musca_Window_Manager)
啦，小声告诉你：我现在写这篇文档，  
也不是在用subtle，哈哈。不过，subtle体现了一种新的思想，  
推荐朋友们尝试一下，尤其是喜欢ruby的同学。  
尽管我不喜欢它的风格，没有坚持用下去，我想应该会有人喜欢的。

（全文完）

</div>

</div>
