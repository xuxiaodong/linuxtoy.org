Title: 关于 Qt 4.5 的二三事
Date: 2008-09-26 16:16
Author: toy
Category: News
Tags: Qt
Slug: about-qt-45

近读 Trolltech Labs Blogs，了解到关于 Qt 4.5
的几件事，个人感觉比较有意思，特此记录与诸位同好分享。

1.  **QGtkStyle 将成为 Qt 4.5 的一部分**

    我们知道，由于使用不同的接口（如
    Qt、GTK+），所开发出来的程序的外观界面也会大相径庭。挑剔的用户往往通过第三方程序来解决这个问题。例如，要使
    Qt 程序与 GNOME 环境中的原生程序的外观保持一致，有同学可能会使用
    [QGtkStyle](http://code.google.com/p/qgtkstyle/)。

    ![Clearlooks](http://i.linuxtoy.org/i/2008/09/clearlooks.png)

    好消息是，[QGtkStyle 将成为 Qt 4.5
    的一部分](http://labs.trolltech.com/blogs/2008/09/05/qgtkstyle-now-part-of-qt/)。毫无疑问，这使
    Qt 程序与 GTK+ 程序的外观无缝的达到统一。

2.  **透明的 widgets**

    记得第一次在 Linux 桌面中实现透明效果，使用的是一个名为 transset
    的小程序。当时的感觉相当好。后来，Compiz
    大行其道，透明效果的实现也变得越来越方便。

    ![Widget](http://i.linuxtoy.org/i/2008/09/argb_widget.png)

    因为某些驱动程序问题导致渲染上的 bug，Qt 不会默认使用 ARGB
    视觉，而提供一种可选的替代方案。只要有混合型窗口管理器运行，在 Qt
    4.5 中你能有[不错的透明效果 Qt
    widgets](http://labs.trolltech.com/blogs/2008/09/23/translucent-widgets-on-x11/)。

3.  **更多的字体配置设定**
    Qt 4.5 可能[将使用 Freetype 的
    filtering，并提供更多的字体配置设定](http://labs.trolltech.com/blogs/2008/09/01/subpixel-antialiasing-on-x11/)，包括
    lcd filter 和 hinting style。

