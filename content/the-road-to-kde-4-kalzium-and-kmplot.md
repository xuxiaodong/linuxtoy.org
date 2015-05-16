Title: 通向 KDE 4 之路（五）：Kalzium 和 KmPlot
Date: 2007-02-08 14:53
Author: toy
Category: Apps
Slug: the-road-to-kde-4-kalzium-and-kmplot

并不是所有的 KDE 4 程序开发还处于基础建设阶段，本周的主题是来自
[KDE-Edu](http://edu.kde.org/)
项目组中的两个应用程序：多用途化学相关软件
[Kalzium](http://edu.kde.org/kalzium/)，以及功能强大的数学方程式绘图程序
[KmPlot](http://edu.kde.org/kmplot/)，详述见下。

我们的诸多教学工具软件在 KDE 4
的整体发展中已经进行了很多的工作，在这其中 Kalzium 和 KmPlot
的进展又尤为迅速，它们的变化之大简直令人惊讶。

Kalzium（对应的德语单词是 Calcium）自 KDE 3.1
开始就是标准发行中的一个组件，现在它已经是 KDE-Edu
小组开发的众多程序中用户最多的产品之一。最初它只是一个用于显示化学周期表的程序，至多一旁再显示着几个如原子量、沸点这样的科学数据。但在不久之后，它逐步拓展加入了许多元素背景方面以及更多细节上的化学信息（如光谱图），这就使得它在化学相关的一些应用场合越来越实用。

在 KDE 3.5.5 中（这是我抓图时所用的版本，然而本周 3.5.6
也该发布了），Kalzium 在第一次启动时的样子是这样的。

[![Kalzium](http://i.linuxtoy.org/i/2007/02/vol5_355_kalzium_default_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_355_kalzium_default.png)

您可以发现这个界面相当简单，但却展示了很多的信息。如果您在任意元素上点击，还将会有更多的元素属性被陈列出来。

在 KDE 4 中，程序的主界面将会有所不同。除了 Qt 4
为我们引入了一些观感上的差异以外，还有些图标被改置到了工具栏（图中有些没显示出来）。在此让我们先窥视一下
KDE 4 开发分支下的 Kalzium 的模样。

[![Kalzium](http://i.linuxtoy.org/i/2007/02/vol5_4x_kalzium_default_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_4x_kalzium_default.png)

Kalzium 将来要达到的视觉效果会和图示的越来越接近。然而，在这 KDE 4
抓图中最值得瞩目的一点是工具菜单，在 KDE 3.5.5
中，这个菜单只包含“绘制数据”和“专业词典”两个项目（*译注：这里说错了，完整的工具菜单还应包括“化学方程式配平器”这条，但因
Ocaml 依赖的缘故这个功能在很多预编译包中都不提供*）。

“绘制数据”的用途是以多种模式来绘制一个元素的坐标图，例如可以基于质量、原子半斤、电负性等模式来工作。而“专业词典”则能给出许多常用化学专业用语的精确定义，不过上面提到的“电负性”一次似乎被遗漏了……总之，很显然这个程序还有充分的改进空间，而对于“专业词典”的改进将为
KDE 4 中的 Kalzium
提供一个能促进非程序员的化学爱好者也能为其作出贡献的良好契机。

不管怎么说，还是让我们先回过来看看一些新的工具，我将着重介绍这些新开发出的东西，它将使
Kalzium 在 KDE 4 中变得更加有用。

新的 Kalzium
将有一个同位素表能为您显示出一份同位素的清单及其衰变模式──假设我是一名地质师，认识到钾-40
这种物质通常会因为电子俘获而产生衰变可是非常重要的事项。

新的化学方程式配平器也相当值得一用，正如现在的 Kalzium 项目开发领导
Carsten Niehaus 给我们带来的这张抓图所显示的那样：

[![Kalzium](http://i.linuxtoy.org/i/2007/02/vol5_4x_kalzium_solver_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_4x_kalzium_solver.png)

基本上您只需要在配平方程式时写上正确的字母，您所期待的相应数字就会被程序反馈出来。在高中的化学授课中，学生往往被要求手动去解出一连串的方程式，但就像大多数方程式那样，一旦您解过很多方程式，会感到这种任务越来越乏味，这种时候这个方程式配平器将会为您节省下很多本该用于处理那些复杂的方程式的时间。

最后，未来的 Kalzium 最值得注意的改变莫过于 Kalzium
里的三维效果，程序会藉此拥有一个三维的分子查看器。这个机制本来是由
Kalzium
的开发者所设计并打算只用于这个程序，但是一些协作开发者也将其纳入了
libavogadro 函数库，这样 Kalzium 和 Avogadro
的开发者将会一起共同研发这个特性。

根据 Kalzium 开发者们当前的进度描述，现在要做的事是通过 libavogadro
函数库去移植 3D 建模器，Donald Curtis 正致力于这项工作，这将提供一个基于
Qt 和 OpenGL 的更通用更强大的分子渲染生成引擎，工作成果将被 Kalzium 和
Avogadro （或许更多）共同享用。Avogadro
是一个更高阶的分子建模程序，可被用于创建真实的分子文件以及量子化学领域，Kalzium
3D 将只是单纯地作为一个能查看此程序所构建的图像的查看工具。

Kalzium 的开发者 Benoît Jacob 提交了一幅抓图来展现使用了 Kalzium 3D
功能的三维分子查看器工作状况预览。在本文发表时，此功能已经进入了 SVN
代码仓库，当然它是和 libavogadro 函数库集成运作的。

[![Kalzium
3D](http://i.linuxtoy.org/i/2007/02/vol5_4x_kalzium3d_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_4x_kalzium3d.png)

Kalzium 以后有可能会和一批由 BlueObelisk
项目提供的常见分子数据共同发布以供您查看，感谢 OpenBabel
项目，它可以帮助我们能去打开一大批各种各样的分子文件格式（据统计已支持文件格式就达
62 种）。

现在轮到了下一个 KDE-Edu
成员：KmPlot。正如现在已知的那样，此应用程序具备绘制一般函数图、参数函数图还有极坐标函数图的能力，还有一些衍生的显示功能和的其它趣味特性。它是一个颇有用的的方程式绘图工具，只是现有的界面未免太拙劣了，甚至还有很多凌乱的对话框会充填屏幕空间。

下面您所看到的是 KDE 3.5.5 中使用默认设定的 KmPlot
启动界面，上面已经绘制了三个函数，每个的形状都不同：

[![KmPlot](http://i.linuxtoy.org/i/2007/02/vol5_355_kmplot_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_355_kmplot.png)

这个对话框是用于撰写像上面的那样要绘制的函数式的，不过对每一个函数形状都会有一个独立对话框。

[![KmPlot](http://i.linuxtoy.org/i/2007/02/vol5_355_kmplot_dialog_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_355_kmplot_dialog.png)

这里还有一张新版 KmPlot
的界面一瞥，上面同样绘制了那三个函数图，不过不会再有那么多对话框来占据空间，而且加上
Qt 4 提供的精致的反锯齿触感，这些线条甚至可以和方形一样平滑！

[![KmPlot](http://i.linuxtoy.org/i/2007/02/vol5_4x_kmplot_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_4x_kmplot.png)

对 KmPlot 的工作现在正紧锣密鼓地开展，我们相信它将会成为 KDE 4
的杀手级程序之一，无论是学生还是工程师还是其他人都有理由喜欢上它。现在它甚至可以绘制微分函数，而且拥有了一个新设计的函数编辑器，并且会为您提供如何校正函数式的即时提示（如上图所示）。

新的函数编辑器如下图所示，对微分函数的编辑支持也包含其中：

[![KmPlot](http://i.linuxtoy.org/i/2007/02/vol5_4x_kmplot_editor_s.png)](http://i.linuxtoy.org/i/2007/02/vol5_4x_kmplot_editor.png)

如您所见，现在输入函数式会比以往更加简单，当您在操作时函数编辑器还会实施友好的语法检查。在本文中还有许许多多
KmPlot
的进步没有被提到，如果您有兴趣了解更多消息，请查阅这个[开发状态页面](http://edu.kde.org/kmplot/development.php)。

总的来说，KDE-Edu
还是一个成长中的项目，许多优秀的应用程序是涵盖了各个年龄层的开发组的产物，它们还需能支持
Windows 和 Mac 操作系统，要感谢 Qt 4 的改进与 KDE 4
类库能让这些程序更加大众化。现在，还有不少很棒的工作在不断取得进展，请期待以后的文章为您带来更多的
KDE-Edu 软件巡礼。

原文：[The Road to KDE 4: Kalzium and
KmPlot](http://dot.kde.org/1170113778/)  
译文：[通向 KDE 4 之路（五）：Kalzium 和
KmPlot](http://www.myswear.net/forum/viewthread.php?tid=7825)

（Troy Unrau／文 千里孤坟 ／译）
