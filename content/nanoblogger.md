Title: NanoBlogger: Unix命令行打造的Blog引擎
Date: 2008-07-28 23:42
Author: lwl
Category: Apps
Slug: nanoblogger

[NanoBlogger](http://nanoblogger.sourceforge.net/)是一款使用Bash编写的Blog引擎。它的特点如下：

-   模块化代码，高度可定制性和扩展性，汉化也很简单。
-   支持多个博客。有全局(nb.conf)和博客(blog.conf)配置。
-   生成静态页面，不需要服务器端脚本，也不需要数据库。
-   其他博客的常见功能都有，如日历、分类、atom、rss
    feed。没有评论和trackback功能，但是通过修改模板，可以使用其他网站提供的服务，例如它的官方网站就使用了[HaloScan](http://www.haloscan.com/)的服务。
-   可以使用自己喜欢的编辑器来写作，例如vim，你可以制作模板，利用快捷键跳转。
-   文件格式可以是raw
    (html)、markdown等。理论上你可以使用任何标记语言来编写，例如txt2tags，只要它能转换成html。编写对应插件也是非常简单，看看自带的markdown.sh就知道了。注意entry和page的插件不是完全一样。
-   因为使用了bash、cat、sed和grep，速度较慢。虽然号称增量更新，但是文章多了之后，速度会非常慢。我的用法是使用模板在特定目录(data或者articles)下进行写作，使用cron来每天定时强制更新和上传。
-   [![](http://i.linuxtoy.org/i/2008/07/screenshot-20080729_0131-340x331.png)](http://i.linuxtoy.org/i/2008/07/screenshot-20080729_0131.png)

[NanoBlogger](http://nanoblogger.sourceforge.net/) <span
style="line-through;">(可能需要翻墙)</span>
