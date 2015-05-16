Title: 也谈“支付宝为苹果与Linux用户准备无控件支付方案”
Date: 2011-08-15 16:01
Author: lovenemesis
Category: Reviews
Tags: Alipay
Slug: review-alipay-provides-plugin-free-payment-method-for-apple-and-linux-users

今日[支付宝官方博客发布网志，宣布为“苹果和Linux用户准备无控件支付方案”](http://blog.alipay.com/2447.html/)。不过作为
Linux 用户，您可能不幸的被“无控件”了……

背景知识[请点击此查看原文(原文授权协议与本站所用不兼容，故不转载)](http://blog.alipay.com/2447.html/)

[那么这张图该怎么理解？这里不是依然标注的 Linux
需要安全控件么？](http://blog.alipay.com/wp-content/2011/08/2011-08-15_140142.png)

[支付宝官方博客的仙客](http://blog.alipay.com/2447.html#comment-15306)点出了要点，原来**支付宝存在安全控件和数字证书控件两种控件！**

可是目前 Linux 平台下仅有一个[版本为 1.0.3.20
的安全控件](https://download.alipay.com/alipaysc/linux/aliedit/1.0.3.20/aliedit.tar.gz)，[用户反馈的情况是不支持数字证书登录](http://linuxtoy.org/archives/4516.html)，支付宝也没有提供
Linux 平台下单独的数字证书控件。

仔细研读原文，发现原来是这么一回事：

**支付宝安全产品在原先的数字证书基础上，增加了“宝令”和“手机动态口令”两种。若是原先已经使用了“数字证书”的用户，可以转而使用其他两款安全产品。之后在未提供安全证书控件的
Linux 系统上就可以通过安全控件实现支付啦！**

个人认为，这种说法与标题中的“无控件支付方案”差距甚远，而这个不知道是不是官方人员的[仙客](http://blog.alipay.com/2447.html#comment-15306)评论也太过于牵强：**本来
Linux 平台就没有数字证书控件，何来省去一说？**

可能是这位朋友**误以为**先前发布的[支付宝 Firefox
数字证书控件](http://blog.alipay.com/2261.html)可以用于 Linux
的。可惜实际情况并非如此……  
顺便吐槽下[支付宝的 Linux
平台安全控件安装图文教程](http://help.alipay.com/lab/help_detail.htm?help_id=240951)……  
另外，个人在这里有个小小的希望：**希望支付宝的 PR 们在发表和制作 Linux
相关文档和博文时，麻烦先询问下公司中使用 Linux
工程师们吧……**据我所知，他们人数不少哦～

这个事情总体上来讲也算是好事情，**至少现在 Linux
平台下的支付宝用户们有了除数字证书以外的其他“安全产品”可以选择**。不过作为国内领先的电子支付平台，**支付宝距离像
Paypal 一样的真正“无控件跨平台安全支付”还有相当长的道路**。
