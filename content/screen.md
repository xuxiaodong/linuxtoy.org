Title: Screen：Shell 孵化器
Date: 2006-10-18 10:29
Author: toy
Category: Apps
Tags: Screen
Slug: screen

[Screen](http://www.gnu.org/software/screen/)
这个东东真的够酷、好玩、十二分地有意思，而且也是相当地实用。Screen
就像一个 Shell 孵化器，只需一个 Shell，在 Screen
的神奇作用下，“道生一，一生二，二生三，三生万物”，想要多少个 Shell
都可以。当然，前提是只要你愿意。有了
Screen，再也不需要同时打开多个终端或者多个标签页了。还有更加好玩的在后头，在
Screen 孵化的 Shell
中执行任务，即便是你退出终端，仍然不会对它造成任何影响。稍后，同样可以再次进入
Screen 的世界。

如果你从来没有安装过 Screen，那么就执行 `sudo apt-get install screen`
吧。然后，在终端中输入 screen 就启动 Screen
了。按照提示按空格键或回车键开始我们的 Screen
快乐之旅吧。现在，你可以随便执行某些命令来测试，如：ls -l。接着，我们就用
Screen 来孵化一个新的 Shell，同时按组合键 ctrl-a
c，同样的，你能够在这里执行命令，我们假如是 ps
aux。加上最初的，那么现在在 Screen 中就有两个 Shell
了。可是，如何在这两个 Shell 间切换呢？试试 ctrl-a ctrl-a
看？是不是很方便地切换回来了呢。假如你要退出，甚至关掉终端，那么好吧，按
ctrl-a ctrl-d，屏幕会显示
[detached]，你就放心的关终端吧。是的，在玩了一圈之后，你又想进入 Screen
了，怎么办？只需输入 `screen -r` 即可。

以下总结一些常用的 Screen 操作快捷键，供大家参考：

-   ctrl-a c：创建一个新的 Shell
-   ctrl-a ctrl-a：在 Shell 间切换
-   ctrl-a n：切换到下一个 Shell
-   ctrl-a p：切换到上一个 Shell
-   ctrl-a 0...9：同样是切换各个 Shell
-   ctrl-a d：退出 Screen 会话

Happy Screen!!!
