Title: 用 OpenOffice.org 3.2 Draw 制作海报
Date: 2010-02-24 05:05
Author: lovenemesis
Category: Funny
Tags: openoffice.org
Slug: create-poster-with-openofficeorg-32-draw

OpenOffice.org 的 Draw 组件或许不像 Writer、Impress 和 Calc
那么常用，但是的确具有不少独特的功能，本文分享 OpenOffice.org 初学者
xiaohuanbear 童鞋用 Draw 制作海报的一些感想。**（软文，慎入！）**

先看最终结果吧，这是由 xiaohuanbear 童鞋在 Mac OS X 上使用
OpenOffice.org 3.2 Draw 制作的海报，也是他**首次使用 OpenOffice.org**
这一开源办公组件。

[![](http://i.linuxtoy.org/images/2010/02/bk-400x282.png)](http://i.linuxtoy.org/images/2010/02/bk.png)

*下面是 xiaohuanbear 童鞋对于 OpenOffice.org 的一些吐槽：*

-   **插入 OLE
    对象是很强大的功能**。通过它可以很方便的将用其他组件创建的内容整合到一起，插入后还可调用其他组件编辑很赞。海报里面所有的图表就是通过这种方式插入的。
-   **文本框的半透明效果在背后添加一个半透明的填充图片达到的**。尽管黑日白月说可以直接修改文本框的填充模式，但是我还是倾向这种方法。
-   **背景图片的设置不人性化**。若是使用自定义图片作为背景，需要通过
    Tools-Format-Area-Bitmaps-Import 先导入，然后才可以在
    Tools-Page-Background-Bitmaps 中找到。若是可以直接在
    Tools-Page-Background-Bitmaps
    中导入会方便不少。一般办公用户并没有查阅帮助的习惯。
-   对于拖放操作的行为比较迷惑。若是从其他地方拖动一个图片或者OLE组件入
    OpenOffice.org
    的话，它默认的行为是**创建指向到拖动对象位置的链接，而并不是复制**，和通过剪切板和插入对象有本质差别，然而在一般用户眼中是这三者之间应该是等效的。对于用户来讲，潜在的问题：当用户从桌面或者浏览器拖动图片进入
    OpenOffice.org 后，看到图片在预期位置出现了，以为图片已经被保存在
    OpenOffice.org
    里了。但是一旦删除桌面上的原始文件或者关闭浏览器后，留给
    OpenOffice.org 的就只剩错误链接的标示了。
-   **扩展的优势没有发挥出来**。应该像 Firefox
    一样提供一个精品扩展推荐，譬如 PDF
    编辑和精选模板很好用，但是若是没有他人告知一般用户很难发觉。
-   **平台优化和外观尚需努力**。 至少在 Mac OS X
    的启动速度和运行效率远不如黑日白月的 Linux
    平台，偶尔还会出现表格渲染错误的情况。尽管耐心+改变窗口大小可以解决，但还是有些恼人。

*吐槽结束*

现在，xiaohuanbear 童鞋已经把 Dock 启动栏上的 M$ Office 替换为
OpenOffice.org 了，他表示对于 OpenOffice.org
总体来说还是满意的，以后会更进一步的使用和挖掘它。

事后，在下以为 **可以针对用户的特殊需要而推广开源软件**。 拿
OpenOffice.org 来说，或许由于某些客观条件的限制以及使用习惯上的问题，
OpenOffice.org
难以立刻成为的主要办公软件，但是可以抓住某些特殊情形进行推广。譬如
xiaohuanbear 此次决定使用 OpenOffice.org 制作该海报就是由于 M$ 的
Publisher 并没有 Mac OS X 版本，决定尝试 OpenOffice.org Draw
的。同理，也可以针对有 “简单的 PDF 文件编辑”
需求的用户进行推广。一旦用户真正开始使用了，就有成为主要办公软件的可能性了。

**附：** 遵循 “署名-非商业性使用-禁止演绎 2.5 中国大陆” 协议共享的 [原始
odg 文件](http://dl.dropbox.com/u/464139/OOoDrawPoster/BK.odg) 及 [PDF
输出](http://dl.dropbox.com/u/464139/OOoDrawPoster/BK.pdf)。
