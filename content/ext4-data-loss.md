Title: 当心: Ext4 可能造成数据丢失
Date: 2009-03-20 10:57
Author: toy
Category: News
Tags: ext4
Slug: ext4-data-loss

正在使用 Ext4  

文件系统的同学可得当心了。据某些用户反映，它可能会造成你的数据丢失。国外一位  
Kubuntu Jaunty 的用户称，使用 Ext4
文件系统使他丢失了大量的数据，相关描述可参见位于  

[launchpad](https://bugs.edge.launchpad.net/ubuntu/+source/linux/+bug/317781)  
上的 bug 报告。

无独有偶，国内的 [albert748](http://cookinglinux.cn/ext4-lose-data.html)
也遇到了类似的问题。他描述道，X  
无缘无故死掉，断电重启后，发现 Firefox  
的配置丢了很多。与上面那位国外用户一样，albert748 也使用 2.6.28 内核和
Ext4  
文件系统。

今天，H-Online 刊登了一篇文章 [Ext4 data loss; explanations and  

workarounds](http://www.h-online.com/open/Ext4-data-loss-explanations-and-workarounds--/news/112892)，其中对此进行了解释，并包含
Ext4 开发者 Ted Ts'o  
提供的解决方案，有兴趣的同学可去看看。
