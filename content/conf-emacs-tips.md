Title: 配置 Emacs 的小技巧
Date: 2011-10-09 18:05
Author: Kardinal
Category: Text Editor, Tips
Tags: elisp, Emacs
Slug: conf-emacs-tips

前几天……大约在冬季吧，我发现了一个惊天小技巧，当然，是关于 Emacs
的……看到标题你也应该懂得

这事要从很久以前说起，我很久以前用 Vim ，很久很久以前用 Emacs
，很久很久很久以前用 Vim ……你懂得，我也不知道我到底在多久以前用 Emacs
或者 Vim…… 后来，出了个叫 Vimim
的东东，输入法再也不用担心我的切换了。然后，我就舒坦了一段时间……然而，Vim
并不太适合折腾，它的脚本语言也让我想起了恐怖的 shell script
……可能它执行效率挺高，但是，你懂得，咱们的口号是“不求效率，但求折腾！”

相对而言，Elisp 的S表达式看起来要舒服多了，但是 Emacs
的快捷键让我的手指很纠结……注意，这里的纠结表示的是动作，而不是心情。你可以参考这个例句：像麻花一样纠结。

回归正题，这个惊天小技巧就是，把 Caps Lock 和 Control
两个键换过来！我指的是软方法，就是不抠键的情况下互换；相对应的，也有硬方法……先别忙找螺丝刀……买
Emacs 脚踏板先

好了，现在正式讲关于“配置”的小技巧。  
(好吧，这里贴出的格式都一塌糊涂，还是打包上传吧
[initemacs7z1](http://linuxtoy.org/img/2011/10/initemacs7z1.zip)
。。。这个包里面，很容易找到的东西我都删了。。。你懂得)

Emacs 的启动文件，大家通常用 dotemacs ，也就是 .emacs \_emacs
。如果你把配置文件分成多个文件，一般会把它放到一个文件夹里，通过
dotemacs 文件读取。这样，你就多了一个文件还有一个夹，是不是挺郁闷？用
windows 的同学，哪儿凉快到哪儿去找 dotemacs

其实在 site-lisp 目录下的 site-start.el
文件作用也差不多，不过它是全局的，而且在 dotemacs 之前启动。

这是我的 site-start.el 文件

    (unless (boundp 'init-dir)

      (setq
       init-start     (time-to-seconds)
       init-dir       (expand-file-name
                       (if (eq system-type 'windows-nt)
                           (concat exec-directory "../init.emacs/")
                         "~/init.emacs/"))
       null           (dolist (init-lp (directory-files init-dir t "^_"))
                        (when (file-directory-p init-lp)
                          (add-to-list 'load-path init-lp)))
       init-files     (mapc 'load (directory-files init-dir t "\.el\\\\'"))
       init-stop      (time-to-seconds)
       )

      (add-hook 'emacs-startup-hook 
                '(lambda ()
                   (message "load %d init file , spend %g seconds ; startup spend %g seconds" 
                            (length init-files) 
                            (- init-stop init-start) 
                            (- (time-to-seconds) init-start))))
    )

  
这个文件里面，用 (time-to-seconds)
获得三次时间，然后计算出加载启动文件所用时间和整个启动过程所用时间。

dolist 那部分把 init-dir 里面以 “\_” 开头的文件夹添加到 load-path 。

"(mapc 'load (directory-files init-dir t "^[a-zA-Z0-9].*el$"))" load
所有 init-dir 里面以 el 结尾的文件。

为什么要 boundp 呢？因为我总是习惯把 site-start.el 文件的原件放在
init-dir ，而 site-lisp
里面的那个我认为它是副本。。。这样一来，site-start.el 会不停的 load
site-start.el ，然后。。。你懂的。。。

开始的时候，我把过滤条件改为
"^[0-9].*el$"，但是这种逃避的态度不够爷们。。。后来我又加了个判断，像这样  

    (mapc '(lambda(ifile)
             (unless (member (file-name-nondirectory ifile)
                             '("site-start.el"))
               (load ifile)))
          (directory-files init-dir t "^[a-zA-Z0-9].*el$"))

  
但是这太纯爷们了，你懂得。。。偶然在哪里看到个 if \_\_name\_\_ ==
"\_\_main\_\_" ，茅塞顿开，心里那个舒坦。

我设置的 init-dir 在 linux 下为 "~/init.emacs/"
……特别感人的一点是，如果没有 init-dir ，它也不会报错。

你可以修改文件名前面的数字，按照指定的顺序读取，比如我的 init-dir
里面的文件为 \_load-path\_dirs/ dirs/ 00\_xxx.el 01\_xxx.el 02\_xxx.el
。。。。秀一下我的init-dir 目录

    00_func.el  01_init.el  02_settings.el  03_outline.el  04_dired.el  05_ido.el  
    06_viewmode.el  07_session.el  08_modeline.el.bak  09_hl-line.el.bak  10_run-file.el  
    11_addons.el  12_auto-complete.el  13_yasnippet.el.bak  14_auto-complete-yasnippet.el.bak  
    18_VsnCtrl.el  21_linum+.el.bak  22_color.el  33_keybindings.el  54_gui.el  55_font.el  
    60_tabbar.el  66_sdcv.el  68_novel.el  77_dev.el.bak  80_gnus.el.bak  81_rss.el.bak  99_test.el
      site-start.el  _color-theme/  _misc/  _sandbox/  auto-complete/  git-emacs/  rss/  yasnippet/ ......    

禁用其中的文件的话，推荐给它加个 bak
后缀，而不是重命名……其实加后缀就是重命名了……我的意思你懂得

在 dired 模式下按 b 就可以了……如果按 b 没有反应的话，在 04\_dired.el
文件中添加：  

    (autoload 'dired-update-file-line "dired-aux" "" t nil)
    (add-hook 'dired-mode-hook (lambda ()
      (local-set-key "b"
                  '(lambda () "rename file to .bak"
                     (interactive)
                     (let* (buffer-read-only
                            (suffix "bak")
                            (from-file (dired-get-filename))
                            (new-file 
                             (if (string-equal suffix (file-name-extension from-file))
                                 (file-name-sans-extension from-file)
                               (concat from-file "." suffix))))
                       (rename-file from-file new-file)
                       (dired-update-file-line new-file)
                       )))
     ))

我的 init-dir 目录里第一个文件是 **00\_func.el**
，定义一些函数，每个函数下面的注释为示例[funcel](http://linuxtoy.org/img/2011/10/funcel.txt)

**我的 01\_init.el 文件**  

    ;; * working dir
    (setq sand-box (expand-file-name "_sandbox/" init-dir))
    (cd sand-box)

    ;; * 打开特定文件时使用 View 模式
    (add-hook 'find-file-hook
              '(lambda ()
                 (when
                     (and
                      (file-exists-p (buffer-file-name))                ; 已存在文件
                      (member (file-name-extension (buffer-name))
                              '("el" "bak" "txt")))                     ; 匹配扩展名
                   (view-mode)
                   )))
    ;; 其实各种 hook，也是列表，可以用 C-h v find-file-hook 查看里面的内容。

    ;; * max
    (setq max-lisp-eval-depth   1000        ;lisp最大执行深度   500
          max-specpdl-size      10000       ;最大容量           1000
          kill-ring-max         1024        ;kill ring          60
          undo-outer-limit      5000000     ;撤销限制           12000000
          mark-ring-max         1024        ;mark ring          16
    )

    ;; * Common
    (setq message-log-max         t        ;完整的 message-log
          inhibit-startup-message t        ;关闭起动时闪屏
          initial-scratch-message          ;初始内容
          (purecopy "  
   ;; In sandbox
    "))

    ;; * 文件编码
    (setq buffer-file-coding-system 'utf-8-unix)

**02\_setting.el**
文件里是一些乱七八糟的设置，我完全相信你可以弄的比我还要乱……自由发挥吧

值得注意的是 setq setq-default 都可以设定多组值，很多同学可能不知道  

    (setq-default                   ; 使用空格缩进 
            indent-tabs-mode nil    ; t 使用 TAB 作格式化字符  nil 使用空格作格式化字符
            tab-always-indent nil
            tab-width 4)

可以指定某字符的类型，比如 \_ [ ] 指定为单词的一部分；具体情况 C-h s  

    (modify-syntax-entry ?_ "w")
    (modify-syntax-entry ?[ "w")
    (modify-syntax-entry ?] "w")

**03\_outline.el**  

    ;; * 设定主题
    (set-display-table-slot
     standard-display-table
     'selective-display
     (let ((face-offset (* (face-id 'shadow) (lsh 1 22))))
       (vconcat (mapcar (lambda (c) (+ face-offset c)) " [...] "))))

如果你想自定义 outline 的层级关系，比如 *** 是 * 的上一级，可以定义
outline-heading-alist ，不过里面的东西必须是 outline-regexp
中定义过了的  

    (add-hook 'diff-mode-hook
          (function (lambda ()
                  (setq outline-regexp "diff\\\\|@@\\\\|*\\\\{10,\\\\}")
                  (setq outline-heading-alist
                    '(("diff" . 1) ("@@" . 2) ("*\\\\{10,\\\\}" . 2))
                    )
                  (outline-minor-mode)
    ;             (hide-body)
                  (view-mode)
                  )))

**22\_color.el**
缓冲区两侧的指示条里面显示的连行符号，就是那些弯曲的小箭头，一般都比较晃眼，可以设置成和缓冲区背景一样的颜色  

` (set-face-attribute 'fringe nil :foreground  (background-color-at-point))`

**54\_gui.el**  
我的标题栏设置，因为我老是分不清我用的到底是 emacs 23 还是 24
，所以把版本也显示在标题栏了  

           (defun fname-title-string ()
             "Return the file name of current buffer, using ~ if under home directory"
             (let
                 ((fname (or
                          (buffer-file-name (current-buffer))
                          (buffer-name))))
               (when (string-match (getenv "HOME") fname)
                 (setq fname (replace-match "~" t t fname))        )
               fname))

            (setq frame-title-format             
                            '(:eval (concat (user-login-name) "@" (system-name) "[Emacs" 
                             (nth 2 (split-string (version))) "]  " (fname-title-string))))

还有一个关于鼠标的设置  

    ;; 鼠标指针规避光标
    ;; exile 模式,光标靠近鼠标指针 mouse-avoidance-threshold 范围,指针
    ;; 跳到 (mouse-avoidance-banish-destination) 的返回值，默认右上角。
    ;; exile模式下，光标离开那个范围后，指针返回原处；banish 模式基本差
    ;; 不多，但是指针不返回
    (mouse-avoidance-mode 'exile)
    (setq mouse-avoidance-threshold 10) ;光标靠近该范围,指针规避

    ;; (defun mouse-avoidance-banish-destination()
    ;;   (let* ((pos (window-edges))) ;; pos 里四个数字为缓冲区的 左上右下
    ;;     (cons (- (nth 2 pos) 2)    ;; 横坐标 
    ;;           (nth 1 pos))))       ;; 纵坐标

**60\_tabbar.el**  
tabbar group
这个扩展挺变态的，你懂得，我也不知道该不该用它。下面是我的分组规则，18禁  
[tabbarel](http://linuxtoy.org/img/2011/10/tabbarel.txt)  
OK，差不多了，有什么我忘了说的……就当我没说好了
