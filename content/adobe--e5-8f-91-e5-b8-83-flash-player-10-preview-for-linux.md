Title: Adobe 发布 Flash Player 10 Preview For Linux
Date: 2008-05-16 11:45
Author: lovenemesis
Category: Apps
Tags: Adobe, Flash
Slug: adobe-%e5%8f%91%e5%b8%83-flash-player-10-preview-for-linux

5月15日，Adobe发布了遵循 OpenFlash 项目技术开放标准的 Adobe Flash Player
10 的Linux预览版。这次的发布也是Adobe 首次同步发布 Windows, Mac OS X 和
Linux 系统下的Adobe Flash Player。

Flash Player 10 包含了众多新功能及错误修正：

-   **创新的表现形式**
    -   可自定义的滤镜和特效
    -   3D 特效
    -   新的文本渲染引擎
    -   文本模块层架构
    -   提升了绘图 API
    -   色彩管理
-   **强化视觉效果**
    -   支持 GPU 混合加速
    -   支持 GPU Blitting(? 这个完全不知道该怎么翻译，望指教)
    -   新的抗锯齿引擎 Saffron 3.1
    -   矢量数据类型
-   **富媒体**
    -   动态流传输
    -   RTMFP (Real Time Media Flow 协议)
    -   Speex 音频解码包
-   **其他社区强烈要求的功能**
    -   文件引用
    -   动态声音生成器
    -   大尺寸图片支持
    -   上下文菜单
    -   GB18030 兼容支持
    -   Ubuntu 系统支持

以下是已经发现的**仅与 Linux 平台**相关的Bug：

-   阴影渲染有时会返回 NaN 而不是一个 Number
    值。(不懂Flash富客户端开发……)
-   GPU
    混合加速功能无法和带有混合特效的窗口管理器共同使用，如Compiz(**会导致CPU占有率偏高**)。
-   在订阅 Speex 格式的流媒体会导致播放器挂起。

发布说明见[这里](http://labs.adobe.com/technologies/flashplayer10/releasenotes.html)。

下载见[这里](http://labs.adobe.com/downloads/flashplayer10.html)。

PS：在本人自己编译的Mozilla Firefox 3.0rc1 X86\_64
上的情况是全屏无法启用……

附：如何在 Fedora 8 X86\_64 位系统下使用安装Adobe Flash Player。

1.  下载下来.tar.gz格式的软件包，解压缩，忽略安装脚本，得到
    libflashplayer.so 。
2.  根据你的 Firefox 本身是32位还是64位的，拷贝到相应的位置。

-   如果你使用的是直接从Mozilla网站上下载的版本，那么就是32位的，不管你的系统本身是32位还是64位的。原因
    Firefox 的“关于”部分会这样标明 i686(X86\_64)。只需要直接将
    libflashplayer.so 拷贝到 firefox/plugins/ 目录下即可完成安装。
-   如果是操作系统自带的 Firefox 2.0，那么把 libflashplayer.so 拷贝到
    /usr/lib64/mozilla/plugins/ 目录下，然后以 root 用户运行
    mozilla-plugin-config ，此时在 /usr/lib64/mozilla/plugins-wrapped/
    目录下应该能找到生成 nswrapper\_64\_64.libflashplayer.so
    ，安装完成。
-   如果是自己编译的 Firefox 3.0rc1，在以上基础上得到
    nswrapper\_64\_64.libflashplayer.so 文件，然后拷贝到
    $PREFIX/plugins/ 目录下即可。

