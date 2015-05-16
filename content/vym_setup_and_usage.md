Title: 头脑风暴软件 FreeMind 的替代品：View Your Mind（VYM）
Date: 2006-07-26 17:42
Author: toy
Category: Tutorials
Slug: vym_setup_and_usage

[FreeMind](http://freemind.sourceforge.net)
在头脑风暴软件领域已经很知名了，但为什么还要选择 [View Your
Mind](http://www.insilmaril.de/vym/)（简称“VYM”）？假如你和我一样曾经对
FreeMind 的安装充满困惑的话，那么将不难回答前面的问题。在我看来，VYM
的安装更为简单，不会像 FreeMind 那般令人过分地担心所谓的依赖问题。而且
VYM 的兼容性很好，虽然是一个 QT 应用，但是在 Gnome
中同样运行良好；更重要的是，VYM
没有恼人的中文显示及输入问题。在目前，VYM 可以说是我的 Ubuntu 环境中
FreeMind 的最佳替代品。

[![VYM](http://i.linuxtoy.org/i/vym_s.png)](http://i.linuxtoy.org/i/vym.png)

**一、安装 VYM**

如果你不打算从源代码编译 VYM，那么我建议你下载 RPM 包：

`wget http://easynews.dl.sourceforge.net/sourceforge/vym/vym-1.8.1-suse-10.0-i586.rpm`

在 Ubuntu 中安装 RPM 包，需要先将其转换为 DEB 包：

`sudo alien -d vym-1.8.1-suse-10.0-i586.rpm`

现在可以使用 dpkg 指令来安装：

`sudo dpkg -i vym_1.8.1-1.1_i386.deb`

**二、使用 VYM**

首先，你可以通过“应用程序->办公软件->VYM”来启动
VYM。我建议你此时花些时间来熟悉 VYM 的用户界面。

然后，我们开始一个 Map 的创建过程。

1.创建 Branch

在默认情况下，启动 VYM 即创建一个文档。这个文档包含已经创建的第一个
Branch：New Map。双击它可以进行编辑。按下“Ins”键来创建一个子
Branch。如果你需要在子 Branch 上再创建子 Branch，先选中子
Branch，再按“Ins”键即可。如果你要删除 Branch，则按“Alt+Del”。

2.添加状态图标

通过图标可以很形象的反映出一个 Branch 的状态。选中需要添加图标的
Branch，然后点选工具栏中的任意图标即可。

3.保存及输出

这样，一个简单的 Map
就创建完成了。现在你可以保存它，并将其输出为图片、网页、XML 等。
