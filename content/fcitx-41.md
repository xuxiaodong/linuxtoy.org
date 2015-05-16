Title: 小企鹅输入法 Fcitx 4.1
Date: 2011-09-05 10:21
Author: lovenemesis
Category: Input Method
Tags: Fcitx
Slug: fcitx-41

小企鹅输入法 FCITX 4.1 发布。感谢 [CSSlayer
来稿](https://twitter.com/#!/CSSlayer/status/109862755607134208)。

主要更新有

-   移植到新的架构上，更易于扩展。
-   增加Android上的Google拼音移植，libgooglepinyin的支持。（fcitx-googlepinyin）
-   增加OpenCC做简繁转换引擎支持。
-   增加支援Fcitx所有拼音引擎的云拼音支持。（fcitx-cloudpinyin）
-   默认界面修改。支持竖排候选词列表，改善绘制性能。
-   增加与KDE整合的配置模块。（kcm-fcitx）
-   采用CMake作为构建系统，增加方便开发者的CMake宏。
-   增加GTK2，GTK3，QT4的输入模块，以期解决Firefox，GTK3，Flash等程序的输入问题。
-   增加窗口显示预编辑文本支持。（默认切换快捷键 Ctrl + Alt +
    P）以期解决Opera下面的光标跟随问题。
-   增加一个移植自默认界面的可选的界面，它以Xlib和Xft作为绘制后端。（fcitx-ui-light）
-   重新排列个人配置的目录结构。
-   增加对fbterm的支持。（fcitx-fbterm）
-   采用doxygen及docbook完善部分开发相关的文档。

另外手册内容有更新，[请参阅](http://fcitx.github.com/handbook)。

感谢
happyaron，lilydjwg，Houge\_Langley，poplarch，maomaol，OracXS，polong，wubuntust，Yue
Liu，以及其他我没有提到的人的测试及建议，没有你们的帮助就没有现在的Fcitx。

**已知问题（已在 Git 版本中修复，正在着手发布修复版本）：**

-   编译时会覆盖默认的LDFLAGS。
-   码表处于不调整频率时有一个性能问题（影响五笔字型）
-   含有拼音码表的码表候选词有顺序问题，以及无匹配自动上屏有一个判断问题以至于无法输入较长拼音（影响五笔拼音）。
-   用输入法输入时如果输入不会转换的半角标点不会进行选中第一个词的操作。

[消息来源](https://www.csslayer.tk/wordpress/fcitx-dev/fcitx-4-1/)
