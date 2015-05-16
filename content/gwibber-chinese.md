Title: 小技巧: 让 Gwibber 显示中文
Date: 2009-03-15 17:59
Author: toy
Category: Tips
Tags: Gwibber, Twitter
Slug: gwibber-chinese

在写了《[Gwibber: 支持 Twitter、Identi.ca、Facebook
等的微博客户端](http://linuxtoy.org/archives/gwibber.html)》一文后，便有朋友在
Twitter 上问我如何让 Gwibber
显示中文，现在又有读者留言询问同样的问题，索性我就在此多罗唆几句。

![Edit Gwibber
theme](http://i.linuxtoy.org/images/2009/03/gwibber-theme.png)

因为 Gwibber
包含多个主题，这里就以修改默认主题为例来说明如何让其显示中文：

1.  转到 Gwibber 的默认主题目录，通常是
    /usr/share/gwibber/ui/themes/default/：  
    `cd /usr/share/gwibber/ui/themes/default/`
2.  打开 theme.html 文件（需要 root 权限）：  
    `vim theme.html`
3.  找到 font-family 那行（在 26
    行），在冒号后添加中文字体名即可，如"Droid Sans
    Fallback"。(参见上图）
4.  保存修改。

这样，你就可以在 Gwibber 中看到漂亮的中文了。
