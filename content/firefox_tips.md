Title: Firefox 使用技巧两则
Date: 2006-08-03 15:06
Author: toy
Category: Tutorials
Slug: firefox_tips

新学到的 Firefox 使用技巧两则，与大家分享。

1.使用鼠标中键直接打开剪贴板中的网址

在 Firefox 地址栏输入 `about:config`，将 `middlemouse.contentLoadURL`
设置为“true”。现在来试一下，随便拷贝个网址，在 Firefox
窗口中按下鼠标中键，看看，Firefox 是不是已经打开了？

2.更改 Firefox 搜索栏的默认大小

你是否觉得默认的 Firefox
搜索栏太小不方便输入呢？不用担心，我们马上就来改造它。

(1)`cd .mozilla/firefox/*.default/chrome`

(2)`mv userChrome-example.css userChrome.css`

(3)编辑 userChrome.css，添加下列代码：  

` #searchbar { -moz-box-flex: 400 !important; } #search-container { -moz-box-flex: 400 !important; }`

OK. 重启 Firefox 吧。

[[via](http://www.pixelbeat.org/settings/firefox/)]
