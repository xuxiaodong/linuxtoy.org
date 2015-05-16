Title: 灵异 Emacs 之画皮
Date: 2011-10-19 06:04
Author: Kardinal
Category: Tips
Tags: Emacs
Slug: emacs-buffer-face-mode

标题起得有点大了!

好吧，这回真的是一个小技巧，我以本站站长的名誉担保……如果你觉得我撒谎了，你可以把站长找出来随意处置……(神秘的声音：偶们是无辜的，找
Kardinal 就行)

话说比较讲究的同学，都喜欢给 emacs
设置个漂亮的字体，一般都是矢量字体，大黑二黑三黑啥的，就不点名了，你懂的……

可是这样也有麻烦的时候，比如说我最近比较爱玩的 eshell ，或者版本控制的
diff 界面之类的……总之，有些情况下，用点阵字体又比较舒服点

虽然说使用其它编辑器的时候我从来没有奢求过使用两种以上的字体，可谁让咱用的是
emacs 呢

很简单，M-x buffer-face-mode
，成功了吧，字体变了吧，狠过瘾吧，这是一个小技巧吧……我代表站长感谢大家捧场!!!  

    git clone git@github.com:ran9er/init.emacs.git

  

再次感谢您继续观看，我也继续了[init.emacs.gz](http://linuxtoy.org/img/2011/10/initemacs.zip)  

[![](http://linuxtoy.org/img/2011/10/eshell1.png)](http://linuxtoy.org/img/2011/10/eshell1.png)

有多们同学不明白为什么要用点阵……这样说吧，矢量字体的小字号通常不太美观……你可能接着又会问为什么要用小字号……因为有的缓冲区用来输出程序生成的内容，都是一大坨一大坨的，这个时候就可以用小点的点阵字体了;也可能你写程序要用等宽字体，而写情书用不等宽字体……像那句著名的台词说的，这些都是策略，而我提供的是机制-\_\_-!!

    (set-face-attribute 'variable-pitch nil :font "宋体-12" :fontset "fontset-standard")

现在 M-x buffer-face-mode，就能看到真正在效果了， buffer-face 默认使用
variable-pitch 在设置，所以不用直接设置 buffer-face。

    (dolist (hook '(
                    eshell-mode-hook
                    help-mode-hook
                    magit-mode-hook
                    dired-mode-hook
                    vc-mode-line-hook
                    diff-mode-hook 
                    ))
      (add-hook hook (lambda () (my-buffer-face-mode))))

给你需要的模式添加 buffer-face-mode ，这里有一个限制条件是，这个模式得有
hook 。有些模式就没有。比如我想给 buffer-face-mode 的 hook
里再写两句调整行距，却发现没有这个 hook ……

所以，你应该注意到了，上面那段最后一个词是 my-buffer-face-mode ， 而不是
buffer-face-mode 。  
把其它的一些设置写在这面就行了

    (defun my-buffer-face-mode()
      (buffer-face-mode)
      (make-local-variable 'line-spacing)
      (setq line-spacing 4)
      )

line-spacing 是一个全局变量，得先把它设置成本地变量，不然所有的 buffer
都受影响。凡是全局变量都如此设置，比如 scroll margin 之类的

ok，如果你是一个追求完美的人，要给每一种模式都设置一种字体，也不是没有办法

    ;先弄一张皮
    (make-face 'your-face)
    ;倒饬下这张皮
    (set-face-attribute 'your-face nil :font "宋体-10")

然后 (buffer-face-set 'your-face)，就可以了，加在 hook 哪的都可以
