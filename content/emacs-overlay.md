Title: 求指教：关于 emacs overlay 的反射机制
Date: 2013-02-23 08:23
Author: Kardinal
Category: AskLinuxtoy
Slug: emacs-overlay

好像还没有人在这里发过求助贴，所以我决定挑战一下。

回到问题上来，简单的说，有一个 overlay ，设置了 keymap
属性，在触发其中的按键时，如何获得当前的 overlay？

不要告诉我看文档，文档我看过，可能是我英文不太好的缘故，我没有找到相关内容。

研究了一下 tempo-snippets 代码，似乎它只是查找符合条件的 overlay
中最近一个；试着看了下 yasnippets
的代码，说实话，看不太懂……特别是那独特的用斜杠分隔的命名方式，让我某处很疼……貌似也是基于
overlays-at 或者 overlays-in 搜索的

其实这种全面撒网的做法也不是不行，通常情况下效率也可以接受，但是它不靠谱，有木有有木有？

说说我的方式：overlay 的几个
hook，定义回调函数时，提供了几个参数，其中有一个 overlay 参数就是当前
overlay；但是只有在改动 overlay
内容的时候，才有可能调用。所以我定义了一对互逆修改，然后返回这个
overlay，因为修改是互逆的，所以也相当于没有改动，代码如下：

    (defun get-overlay()
      (interactive)
      (save-excursion
        (save-restriction
          (insert " ")
          (backward-delete-char 1)))
      current-overlay)

然后定义一个回调函数，加到 hooks 中：

    (defun this-overlay (overlay after-p beg end &optional length)
      (setq current-overlay overlay))

然后就可以在 define-key 的代码中调用 get-overlay 了。

这种方式可以说绝对靠谱，但是缺点也明显：

1.需要使用全局变量传递引用，可以说非常不安全（而且在词法作用域下可能需要特殊处理……而
emacs 正在打算支持词法作域……）

2.虽然看不出来，但是实际上还是对 overlay
进行了无意义的修改，可能对流程造成不可预料的影响

待续……
