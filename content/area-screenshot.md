Title: Area Screenshot
Date: 2011-12-28 00:02
Author: lovenemesis
Category: Desktop Stuff
Tags: gnomeshell
Slug: area-screenshot

或许你已经使用过 GNOME Shell
默认屏幕录像工具(`CTRL+ALT+SHIFT+R`)，那么也可以体会下这款提供高级截图功能的
GNOME Shell 扩展 Area Screenshot。

前往 [Shell Extensions 即可安装 Area
Screenshot](https://extensions.gnome.org/extension/61/area-screenshot/)，非常简单。

之后需要额外配置下快捷键，这里以推荐的 SUPER+PRINT (常见键盘上 SUPER
即是 WIN 键)为例：

`key='/apps/metacity/global\_keybindings/run\_command\_10'`  
`gconftool-2 -s --type string "$key" 'Print'`

之后当**按下 SUPER+PRINT
组合键**的时候就进入截图模式了。此时可以**拖拽出一个矩形区域**，**松开鼠标**即可完成截图。亦可**按下数字键
1 ～9**启动倒计时器，代表等待 1～9
秒后再进行截图，过程中会在左下角读秒，从而实现对于普通截图工具做不到的弹出菜单截图。若再次按下
0 则关闭倒计时器。

截图默认保存在 `$HOME/Pictures` 目录下。

此外在截图完毕后还会尝试运行位于 `$HOME/bin/` 下的名为
`area-screenshot-post` 的 Bash 脚本 ，于是可以**自由定义截图后的行为**。

[项目 Github
首页](https://github.com/DASPRiD/gnome-shell-extension-area-screenshot)
