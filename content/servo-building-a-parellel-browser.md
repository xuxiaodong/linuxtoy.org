Title: Servo: 构建并行化浏览器
Date: 2015-01-20 14:19
Author: lovenemesis
Category: Videos
Tags: Mozilla, rust
Slug: servo-building-a-parellel-browser

随着 Rust 1.0 Aplha 的发布，基于其编写的 Mozilla 下一代浏览器引擎 Servo
也逐渐明朗起来，有望在 2015 年看到 Alpha 版发布。

在当下正在奥克兰进行的 Linux.Conf.Au.2015 上，[Mozilla 的 Jack Moffitt
详细讲解了关于 Servo
的各个方面](https://www.youtube.com/watch?v=7q9vIMXSTzc)以及其相对于现有浏览器的提升。要点如下：

* Servo 引擎依然处于研究阶段，当下尚未确定何时会进入产品。  
* 高效且安全的 Rust 帮助 Servo 可以实现一些 C++ 难以实现的特性。  
* Servo 的开发主题是并行化，其中之一即是**DOM 并行化处理**。  
* Servo 目前已经基本通过 Acid2 测试，可以基本正常的渲染 Alexa
排名考前的网站  
* CSS 兼容性方面当下目标是 2015 年实现的依据普遍性排名前 50%
的特性，可以满足绝大多数网站的显示需求。  
* 整体浏览器架构方面，Servo 实现了统一化的 JavaScript/Rust 内存管理。  
* 良好的嵌入式支持，兼容 Chromium 嵌入式框架。  
* 初步实现 Firefox OS 及 Android 支持。  
* Servo 的网页渲染性能在单线程模式已经**仅需 Gecko
一半的时间渲染测试网页**，多线程模式性能更佳，超越当下全部浏览器。  
* 接下来计划在 2015 年发布一个 Alpha 质量使用 Servo
引擎的版本，注意其中 JavaScript 引擎及 Skia 渲染部分并非 Rust。  
* 另一方面，Gecko 中的部分模块将逐步开始用 Rust
重写，享受其带来的性能及安全性提升，首先实现的将是 bmp 解码器。

[主题演讲视频](https://www.youtube.com/watch?v=7q9vIMXSTzc)（朝内镜像稍后奉上）

*消息来源*：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=Mozilla-Servo-Engine-LCA2015)
