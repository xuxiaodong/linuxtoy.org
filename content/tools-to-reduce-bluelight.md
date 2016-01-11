Title: 降低屏幕蓝光的小工具
Author: lovenemesis
Date: 2015-12-08
Category: Tools
Tags: bluelight
Slug: tools-to-reduce-bluelight
Summary: 近日一则来自哈佛医学院旗下的哈佛健康出版社的报道，又引出了一番关于蓝光可能对人体造成的危害的讨论。

[哈佛健康报道1](http://www.health.harvard.edu/press_releases/light-from-laptops-tvs-electronics-and-energy-efficient-lightbulbs-may-harm-health)
[哈佛健康报道2](http://www.health.harvard.edu/staying-healthy/blue-light-has-a-dark-side)

简单来说，上述两篇报道中分别提及多项研究，这些研究讨论了 LED 以及现代以 LED 为光源的电子设备（绝大部分手机、平板及平板电视）带来的蓝色光在夜间对人类的作息和睡眠的负面影响。这些影响包括更高的糖尿病风险、睡眠节率紊乱以及体内褪黑素水平降低。尽管目前仅仅是**相关研究**，作用机制完全不明，不过两篇报道依然给出了一些建议，指导人们如何降低夜间生活中的蓝光。

精明的商家当然不会放过机会推出配套产品，放开某宝上铺天盖地的防蓝光贴膜，从[抗蓝光电视](http://www.amazon.cn/dp/B00U0T5UVA/) 到[具备防蓝光模式的平板电脑](http://www.amazon.cn/dp/B014JWQ78S/)，“防蓝光”已经俨然成为和“降雾霾”一样的卖点了，尽管原理其实很简单，成本也不高……

所以借助本文提及的一些小工具，完全可以避免为这些“防蓝光”产品额外支出：

#### Linux 平台：[Redshift](https://github.com/jonls/redshift)

一款开源小工具，会根据当地时间在夜晚时段降低屏幕色温，既可以在命令行唤起，亦可通过托盘小程序控制。它已经被包含在各大发行版仓库中。在 Fedora 中安装方式如下：

`sudo dnf install redshift-gtk`

注意启动后它会请求位置服务，根据所在位置来确定自动切换时机：白天默认 5500K，夜间 3500K。

#### Android 平台：[J抗蓝光](https://play.google.com/store/apps/details?id=com.jintin.jbluecut.free)

Android 平台有一大堆起到类似效用的工具，这款属于干净且没有要求无关权限的。提供任务栏快速控制，且可以自定时调整。若是觉得好用的话，可以选择购买[功能更全面的 Pro 版](https://play.google.com/store/apps/details?id=com.jintin.jbluecut)。

经测试该程序亦可在亚马逊 Kindle Fire 系列平板使用。


其实对于需要长期面对电脑屏幕的程序媛和攻城狮，缓解眼部疲劳最有效的措施恐怕是“多喝水”和“常走动”了吧……

