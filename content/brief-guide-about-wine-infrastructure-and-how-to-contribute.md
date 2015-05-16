Title: Wine 社区的基础设施和贡献简明指引
Date: 2014-04-05 12:05
Author: lovenemesis
Category: Featured
Tags: Wine
Slug: brief-guide-about-wine-infrastructure-and-how-to-contribute

成熟的社区都有丰富、完备的文档来介绍如何融入到社区，但还是经常会有朋友抱怨不知道如何给上游提交代码，或者如何给开源社区做一些力所能及的贡献、参与到开源社区中去，本文就以我个人比较熟悉的
[Wine](http://www.winehq.org/)
社区为例子，说一下社区的基础实施和如何提交代码、报 bug 这些事情。*感谢
Jactry 来稿*

（ 个人经历有限，如文中有遗漏、不妥，还请各位不吝赐教，谢谢 :) ）

### Wine 社区的基础设施

#### [Bugzilla](http://bugs.winehq.org/)

这是给 Wine 报 bug 的地方。

#### [Wiki](http://wiki.winehq.org/)

Wine 社区的 wiki，上面有大量的文档向新手介绍如何参与到社区，从如何报 bug
到提交代码、包罗万象。得益于来着华文世界的诸多朋友的辛勤劳动，wiki
上一些面向用户、基础的文档已经被翻译成中文。

这里列出一些常用的条目：

* [如何给 Wine 提交 bug](http://wiki.winehq.org/bug%E6%8A%A5%E5%91%8A)  
* [FAQ](http://wiki.winehq.org/FAQ\_zhcn)  
* [FAQ for developer](http://wiki.winehq.org/DeveloperFaq)  
* [Submitting Patches](http://wiki.winehq.org/SubmittingPatches)
（提交补丁的相关内容）

#### [邮件列表](http://www.winehq.org/forums)

* wine-users@winehq.org：Wine 用户邮件列表，所有使用 Wine
过程遇到的问题可以在这里讨论；  
* wine-devel@winehq.org：开发者讨论邮件列表，有任何和 Wine
开发有关的问题都可以到上面讨论、寻求帮助；  
* wine-patches@winehq.org：提交 patch 的邮件列表，所有提交给 Wine 的
patch 都需要发送到这里，接受其他开发者和 [Alexandre
Julliard](http://wiki.winehq.org/AlexandreJulliard) 的检查；  
* wine-cvs@winehq.org：显示 Wine 主干代码库变更的列表，所有 Alexandre
Julliard 检查、测试通过、合并进主干的 patch 都会被发送这个列表；  
* wine-zh@freelists.org：由华文世界 Wine
开发者、爱好者建立的中文社区，旨在吸引和帮助新人参与 Wine
项目，为不熟悉上游社区的潜在贡献者提供过渡性指引，充当上游社区和中文社区的桥梁，根本目标是鼓励和引导中文贡献者直接加入
Wine 上游社区。

（注意：以上除最后一个是中文列表外，其他四个都是以英文为交流语言的列表）

#### IRC

IRC 有时候也是一种快速和其他开发者交流、寻求帮助的途径。Wine 的 IRC 都在
Freenode.net  上：

* #winehq：Wine 用户讨论、交流的地方；  
* #winehackers：Wine 开发者讨论、交流的地方。

尽管 IRC
有时候确实比邮件列表快捷，也能一定程度加强自己和其他开发者的“私交”，但是
IRC
也有一些需要遵守、注意的规定：[http://www.winehq.org/irc](http://www.winehq.org/irc)
。

#### 代码仓库

*
[http://source.winehq.org/git/wine.git/](http://source.winehq.org/git/wine.git/)
Wine 的代码主干  
*
[http://source.winehq.org/git/website.git](http://source.winehq.org/git/website.git)
WineHQ 网站的代码镜像  
* 其他 Wine 项目的仓库
[http://source.winehq.org/git/](http://source.winehq.org/git/)  
* Wine
代码主干国内镜像：[https://gitcafe.com/WineHQ/Wine](https://gitcafe.com/WineHQ/Wine)

#### 其他设施

* Testbot：[http://testbot.winehq.org/](http://testbot.winehq.org/)
自动化的测试服务  
*
[http://source.winehq.org/patches/](http://source.winehq.org/patches/)
查看 patch 状态

### 如何给 Wine 提交 bug

简单说，给 Wine 提交 bug，就是要用英文把这个 bug
是什么、怎么重现说清楚，让开发者能够重现、调试、修复。必要时我们还得附上
log 或者图片加以说明。

[![image](http://lt-file.b0.upaiyun.com/files/2014/04/wpid-wp-1396670507779.png "wp-1396670507779")](http://lt-file.b0.upaiyun.com/files/2014/04/wpid-wp-1396670507779.png)

上图是著名的“QQ 登陆窗口点击密码框崩溃”的 bug，这里面有些地方值得注意：

1. 报 bug 前先搜索 bugzilla 中是否已经有人报 bug 了，避免重复；  
2. 要以一个简练扼要的标题来描述该 bug，可以参照这种模式：xxx
软件在怎么样的情况下出现了什么问题，一个报告只描述一个
bug，同个软件的多个 bug 应该分开报告；  
3. Component：指的是该 bug 涉及的模块，如果报 bug 者不明，可以填
unknown；  
4. Version：填写的是你发现 bug 的 Wine 版本；  
5. URL：通过这里，我们可以先其他有兴趣重现该 bug
的人提供该软件的下载。（注意，Wine
对版权、软件来源要求十分严格，不能是含有盗版、有版权争议的下载！最好是软件商直接发布的下载。）；  
6.
如果软件的界面、安装程序是中文界面，应该附上适当的中英文对照，必要时最好加上图片以更准确的说明重现的步骤细节；  
7. 恰当的 log 附加上去有时会使进度更快，最简单的 log 就是用“wine
xxx.exe &> log.txt”的方式把输出重定向，然后作为附件上传。（注意，不要在
bugzilla 直接粘贴大篇幅的 log 上去，而是要以附件的形式。）；

这里再举一个比较成功的例子：[Bug 35837: The progress bar always stop at
%87 when installing the Kingsoft disk installation
package](http://bugs.winehq.org/show\_bug.cgi?id=35837)

这个 bug
是一位中文用户上报的，因为他提供的信息很全面，问题描述也很到位，所以开发者得以迅速地分析了这个问题，然后修复，整个过程大概历时大概一个星期（2014.03.21~03.28）。可见一个良好的
bug 报告对于尽快修复一个 bug 很有很大作用的！

### 如何向 Wine 提交代码

![](http://jactry.com/post/2014/04/04/093335/workflow.png)

上图是把代码提交到 Wine 的一个基本 workflow。

首先在邮件客户端中设置 reply-to 字段为 wine-devel 邮件列表地址，再将
patch 发送到 wine-patches 列表。提交完系统会自动将 patch 推送到 Wine 的
testbot 进行测试。如果测试失败 testbot 会发送一封邮件回复到
wine-devel，其他开发者如果检查了你的 patch 发现有问题也会回复到
wine-devel 进行讨论。

之后就是等待  Alexandre Julliard 的审核，如果通过就会被顺利合并到 Wine
的主干。有时候 Alexandre Julliard 也会把 patch
进行一些小修改然后再合并。具体的 patch 状态是什么可以在
[http://source.winehq.org/patches/](http://source.winehq.org/patches/)
查看。

（注意：Wine
对代码的版权、合法性要求十分严格！微软员工、实习生，看过通过任何途径获得的
Windows 代码的人，做过 Windows 逆向工程的人皆不能为 Wine
提交补丁！具体可以查看：[http://wiki.winehq.org/CleanRoomGuidelines](http://wiki.winehq.org/CleanRoomGuidelines)）

### Wine 中文社区概况

大概 3 年前，现 wine-zh 的成员有些已经开始有目的地为 Wine
社区做一些贡献、参与到 Wine
上游去，同时也在中文社区积极开展“科普布道”，以此希望 Wine
能够对中文软件提供更优良的支持。

3 年过去了，虽然 Wine
在中文世界依然还有种种误会、直接到上游参与的开发者也在 10
位以内，但是通过诸位的努力和坚持，也积累了这样一些成果：

* 为各种中文软件提交的 bug 数目以数百个计，涵盖各种常用软件，如
QQ、阿里旺旺、迅雷、网银、股票软件等等。其中有三分之一以上得到修复；  
* 向上游提交补丁上百个，改动代码数千行，涉及
atl、gdi32、kernel32、user32、imm32、richedit、rsaenh、mshtml、ole32、oleaut32、vbscript、wineserver
等十多个模块；  
* 较 3 年前，极大地改善了 Wine 对中文的支持！（各位用 Wine
稍早一点的朋友一定不会忘记之前使用 Wine 经常会碰到各种中文乱码的问题
T\_T）；  
* Wine 本身以及 Wine 社区网站、wiki 的中文化，字数累计几万。  
* ...

### 你想参与？（广告 2333）

欢迎各位对 Wine 开发感兴趣的朋友加入到
[wine-zh](http://www.freelists.org/list/wine-zh)
邮件列表进行交流，也可以私邮和我交流！特别欢迎大学低年级学生：

* 对于爱好编程的同学来说，Wine
项目就是一个充满乐趣的巨型玩具，计算机专业的大部分课程知识都可以在这里找到用武之地；  
* 如果你会 C 语言也会 C++，那就不能错过亲自动手用 C 语言实现 C++
运行库 Wine msvcp 的实战机会；  
* 如果你想了解浏览器工作原理，不如一起来实现 Wine builtin
IE，我们一起阅读讨论 gecko 内核代码；  
* 如果你想检验编译原理是否学得扎实，那就一起来改进 Wine 的
Javascript、VBScript 解释器；  
* 如果你嫌阿拉伯文太简单，如果你从右向左写字，如果你习惯 45 度仰望天空
90 度横看屏幕，那么 Wine 项目的多国语言字体渲染和文本排版难题在等着你；  
* 如果你觉得汇编太好玩根本停不下来，何不一起把 Wine 移植到各种架构？
然后没有然后... XD

如果你不嫌罗嗦，我们的排比句可以写五百行，因为 Wine 项目有 500
多个模块，总有一个对你的胃口...

我们的愿望就是：

pian  ni   tiao  jin   zui  xian   e   de   da   keng

帮   你   找   到   最    好    玩   的   课    题

* 还有，如果你想参与 Wine 的 Google Summer of Code 的话，嘿嘿 ;)

---  
谨以此文，献给对开源世界有贡献的前辈、朋友！
