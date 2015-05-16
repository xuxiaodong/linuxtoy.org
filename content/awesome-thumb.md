Title: Awesome 窗口管理器——缩略图技巧
Date: 2009-11-09 22:46
Author: vern
Category: Cli
Slug: awesome-thumb

如果你的桌面经常运行着两位数以上的虚拟终端，即使你为此定义了多个虚拟桌面(tag)，然而有时候你仍然会迷失。这就好像在
Firefox
浏览器里打开了20个页面，当你想要定位其中某一个的时候就显得不那么容易。

这里我讲的缩略图，并不像在文件管理器打开一个图片文件夹时显示的那样，但凭借窗口平铺的功能，结果很像那么回事。

[![](http://i.linuxtoy.org/images/2009/11/2009-11-09_1680x1050-400x250.png)](http://i.linuxtoy.org/images/2009/11/2009-11-09_1680x1050.png)

当我迷失的时候，我用 Meta-1 在 tag1 中查看所有终端的缩略图，通过
Meta-h/j/k/l 选中感兴趣的终端，接着用 Meta-Enter 跳转至该终端所在
tag。配置如下：

v3.3

    ...
    toggletags = {
        ["x-terminal-emulator"] = { screen = 1, tag = 1 },
    }
    ...
    -- Hook function to execute when a new client appears.
    awful.hooks.manage.register(function (c, startup)
        ...
        -- Check if the application should be floating.
        ...
        -- Check application->screen/tag mappings.
        ...
        -- Check application->toggletag mappings.
        if toggletags[cls] then
            target = toggletags[cls]
            awful.client.toggletag(tags[target.screen][target.tag], c)
        elseif toggletags[inst] then
            target = toggletags[inst]
            awful.client.toggletag(tags[target.screen][target.tag], c)
        end
        ...
    end)
    ...
    clientkeys = awful.util.table.join(
        ...
        awful.key({ modkey,           }, "Return",  function (c)
            if (c:tags()[2]) then
                awful.tag.viewonly(c:tags()[2])
            end
        end)
    )

v3.4

    ...
    toggletags = {
        ["x-terminal-emulator"] = { screen = 1, tag = 1 },
    }
    ...
    -- Signal function to execute when a new client appears.
    client.add_signal("manage", function (c, startup)
        ...
        -- Disable sloppy focus
        ...
        -- Check application->toggletag mappings.
        local cls = c.class
        local inst = c.instance
        local target
        if toggletags[cls] then
            target = toggletags[cls]
            awful.client.toggletag(tags[target.screen][target.tag], c)
            client.focus = c
        elseif toggletags[inst] then
            target = toggletags[inst]
            awful.client.toggletag(tags[target.screen][target.tag], c)
            client.focus = c
        end
        ...
    end)
    ...
    clientkeys = awful.util.table.join(
        ...
        awful.key({ modkey,           }, "Return",  function (c)
            if (c:tags()[2]) then
                awful.tag.viewonly(c:tags()[2])
            end
        end)
    )

简单说明一下。在 Awesome 新建一个窗口时，我们让它检查我们定义的
toggletags：该窗口的 CLASS 是否是 x-terminal-emulator (通过 xprop
命令可以查询某个窗口的 CLASS 值)。如果是的话，把这个终端添加到我们定义的
screen = 1, tag = 1 里面。
