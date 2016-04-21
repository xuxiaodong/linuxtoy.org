Title: Emacs Markdown 模式简介
Date: 2009-04-14 16:05
Author: toy
Category: Apps
Tags: Emacs, Markdown
Slug: emacs-markdown-mode

受 [Rainux](http://rainux.org/) 兄的影响，我现在迷上了用 [Markdown](http://daringfireball.net/projects/markdown/) 格式来写东西。为了在 Emacs 中更加方便的完成 Markdown 格式的内容，我找到了 Emacs markdown-mode。

<!-- PELICAN_END_SUMMARY --> 

Emacs markdown-mode 是一个 Emacs 主模式，用来在 Emacs 中创建或编辑 Markdown 格式的内容，非常便捷和高效。

**安装与配置**

安装 markdown-mode 非常简单，只需将下载的 markdown-mode.el 文件置于 Emacs 可找到的路径，例如 ~/.emacs.d/modes。然后把下列内容添加到 .emacs 文件中即可：

```
(add-to-list 'load-path "~/.emacs.d/modes")  
(autoload 'markdown-mode "markdown-mode.el"  
"Major mode for editing Markdown files" t)  
(setq auto-mode-alist  
(cons '(".markdown" . markdown-mode) auto-mode-alist))
```

这样，当 Emacs 打开扩展名为 markdown 的文件时，就会自动进入 Markdown 主模式。如果你定义的 Markdown 扩展名与此不同，那么你将需要替换上面配置内容最后一行中的 .markdown。

**编辑命令**

Markdown 模式将常用的编辑命令都绑定到了特定的组合键上，因此要插入某个项目，只需按相应的组合键。比如：

* C-c C-t n 插入 hash 样式的标题，其中 n 为 1~5，表示从第一级标题到第五级标题。  
* C-c C-t t 插入 underline 样式的标题，这是一级。  
* C-c C-t s 同上，这是二级。  
* C-c C-a l 插入链接，格式为 `[text](url)`。  
* C-c C-i i 插入图像，格式为 `![text](url)`。  
* C-c C-s b 插入引用内容。  
* C-c C-s c 插入代码。  
* C-c C-p b 加粗。  
* C-c C-p i 斜体。  
* C-c - 插入水平线。

如果是在选定的内容上按这些组合键，那么将把选定的内容设为相应的格式。

**大纲视图**

按 S-Tab 将在大纲视图、目录视图、及正常视图间切换。

**预览**

如果你的系统中安装有 Markdown 程序包的话，那么在 Emacs 中便可以运行 Markdown，并预览其输出。相应命令如下：

* C-c C-c m 在当前缓冲运行 Markdown，并在另一个缓冲预览。  
* C-c C-c p 同上，但在浏览器中预览。

Emacs markdown-mode 可从其主页下载，在它的主页上，你也可以找到完整的使用说明。

[Emacs markdown-mode](http://jblevins.org/projects/markdown-mode/)
