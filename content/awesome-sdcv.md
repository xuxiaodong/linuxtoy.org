Title: Awesome 窗口管理器——换种方式使用星际译王
Date: 2009-11-10 20:29
Author: vern
Category: Cli
Slug: awesome-sdcv

星际译王被广泛使用的两个功能应该是划词翻译和手动输入翻译。由于星际译王缺少划词功能的开关快捷键，导致每次划词功能使用结束后，必须手动关闭此功能。

否则在 vim
视图模式下选择文本的时候会弹出不需要的翻译窗口，这有点让人苦恼。虽然它提供了‘在修饰键按下时才取词’的功能，但是如果你真的使用过你就知道，它需要你一直按住修饰键不松，否则翻译窗口立即被隐藏。另一种情况是，你不必始终按住修饰键，但是当你想隐藏翻译窗口时，你必须动动你的鼠标。简单来说，你有两个选择，要么按住修饰键5秒、10秒、甚至20秒，要么每次查询结束你的手就得离开键盘动动鼠标。

对于手动输入翻译这个功能来说，sdcv
是个很好的想法，但它需要你始终保持一个虚拟终端以备你随时的查询，而且这将破坏你目前的状态，因为你必须切换终端，甚至切换到另一个虚拟桌面。

Awesome
能帮我较好的解决这些苦恼，我甚至不用打开星际译王的程序，就可以使用‘在修饰键按下时才取词’的划词翻译功能，和更方便的手动输入翻译功能。只需两个额外的软件包
sdcv 和 xsel 就能换来更好的使用体验。

无论是用鼠标在 Firefox 里，还是用键盘在 Vim 里，当你选中一个单词，按
Meta-d 就会在右上方弹出翻译结果。当你要手动输入某个单词的时候，按
Meta-Shift-d 就会在任务栏那里弹出一个 Dict:
输入栏，输入后回车即可看到翻译结果。可设置超时自动关闭翻译结果，也可以再按
Meta-d
立即关闭翻译结果。当然你愿意的话，用鼠标点一下翻译结果也可以关闭它。

[![](http://i.linuxtoy.org/images/2009/11/2009-11-10-201741_1680x1050_scrot-400x250.png)](http://i.linuxtoy.org/images/2009/11/2009-11-10-201741_1680x1050_scrot.png)

配置如下:

3.3 || 3.4

    ...
    globalkeys = awful.util.table.join (
    ...
    -- {{{ sdcv/stardict
    awful.key({ modkey }, "d", function ()
        local f = io.popen("xsel -o")
        local new_word = f:read("*a")
        f:close()

        if frame ~= nil then
            naughty.destroy(frame)
            frame = nil
            if old_word == new_word then
                return
            end
        end
        old_word = new_word

        local fc = ""
        local f  = io.popen("sdcv -n --utf8-output -u '牛津英汉双解美化版' "..new_word)
        for line in f:lines() do
            fc = fc .. line .. '\n'
        end
        f:close()
        frame = naughty.notify({ text = fc, timeout = 10, width = 320 })
    end),
    awful.key({ modkey, "Shift" }, "d", function ()
        awful.prompt.run({prompt = "Dict: "}, mypromptbox[mouse.screen].widget, function(cin_word)
            naughty.destroy(frame)
            if cin_word == "" then
                return
            end

            local fc = ""
            local f  = io.popen("sdcv -n --utf8-output -u '牛津英汉双解美化版' "..cin_word)
            for line in f:lines() do
                fc = fc .. line .. '\n'
            end
            f:close()
            frame = naughty.notify({ text = fc, timeout = 10, width = 320 })
        end, nil, awful.util.getdir("cache").."/dict")
    end),
    -- }}}
    ...
    ) -- globalkeys

简单说明一下，sdcv -u 参数后面跟的是字典名称，用 sdcv -l
可以查询现有的字典。推荐两本字典  

[xdict](http://prdownloads.sourceforge.net/stardict/stardict-xdict-ec-gb-2.4.2.tar.bz2?download)
(简要)，  

[牛津英汉双解美化版](http://prdownloads.sourceforge.net/stardict/stardict-oxford-gb-formated-2.4.2.tar.bz2?download)
(丰富)
