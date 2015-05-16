Title: 0 A.D 中文版
Date: 2014-05-27 13:24
Author: lovenemesis
Category: Games
Slug: 0ad-chinese-edition

0ad是一款类似于《帝国时代》的策略类3D游戏。通过OpenGL支持3D功能，同时可支持windows/Linux/Mac
OSX平台。并开放源代码。开发多年仍处于Alpha状态，但其可玩性还不错。最近发布的Alpha16里添加了许多新功能吸引了我的注意。其中最吸引人的时添加了对多语言的支持。*感谢
Henryliu 来稿*

但默认暂时缺少对中文的支持。同时还需要添加对CJK字体的支持。下面说一下处理过程：

一、
[按常规方式安装0ad](http://play0ad.com/alpha-16-patanjali/)（不限平台）。

二、
下载east-asian-locales包，该档源自于这里，请从[这里下载east-asian-locales-0.0.16.zip](http://trac.wildfiregames.com/wiki/Installing_East_Asian_Locales)。这个包里包含有0ad适用的CJK字体（你也可以自己mod替换其它字体）。

三、
下载0ad适用的po中文翻译档，该档源自于[这里](http://trac.wildfiregames.com/wiki/Installing_East_Asian_Locales)，请从这里分别下载for\_use\_0ad\_engine\_zh.po和for\_use\_0ad\_public\_zh.po并分别改名为zh.engine.po及zh.public.po下载前需要登录。不另外提供下载了，也是表示对该翻译项目的一个支持吧（动机有一点点不纯喔）。在本文发表时public翻译档完成度68%。

四、
如果你使用Windows平台，则可以直接使用east-asian-locales-0.0.16.zip，按第二步链接里的方法操作。你需要额外做的就是将zh.engine.po及zh.public.po两个档放进east-asian-locales-0.0.16.zip的l10n目录下。

五、
不限平台直接修改public.zip（Linux平台该档一般位于/usr/share/games/0ad/mods/public/public.zip），将east-asian-locales-0.0.16.zip内fonts目录所有文件替换进入public.zip同目录。再将zh.engine.po及zh.public.po两个档置入public.zip内l10n目录下（可以先解压public.zip，修改完后再压缩）。

六、 进入游戏，应该就是中文界面了。也可以直接切换不同的语言界面。

顺便说下对0ad的感受。虽然说是开源版的《帝国时代》，但其AI处理方式有明显的不同。比如在0ad里建立市政中心后周围就是你的“势力范围”，别人不能在你的地盘上搞建筑。另外该游戏对电脑显卡的要求颇高，使用大地图及超过300人上限可要注意了，在游戏的后期或许你只能欣赏慢动作了。还有，你可不能像《帝国时代》那样前期只需管经济，在0ad可能开玩不多久便“兵临城下”了，而且黑压压的一片。这里告诉你一个窍门，在同一个地方同时建几个兵营，全部选中后可同时出多个士兵，这样电脑中级AI怎么也玩不过你了。呵呵

[点击此查看效果图](https://k9bk8w.by3302.livefilestore.com/y2pukPI_OxZWvOFwUXGMTL3_ntSy6Ns1YkYjkw2IvoKANkyLplyS1IukyECNlEPZsRZnAYZrWJOxkI8JBSJ-dnNZVetsZ7xvtIcohG6YUo5wdI/0ad.png?psid=1)

*编者注：*此文所述的中文支持为 Hack 方式，若想完美体验，请加入 [0.A.D
的中文本地化项目](https://www.transifex.com/projects/p/0ad/)。
