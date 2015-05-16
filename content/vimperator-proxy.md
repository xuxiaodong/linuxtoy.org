Title: 用 Vimperator 快速启用/禁用代理
Date: 2010-05-14 18:50
Author: vern
Category: Cli
Slug: vimperator-proxy

以前用 AutoProxy，它的优点很明显就如它在广告中说的 “使用
AutoProxy，您不再需要在代理和非代理之间不停地切换。只要在 AutoProxy
的首选项中加入需要使用代理的网站，它会帮助您自动判断。指定的网站使用代理，而其它的网站直接连接。”

然而对于频繁使用 Google.com 的用户来说，它的优点越来越不明显了。当你点选
Google 搜索结果页面中的链接时，你不知道这个链接是否会被重置，进而导致
Google.com
的暂时无法使用。每当发生这种情况的时候，我都要用鼠标右键状态栏的
AutoProxy
图标并启用全局代理模式；等过了一会我又要用鼠标换回自动代理模式。这种依赖鼠标切换的方式让我不舒服。

现在我只要通过键盘快捷键就可以方便的启用/禁用代理，在状态栏还有一个图标能指示当前是否在使用代理。

编辑 ~/.vimperatorrc

    ...
    " ref@http://vim.group.javaeye.com/group/topic/16187
    map <F12> :set! network.proxy.type=1<CR>:echo ":("<CR>
    map <S-F12> :set! network.proxy.type=0<CR>:echo ":)"<CR>
    ...

用于指示代理状态的图标需要额外安装一个 Firefox 插件 QuickProxy[1]

[1] https://addons.mozilla.org/zh-CN/firefox/addon/1557/
