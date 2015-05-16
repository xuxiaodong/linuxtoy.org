Title: GIMP 核心开发者之一 Martin Norholts 的专访
Date: 2008-12-30 12:14
Author: toy
Category: News
Tags: GIMP
Slug: interview-martin-nordholts-the-gimp

[撰文/Thom Holwerda 翻译/jcome]

高位深支持，非破坏性编辑（“效果”层）和色彩管理，是图像编辑的三个热点话题。这些用户长久期盼的特性已在
GIMP 安营扎寨了。Linux & Photography Blog 做了篇 GIMP
核心贡献者之一，[Martin Nordholts
的独家采访](http://jcornuz.wordpress.com/2008/12/27/an-exclusive-interview-with-martin-nordholts)。[Nordholts](http://www.chromecode.com/)
讲到了一些重要的事情的当前进度，深入解释了在 GIMP（包括
GEGL）内部的变化，揭开了将要发生的变化的神秘面纱的一角。

通过整合
[GEGL](http://www.gegl.org/)，提供高位深支持和非破坏性编辑。GEGL，通用图像库（Generic
Graphical Library），是基于图表（Graph）的图像处理框架。“GEGL
提供满足非破坏性图像编辑的基本结构”，GEGL 网站解释说，“通过
[BABL](http://gegl.org/babl/)
提供超宽范围色彩模式和像素存储格式的支持，以供输入和输出”。GEGL 也扮演给
GIMP 带来高质量的色彩管理流程的角色之一，但是要得到这个特性，对 GIMP
的核心也要做许多的工作。

Nordholts 解释说，其实 GIMP
已经拥有一个完全能够提供高位深和非破坏性编辑的核心了，但是重要的是收养代码，这样用户可以完全使用这个当前还是孤立的核心。他说，“推测一个完工的准确时间是不可能的，也是没有意义的。我们唯一能够确定的是所有工作都在有条不紊的进行，而且最终会完成。”

对于高位深问题，Nordholts 认为 GIMP 遗留的每个通道 8 bits
的代码也不需要重新编写，而是用 GEGL
来替换。为了在新的框架中提供遗留（Legacy）组件的支持，要编写一些封套（Wrapper）。“但这并不是真正意义上的代码重写”，“对于位深问题，我不觉得有什么大的挑战，要做的只是写代码”。

另外一个普遍的抱怨是，GIMP 混乱的，而且不够直觉化的多窗口界面。Nordholts
说相关工作也在进行中，“讨论了很多的单一窗体，标签式（tab）界面，或许会引起大家的兴趣”。*(感谢
gimper!)*

[via
[OSNews](http://osnews.com/story/20701/Interview_Martin_Nordholts_the_GIMP)
& [Fedora 中文用户组](http://bbs.fedora-zh.org/showthread.php?t=868)]
