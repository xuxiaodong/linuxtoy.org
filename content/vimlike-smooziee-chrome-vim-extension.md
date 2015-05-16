Title: Vimlike Smooziee  - Chrome Vim 扩展
Date: 2009-12-21 10:58
Author: toy
Category: Google Chrome Extension
Tags: Google Chrome, Vim, Vrome
Slug: vimlike-smooziee-chrome-vim-extension

{ 撰文/[Jinzhu](http://github.com/jinzhu) }

Vimlike Smooziee
又一个新版本在经过一个星期的熬夜激烈开发后出来啦，这次更新增加了很多很多功能  
;)

虽然还有很多想法还没有开始做，还有很多地方看起来很粗糙，但我还是忍不住想
release 一把  
;)

如果你还不知道 Vimlike Smooziee，它是一个可以让 Chrome 以 Vim
的方式去操作的扩展，你可以点击下面地址安装:  

源代码：  
Bug Report、Feature Request 可以从上面的地址开一个 issue，  
也可以直接给我发邮件: wosmvp@gmail.com

不善于写文章，列特性 :0

### 放大网页

    [count]zi  放大[count]级，默认放大一级，例如 3zi 放大三级(下同)  
    [count]zo  缩小[count]级  
    [count]zm  放大3*[count]级  
    [count]zr  缩小3*[count]级  
    zz         重置到100%  

    [count]zI  放大当前页面[count]级，放大后仍显示当前位置(下同)  
    [count]zM  放大3*[count]级  
    [count]zO  缩小[count]级  
    [count]zR  缩小3*[count]级  
    zZ         重置到100%  

### Page

    ]]    下一页  
    [[    上一页  
    Y     复制当前选择文本  

### Url

    [count]C-a    当前地址最后一个数字加[count]，默认为1，例如 bbs.org/post/1 执行C-a 转到 bbs.org/post/2 (下同)  
    [count]C-x    当前地址最后一个数字减[count]，默认为1  
    [count]gu     到上[count]级目录，默认为1， linux.com/forum/os/arch 执行 2gu 转到 linux.com/forum  
    gU            转到根目录，上面地址执行gU，转到linux.com  

    o      在当前页打开地址，可以指定多个地址使用 ', ' 分开，注意后面的空格(下同)  
    O      同上，当前页为默认地址  
    t      在新标签页打开地址  
    T      同上，当前页为默认地址  

### Scroll

    gg    跳到页首  
    G     跳到页尾  
    0     跳到最左边  
    $     跳到最右边  

    [count]k    向上移动[count]*30px  
    [count]j    向下移动[count]*30px  
    [count]h    向左移动[count]*30px  
    [count]l    向右移动[count]*30px  
    [count]%    跳到 [count]% 处  

    [count]C-f  下[count]页  
    [count]C-b  上[count]页  
    [count]C-d  下[count]半页  
    [count]C-u  上[count]半页  

### Tab

    r        刷新当前页  
    d        关闭当前页  
    [count]u       打开前面第[count]个关闭的页面  
    [count]C-p     跳到往前[count]个Tab，首尾循环  
    [count]C-n     跳到往后[count]个Tab，首尾循环  
    [count]gT      同C-p  
    [count]gt      同C-n  
    y       复制当前url  
    g0/g^   跳到第一个tab  
    g$      跳到最后一个tab  
    C-^     跳到前一次访问的tab  

### 历史

    [count]H        前[count]历史，默认1  
    [count]L        后[count]历史  
    [count]C-o      同H  
    [count]C-i      同L  

### 快速选择 (使用字符串，或者数字选择)

    f         快速选择模式，当前页面打开  
    F         快速选择模式，新标签打开  

### 搜索

    /          向前搜索  
    ?          向后搜索  
    [count]n   下[count]个匹配 ( 输入框外 )  
    [count]N   上[count]个匹配 ( 输入框外 )  

    Enter      下一个匹配 ( 输入框内 )  
    S-Enter    上一个匹配 ( 输入框内 )  
    *          向前搜索当前选择文本  
    #          向后搜索当前选择文本  

    [count]gi  跳到第[count]个输入框,默认1  
    C-z        关闭 Vimlike，Esc重新打开  
    C-v        暂时关闭Vimlike，不匹配下一次输入  
    [count].   重复执行上次命令[count]次，默认1，例如 先执行 3j(向下移动3格) 再执行 4. 向下移动12格，再执行 . 一次，还会向下移动 3格  

### 输入模式

    Esc/C-[ 退出输入框  

    C-a    移到第一个字符串位置，如果已经在第一个字符处时，就全部选择  
    C-e    移到最后一个字符串位置  

    C-d    删除前一个字符  
    C-h    删除后一个字符  

    C-w    删除前一个单词  

### disable sites（默认不开启 Vimlike 的站点)

点击地址栏上的 Vim 按钮即可增加，还可以在插件选项里配置。

### 更新

Vimlike Smooziee 现已更名为
Vrome，详见[这里](http://linuxtoy.org/archives/vimlike-smooziee-chrome-vim-extension.html#comment-133032)。

{ Thanks Jinzhu. }
