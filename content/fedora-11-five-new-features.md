Title: Fedora 11 5大新功能简介
Date: 2008-11-25 13:13
Author: lovenemesis
Category: News
Tags: Fedora
Slug: fedora-11-five-new-features

发现大家对这些前瞻性的东西比预想的要感兴趣啊～个人经常看这方面的文章，但觉得太过前瞻就没翻译……好吧，今天就从
Fedora 11 的5大新功能开始吧！

**DeviceKit**  
DeviceKit is
是一个简单的系统服务，可以用来实现以下三个功能：1）列举出设备;2）当添加或拔出设备时发出信号；3）提供将设备信息和设备本身结合的方法。它被设计用来部分的取代
HAL 以超越其在设计上的一些局限。

除了 DeviceKit 本身， 还有一个名为 DeviceKit-disks
的系统服务用来与块设备保持联系。DeviceKit-disks 还有一个图形前端
palimpsest。还有一个用来替代 HAL 中电源管理部分的 DeviceKit-power。

此外，将会有一个 nautilus 扩展，支持格式化磁盘。

**多座支持** （感谢 ganloo指教！）  

简化多座系统的配置，可以让两个或更多的用户使用自己的键盘、显示器和鼠标相互独立的在一台计算机上工作。这个跟
Multi-Pointer X 不一样。后者是允许在一个用户同时使用多个 X
输入设备，比如多个鼠标。

**增量软件包支持 (Presto)**  
presto 插件可以让 yum 下载 deltarpm
（增量RPM包，只包含相比已有旧软件包不同的部分）并本地生成新软件包。如果默认提供该插件的话，将会显著降低用户更新时下载的数据量。

**音量控制**  
让音量控制更加直观和便于使用。使用 libcanberra
对音频进行集中式管理，以实现1）将音量控制的变化直接反应到 PulseAudio
默认输出混音器的变化山；2）显示蓝牙耳麦等热拔插设备的状态；3）对麦克风的基本检查；4）依据一定的规则对多音频流进行管理（比如将音乐通过音箱播放，而将VoIP电话通过耳机播放）；5）将混音器
applet 转变成音频状态图标，以避免一些由于 applet 可能导致的问题。

**Windows 跨平台编译**  
在 Fedora 平台下就可以编译和测试全功能的 Windows 应用程序。Fedora MinGW
计划目标是减少 Windows 应用程序开发者将跨平台的库文件从 Linux 迁移到
Windows 下所花费的精力。这样子会带来两方面好处：一是开发者不用费劲与
Windows 平台上那些私有版权的编译软件们打交道，直接可以在 Fedora
下使用开源的编译器，最大程度减少对 Windows
的使用；二是从长远看来，这会提高 Windows
平台上开源软件的整体水平。因为在 Linux 平台上编译 Windows
程序方便了，通常使用 Linux 的开发者们也可以像对 Linux
下的程序那样最快的对错误反馈做出相应，而不用将时间浪费在调试 Windows
平台的编译器上了。
