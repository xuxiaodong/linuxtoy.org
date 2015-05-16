Title: Firefox OS 架构简析（1）
Date: 2012-08-27 15:21
Author: lovenemesis
Category: Embedded
Tags: firefoxos
Slug: firefox-os-architecture-brief-1

十个月前，[本站首次报道 Mozilla B2G
系统](http://linuxtoy.org/archives/mozilla-boot-to-gecko-os.html)。现在它已经成长为
Firefox OS，是时候去看看的它的架构了。

[本文脱胎自 B2G 官方 Wiki
页面](https://wiki.mozilla.org/B2G/Architecture)，略过了其中代码示例的部分。为了方便理解，在部分描述时会跟当下流行的
Android 操作系统进行比较。

**女神、壁虎和娃娃**

Firefox OS 从架构上来讲具有了三个层面：

**Gaia（盖亚，大地女神）**：**Firefox OS
的用户界面**，包含了在开机之后所有用户能看到部分，比如锁屏、主屏幕、应用程序启动器、拨号器、短信、相机等等作为智能手机必须具备的。Gaia
完全使用 HTML、CSS 和 JavaScript 编写，使用成为[标准的 Web
API](http://linuxtoy.org/archives/webdriver-api-is-about-to-be-standardised-by-w3c.html)
的接口和底层设备关联。因此，Gaia 可以在任何实现了 Web API
的设备上运行，比如桌面浏览器。Firefox OS
上的第三方程序也是以类似的方式运行并与 Gaia 共存的。

**Gecko（壁虎）**：**Firefox OS 的应用程序运行时环境**，用
C++（不知道后期是否会转用 [Rust](http://www.rust-lang.org/) ）实现了 Web
API，供包括 Gaia 在内的应用程序使用，同时保证 Web API 可以在 Firefox OS
的目标硬件平台上运行。于是乎 Gecko
包含了必要的网络层，图像层、布局管理和 JavaScript 虚拟机以及移植层。

**Gonk（蛋形娃娃）**：**Firefox OS 的操作系统底层**，也是 Gecko
的一个目标移植平台，包含 Linux 内核和用户态的硬件抽象层，这一部分和
Android 以及嵌入式 Linux 共享了很多组件和驱动，比如 bluez, libusb
等。说是一个目标移植平台，是由于 Gecko 抽象层在理论上也可以运行在
Android 或者桌面操作系统上，不过由于 Firefox OS 项目主导了 Gonk
开发，可以提供一些其他系统上不具备的接口给 Gecko
使用，比如完整的电话通讯层。

**光、信号和起源**

和绝大多数 Android 手机一样，预装 Firefox OS
的手机在开机后也会首先由极小化的 `bootloader`
实现最初的引导操作，然后链式引导更高级别更复杂的引导器，最终实现内核的加载。这个过程具体如何与设备制造商有关，相应的
bootloader 操作很有可能重用现在各个厂商在 Android 设备上所用的私有
`fastboot` 协议实现。意味着只要适当调整 Firefox OS 所用的引导器，**在
Android 手机上使用现有刷机工具刷入 Firefox OS 在技术上没有障碍**。

由于嵌入式领域还比较封闭，这个过程也会加载很可能是**设备相关的私有调制解调器固件**。于是乎在这个层面上
Firefox OS 和 Android 一样不是开放的。

紧接的故事就是 Linux 内核的载入和 PID 1 号 `init`
进程的产生了，和一般嵌入式 Linux 的初始化没有太大差别。这里使用的 Linux
内核会紧随上游，不过也会吸纳厂商通过 [Android Open Source
Project](http://source.android.com/)
提交的一些尚未合并的设备相关代码。内核载入之后的大多数设备访问将通过
`sysfs` 的方式供用户态程序访问。

**爬行动物时代**

在这里，`b2g` 以主系统进程的形态被 init 进程激活，并通过 RPC 或者 Socket
的方式实现和其他负责诸如网络、无线电等功能的进程通讯。除此之外，`b2g`
还会通过 `dbus-daemon` 和 IPDL 这两种特殊的方式实现用户态进程间通讯。

[dbus](http://www.freedesktop.org/wiki/Software/dbus)
不用赘述，用过任意一个现代桌面 Linux
发行版的用户对其都不陌生~~最近合并入了
[systemd](http://freedesktop.org/wiki/Software/systemd/)
成为其一部分，不过依然可以单独运行~~。[IPDL](https://developer.mozilla.org/en-US/docs/IPDL)
则是 **Mozilla 特有的进程间通讯协议定义语言**，允许在 C++
进程间安全且有组织的传递消息。运行着 `libxul.so` 的`b2g` 进程将使用
[IPDL](https://developer.mozilla.org/en-US/docs/IPDL)
启动一系列**内容子进程**，上层的网页程序和其他网页内容将在独立的内容子进程中运行，在技术上和现在
Firefox 浏览器的标签页处理类似。

面对多媒体文件， Gecko 对于 OGG Vorbis 音频, OGG Theora 视频和 WebM
视频这些**开放格式将提供原生支持**，以后正式发布时为了 WebRTC 引入对
[Opus](http://hacks.mozilla.org/2012/07/firefox-beta-15-supports-the-new-opus-audio-format/)
的支持也是完全有可能的。而对于私有格式将通过
[libstagefright](https://github.com/cgjones/android-frameworks-base/tree/gingerbread-b2g/media/libstagefright)
的方式访问私有解码器和实现硬件加速。

**感触、表现和尾巴**

Gecko 负责将来自 Gonk 的各种输入事件解析成可供标准网页程序使用的 DOM
事件，包括按键、触屏操作等等，源自标准 Linux 输入设备
input-device。这些来自 Gecko 的 DOM API 由在 C++ 和 JavaScript
之间的外部函数接口和对象模型组成，使用普遍的
[XPIDL](https://developer.mozilla.org/en-US/docs/XPIDL) 规定。

网络通讯则分别交由 `wpa_supplicant` 和 RIL(Radio Interface Layer)
完成。和桌面 Linux 发行版一样，wpa\_supplicant 负责 WiFi
环境下的接入，Gecko 为其开发了附属的 `WifiWorker.js` 供网页程序了解 WiFi
连接状态。RIL 则负责广域网络的通讯，其中负责跟调制解调部分沟通的 `rild`
很可能是来自制造商的私有代码，`rildproxy`
则是一个为了安全考虑而设置的中间代理，起到连结 `rild` 和 `b2g`
的作用。同样，也有 `ril_worker.js` 暴露状态和操作接口供上层程序使用。

和 Android 4.0+ 类似，**Gecko 完全使用 OpenGL ES 2.0 实现混合**。Gecko
会将页面的各个区域绘制入内存缓冲，然后调用 OpenGL
命令将内容混合并渲染于屏幕上。和 Android 早期借助 skia
实现的软件混合相比，Firebox OS 从一开始就依赖于 GPU
的渲染能力，其效果值得期待。

在 Gecko
的最底层则是负责和目标系统交互的移植层。在这一部分包含针对不同目标系统的平台相关代码(Gonk，Android，OS
X 等)，并将其统一化为可供 Gecko 上层子系统使用的 C++ API。

*更多内容敬请期待*
