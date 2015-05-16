Title: Wine 1.2 正式发布
Date: 2010-07-17 15:46
Author: lovenemesis
Category: Emulator
Tags: Wine
Slug: wine-12-%e6%ad%a3%e5%bc%8f%e5%8f%91%e5%b8%83

时隔两年，开源的 Win API *Nix 实现 wine 今日发布了 1.2 正式稳定版本。

Wine 1.2 的相对于 1.0 的改进有：

**核心改进**

-   64位 Windows 程序运行支持。
-   区分仅可执行32位程序的 WINEPREFIX 和32/64兼容模式 WINEPREFIX 。
-   WoW64 文件系统和注册表重定向支持。
-   16位程序代码移至独立模块执行。
-   挂载模块可以识别 UUID。
-   注册表支持符号链接。
-   最近的 VC++ 运行库功能得到部分实现。

**用户界面**

-   内置程序图标全部得到更新。
-   支持动画指针，不过仅能显示第一桢
-   标准的“打印”和“页面预览”实现有改善。
-   添加了管理已安装程序的应用程序向导。
-   双向文字输入得到较好的改善，增加阿拉伯语支持。
-   RichEdit 实现得到改善，比如对于表格、URL检测的支持等。
-   改善常见控件的现实，比如日历、表格和列表视图。
-   部分实现文字输入服务，方便使用各类输入法。
-   增加了管理、导入和导出密钥和证书的界面。
-   改善了 wine 国际化状况。

**桌面整合**

-   实现 XDG 标准应用程序启动提示。
-   NET\_WORKAREA 得到支持，显示应用程序时会考虑 *nix
    系统的任务栏尺寸。
-   文件关联和 *nix 结合。
-   窗口管理支持 Alpha 通道。
-   程序正确相应 *nix 窗口管理器的最大化操作。
-   当程序需要唤起屏幕保护程序时会启动 XDG 屏幕保护。
-   开始菜单项当程序卸载后会被移除。
-   支持在 Windows 和 *nix 之间进行图片复制操作。
-   可以在 Windows 内启动一个外部的 *nix 浏览器。
-   绑定 msi 文件。
-   当屏幕适合时虚拟桌面会自动切换至全屏。

**图像**

-   实现利于 LCD 的次像素字体渲染。
-   图标 Alpha 通道渲染支持。
-   通过 windowscodecs 动态链接库实现 JPEG, GIF, PNG, BMP, ICO, 和 TIFF
    支持。
-   默认使用 GDIPlus 渲染。
-   DirectDraw 中支持层重叠。
-   通过 SANE 实现扫描程序支持。

**音频**

-   实现 openal32 接口，成为 *nix 平台上的 OpenAL 的 Wrapper。
-   通过 OpenAL 部分实现 mmdevapi.dll 声卡架构。
-   支持 GSM 编码。
-   ALSA 声卡模拟和 PulseAudio ALSA 模拟更好的工作。
-   音频 CD 数字回放支持。

**互联网和网络**

-   HTTP协议得到更多实现，譬如 Cookies 、IPv6 等。
-   Gecko HTML 渲染引擎得到升级。
-   远程调用支持服务器端授权，可以通过 HTTP 协议链接。
-   实现必要的 JavaScript 功能。
-   红外线网络传输在 Socket 层得到实现。
-   实现 inetmib1，可以使用标准 SNMP MIB 表。
-   实现 inetcomm，可以使用 POP3 和 SMTP 协议。
-   调用外部邮件客户端支持，以及对邮件附件的支持。
-   实现 shlwapi，改善 IE 使用。

**Direct3D**

-   FBO 成为默认的离屏渲染方式。
-   实现了大量的 dxd9 动态链接库。
-   Fog 管理得到改善。
-   多种 YUV 材质得到支持。
-   wined3d 采用线程级别管理方式处理 wine3d 和 opengl 程序。
-   显卡识别代码得到改善。
-   初步实现 dxd10 动态链接库。
-   阴影样品得到实现（星际争霸2）。
-   通过 Shader 实现贴片表面（半条命2水面效果）。
-   通过 shader 实现固定函数分块处理。
-   支持使用压缩材质的部分更新。
-   增加了大量 OpenGL 扩展支持。

[二进制包及源代码下载](http://www.winehq.org/download/)

[完整英文更新摘要](http://www.winehq.org/announce/1.2)
