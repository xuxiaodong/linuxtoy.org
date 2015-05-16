Title: Awesome 提示三则
Date: 2008-09-30 09:09
Author: toy
Category: Tips
Tags: Awesome
Slug: awesome-tips

与使用 Awesome 的同学分享三则提示。注意，本文以 Awesome 3.0
为准。如果你还不知道 Awesome 是何物的话，那么我推荐你阅读 Kardinal
的文章《[平铺式窗口管理器——Awesome](http://linuxtoy.org/archives/awesome.html)》。下面言归正传。

1.  **呼出命令提示框**
    按 Win + F1 可以呼出命令提示框，在 Run:
    后输入相关命令可以立即执行程序。这个命令提示框也是支持 Tab
    补全的，可以省去输入长命令的麻烦。如果要取消执行，则可以按 Esc。
2.  **更改状态栏的高度**

    Awesome
    默认的状态栏看上去有点肥，如果你想要一个更苗条的状态栏，那么可以通过修改配置文件实现。具体的步骤是，打开
    rc.lua 文件，找到：

    `mystatusbar[s] = statusbar({ position = "top", name = "mystatusbar" .. s,`

    将其修改为：

    `mystatusbar[s] = statusbar({ position = "top", height = "16", name = "mystatusbar" .. s,`

    这里的 height 就是用来控制 Awesome
    状态栏高度的，你可以根据自己需要调整。

3.  **窗口操作**
    有时候我们想移动窗口的位置，或是调整窗口的大小。在浮动布局中，Win +
    鼠标左键可以移动窗口的位置，而 Win + 鼠标右键则可以调整窗口的大小。

补充一条：默认的 rc.lua 有定义 Mod4\_Ctrl\_Space 将窗口设成
floating。[感谢 邱焜 读者]
