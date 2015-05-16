Title: GNU Octave 3.8
Date: 2014-01-02 09:11
Author: lovenemesis
Category: Development
Tags: octave
Slug: gnu-octave-3-8

开源的数值计算工具 [GNU
Octave](http://www.gnu.org/software/octave/index.html) 已经发布了 [3.8.0
版本](http://ftp.gnu.org/gnu/octave/)。*感谢 [Alick
Zhao](https://fedoraproject.org/wiki/User:Alick) 来稿*

该版本的新特性包括：

-
搭载了广受期待的图形用户界面。它应该已经可以较好的运行，不过还没到达开发者期待的完好程度，所以还不是默认的用户界面。  
- 绘图默认使用 FLTK 控件，并使用 OpenGL。如果没有 OpenGL 或者 FLTK
支持，仍然会使用 gnuplot 绘图。  
- 支持嵌套函数，与 MATLAB 的作用域规则兼容。  
- 对命名异常 (named exception) 提供有限支持。  
- 正则表达式接受全部的 MATLAB 正则选项，以与 MATLAB
兼容的方式处理单引号括起来的模式串中的反斜线转义序列。  
- 实现了 FLTK 的 TeX
解析器，默认用于包括标题和坐标轴标签等的任何文本对象。这一支持只用于显示器显示，不用于打印。  
- plot 目录中的 m 文件大修，现在的绘图输出和 MATLAB 视觉上接近兼容。  
- kurtosis, moment 函数与 MATLAB
兼容，分别返回峰度（而非超值峰度）和中心矩（而非原点矩）的值。  
- 添加了 citation 命令，可以显示如何在文献中引用 Octave 及其包的信息。  
- Octave Forge 的 java 包现在已经是 Octave 核心的一部分。

更完整的变更列表可见于[此页面](http://www.gnu.org/software/octave/NEWS-3.8.html)。

消息来源：[GNU Octave](http://www.gnu.org/software/octave/index.html)
