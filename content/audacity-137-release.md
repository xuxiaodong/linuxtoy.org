Title: Audacity 1.3.7 发布
Date: 2009-02-01 12:07
Author: lovenemesis
Category: Audio Converter
Tags: audacity
Slug: audacity-137-release

跨平台的免费声音编辑器 Audacity 于1月28日发布了最新的 1.3.7 正式版本。

该修正版本在稳定性和可用性上有显著的提升，尤其是在 Mac OS X
上。同时也带来了一些新功能，包括对于 Windows 上 DirectSound 设备的支持。

**所有平台上 Bug 修复包括：**

-   静音/单声道化 导致输出立体声文件时错误的声道
-   尼奎斯特效果：在粘帖未修改音频时没有进度条，取消时会损坏当前音频
-   噪音消除：在粘帖未修改音频时会产生额外的尾部过滤
-   未压缩输出：
    1.  覆盖文件的 WAV 输出导致损坏
    2.  同时输出多个未压缩音频将只能生成 16-bit WAV
-   压缩输出：
    1.  MP3
        输出现在可以生成正确的比特率模式、质量和长度，以及在播放器中更直观的元数据信息
    2.  WMA 输出现在包含正确的元数据信息
-   恢复 Audacity 使用多声道录音设备录制多于两声道音频的能力

**平台相关的 Bug 修复**

-   Windows Vista：修复当没有音频启用和连接时打开首选项崩溃的问题
-   Mac OS X 和 Linux：
    1.  修复虚假剪辑，标签命名和运行特效后没有热键
    2.  项目采样率现在会随着首个导入文件的变化而变化
-   Mac OS X ：
    1.  修复不活动或者损坏的菜单和隐藏的对话框，无法探测便携配置以及不能设置独立命令和控制热键的问题
    2.  添加 FFmpeg 安装包

**新功能**

F11 全屏模式，高质量的 "Sliding Time Scale/Pitch Shift" 特效，
音频对比析波器

Windows: 现在可以用更有效的DirectSound API 打开声音设备

**其他变化**

做为改善延迟修正的第一步，现在应用了一个修复，而不是更多的修正

众多的界面修复和改善

[英文原文](http://audacity.sourceforge.net/)  
[下载](http://audacity.sourceforge.net/download/)
