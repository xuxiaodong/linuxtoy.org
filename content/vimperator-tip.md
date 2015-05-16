Title: 小技巧: 在 Vimperator 中调用外部编辑器
Date: 2009-03-20 09:32
Author: toy
Category: Tips
Tags: Vim, Vimperator
Slug: vimperator-tip

若你使用  

[Vimperator](http://linuxtoy.org/tag/vimperator)，那么可以通过调用外部的文本编辑器来输入网页上文本框中的内容。Vimperator  
的这项特性和 Firefox 扩展 [It's All  
Text!](https://addons.mozilla.org/en-US/firefox/addon/4125)  
挺相似，不过后者不支持调用命令行下的文本编辑器，相较而言，Vimperator  
的则更为实用。

\_\_设置方法\_\_

你只需设置 editor 选项即可，GVim 可设置为：

:set editor=gvim\\ -f

如果你要使用 Vim，则可以这样设置：

:set editor=urxvt\\ -e\\ vim

要是你使用其他的终端，那么需要替换上述设置命令中的 urxvt。

你也可以将设置写入 Vimperator 的配置文件 $HOME/.vimperatorrc。

\_\_如何使用\_\_

很简单，定位到需要输入内容的文本框，按 Ctrl + i 组合键。一旦在 (G)Vim  
中编辑完成，直接保存即可。
