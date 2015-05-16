Title: 通向 KDE 4 之路（十）：Oxygen 美工项目和图标
Date: 2007-03-09 20:51
Author: toy
Category: Apps
Slug: the-road-to-kde-4-oxygen-artwork-and-icons

KDE 4 的视觉效果由于 [Oxygen 图标集](http://oxygen-icons.org/)引入
kdelibs
而发生了翻天覆地的变化。这次的引入过程仍在继续，其中还包括一个影响了数千个文件的大型图标命名方案的改变。但是
Oxygen 美工项目不仅仅是图标集，它是 KDE 4 中统一的美工效果。Oxygen
中不可或缺的 SVG 部分为很多具备 SVG
显示功能的程序带来了全新的风格体验。下面是详细内容。

请注意我今天所展示的美工效果仍然还只是进行中的工作图而并没有完全定型，但这种从
KDE 的 SVN 库中编译出来的效果正是 KDE 新的默认效果。Oxygen 将是 KDE 4
的新美工方案，但其中的各个元素仍可能变更。Oxygen
团队将很乐意在评论中看到您对今天所演示的效果的任何有意义的反馈。

在一月份，我在[第一篇通向 KDE 4
之路文章](http://linuxtoy.org/archives/the-road-to-kde-4-svg-rendering-in-applications.html)中向大家展示了一些
KDE 4 中的 SVG 技术，这项技术大部分应归功于 Qt 的新 SVG
显示功能。在那篇文章中的部分美工正是 Oxygen
团队的作品。过了两个月了那些图形又多了很多改进，但真正最大的视觉改变还是新
Oxygen 图标集的被引入 kdelibs，并作为新的默认图标。

Oxygen 实在是个庞大而远未完成的项目，图标集只是它的一部分而已。Oxygen
有句非正式的标语：“让看到您的桌面就像呼吸清新的空气”，它带来的是整个 KDE
环境的视觉感观的新体验。Oxygen
团队由一群开发者与艺术工作者组成，他们致力于让 KDE
看起来很漂亮。他们不仅带来了明亮的效果，还保证 KDE
有一个统一的、易于辩识的界面。例如，竖立于工具栏上的图标在它们下部都有相同的阴影，这就带来了一致的视觉效果。在美工中构建起来的调色板确保了图标之间的和谐，并仍有相当好的可辨别性。所有图标都是用
Inkscape（或其它有 SVG 功能的程序）做出来的 SVG 文件，而这些 SVG
文件也非常易于调整。

我们现在也有了一个正式的 KDE 4 图标命名方案。以前的 KDE
图标命名方案都是随着 KDE
的发展而逐步演化生成的，所以在很多地方都显得很随意。Oxygen
团队这次直接开发了一套命名方案，而且他们是将之作为 freedesktop.org
的一部分来做的，这使得未来 KDE 与其它桌面环境在图标的命名上不会混淆了。

好了，对 Oxygen 的文字描述告一段落，下面请看一些 Oxygen 的图片描述。

下面是一张显示 Oxygen 图标的 Dolphin 文件管理器的截图，以及一张 KDE
3.5.6 中 Konqueror
的截图，它们打开的是同一个文件夹。当然预览功能打开的时候，很多类型的文件也可以预览。

[![Dolphin](http://i.linuxtoy.org/i/2007/03/vol11_4x_dolphin_s.png)](http://i.linuxtoy.org/i/2007/03/vol11_4x_dolphin.png)

[![Konqueror](http://i.linuxtoy.org/i/2007/03/vol11_356_konq_s.png)](http://i.linuxtoy.org/i/2007/03/vol11_356_konq.png)

您可以注意到在 Dolphin 截图中虽然有 Oxygen
的新图标代替了老图标，但仍有些老图标依然可见。在 Oxygen
图标引入的过程中，图标的名字被改变了。老的代码也许还用着老的图标名字，还没有使用新的修正过的
Oxygen 图标名。当原来的水晶 SVG 图标从 kdelibs
中删掉后，老图标名的影响就会消除了，而新图标就会显得更清晰了。对于那些更喜欢老图标的朋友们，在
KDE 4
中也将会对老图标重新命名后作为一种图标主题提供给大家，它们将被包含在
kdeartwork 包中。

Oxygen 图标目前已被设为默认，您也将会在所有以后的“通向 KDE 4
之路”系列文章中看到它们，而大家肯定会对这套美工的完整性表示欣赏的。当然一些图标仍有进一步提升的空间，这要多谢
SVG 源文件的使用了。我不会在本文中提供完整的 Oxygen 图标集，大家可以在
[websvn](http://websvn.kde.org/trunk/KDE/kdelibs/pics) 中或通过自己构建
KDE 4 来看到它们。下一个 KDE 4 的快照版当然会将这套图标集包含在内。

但是我还是得重复这句话：Oxygen 不只是一套图标集。Oxygen 美工在 KDE 4
中处处都有所体现。这是 KDE 4 新的注销对话框的一张截图。

![KDE 4 Logout](http://i.linuxtoy.org/i/2007/03/vol11_4x_logout.png)

在整个 KDE 中使用 Oxygen
图标所带来的最大的好处是它（几乎）与图像分辨率无关。这个意思是某些程序可以缩放到任何尺寸，它的视觉表现依然很好。例如，如果您在玩
KDE 游戏中的 KBounce，您想要让它变大或者变小，它就会调整到您想要的尺寸。

[![KBounce](http://i.linuxtoy.org/i/2007/03/vol11_4x_kbounce_s.png)](http://i.linuxtoy.org/i/2007/03/vol11_4x_kbounce.png)

KDE 4 并不是一个分辨率无关的桌面环境，这也不是当前 KDE
的努力目标，但某些 KDE 组件的确建立在分辨率无关的基础上。

Oxygen 的另外两个部分仍在开发中，它们还没有完成。它们是 Oxygen
器件风格和 Oxygen 窗口装饰。这两个组件还没有被 KDE 4
设为默认，因为它们远未成熟。也正是由于它们还不是 KDE
默认，所以我也不想现在就把它们展示出来。但大家须知 Oxygen
图标与相关的美工只是 Oxygen 项目中的一部分。Oxygen
团队在程序风格和窗口装饰上有很大的进展，但整个项目实在是巨大的工程。

KDE 4 中的其它可视化元素并不都直接由 Oxygen
团队完成，但那些工作也会在必要时与 Oxygen 项目协同工作。它们是 KWin
中的合成显示分支，还有 Plasma 的工作区主题功能等。

有兴趣参与 KDE 的美工创作的朋友们可以访问 irc.kde.org 的 #kde-artists
频道与一些美术工作者相交流。他们非常友好，对专业或非专业人员的建设性回馈意见他们都执同一态度。

单个的 KDE 项目也在寻找美工帮助：最近 Kalzium 的 Carsten Niehaus
发出邀请，希望有人帮助制作一些可爱的元素图标，这些图标将与一个可选的对小孩子比较友好的界面配套。有兴趣的朋友请访问
#kalzium 的 irc 频道。

Amarok 项目最近也告诉我他们的 Amarok 1.4.6（运行于 KDE
3.5.x系列中）也需要一些美工帮助，这些美工不需要是 Oxygen 风格的，因为
Oxygen 风格是 KDE 4 的计划。如果有兴趣，请与 #amarok 中的“markey”联系。

评注旁白：我很高兴有很多朋友对 KDE 4
的开发抱有兴趣，但也请提出有助益的反馈以帮助 KDE 4
使之得到改进。很多开发者们查看了在
dot.kde.org上的评论，并针对用户的建议中有意义的部分在各自的程序增加了新特性。例如
Peter Penz 在 Dolphin 中实现了树状查看功能，Rafael Fernández López
也通过反馈对工作进度管理器作了改进。很欢迎大家多提建议，但上周的文章帖出之后，评论乱了套，这就很难从中选出有意义的东西。不过上周也着实破了
dot.kde.org 的评论纪录了。很希望某天我们在欣喜 KDE 4
进步之余再破一次纪录。下周见。

[原文](http://dot.kde.org/1173332156/) by Troy Unrau  
[翻译](http://www.myswear.net/forum/viewthread.php?tid=7927) by
yuanjiayj
