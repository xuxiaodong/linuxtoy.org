Title: Fcitx 4.1的开发进度
Date: 2011-06-02 16:40
Author: lovenemesis
Category: Input Method
Tags: Fcitx
Slug: fcitx-41-progress

小企鹅输入法 FCITX 当前维护者 @csslayer
正在将Fcitx的一个个功能都移植到新的框架下面。

现在以下功能都**将成为独立模块**：

-   module/chttrans （简繁转换）
-   module/punc （标点转换）
-   module/quickphrase （快速组词）
-   module/vk （虚拟键盘）
-   module/x11 （x相关功能）
-   module/autoeng （自动英文模式）

其实并没有增加什么新的功能，除了简繁转换我**增加了opencc支持**之外（感谢
byvoid1）。

主要目的是想让再Fcitx上进行开发变得更加容易，同时也会**整理一份全新的文档**出来。

另外也让支持一些功能（例如 GTK IM MODULE
这类）变得容易，还有将图形功能从核心中剥离，使得移植到其他系统能变得更加简单一些。

还有一个比较重大的变化就是我把 fcitx 的 makefile 已经**全面移植到
CMake** 上面了。

等到恢复了大部分原有功能后就会把这部分修改 push 回google
code，现在这部分代码还躺在我自己的 bitbucket 里面。

现在基础的界面其实只移植了输入窗口，因为扩展性增加的缘故使得皮肤的设置需要有改变。还差主界面，虚拟键盘，kimpanel，fcitx-remote，4个功能没有移植到新的框架下面。当完成了前两个之后就会
push 回 google code，到时候欢迎大家测试。

如果你真的想试试（其实真没什么好试的），可以到这里clone
`https://bitbucket.org/csslayer/fcitx-personal`

**以上内容摘自 [@csslayer
个人博客](https://www.csslayer.tk/wordpress/fcitx-dev/fcitx-4-1-dev/)**。
