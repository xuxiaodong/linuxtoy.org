Title: GNU Emacs 24.3 即将发布
Date: 2013-02-27 09:46
Author: lovenemesis
Category: IDE
Tags: Emacs, gnu
Slug: gnu-emacs-24-3-will-release-soon

GNU Emacs 将于28日发布新的 24.3 版本。*感谢 xfq 来稿*

GNU Emacs 24.3主要为用户添加了如下新特性（相对于24.2）：

* 默认的X
toolkit现在是Gtk+3了。如果你configure的时候不用“--with-x-toolkit”/“--with-x-toolkit=gtk”/“--with-x-toolkit=yes”，configure就会尝试Gtk+3,
如果失败,再尝试Gtk+2。当然，如果你愿意，你也可以用“--with-x-toolkit=gtk2”或者“--with-x-toolkit=gtk3”来configure。

* 新的configure选项 “--enable-link-time-optimization”，只有用GCC
4.5.0编译的以后的才能用哦。

* 新的configure选项 “--without-all”
可以关闭各种默认打开的可选特性（比如图像支持等等）。

* 新的configure选项 “--enable-gcc-warnings” (用于开发和调试Emacs).
如果你用GCC编译Emacs，这可以打开编译时的一些错误检查。

* configure选项
“--enable-use-lisp-union-type”被改名为“--enable-check-lisp-object-type”，因为Lisp\_Object这个类型不再用union来实现了。

* configure选项 “--disable-maintainer-mode”被移除了，因为没什么人用。

* 如果你的系统上有libtinfo的话，Emacs不再使用libncurses。

*
在FreeBSD和NetBSD上，configure不再把/usr/local/lib和/usr/pkg/lib添加到链接器的搜索路径。你若想用，必须自己加。

*
“rcs-checkin”和“vcdiff”这两个脚本被删除了（从bin和libexec目录）。前一个是因为没什么人用了，后一个是因为被vc-sccs替代了。

* “--no-site-lisp”这个命令行参数现在也可以在Mac OS X上用了。

* “C-h f” (“describe-function”)
现在可以知道autoloading了。当这个命令被调用时，如果docstring里有key
substitution的话，那个函数的feature会被自动load，所以文档将被正确的显示。若要关闭此特性，把“help-enable-auto-load”设置为nil。

* “C-h f” 现在把之前autoload过的函数显示为“autoloaded”了。

*
ImageMagick支持默认开启。“imagemagick-register-types”函数在Emacs启动时默认执行。

* 把“imagemagick-types-inhibit”设置为t就会禁用ImageMagick支持。

*
在minibuffer的文件名prompt里，“C-M-f”和“C-M-b”现在可以分别移动到下一个和前一个目录分割符了。不过这个功能ido和Icicles都可以很轻松的做到。

* 你可以在mode line的coding system
indicator按鼠标中键来调用“set-buffer-file-coding-system”了。

* emacsclient现在遵循“initial-buffer-choice”这个变量了。

* 新变量 “server-auth-key”可以指定一个分享式server key了。

* Emacs现在可以在致命错误上显示backtrace了。

* “C-x C-q”现在被绑定到了新的次要模式
“read-only-mode”，这个次要模式替代了“toggle-read-only”。

* 大部分的“y-or-n”提示现在允许你在不退出提示的情况下滚动窗口了。

* 在Package菜单中，新包会被标记为"new"。

*
如果你从bzr.sv.gnu.org的repository里的代码编译Emacs，新变量“emacs-bzr-version”会包含你用的Emacs
revision。这个在报告bug的时候还是很有用的。

* 新变量
“enable-remote-dir-locals”,如果不为nil，允许远程目录局部变量的设置。

* PCL-CVS的命令被从Tools菜单剔除，PCL-CVS的命令现在只能通过键盘调用。

* 文件局部变量"unibyte: t"被弃用，请使用"coding: raw-text"。

* 波斯语支持

* 新的输入法“vietnamese-vni”

* 在Mac OS X下终于可以使用native fullscreen了，真心不容易。

* 新的键绑定：“M-g c”绑定到“goto-char”

* 新的键绑定：“M-g TAB”绑定到“move-to-column”

* “M-g TAB” (“move-to-column”)如果被交互式（无prefix
argument）调用，提示输入列名。

*
新变量“yank-handled-properties”允许操作召回后的文本属性，而不是移除它们。

* “C-u M-=”现在可以计算整个缓冲区的行数、字数和单词数了。

* “C-x 8 RET”被绑定到了“insert-char”，“ucs-insert”被弃用。

*
“z”不再在大部分模式中有命令绑定，这个键以前被绑定为“kill-this-buffer”，但是
“z”太容易被误按了。

* 调用CL现在需要用 “(require
”cl-lib)”了。“cl-lib”和原来的“cl”差不多，除了“cl-lib”用了更清爽的命名空间，也就是说，所有的函数、宏、变量都有了"cl-"前缀或者"cl--"前缀。如果“cl”有一个特性名为“foo”，那么“cl-lib”的名字就叫“cl-foo”，除了少数
叫做“foo*”的被改名为“cl-foo”而不是“cl-foo*”。

* 当当前区域被激活时，dired的“m” (“dired-mark”), “u”
(“dired-unmark”),“DEL” (“dired-unmark-backward”)和“d”
(“dired-flag-file-deletion”)将mark/unmark/flag激活区域中所有的文件。

* GHDL编译器被支持。

* VHDL-AMS的支持被更新。

*
Apropos的face现在可以直接定制了。这些face的名字为“apropos-symbol”，“apropos-keybinding”，等等。详细请见“apropos”定制组，这里就不细说了。

* 定制apropos的老方法被移除（“apropos-symbol-face”,
“apropos-keybinding-face”等等）

* buffer
menu被完全重写，变量“Buffer-menu-buffer+size-width”被弃用，请使用“Buffer-menu-name-width”和“Buffer-menu-size-width”。

* 你可以定制日历上每个月的标题，请看变量“calendar-month-header”的文档。

* 新的LaTeX日历风格，请看“cal-tex-cursor-week2-summary”。

* Compile包有了一个新变量 “compilation-always-kill”。

* “custom-reset-button-menu”现在默认为t

* 变量“term-default-fg-color”和“term-default-bg-color”被弃用。

*
你可以定制ANSI终端颜色了（通过定制“term-color-”,“term-color-underline”和“term-color-bold”这些faces）。

* notifications.el现在支持Notifications API 1.2了。

* Flymake现在运用边缘位图来显示错误和警告，请看
“flymake-fringe-indicator-position”,
“flymake-error-bitmap”和“flymake-warning-bitmap”.

* FFAP变量“ffap-url-unwrap-remote”可以是一个链表，默认为'("ftp").

* 新变量 “mouse-avoidance-banish-position”可以指定“banish”mouse
avoidance的移动位置。

* 新变量 “async-shell-command-buffer”可以指定当“*Async Shell
Command*”正在被用的时候使用的缓冲区。

* “which-func-modes”的新默认值是t，所以如果Which Function
mode被启用，将被用于所有的主要模式。

* “follow-intercept-processes”变量被移除。

* “javascript-generic-mode”被弃用。

* 很多钩子变量被改名：  
* semantic-lex-reset-hooks -> semantic-lex-reset-functions  
* semantic-change-hooks -> semantic-change-functions  
* semantic-edits-new-change-hooks ->
semantic-edits-new-change-functions  
* semantic-edits-delete-change-hooks ->
semantic-edits-delete-change-functions  
* semantic-edits-reparse-change-hooks ->
semantic-edits-reparse-change-functions  
* semanticdb-save-database-hooks ->
semanticdb-save-database-functions  
* c-prepare-bug-report-hooks -> c-prepare-bug-report-hook  
* rcirc-sentinel-hooks -> rcirc-sentinel-functions  
* rcirc-receive-message-hooks -> rcirc-receive-message-functions  
* rcirc-activity-hooks -> rcirc-activity-functions  
* rcirc-print-hooks -> rcirc-print-functions  
* dbus-event-error-hooks -> dbus-event-error-functions  
* eieio-pre-method-execution-hooks ->
eieio-pre-method-execution-functions  
* checkdoc-style-hooks -> checkdoc-style-functions  
* checkdoc-comment-style-hooks -> checkdoc-comment-style-functions  
* archive-extract-hooks -> archive-extract-hook  
* filesets-cache-fill-content-hooks ->
filesets-cache-fill-content-hook  
* hfy-post-html-hooks -> hfy-post-html-hook  
* nndiary-request-create-group-hooks ->
nndiary-request-create-group-functions  
* nndiary-request-update-info-hooks ->
nndiary-request-update-info-functions  
* nndiary-request-accept-article-hooks ->
nndiary-request-accept-article-functions  
* gnus-subscribe-newsgroup-hooks ->
gnus-subscribe-newsgroup-functions  
* input-method-inactivate-hook -> input-method-deactivate-hook  
* robin-inactivate-hook -> robin-deactivate-hook  
* quail-inactivate-hook -> quail-deactivate-hook

* 被弃用的包：  
* assoc.el  

大多数情况下，assoc+member+push+delq可以工作的非常好。而且这也是个让人头疼的包：不清晰的语义，低下的效率，还有不干净的命名空间。  
* bruce.el  
* cust-print.el  
* ledit.el  
* mailpost.el  
* mouse-sel.el  
* patcomp.el

*
以“*”开头的docstring不再表示用户选项。只有用defcustom定义的变量才被看做用户选项。函数“user-variable-p”被弃用，请使用“custom-variable-p”。

* “defalias”, “defun”和“defmacro”的返回值有所改变，现在的值是未定义。

* “set-buffer-multibyte” 现在在窄化缓冲区中不能使用了。

* CL的“get-setf-method”函数将不复存在。

*
“dbus-register-signal”的参数将不只是字符串，而是关键字和关键字-字符串对。

* 一些函数改名了：  
* hangul-input-method-inactivate -> hangul-input-method-deactivate  
* inactivate-input-method -> deactivate-input-method  
* quail-inactivate -> quail-deactivate  
* robin-inactivate -> robin-deactivate  
* viper-inactivate-input-method -> viper-deactivate-input-method  
* viper-inactivate-input-method-action ->  
viper-deactivate-input-method-action  
* ucs-input-inactivate -> ucs-input-deactivate

* 改名的变量：  
* follow-deactive-menu -> follow-inactive-menu  
* inactivate-current-input-method-function ->  
deactivate-current-input-method-function

* 全新的基于样例的Elisp profiler。你可以试一试用M-x profiler-start,
干一些其他事，然后M-x profiler-report。结束时，用M-x profiler-stop。

* 新的宏“setq-local” and “defvar-local”。

* 下划线的face可以用波浪线了。

* 新的错误类型和新的函数“user-error”，他们不会触发Lisp调试器。

* 新变量 “debugger-bury-or-kill”，用来决定退出Lisp调试器的方法。

* 新命令“fit-frame-to-buffer”，这个命令可以自动调整当前frame的大小。

* 命令“fit-window-to-buffer”可以调整frame的高度（如果新变量
“fit-frame-to-buffer” 不为nil）

* 新宏“with-temp-buffer-window”，和“with-output-to-temp-buffer”相似。

* “temp-buffer-resize-mode”不再调整被重用的窗口的大小。

* 新变量
“switch-to-buffer-preserve-window-point”，可以在切换缓冲区时恢复一个窗口的光标位置。

* 函数“get-lru-window”,
“get-mru-window”和“get-largest-window”现在有了第三个参数，可以防止选择当前窗口。

* 以下变量被弃用，因为他们能够被GNU Emacs
24.1中引入的“display-buffer-alist”替代：  
* “dired-shrink-to-fit”  
* “display-buffer-reuse-frames”  
* “display-buffer-function”  
* “special-display-buffer-names”  
* “special-display-frame-alist”  
* “special-display-function”  
* “special-display-regexps”

*
“current-time-string”不再要求参数中的年份在1000到9999之间了，现在，只要是C能支持的年份，它都能支持。

* 处理浮点型变量的函数现在在遇到错误时会返回NaN而不是报错，如(log -1.0)
=>
NaN。原来Emacs在有些平台上报错，却在另外一些平台上返回NaN。影响到的函数有：acos,
asin, tan, exp, expt,log, log10, sqrt,还有mod.

* “kbd” 现在是一个函数而不是一个宏了。

* 新函数“autoloadp”可以测试参数是不是autoloaded对象。

* 新函数“buffer-narrowed-p”可以测试缓冲区是否被窄化。

* “posnp”可以测试一个对象是否是“posn”。

* 新函数“system-users”可以返回当前用户名。

* 新函数“system-groups”可以返回当前组名。

* Cygwin编译的Emacs可以用MS
Losedows的UI了，用configure的“--with-w32”就可以，不过默认的还是X11的UI。

*
Cygwin编译的Emacs将有2个新函数：“cygwin-convert-file-name-from-windows”
和“cygwin-convert-file-name-to-windows”。

*
当Emacs在Losedows下用-nw参数调用时（cmd.exe），新版的Emacs可以支持“mouse-highlight”,
help-echo (在echo area),和“mouse-autoselect-window”。

* 在MS-Losedows Vista后的版本中，Emacs将支持符号链接。

* 在“M-x report-emacs-bug”生成的缓冲区中，“C-c m”快捷键已被改为“C-c
M-i”
(“report-emacs-bug-insert-to-mailer”)。之前的快捷键是一个错误，因为“C-c
LETTER”是为了留给用户自定义的。

当然，除了以上新特性，还有各种bug修复，这里就不细说了。因为最近Chong
Yidong比较忙，所以他把Emacs的release management交给了Glenn
Morris（从1月9日的Emacs pretest 24.2.92开始）。有关 GNU Emacs 24.3
的更多详情，可查看emacs-24的[branch
changes](http://bzr.savannah.gnu.org/lh/emacs/emacs-24/changes/111300?start_revid=111300)。Happy
hacking!
