Title: 邪恶的 eshell
Date: 2011-10-16 19:18
Author: Kardinal
Category: News, Themes
Slug: emacs-eshell

对于一个经常“被跨平台”的人来说，Windows 下没有一个好用的
shell，不能不说是一个  
遗憾。

虽然说 bash zsh 都有 windows
的版本，但几乎一无是处……此处暂省略1000字，且不说应有  
尽没的功能，光是那速度就让人抓狂，动不动装死，让人想撞死，还不如 eshell
来的机灵……等等，  
eshell 不就是天生跨平台的 shell 么？

当然，要用 eshell 必需要有 emacs，因为它就是用 elisp 写的。你不能把它从
emacs 里面抠出来单独使用……就像你不能把 emacs
从屏幕里抠出来单独使用，一样一样的  

废话不多说，这回先上图  

[![](http://linuxtoy.org/img/2011/10/eshell.png)](http://linuxtoy.org/img/2011/10/eshell.png)

eshell 够坏的，shell 里面能用 outline，我还真不知道有别的 shell 或者
editor 能够做到……淘气！

当然，仅仅一个 outline mode 还不能称得上 evil ，eshell 里面可以同时使用
shell 和 elisp 两种语言。

    cmd $(elisp)
    $(shell-command-to-string "cmd")

$ 不是必须的，甚至最外层的括号也可以省略，不过据说可能会出问题

eshell 还有变态的修饰器和文件类型断言

    echo *(:U) => ("BAR" "BIN/" "DEV/" "ETC/" "FOO" "HOME/" "LIB/" "TMP/" "USR/" "VAR/")

(:U) 括弧中以冒号开头的是修饰器，U 表示转换为大写。

    echo *(^/) => ("bar" "foo")

(^/) 就是文件类型断言了，/ 表示文件夹，前面的 ^ 表示 非

    echo ("foo" "bar" "baz" "foo")(:gs/foo/blarg/)
    => ("blarg" "bar" "baz" "blarg")

是不是有点眼熟？请自由联想……需要注意的是，修饰器和文件类型断言要紧跟在列表的后  
面。你没有看错，前面例子中的 * 不是列表，从哪个角度看都不是，但它爸是
eshell，所以它叫通配符

如果想了解更多修饰器和文件类型断言的信息，M-x
eshell-modifier(predicate)-alist  
不过符号是用数字表示的，理解起来有一定难度，点那个 customize 的链接。

下面又到了每月一次的配置文件时间

首先绑定一个快速启动 eshell 的快捷键，我绑定的是 C-x C-x
。如果想多开，加个前缀  
参数就可以了，比如 C-u C-x C-x 。

    (add-hook 'eshell-mode-hook (lambda()
               (outline-minor-mode 1)
               (color-theme-my-eshell)
               (setq outline-regexp "^[^#$\n]* [#>]+ "
                     scroll-margin 0
                     eshell-scroll-to-bottom-on-output t
                     eshell-scroll-show-maximum-output t)
               (add-to-list 'eshell-output-filter-functions 
                            'eshell-postoutput-scroll-to-bottom)
               (def-key-s eshell-mode-map 
                 "<up>"     'eshell-previous-matching-input-from-input
                 "<down>"   'eshell-next-matching-input-from-input
                 "<tab>"    'user-tab
                 "<return>" 'user-ret
                  "SPC"      'user-spc
    )
    ))

尽管 eshell 也有 auto cd
的功能，就是输入目录回车，自动cd；不过我还是习惯空行按  
tab 补全 cd ，那样比较一致。

我把这几个键的功能整理到一个文件里了，需要的时候 require 一下就可以了  

[eshell-user-key.el](http://linuxtoy.org/img/2011/10/eshell-user-keyel.txt)

    ;tab 空格再tab ，就会变成 cd -0，一直按tab，数字一直加
    (defun user-tab ()

狠了狠心，我又加了一个 user-ret 。男人嘛，就应该对 Shell 狠一点

    (defun user-ret ()

这个函数的作用是，空行按回车自动 ls; 展开 "..."=>"../.." ;
"...."=>"../../.." ……狠不狠？

还是不够狠啊……

    (defun user-spc ()

下面是一些基本设置，不解释


    (setq
          eshell-save-history-on-exit   t
          eshell-history-size           512
          eshell-hist-ignoredups        t
          eshell-cmpl-ignore-case       t
          eshell-cp-interactive-query   t
          eshell-ln-interactive-query   t
          eshell-mv-interactive-query   t
          eshell-rm-interactive-query   t
          eshell-mv-overwrite-files     nil
          ;; aliases-file 里面不能有多余的空行，否则会报正则表达式错误
          eshell-aliases-file       (expand-file-name "_eshell/eshell-alias" init-dir)

          eshell-highlight-prompt   t
          ;; 提示符设置，下面两项必须对应起来，
          ;; 否则会报 read-only，并且不能补全什么的
          eshell-prompt-regexp      "^[^#$\n]* [#>]+ "
          eshell-prompt-function    (lambda nil
                                      (concat
                                       (abbreviate-file-name
                                        (eshell/pwd))
                                       (if
                                           (=
                                            (user-uid)
                                            0)
                                           " # " " >>> ")))
    )

作为一个有时间观念的人，我需要知道每一个命令花了多少时间。。。其实我总觉得  
eshell 有点慢，这样心里感觉踏实一点 -\_\_-!!!

    (add-hook 'eshell-load-hook
              (lambda()(setq last-command-start-time (time-to-seconds))))
    (add-hook 'eshell-pre-command-hook
              (lambda()(setq last-command-start-time (time-to-seconds))))
    (add-hook 'eshell-before-prompt-hook
              (lambda()
                  (message "spend %g seconds"
                           (- (time-to-seconds) last-command-start-time))))

设置一些常用的命令

    (defalias 'ff 'find-file)
    (defalias 'ee (lambda()(find-file (expand-file-name "44_eshell.el" init-dir))))
    (defalias 'aa (lambda()(find-file eshell-aliases-file)))
    (defalias 'rr (lambda()(find-file (expand-file-name "_qref.org" sand-box))))
    (defalias 'ss  'shell-command-to-string)

差点忘了，auto-complete 设置

    (defvar ac-source-eshell-pcomplete
      '((candidates . (pcomplete-completions))))
    (defun ac-complete-eshell-pcomplete ()
      (interactive)
      (auto-complete '(ac-source-eshell-pcomplete)))
    ;; 自动开启 ac-mode
    ;; 需要 (global-auto-complete-mode 1)
    (add-to-list 'ac-modes 'eshell-mode)
    (setq ac-sources '(ac-source-eshell-pcomplete
                       ;; ac-source-files-in-current-dir
                       ;; ac-source-filename
                       ;; ac-source-abbrev
                       ;; ac-source-words-in-buffer
                       ;; ac-source-imenu
    ))

还有胡乱收集的一些小函数

    (defun eshell/ii (file)(ido-find-file file))
    (defun eshell/ed (file1 file2)(ediff-files file1 file2))

    ;; 按一次 C-a 到命令在前面，再按一次到命令提示符的前面，感觉用处不大
    (defun eshell-maybe-bol ()
      (interactive)
      (let ((p (point)))
        (eshell-bol)
        (if (= p (point))
            (beginning-of-line))))

    (defun eshell/gvim (&rest args)
      "Invoke `find-file' on the file.
    \"vi +42 foo\" also goes to line 42 in the buffer."
      (while args
        (if (string-match "`\\+\\([0-9]+\\)\\'" (car args))
            (let* ((line (string-to-number (match-string 1 (pop args))))
                   (file (pop args)))
              (find-file file)
              (goto-line line))
          (find-file (pop args)))))

我知道排版很混乱，但是 linuxtoy
现在还是没有语法高亮的插件，我也无能为力。。。这也算stay hungry stay
foolish的另一种诠释?(当然不是所谓的“求知若饥，虚心若愚”，这种翻译傻逼的让我吐血)

作为你忍受了这么久还能看到结尾的回报，我送上我精心配置的2.5个主题……其中有一个主题是我分析了某人网站的css文件提取出来的，折腾了半夜，另外那半个是
eshell 的主题[color.el](http://linuxtoy.org/img/2011/10/colorel.txt)  
需要 color-theme 支持……不过你可以把 color-theme-library.el 删了
