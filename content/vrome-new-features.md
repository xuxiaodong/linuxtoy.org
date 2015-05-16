Title: Vrome (Chrome Vim 扩展）-- 新版增加功能
Date: 2010-01-04 10:21
Author: toy
Category: Google Chrome Extension
Tags: Google Chrome, Vim, Vrome
Slug: vrome-new-features

{ 撰文/[Jinzhu](http://github.com/jinzhu) }

[Vrome](http://github.com/jinzhu/vrome)，一个 Chrome 的 Vim
扩展，最最原始的代码来自 Vimlike Smooziee  
(感谢原作者)，自从上次在 Toy  
发贴以来，不少朋友建议改一下名字，于是就有了现在的名字  
Vrome，嗯，我现在终于能记住名字了;)

虽然新版本带来的东西远没有上次版本更新来的多，  
不过也许会有些值得关注的更新，希望大家喜欢。  
因为一： 感觉这些功能对大多用户已经够用了，二：  
老熬夜开发太累了;)

新版增加的功能有：

### 插入模式

    C-i   使用外部编辑器编辑，要使用这个功能你需要执行一个 Ruby 程序。代码在这里：  
    http://github.com/jinzhu/vrome/tree/master/system/  
    ，执行那个 server.rb 文件即可，建议将它加到自动启动里面，或者在启动时在 profile   
    等类似文件里去执行它。你可以在 popup 这个页面去配置编辑器，例如 gvim，emacs，
    默认为 gvim。

    M-d    删除光标前面一个单词

    C-u    删除到行首
    C-k    删除到行尾

    M-h    向后移动一个字词
    M-l    向前移动一个字词
    M-j    向后移动一个字符
    M-k    向前移动一个字符

### 普通模式

    gf   在浏览网页模式下面：在本标签下查看网页源代码，在查看源代码模式下面：在本标签下打开网页
    gF   与 gf 不同的是，在新标签下打开

    D    关闭当前标签，选择前一个 (d 为选择后一个)
    M-d  关闭当前标签，选择最后一次选择的标签

    C-y  缩短当前网址，并且复制缩短后的地址到剪贴板

{ Thanks Jinzhu. }
