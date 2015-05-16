Title: 优化 Firefox 3
Date: 2008-07-06 10:02
Author: toy
Category: Tips
Tags: Firefox 3, Tricks
Slug: optimize-firefox-3

虽然 Firefox 3 相比 Firefox 2
在执行效能上有了很大的进步，但时间用长了还是让人颇有一种执行缓慢的感觉。OK，那就让我们来做一些优化，使
Firefox 3 运行更快些吧。

**减少 Awesome Bar 显示数量**

Firefox 3 新引入的 Awesome Bar
功能，我真的是很喜欢。我只需输入极少的字便能获得想要打开网页的建议。对我来说，默认的
Awesome Bar
显示数量似乎有些偏多。它经常要在停顿一小会儿后，才能完全显示出来。为了改善这个问题，我们可以通过减少
Awesome Bar 的显示数量来解决。具体操作步骤如下：

1.  在 Firefox 地址栏输入“about:config”，在确认警告信息后进入 Firefox
    配置页面。
2.  在 Filter 过滤框输入“browser.urlbar.maxRichResults”（或直接复制）。
3.  我们可以看到 Awesome Bar 默认的显示数量是
    12。双击该条目可以更改为自己想要显示的数目。当我设置为 5
    后，这种停顿的现象终于消失了。

**增大磁盘缓存容量**

随着 Firefox 打开的页面愈加增多，Firefox
似乎也变得有些迟钝起来。如果你担心 Firefox
同时会吃掉更多的系统内存，让其他程序无容身之地，那么可以增大 Firefox
的磁盘缓存容量。具体操作步骤为：

1.  地址栏输入“about:config”，并进入其配置页面。
2.  Filter 过滤框输入“browser.cache.disk.capacity”。
3.  Firefox 默认的磁盘缓存容量为 50000，也就是 50000
    KB。假如你的系统内存在 512 MB 至 1 GB
    之间，不妨将该值调大些，如设成“150000”。

**让 Firefox 在最小化时释放内存**

当 Firefox
最小化时，我们可以让它把占用的部分内存释放出来以供其他程序使用。具体操作步骤为：

1.  在地址栏输入“about:config”进入其配置页面。
2.  右击点选“New->Boolean”。
3.  在打开的对话框中输入“config.trim\_on\_minimize”。
4.  点击 OK 后，接着选择 true。
5.  重启 Firefox。

