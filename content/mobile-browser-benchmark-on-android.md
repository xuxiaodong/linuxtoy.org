Title: Android 平台三款移动浏览器测试
Date: 2011-04-03 13:18
Author: lovenemesis
Category: Featured
Tags: Android, Firefox, Opera
Slug: mobile-browser-benchmark-on-android

无论您中意于哪款主流网页浏览器，在 Android
平台上总能找到那个熟悉的面孔。本文将考察这些浏览器在移动平台上的表现。

**测试平台**

[Sony Ericsson Xperia
Neo](http://www.sonyericsson.com/cws/products/mobilephones/overview/xperia-neo?cc=gb&lc=en):

-   Android 2.3.2 系统
-   Qualcomm MSM 8255 1 GHz Scorpion + Adreno 205 GPU
-   RAM 512 MB

**测试项目**

-   [Acid3](http://acid3.acidtests.org/)：网页标准测试，得分越高越好
-   [Sunspider
    0.91](http://www.webkit.org/perf/sunspider/sunspider.html)：来自
    webkit 的 JavaScript 测试，**用时越少越好**。
-   [V8 Benchmark
    v6](http://v8.googlecode.com/svn/data/benchmarks/v6/revisions.html)：来自
    Google V8 的 JavaScript 测试，**得分越高越好**。
-   [HTML5 Test](http://html5test.com/)：测试对 HTML5
    标准的兼容性，结果包括基础分(标准)+附加分(主要支持各厂商自行添加的)两部分，**得分越高越好**。

**评测浏览器**

-   Mozilla Firefox 4 for Mobile 4.0
-   Opera Mobile 11.00.1103311355
-   Android Browser 2.3.2(系统默认浏览器，类似 Google Chrome )

**Acid3 得分比较**

1.  **Firefox：97**
2.  **Opera：97**
3.  Browser：93

**Sunspider 得分比较**

1.  **Firefox：3215.6ms +/- 14.6%**
2.  Opera：5212.4ms +/- 55.3%
3.  Browser：5564.6ms +/- 3.3%

**Google V8 得分比较**

1.  **Browser: 241**
2.  Opera：170
3.  Firefox：*Crashed!*

**HTML5 Test 得分比较**

1.  **Firefox：235 + 9**
2.  Opera：234 + 8
3.  Browser：182 + 1

**总结**

从以上三款常见测试结果来看，Firefox for Mobile 4 有着明显优势，而 Opera
Mobile 则稳定在第二位。系统自带的 Browser 似乎并没有师出同门的 Google
Chrome 桌面版本的良好特性，除了在 V8
测试中获得高分以外，各种落后，尤其是在 Acid3 和 HTML5
测试中。不过这似乎也验证了进行新一代移动网页开发者对 Android
内置浏览器兼容性不良的诟病。

看完标准兼容性和速度比较，再来看看这些浏览器的功能方面的比较：

**Firefox**  
**亮点：**

-   继承了高度自定义的特性，有多达 150 款扩展满足各类需求。
-   创新的操作方式，特别适合多标签页浏览。
-   支持 Firefox Sync，实现在自己的多台设备上 Firefox
    书签、历史纪录、个人信息等同步。

**缺点：**

-   启动时间稍长，特别是当启用 Sync 历史纪录同步时。
-   目前不支持 Flash 播放。

**Opera**  
**亮点：**

-   颇具特色的九宫格快速启动界面
-   Opera Link：在多个 Opera 设备间实现 Firefox
    书签、历史纪录、个人信息等同步。
-   Opera Turbo：可以启用如同 Opera Mini
    一样的服务器端预处理压缩技术，节省流量。

**缺点：**

-   部分 Google 网页显示异常。

**Android Browser**  
**亮点：**

-   飞快的启动速度。

**缺点：**

-   多窗口浏览使用不便。

**FAQ**

1.  **Q：**为什么没有截图？**A：**当使用 ddms 对 Xepria Neo
    截图时，不知为何结果只有红色和绿色通道的信息，蓝色全无，导致非常难看。故未上截图。
2.  **Q：**为什么没有 Kraken Benchmark 的比分？**A：**无论用哪个 Kraken
    浏览器跑 Kraken 测试，用时都非常的长，于是作罢。
3.  **Q：**为什么没有 Dolphin HD/UC Web/Opera Mini/Maxthon
    的比较？**A：**它们准确来讲不属于浏览器，因为不具有自己的 HTML 和
    JavaScript 解析引擎。他们的网页显示通过以下两种方法实现：a)
    调用系统的 Browser，自己只是外壳。典型特点：在各种测试中得分和系统
    Browser 完全一致。典型代表： Maxthon 和 Dolphin HD；b)
    在其独有的服务器端对网页进行预处理，将结果发送至客户端显示。典型特点：各种测试无法运行或结果异常。典型代表：UC
    Web 和 Opera Mini。

