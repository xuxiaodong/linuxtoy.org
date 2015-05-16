Title: 全能的笔记软件——Evernote （3.0 beta）
Date: 2008-04-15 14:30
Author: Ning Bao
Category: Apps, Note-Taking
Tags: Beta, Evernote
Slug: evernote

我脱离Windows使用Linux已经有差不多快一年了，大部分Windows里的软件都可以在Linux中找到更好的替代。然而，只有一个东东我实在是很难割舍，那就是笔记软件[Evernote](http://evernote.com/)。其实，Linux里的Tomboy和Basket都是很出色的笔记软件，但它们只能用来检索管理已经数字化的信息。

在生活当中有很多时候我们是不能用电脑的，我们往往要用到纸和笔。就我个人来讲，我还没有那个本事在开会、听讲座的时候用笔记本电脑作笔记。还是用笔写比较快。

为了解决这个问题，Evernote提供了一项特别强大的功能，**它能够识别图形文档中的字符信息**。

[![Remember Everything - Capture what you like. Find it when you
want.](http://i.linuxtoy.org/i/2008/04/evernote.jpg "evernote")](http://i.linuxtoy.org/i/2008/04/evernote.jpg)

大家可以看以上的图片。有人在一张餐巾纸上画了草图，其中有“remember
EVERYTHING”这样的字样。之后，他可以用iPhone把草图拍下来，然后传给桌面软件Evernote。

于是，你如果在Evernote中输入“remember
everything”，就能很容易的找到你画的这张草图。

除了通过拍照片，你也可以扫描你的手写笔记。另外，还有一些Digital
Tablet，比如我用的[Adesso
Cyberpad](http://www.adesso.com/products_detail.asp?productid=294)，可以很方便地和Evernote同步我的手写笔记。

另外，Evernote还会自动识别你笔记中的一些简单图形，比如矩形、圆形……，然后矢量化。如果你的绘画水平很一般的话，Evernote会把你的图表修正得很漂亮。

有些人不单单把Evernote用来管理手写笔记，他们还利用Evernote的字符识别能力来管理照片（通过照片中的标语检索），或者用来管理收据等等。

Evernote的另外一项强大功能是它**可定制的笔记模版**。

笔记模版是标准的xml文档，你可以根据自己的需要设计笔记模版，例如下面的“处方药记录”和“菜谱”模版。

[![prescription](http://i.linuxtoy.org/i/2008/04/prescription.jpg "prescription")](http://i.linuxtoy.org/i/2008/04/prescription.jpg)

[![recipe](http://i.linuxtoy.org/i/2008/04/recipe.jpg "recipe")](http://i.linuxtoy.org/i/2008/04/recipe.jpg)

当然，Evernote还有各种检索方式，比如标签检索、时间检索、类别检索……Evernote还有很多非常好用的功能。我在这里只介绍上面最有特色的两个功能。总而言之，Evernote可以帮助你管理你所有的信息，能够让你在最短的时间里找到你要找的东西！

Evernote再好，也只能在Windows中用。我从2005年开始使用这个软件就一直在要求他们提供Linux的支持。他们的开发人员有很多也是Linux的忠实用户。他们告诉我其实他们也很想把Evernote移植到Linux平台上，可是他们的老板不允许。我也试着用wine来运行Evernote，可是不成功。所以，我一直要通过一个Windows的虚拟机来运行（其实用VirtualBox的Seamless功能就很好了）。

最近，他们推出了最新的3.0
beta版本，以下是一段[youtube的演示](http://www.youtube.com/watch?v=i_ncr1Ee9e8)。

在这一版本中有两个最大的变化：

-   提供了Mac OS X和移动平台的支持；
-   通过一个简单的bookmarklet，可以在浏览器中选择当前浏览的网页（全部或部分），成为新的Evernote笔记；

那就是Evernote的网页同步功能。过去，我只能在不同的PC之间（包括U盘）同步我的Evernote笔记。现在，我可以把我的笔记同步到Evernote的网站上，也可以在网站上直接编辑我的笔记。这一点意义重大，因为我也可以在没有安装Evernote的电脑上获取我的笔记了！

虽然这个版本还不支持Linux，但是我测试发现**3.0
beta可以在wine下面顺畅地安装和运行**！

目前，这个版本还没有正式发行，你必须要通过[申请](http://evernote.com/about/prereg/)，等侯成为测试版的用户。
