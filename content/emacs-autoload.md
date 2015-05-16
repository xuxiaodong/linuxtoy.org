Title: emacs autoload 集装箱
Date: 2013-02-09 02:45
Author: Kardinal
Category: IDE
Tags: Emacs
Slug: emacs-autoload

可能同学们不知道我要表达的是什么，那么先讲两个典型应用吧：

====1====

把你所有的非emacs自带函数集中起来，放到一个文件夹里；然后拆分成许多文件（每个文件里的函数建议不要超过5个），然后函数前面加上
;;;###autoload ，在你的配置文件里写：

;假设你的这个文件夹路径为 /x/y/z

(lazily "/x/y/z")

通俗的说，效果就是，给这些文件里面的函数生成一个路径表，这些函数文件都不用读取了，只读取这个路径表，用到这些函数的时候再根据这个路径表读取所在文件，对于加快
emacs 的启动速度有一定帮助

====2====

类似于 eval-after-load，利用 autoload 的递归定义，在正式加载前进行配置。

如何递归定义 autoload ：

~/a.el 文件中：(autoload 'x "~/b.el" t)

~/b.el 文件中：(autoload 'x "~/a.el" t)

对 a 表达式求值，然后执行 (x) ；会读取 b 文件查找 x 函数的实际定义，但是
b 文件中的定义会让 emacs 到 a 文件中查找……然后就是死循环了（按 "C-g"
中断）。

换一种方式，如果 b 文件中的定义不指向 a 文件，而是指向 x
的实际定义，并且写上一些自定义配置，那么就相当于在执行 x 的时候先加载了
b 文件，然后加载 x 实际定义所在文件，然后执行 x。

这种方法比较适合提高启动速度，只要在配置文件中写 (autoload 'x "b.el" )
，那么执行 (x) 的时候会加载 b 文件中的配置，再根据 b 文件中的 (autoload
'x "x.el" ) 找到实际的 x 定义并执行 x。

例如，
[这个文件](https://github.com/ran9er/init.emacs/blob/master/_autoload-conf/evil-mode.el "这个文件")
里包含一些 evil-mode
相关的配置，一般情况下都是直接写进配置文件，启动必须加载，或者高级点的用
eval-after-load。前一种情况不用说了，大部分人都这样，这也是 emacs
为人诟病的启动速度的直接原因；eval-after-load 其实已经把需要 eval
的内容读取了，load
后再计算，当然这点内存一般不成问题，一般人也不会写几万行配置文件不是，真正的问题在于
eval-after-load
是和特性（或者说文件）挂钩的，不方便理解，这个文件还得存在于 load-path
，并且要 provid。

这样看起来还不错，但是配置起来却比较麻烦，所以，重点是：

把这种预配置的文件都放在一个文件夹里，假设是 "/x/y/z"，在实际的 autoload
定义前写个 ;;;###autoload ,然后在配置文件里写……你懂得

(lazily "/x/y/z")

  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[“它看起来像个函数！”](https://github.com/ran9er/init.emacs/blob/master/__lazily.el "nea")

首先，什么是 autoload？

实际上，它就是个函数。

所谓“实际”，是指在实际使用的时候，你是区分不出来 autoload
和普通函数的区别的。

autoload 在 emacs
中也是一种类型，和符号、数字、字符串、函数是同等级别的对象，它和函数的区别类似于函数原型和函数的区别——没有实际的定义，只有简单说明，
调用的时候才加载相关定义。

autoload 对象需要用 autoload 函数生成，类似下面这种：

(autoload 'fn "file" "docstring" interactive type)

参数包含： fn （没有名称你敢怎么调用） file （具体定义实际存储的位置）
docstring （使用说明） interactive （如果非 nil
表示可以通过交互方式调用） type （类型：函数、宏、键图）

使用 autoload
有什么好处？简单的说就是节约资源，包括广大人民群众喜闻乐见的缩短 emacs
启动时间……当然作为一个实诚人，我必须说，效果不明显。

更有意义的就是在加载方面，因为加载 autoload 的时候，是把该 autoload
所在文件一起读取，所以理论上，你可以一个 require 也不用写，全用 autoload
！某种程度上，这也是一种抽象，你不用再为加载哪个文件犯愁，比如有些该加载的文件没有加载——其实也没什么问题，无非是报错，然后除错——相信自己，这不算什么，尤其是比起不该加载的文件被加载这种情况，起码它还会报错不是？

如果你足够细心，会发现很多 emacs 内置的 elisp 文件，你并不需要显式的
require/load
，用到的时候就加载了，很是神奇。打开这些文件，可以看到里面有一些
“;;;###autoload” 样子奇怪的东东（autoload magic cookies）。

我曾经也认为，在函数定义前面添上 magic cookies
就万事大吉了。其实完全不是这么回事，理论上还需要调用
update-directory-autoloads 之类的函数，根据 magic cookies 生成 autoload
定义文件，然后再读取该文件。

关键的问题是 emacs 内置的 update-directory-autoloads
并不好用，参数很古怪，完全让人无所适从。甚至在 emacs 24
之前，要通过指定外部变量 generated-autoload-file
来确定输出文件……你根本无法理解，函数和函数之间的差距咋就这么大呢！

其实这些也不是没有人能够忍受，如果你是个 M
的话；关键的问题在于，它生成的 autoload 定义，位置参数只是一个文件名！

然后怎么找到这个文件呢？很简单，这个文件要在 load-path
里面，如果你把自己收集整理的函数放在一个文件夹中的话，那么你要把这个文件夹加入
load-path
……当然这也不是什么问题，然后你要给文件起一个名字，比如你把一些函数放在
xxx.el 里面，然后会发生什么事情呢？

假设 emacs 自带了一个 xxx.el(a) 文件，在 load-path 中，它里面定义了一个
autoload 函数 y；而你自己的 xxx.el(b) 文件也加入 load-path，那么当你调用
y 的时候，它会到你自己的 xxx.el(b) 文件中查找，然后就悲剧了。

这有点类似于 lisp-1
中的变量捕获，所以我给它起了一个好听的名字：文件捕获。为了避免这个有着好听名字的问题，我给自己的文件起些不太好听的名字，类似 +xxx.el
这样，人生真是寂寞啊……

所以，如果能够在 autoload
中指定文件位置的话，就可以避免像这样沦落为一个寂寞的二逼青年，为了成为一名正义的二逼青年，我弄了这么个东东，主要特点：

1.不再依赖于 load-path ，你可以自己指定位置，生成的 autoload
定义是这样的（保存在loaddefs文件中的定义）

(autoload 'calc-column  
(expand-file-name "\_autoload/column" *init-dir*)  
"Not documented.\\n\\n(fn fn)" t nil)

可以看到，路径的位置是一个表达式，使用相对位置来定位，执行上面定义，得到定义为（读取loaddefs文件后得到的定义）

(autoload "d:/apps/emacs/init.emacs/\_autoload/column" "Not documented.

(fn fn)" t nil)

2.loaddefs 文件中使用列表来保存数据，比较文艺；而 emacs
自带的版本，文件名和时间的信息保存在注释中。但是从另一个方面来说，原来版本的
loaddefs 可以直接
load，而现在的这个需要有一个专用的函数来加载，这点比较二逼。

3.使用简单

(lazily 目录)

[文件下载地址](https://github.com/ran9er/init.emacs/blob/master/__lazily.el "nea")
