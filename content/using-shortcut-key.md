Title: 使用你喜欢的快捷键
Date: 2009-08-06 19:06
Author: toy
Category: Tips
Slug: using-shortcut-key

{ 撰文/wxqy }

Google 的 Glen Murphy 写了 WinXP 下的 Chrome 的一个 hack，使用 CapsLock
来新建标签。这里给出 Linux 下的替代方法，而且可以推广到其它程序。

我使用的管理器是 Sawfish。利用 Sawfish 中的函数 synthesize-event
和系统程序 xmodmap 可以如下实现：

将下列代码加入 .xmodmap


    remove Lock = Caps_Lock
    keycode 66 = XF86New

再在 Sawfish 中定义函数 send-event-to-window-if-match


    (defun send-event-to-window-if-match (class-regexp event else-event)
     (lambda (w)
       (interactive "%W")
       (if (string-match (window-class w) class-regexp)
           (synthesize-event event (input-focus))
           (synthesize-event else-event (input-focus)))))

和函数 rebind-key


    (defun rebind-key (class-regexp orig-event sim-event #!optional replacement)
     (bind-keys window-keymap orig-event
                (send-event-to-window-if-match class-regexp sim-event orig-event))
     (if replacement
         (bind-keys window-keymap replacement
                    (send-event-to-window-if-match class-regexp orig-event replacement))))

现在，我希望用 XF86New，也就是 CapsLock，来新建标签，只需重新绑定键：


    (rebind-key "^Chrome$" "XF86New" "C-t")

如果我想在 Chrome
中用不常用的键“`”来关闭标签，并用“Ctrl-`”输入字符“`”，只需绑定：


    (rebind-key "^Chrome$" "`" "C-w" "C-`")

同理可以应用到其他程序中。
