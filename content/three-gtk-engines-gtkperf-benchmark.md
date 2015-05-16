Title: 三套 GTK 引擎 GTKPerf 比较
Date: 2009-10-16 06:45
Author: lovenemesis
Category: Featured
Tags: GTK+, Murrine, nimbus, nodoka
Slug: three-gtk-engines-gtkperf-benchmark

GTK 引擎作为 GNOME 图形环境的基石，对于 GTK
程序的渲染具有重要影响。本文将在 Fedora 11 平台上比较 Nodoka、Murrine 和
Nimbus 引擎在 GTKPerf 下的表现。

**测试平台：**

AMD Turion 64 X2 TL-58 1.9GHz

Nvidia GeForce 8400M G 128M

Apacer DDR2 800 2G*2

Fedora 11 i686 Kernel 2.6.30.8-64.fc11.i686.PAE

Nvidia Official Binary Driver 190.36

**测试工具：**

使用官方源安装 GTKPerf 0.40 ，比较在 Test Round 为 1000 时 Test All
各引擎的用时。

[Nodoka](https://fedorahosted.org/nodoka/): 0.7.2 Fedora Theme

[Murrine:](http://www.cimitan.com/murrine/) 0.90.3 Blue Crystal Theme

[Nimbus:](http://dlc.sun.com/osol/jds/downloads/extras/nimbus/) 0.1.4
Nimbus Theme

**测试结果：**

首先是 Fedora 默认的 Nodoka ：

GtkPerf 0.40 - Starting testing: Wed Oct 14 23:58:31 2009

    GtkEntry - time:  2.17
    GtkComboBox - time: 14.84
    GtkComboBoxEntry - time: 10.23
    GtkSpinButton - time:  3.59
    GtkProgressBar - time:  2.39
    GtkToggleButton - time:  1.70
    GtkCheckButton - time:  0.67
    GtkRadioButton - time:  1.46
    GtkTextView - Add text - time: 20.78
    GtkTextView - Scroll - time:  9.59
    GtkDrawingArea - Lines - time:  2.50
    GtkDrawingArea - Circles - time:  4.26
    GtkDrawingArea - Text - time:  4.27
    GtkDrawingArea - Pixbufs - time:  0.92

---

**Total time: 79.44**

下来是支持 RGBA 的 Murrine:

GtkPerf 0.40 - Starting testing: Wed Oct 14 23:52:00 2009

    GtkEntry - time:  1.66
    GtkComboBox - time: 23.66
    GtkComboBoxEntry - time: 13.11
    GtkSpinButton - time:  3.39
    GtkProgressBar - time:  2.50
    GtkToggleButton - time:  3.57
    GtkCheckButton - time:  1.32
    GtkRadioButton - time:  2.33
    GtkTextView - Add text - time: 21.10
    GtkTextView - Scroll - time:  9.33
    GtkDrawingArea - Lines - time:  4.21
    GtkDrawingArea - Circles - time:  4.39
    GtkDrawingArea - Text - time:  4.34
    GtkDrawingArea - Pixbufs - time:  0.95

---

**Total time: 96.09**

最后是来自 Sun OpenSolaris 的 Nimbus：

GtkPerf 0.40 - Starting testing: Wed Oct 14 23:48:53 2009

    GtkEntry - time:  1.66
    GtkComboBox - time: 14.92
    GtkComboBoxEntry - time:  8.73
    GtkSpinButton - time:  2.37
    GtkProgressBar - time:  0.97
    GtkToggleButton - time:  1.19
    GtkCheckButton - time:  0.78
    GtkRadioButton - time:  0.99
    GtkTextView - Add text - time: 21.44
    GtkTextView - Scroll - time:  6.23
    GtkDrawingArea - Lines - time:  2.74
    GtkDrawingArea - Circles - time:  3.95
    GtkDrawingArea - Text - time:  4.56
    GtkDrawingArea - Pixbufs - time:  1.00

---

**Total time: 71.80**

**总结：**

从结果可以看出 Nimbus 的总所用时间最短，但只比 Fedora 默认的 Nodoka
快了不到8秒， Murrine 则以20余秒的差距位于最后。

不说明什么， just for fun。 GTK
引擎主要还是跟个人喜好有关，则其所好即可。欢迎补充更多引擎的比较～

注意 GTKPerf 测试会受到系统硬件和驱动程序的影响。

本文得到
[ShareItem.org](http://shareitem.org/archive/murrine-aurora-candido-engine-performance-contrast.html)一文的启发，特此表示感谢。
