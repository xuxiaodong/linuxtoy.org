Title: emacs 小技巧：根据主模式加载配置
Date: 2011-12-25 00:52
Author: Kardinal
Category: Tips
Tags: Emacs
Slug: emacs-tip

很多人的配置文件，各种主模式的配置写在一起的，可能既有 c 又有 lisp 又有
js 什么的，其实大部分情况下你不会同时用那么多。

于是有了另一种方式，拆分到文件，每种模式用一个单独的文件。在主配置文件里写上
(load 'xxx)

但是这挺麻烦的，你要新建一个文件名为 xxx，然后主配置文件里又得写 load
xxx，这显然是重复劳动……这是我最痛恨的……因为我一年级就上了好几次

于是我弄了一个文件夹，按顺序自动 load 里面的文件，当然不是随便
load，得符合条件才行。比如我设定的条件是扩展名为 el。

这样一来，不想 load
的文件改下扩展名就可以了……我还弄了一个函数，专门给文件添加/删除扩展名
.bak  
但是时间长了也挺麻烦的，因为要手动改，而且下次才能生效…… 你还得自己
load-file  

……其实一般情况下，这不是什么问题，你就是给每种模式写上几万行的配置，都写在一个文件里，对于现在的机器而言，压力也不是太大……但是咱追求的不是方便，而是折腾

好了，开始动手

    (let (name
          (dir (expand-file-name "\_major-mode/" *init-dir*)))
      (mapcar
       (lambda(x)
         (setq name
               (file-name-sans-extension (file-name-nondirectory x)))
         (add-hook  (concat-symbol name "-mode-hook")
                   `(lambda()(load ,x))))
       (directory-files dir t ".el\\\\'")))

简单的说，假设 ~/init.emacs/\_major-mode/ 目录下有 3 个文件
emacs-lisp.el nxml.el js2.el.bak ，则会：

在 emacs-lisp-mode-hook 里添加 (lambda nil (load
"~/init.emacs/\_major-mode/emacs-lisp.el"))

在 nxml-mode-hook 里添加 (lambda nil (load
"~/init.emacs/\_major-mode/nxml.el"))

里面用到的 concat-symbol

    (defun concat-symbol (&rest lst)
      (read (apply 'concat (mapcar (lambda(x)(if (symbolp x) (symbol-name x) x)) lst))))

需要注意的是，这简直就是一个特大号的 hook ，所以不用在里面再写什么
add-hook 'xxx-mode-hook 了，里面所有的东西都相当于在 xxx-mode-hook 里。

如此一来，就产生了另一个问题，每打开一个 a.xxx 文件，xxx-mode-hook
就要运行一次，然后 load 一次，真二，实际上只要 load 一次就可以了。

这个问题可以用 require 来解决，但缺点是，你要在新建一个文件为 xxx.el
，还要在里面写 provide 'xxx ，并且还要把当前目录加到
load-path，重复劳动还是比较多。

另一种方案就是 load-once

    (defmacro load-once (&rest s)
      (let* ((name (file-name-sans-extension
                    (file-name-nondirectory
                     (or load-file-name (buffer-file-name)))))
             (a (concat-symbol "*load-once--" name "*")))
        `(if (boundp ',a)
             nil
           ,@s
           (setq ,a t))))

在 xxx.el 里面只运行一次的部分可以写在 load-once 里面，像这样

    (load-once
     (foo)
     (bar)
    )

基本上，你把所有内容都写在 load-once 里面就对了，不管这个文件被 load
了多少次，都只运行一次。

这种方法的缺点是，需要在文件开头和结尾分别写 (load-once 和 )，而 provide
只要写在一处；  
每种模式被 load 后，自动生成了一个值为 t 的变量 *load-once--xxx*
、*load-once--yyy* ……

所以，我觉得我有责任给你一个十分专业的建议：你自己看着办

[我的配置文件](https://github.com/ran9er/init.emacs/tarball/master)

->>---------------2011-12-31--6--22:38:13------------------>

emacs 23 的话会有点问题，因为 update-file-autoloads 在 24
里可以三个参数，而 23 里最多两个，output file 需要在上下文中绑定
generated-autoload-file 变量来指定，真 TMD 操蛋

    (funcall
     (lambda (dir &optional f loaddefs basedir)
       (let* ((path
               (expand-file-name dir (or basedir *init-dir*)))
              (ldfs
               (or loaddefs (expand-file-name "_loaddefs" path)))
              index force)
         (setq index
               (funcall
                (lambda (dir)
                  (let (out i p)
                    (with-temp-buffer
                      (insert-file-contents dir)
                      (setq p (point-max))
                      (while (setq i (search-forward-regexp "^;;; Generated autoloads from " p t))
                        (setq out (cons (buffer-substring-no-properties i (line-end-position))
                                        out)))) out))
                ldfs))
         (setq force (or f (null (equal (reverse index)
                                        (directory-files path nil ".el\\'")))))
         (if force (delete-file ldfs))
         (let ((generated-autoload-file ldfs))
           (mapcar
            (lambda (fl)
              (if (or force
                      (null (file-newer-than-file-p ldfs fl)))
                  (update-file-autoloads fl t)))
            (directory-files path t ".el\\'")))
         (load ldfs)))
     "_autoload_/")

->>---------------2011-12-30--5--20:42:25------------------>

把不是特别常用的函数放到一个文件夹里，然后通过 autoload 的方式加载

--------------|2011-12-28|--|3|--|23:35:11|---------------

或者 eshell 需要一个单独的 hook ：

    (let* ((dir (expand-file-name "\_extensions/" *init-dir*))
           (ext (mapcar
                 (lambda(x)(cons (file-name-sans-extension (file-name-nondirectory x)) x))
                 (directory-files dir t ".el\\\\'"))))
      (add-hook 'find-file-hook
                `(lambda ()
                   (let (mode)
                     (mapcar (lambda(x)
                               (and
                                (string-match (car x)(buffer-name))
                                (setq mode (symbol-name (cdr x)))))
                             auto-mode-alist)
                     (load (or
                            (cdr (assoc mode ',ext))
                            (make-temp-name ""))
                           t))))
      (add-hook 'eshell-load-hook
                `(lambda ()
                   (load ,(cdr (assoc "eshell" ext))))))

------------------------------2011-12-27 {2} 23:03:00

尝试把不常用的函数分离出来，但是update-file-autoloads
似乎并不按我期望的方式工作，所以下面的

(autoload-directory "\\\_autoload/") 暂时可以 (autoload-directory
"\\\_autoload/" t) 强制执行

    (defun autoload-directory (dir &optional force loaddefs basedir)
      (let* ((path
              (expand-file-name dir (or basedir *init-dir*)))
             (ldfs
              (or loaddefs (expand-file-name "\_loaddefs" path))))
        (mapcar
         (lambda(f)
           (if (or force
                   (null (file-newer-than-file-p ldfs f)))
               (update-file-autoloads f t ldfs)))
         (directory-files path t ".el\\\\'"))
        (load ldfs)))

    (autoload-directory "\_autoload/")

------------------------------2011 12 26

根据扩展名判断的话，有时一种主模式对应多个扩展名，比如 .c .h .i .lex
都是 c-mode

遇到这种情况难道得分别弄4个文件不成？最关键的是这些文件的同步问题……可能用符号链接也可以，  
但是那超出了 emacs 的范围，而是属于文件系统的层面……这应该比较危险吧

用主模式判断的话，则更新了太多的 xxx-mode-hook
，影响环境，关键是不能在里面写  
add-hook 'xxx-mode-hook
，可能很多以前的配置要改（而据我观察，ifind-file-hook 应该在
xxx-mode-hook 之前运行，在 find-file-hook 里面定义 xxx-mode-hook
是可行的）

更重要的是，find-file-hook
里面添加的代码虽然可能长一点，但是不管怎么说，只是修改一个 hook
而已，比较环保

    (let* ((dir (expand-file-name "\_extensions/" *init-dir*))
           (ext (mapcar
                 (lambda(x)(cons (file-name-sans-extension (file-name-nondirectory x)) x))
                 (directory-files dir t ".el\\\\'"))))
      (add-hook 'find-file-hook
                `(lambda ()
                   (let (mode)
                     (mapcar (lambda(x)
                               (and
                                (string-match (car x)(buffer-name))
                                (setq mode (symbol-name (cdr x)))))
                             auto-mode-alist)
                     (setq mode
                           (or mode
                               (and (string-equal "*" (substring (buffer-name) 0 1))
                                    (substring (buffer-name) 1 -1))))
                     (load (or
                            (cdr (assoc mode ',ext))
                            (make-temp-name ""))
                           t)))))

这段代码在 file-file-hook 里面添加如下内容

    (lambda nil
      (let (mode)   
        (mapcar
         (lambda (x)
           (and (string-match (car x) (buffer-name))
                (setq mode (symbol-name (cdr x)))))
         auto-mode-alist)
        (setq mode
              (or mode
                  (and (string-equal "*" (substring (buffer-name) 0 1))
                       (substring (buffer-name) 1 -1))))
        (load
         (or
          (cdr (assoc mode
           '(("emacs-lisp-mode" . "~/init.emacs/\_extensions/emacs-lisp-mode.el")
             ("js-mode" . "~/init.emacs/\_extensions/js-mode.el")
             ("xml-mode" . "~/init.emacs/\_extensions/xml-mode.el"))))
          (make-temp-name ""))
         t)))

从文件名，通过查找 auto-mode-alist
来确定主模式，再根据主模式加载配置文件

（为什么 wordpress 的解析如此不人性化，都用了 pre 标签了，依然解析 *
` \\\_
这些字符……每次都让我很纠结……干脆写了一个小函数来替换这些字符-\_-||||）

------------------------------xxx

或者也可以根据 buffer-name 来判断

    (let* ((dir (expand-file-name "\_extensions/" *init-dir*))
           (ext (mapcar
                 (lambda(x)(cons (file-name-sans-extension (file-name-nondirectory x)) x))
                 (directory-files dir t ".el\\\\'"))))
      (if nil
          ;; if nil  ;; by extension
          ;; if t    ;; by major-mode
          ;; if nil t  ;; all
          (mapcar
           (lambda(x)
             (add-hook  (concat-symbol (car x) "-mode-hook")
                        `(lambda()(load ,(cdr x)))))
           ext)
        (add-hook 'find-file-hook
                  `(lambda ()
                     (load (or
                            (cdr (assoc (or (file-name-extension (buffer-name))
                                            (and (string-equal "*" (substring (buffer-name) 0 1))
                                                 (substring (buffer-name) 1 -1)))
                                        ',ext))
                            (make-temp-name ""))
                           t)))
        ))

假设在 init-dir/\_extensions/ 目录下文件为： xml.el el.el js.el
eshell.el

普通文件通过扩展名来加载配置，xxx.js -> load js.el

以 *
开头的临时文件则去掉第一个和最后一个字符后，通过得到的名字来加载配置，*eshell* ->
load eshell.el
