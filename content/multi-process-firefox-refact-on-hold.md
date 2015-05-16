Title: 多进程 Firefox 开发暂缓
Date: 2011-11-21 22:41
Author: lovenemesis
Category: News
Tags: Firefox
Slug: multi-process-firefox-refact-on-hold

Mozilla 经过最近的讨论，将 Firefox 按照多进程方式重构的项目 Electrolysis
(E10S) 计划暂缓，转而通过一些见效更快的方式改善用户界面响应。

Electrolysis (E10S)
的主要目的是**改善界面相应时间**，主要通过以下两点实现：

-   将用户界面绘制进程和内容绘制进程分离开。
-   改善垃圾回收机制。

同时还有一些次要目标：

-   对于多核系统的支持。挑战： **现阶段 DOM 依然是单线程的**。
-   改善内存管理。
-   崩溃保护。
-   沙箱安全。

目前 **Firefox for Android
已经完全实现了多进程**，但是桌面版本的重构难度比预期的要大，尤其是**如何保证原有的扩展还可以在多进程模式下正常工作**这个问题还没有比较好的解决方法。结合其他因素，
Mozilla
决定将有限的资源调整到其他可以在短期内实现的改善界面相应时间的措施上，包括：

-   优化自在 Firefox 3.6.14 起实现的进程外插件管理(Out of Process
    Plugin)。
-   Places 优化(Places-optimization)。
-   递增式垃圾回收。

Mozilla
方面认为通过优先实现以上改善，可以**更快的使最终用户体会到在界面响应方面的进步**。另一方面，多进程
Firefox 项目 Electrolysis (E10S) 将暂缓，但不会取消。

[多进程 Firefox
重构详细目标](http://blog.mozilla.com/products/2011/07/15/goals-for-multi-process-firefox/)

[英文原文](http://lawrencemandel.com/2011/11/15/update-on-multi-process-firefox-electrolysis-development/)

**PS：**貌似很多 JavaScript 的大牛的都吐槽 DOM 是网页应用性能瓶颈啊……
