Title: Linux 兼容内核 (longene) 0.2.3 版 (UnifiedKernel-0.2.3) 发布
Date: 2009-02-14 17:26
Author: toy
Category: News
Tags: Longene, unifiedkernel
Slug: linux-unifiedkernel-023

[撰文/linooxlee<[linoox.lee AT
gmail.com](mailto:linooxlee@gmail.com)>]

2009 年 2 月 12 日，Linux 兼容内核项目开发组正式发布了 Linux 兼容内核
0.2.3 版本。该版本在 0.2.2-1 版的基础上，将 Wine
的注册表管理机制整体移植到内核，使得应用程序运行效率有了一定的提高。

**兼容内核项目计划及项目进展：**

一、兼容内核项目是什么

兼容内核项目是一个开源的计算机操作系统内核计划，它试图利用 Linux
内核材料来构建一个 MS Windows 内核的替代品，使之在内核层面上高效地运行为
Windows 平台设计开发的应用程序和硬件驱动程序。

兼容内核项目由中国的浙大网新公司发起。兼容内核项目在 2005 年 9
月正式启动并开通官方网站。作为兼容内核项目的领导者，操作系统专家毛德操先生提出了兼容内核的技术设想和和开发路线。他写了一系列关于市场、知识产权和技术的文章阐述了为什么人们需要兼容内核和如何实现兼容内核。这些文章被汇编成兼容内核白皮书，作为兼容内核的纲领性文件。

根据兼容内核白皮书，为实现兼容内核需要将 Linux
的内核加以扩充，使其既支持 Linux 本身的应用和设备驱动，又支持 Windows
的应用和设备驱动，从而成为一个“兼容内核”。要实现这样一个内核，就得在
Linux 的内核中增添以下几部分内容：

1.  一个符合 Windows 设备驱动程序的特征和要求的框架，即 Windows
    设备驱动框架（WDM），使得可以把多个 Windows
    设备驱动模块装入内核，并使这些模块间的关系和运行条件跟它们在 Windows
    内核中时相同。
2.  一组由 Windows 内核导出 (Export) 函数界面 (见 Windows DDK)
    定义的导出函数。对于设备驱动程序而言，这些函数就相当于由内核提供的库函数。
3.  Windows
    的系统调用界面。微软并没有公开它的系统调用界面，但是在“Windows
    NT/2000 Native API Reference”和其他资料中已经揭开了这个秘密。在
    Linux 内核中实现 Windows
    的系统调用界面，就相当于用汇编语言来实现另一种高级语言。这是因为，在内核里面，可以使用的“砖块”就不再是宏观的
    Linux 系统调用，而是 Linux 的许多微观的内核函数了。

二、兼容内核可利用的技术资源

开发一个操作系统是相当困难的。考虑到 Windows
内核的复杂性和微软对其技术细节进行保密，开发一个兼容的操作系统在以前被认为是不可能的。但在当前开源和网络合作开发盛行的今天却为兼容内核带来了前所未有的机遇--兼容内核可以充分利用开源社区已经取得的成就和人才来达到自己的目标。

兼容内核主要的技术依托为 Linux Kernel、Wine、NdisWrapper 和 ReactOS
等。它们都是开源项目，源码公开可以自由取得。

Wine 是在 Linux 的用户空间构建 Windows 内核环境（wineserver），把
Windows 应用向 Windows 内核的系统调用等操作转向为对 Linux
的系统调用操作。除了仿真 Windows 内核，Wine 还仿制了大量核外的 dll
文件。Wine 项目已经运作了十多年，对 Windows
系统的运作机制和相关数据结构有较深的研究。这些数据结构和 dll
文件等兼容内核是可以直接加以利用的。

NDISWrapper 在 Linux Kernel 中实现了 Windows NT 内核的一些部件 – 包括
NTOSKRNL API（一个基本的 WDM 控制器）和一系列诸如 Wireless/NDIS/USB/PnP
的 Windows 调用转向 Linux API 的封装。NDISWrapper 不限于执行 NDIS
驱动，只要 WDM 驱动不调用未实现的 Windows API
也是可以运行的。因此可以认为 NDISWrapper 是一个 WDM
的雏形。兼容内核可以参考 NDISWrapper 和 ReactOS 的 WDM 实现构建自己的
WDM。

ReactOS 是一个 Windows 内核的开源仿制品。ReacOS
的开源代码为兼容内核提供了一个可资参考的样本。

Linux Kernel
中有非常丰富的内核构建材料，兼容内核可以使用这些材料构建系统调用内核函数。主要的方法包括：

1.  有些 Windows 系统调用可以嫁接到相应的 Linux
    系统调用。如键盘的输入输出等。
2.  有些系统调用可以部分地重用相应 Linux 系统调用的代码。
3.  有些系统调用在 Linux 中没有对应物，需要借助 Linux
    内核中的低层函数予以实现。

由于兼容内核是利用 Linux
内核材料构建自身功能模块的，因此能保持比较小的体积，而不是 Linux 内核与
Windows 内核的简单相加。

三、兼容内核开发路线

兼容内核不采取一步到位、而采取逐步逼近的策略。对于 Windows
系统调用部分它以 Linux+Wine 为起点，兼容内核开发自身的功能模块来替代
Wine 的功能模块。兼容内核每实现一个功能就对 Wine 打相应的补丁，使得
Windows 程序转向使用兼容内核的功能。可以表示为：

IF （兼容内核实现了该功能）  
使用兼容内核功能模块  
Else  
使用 Wine 的功能模块（wineserver 移入核内空间以提高效率）  
Endif

即 (Linux + Wine) => … => … => (Linux’ + Wine’)。起点 Linux+Wine
显然是可以运行的，开发过程中的每一步都实现一组有限的目标，每一步的结果都应该是一个可以运行的、更逼近
Windows 的、可以发行的版本。

对 Linux 内核的修改原则上以动态安装模块的形式实现，尽可能不改变 Linux
内核原有的代码，必要时才打一下补丁。这有利于保持原 Linux 内核的稳定。

对于设备驱动支持部分兼容内核以 NDISWrapper 为起点，通过扩充和替换
NDISWrapper 功能模块和增加 Windows API 支持来实现设备驱动的装入和运行。

四、兼容内核项目进展

兼容内核已经实现了 Windows
系统的进程/线程管理、对象管理、虚拟内存管理、进程间同步管理和注册表管理等
Windows
系统的基本机制。文件系统整合工作也已经完成正在进行测试并在以后的版本发布。

五、竞争项目

Wine、ReactOS 和兼容内核的目标都是兼容 Windows
应用和驱动软件，它们是互相竞争的项目。由于兼容内核的起点高其竞争力明显强于前两者。

虽然 Wine 1.0 已经可以运行近万个 Windows 应用软件，但它在用户空间模拟
Windows（把调用 Windows API 转向为调用 Linux
API）的技术特点决定它效率低下，兼容性难以进一步提高。由于在用户空间运行，除了实现一些简单的
USB 打印机驱动外，在驱动上基本没有什么作为。终究 Wine
只是一个应用而不是操作系统。它不具有取代 Windows 的能力。而且 Wine
所取得的进步可以被兼容内核利用。

ReactOS 项目是由俄国人主导的开源项目，目标是开发一个开源的 Windows
内核。令人佩服的是它的开发基本上是从零开始的！这个项目的进展很快，现在
0.3.8 版已经可以运行好些 Windows 应用了。不过，考虑到 Windows
内核的复杂性，ReactOS 离实用还是有相当大的距离—当 Wine
和兼容内核已经借助 Linux 内核使用各种各样的设备时，ReactOS
还在为未能支持声卡和 USB 键盘而苦恼。预计 ReactOS 要到 0.4 版才能实现
USB 的支持（把 Linux 的 USB 驱动移植到 ReactOS，这工作已经做了很久）。

兼容内核的起点比较高，是继承 Linux
内核资源的基础上进行发展的。操作系统在管理资源的实现上虽然不尽相同，但原理是大同小异的，兼容内核所做的只是补上
Windows 内核与 Linux 内核之间的差异，工作量比 ReactOS
小的多，而且即使是对于这些差异也可以利用和借鉴现有的开源代码资源，包括
Wine、ReactOS 等。

六、前景

随着技术的发展预计三到五年内将会出现功能和现在主流电脑基本相当但价格在一千元以内的低端计算机。低端机的竞争非常激烈，每台机厂家的利润也就
100 元以内，因此难以承受 Windows 高昂的价格。作为 Windows
的替代品的兼容内核将能在这个细分市场取得较大的份额。

下载地址：  
<http://www.longene.org/fileDownload.php?id=32&page=download>

兼容内核官方网站：  
<http://www.longene.org/index.php>

兼容内核 Wiki：  
<http://en.wikipedia.org/wiki/Linux_Unified_Kernel>

Linux
兼容内核白皮书（关于兼容内核的必要性、知识产权问题、开发路线和技术方案）：  
<http://www.longene.org/whitepaper.php>
