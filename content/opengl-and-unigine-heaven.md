Title: OpenGL 和 Unigine Heaven
Date: 2010-03-26 11:01
Author: toy
Category: News
Tags: OpenGL, Unigine Heaven
Slug: opengl-and-unigine-heaven

{ 撰文/Guest }

近日 Khronos 工作组同时发布了 OpenGL 的两个主要的新版本 OpenGL 3.3 和
OpenGL  
4.0。由于 Linux 上的 Mesa3D 对于 OpenGL 3.0  
还没有正式的支持，所以也没什么好写的。不过随着各大厂商的开发，OpenGL  
相关的新闻也攒了不少，就放在一起介绍一下吧。

**OpenGL 3.3 和 OpenGL 4.0 发布**

OpenGL
史上头一次的两个主要版本的同时发布。按照[这篇文章的介绍](http://rastergrid.com/blog/2010/03/a-brief-preview-of-the-new-features-introduced-by-opengl-3-3-and-4-0/)，
4.0 标准主要对应了支持 Shader Model 5.0 的硬件（NV4xx、ATI5xxx），而 3.3
则主要对应了支持 Shader Model 4.0 的硬件。这篇 Blog 中作者个人的说法是：

> we got an API that is a really competitive alternative for
Microsoft’s DirectX API。

这篇 Blog 中有着 OpenGL 4.0
中新特性的较为详尽的介绍，篇幅很长，内容也比较深入，就不一一翻译了（主要还是因为看不懂）有兴趣的可以去看看。

**Unigine Heaven demo**

与之相对应的就是 Unigine Heaven demo，这个 demo 是
Unigine（虚幻竞技场，Unreal  
引擎）公司用来秀最新显卡技术的花哨程序，支持  
DX 11、DX 10、OpenGL。最重要的特性就是  
tessellation，基于显卡的网格细分，想必已经被 DX  
相关的各种新闻介绍的差不多了吧。这个 demo 的 tessellation 部分只有 DX
11  
的显卡（外加 Win7 上的 DX 11）才能跑。近日，Unigine Heaven 2.0
已添加了基于  
OpenGL 3.2 的渲染引擎，官方已经给出了 [Linux 版的 demo  
下载](http://unigine.com/download/)。

除 tessellation 部分不能展示外(tessellation 在 4.0
中才是核心标准)，根据  
Phoronix 的评测  
和  
  
已经 "seems to be in rather good shape"。在 OpenGL 4.0
中，tessellation  
成为核心标准，因此 Unigine Heaven 的 Linux 版在之后也可展示
tessellation  
技术。与之相对应的就是 ATI 发布了支持 OpenGL 4.0 的驱动，也包含了
[Linux
版](http://support.amd.com/us/kbarticles/Pages/Catalyst-OpenGL-preview-driver.aspx)。

暂未测试 Unigine Heaven demo 2.0 的 Linux 版，不过 Phoronix 上放出的
Linux 版截图和我在 Windows 上看到的 Unigine Heaven demo 1.0 效果，可以说
Unigine 引擎已经毫无疑问成为了 Linux 下 OpenGL 3D
引擎的霸者了（虽然他不开源）。

PS: Linux 下另一个 3D 引擎王者就是 ID software 了，其早期的 Quake3  
引擎开源后派生出了 N 多的 FPS 游戏和引擎，后期的 Doom3 在 Linux
上游戏效果与  
Windows 下无异，也算是我这种支持 Linux 又想玩花哨游戏之人的福音啊。  
另外作为一个 OpenGL 的支持者，也顺便鼓吹一下： 对于 OpenGL  

而言，硬件的新特性即使是在新版本规范未发布之前，也是可以通过扩展机制来支援的。比如  
tessellation。有兴趣的人可以去查查 OpenGL  
官网上[扩展注册的网页](http://www.opengl.org/registry) 上 tess
开头的几个扩展，看看都是几年前注册的。

另外附带一个[链接](http://www.gamasutra.com/blogs/DavidRosen/20100108/4051/Why\_You\_Should\_Use\_OpenGL\_And\_Not\_DirectX.php)，  

[原文地址（现已不能访问）](http://blog.wolfire.com/2010/01/Why-you-should-use-OpenGL-and-not-DirectX)。个人的看法是
OpenGL 的走位也是很猥琐的，众多新技术（通常是仅有 ATI 或 NVIDIA
中的一家支持）通过扩展支持后，并不纳入核心标准，而新版 DX
的发布，则总是带着超前于硬件的配置要求。等这些技术真正被各大厂商统一支持了，
OpenGL 再将其纳入核心标准（总感觉像是 dota
火枪在补最后一刀？），从近几年显卡发展中较为重大的几项技术飞跃 shading
language (DX 9，OpenGL 2.1)，Geometry shader (DX 10,OpenGL
3)，Tessellation (DX 11,OpenGL 4.0)来看都是如此。

当然 OpenGL 这样做也是有道理的，作为工业标准最重要的是稳定。OpenGL 3
中，为最大限度释放新显卡能力，去除老旧标准中过时的思想和模型，提出了
core profile 的概念，在此 profile 中标为 deprecation
的函数将不再有效，但同时也提供了 Compatibility profile，此 profile
中仍保持前向兼容。事实上 ATI 和 NVIDIA 都支持 Compatibility
profile，也就是说即使是基于 OpenGL 1.0
代码基础开发的程序，也一样可以加入新显卡技术的支持（DX
中能否做到我不明确，大概是做不到。不过估计也没有人在基于 OpenGL 1.0
代码基础开发的代码上加入 OpenGL 4中的新技术吧）。

另外补充一句，OpenGL 和 DX 都是调用硬件功能的
API，硬件不支持的谁也不可能支持的好。差别可能就是思考模式了吧（这句纯属乱说，可以无视）。所以最重要的还是你的显卡好...当然也希望
Linux 下的 OpenGL 支持越来越好，让我们能有更好的 3D 体验；希望基于
OpenGL 开发的游戏（这类游戏大多跨平台）越来越多，让我们在 Linux
下更好的娱乐...

{ Thanks Guest. }
