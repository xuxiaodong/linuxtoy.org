Title: 独家：Hotot 作者 Shellex 专访
Date: 2011-09-14 13:12
Author: lovenemesis
Category: Featured
Tags: hotot
Slug: exclusive-interview-with-hotot-founder-shellex

给 LT 读者朋友们迟到的中秋节大餐：Hotot 开发者 Shellex 独家专访。Here's
the mooncake for the LinuxTOY fans: Exclusive Interview with Shellex,
the founder of Hotot.

*Scroll Down for English Version*

**黑日白月: 很高兴在 9/11 这个日子可以采访 Hotot 的开发者 Shellex
，晚上好啦！**

shellex: 黑月好 ……^\_^ 9.11这个日子很特殊啊。。

**那么，先给读者朋友们介绍下自己吧！**

我叫 @shellex ，是一个... 嗯，喵星人... 现在呆在北京。

**哇，还是保留神秘本色啊 。**

一点都不神秘... 其实很多人都见过我的啦。

**哈哈，肯定没有 Hotot 的用户多啊。聊聊当初是怎么想做 Hotot 的吧~
相信很多朋友对此都很好奇。**

嗯，最初的时候，是 @doublechou 说，壳酱，做个 Twitter
客户端吧。于是就有了这个 Twitter 客户端。

好吧，真实情况是当时 Linux 下 的 Twitter 客户端 Gwibber
太破了，逼着大家用 AIR 客户端。于是不得不自己做个顺手的。

**AIR 的，是指 Spaz 么？**

我当时用的是 twhirl，Spaz 倒是没用过。

**哦……既然这么说，那么可不可以回想下当初进行 Hotot
设计的时候，特别注意的地方呢，比如上面提到的其他客户端的不足？**

不过后来各种 Twitter 的客户端雨后春笋般出现了，大家的选择就多了。

说起来，Hotot确实经历过几次大的变化。

**愿闻其详**

最初的时候，Hotot 是完全使用 GTK 来作为 GUI 的，直到发现使用 Webview
处理大量小对象更加得心应手，于是将 Tweet 列表使用 Webview 来显示。

紧接着发现 Native 的 GTK 外观看上去如此笨重，不如将所有 UI 都用 Web
技术来实现好了。既然这样，那么所有的 U I逻辑都使用 JavaScript
重写了一遍。  
而 Python
只处理和操作系统紧密相关的部分，比如通知和文件系统访问。哦，还有网络。

到最后，我和花喵 @shellexy 把对 Twitter 的 HTTP 请求也用 JavaScript
实现了，那么 Python 所需要做的工作就越来越少，于是就可以平滑移植到
Chrome 下了。关于移植到 Chrome，一是为了别的平台的同学也能用上；二是对
WebkitGTK 的性能和特性表示不满。Chrome 更能满足我们。

（其实现在我和花喵都用 Hotot for Chrome，而不是 Hotot。

**哇，会不会独立的版本在某个时间会退役呢？**

唔，应该不会吧...除非 Linux 桌面死了...

现在 Hotot 就是一个 Web App 罢了，放到任何一个 Webkit
实现的容器里都能跑起来。

**恩……可不可以说某一天会看到 Qt 版本的 Hotot?(笑**

这个在开发初期就讨论过呢...甚至还曾经存在一个 Hotot-QT
的大分支，不过嘛，后来有了 Hotot for
Chrome，这个QT外壳计划就搁置了咯。W(**编者注：**在本采访发稿之际，
@CSSlayer 写出了 Hotot-QT )

不过欢迎大家往各种 Web 容器里移植。因为现在 Mac 和 Windows 下都没有独立
Hotot。

**很有意思哦，Hotot 为了跨平台，首先选择了走向 Web
App，而不是使用跨平台的 GUI
框架。这是基于技术上的考虑？未来趋势的把握？还是铬粉的原因？**

其实我是个 JavaScript 苦手，因为之前没写过什么 Web
的东西，所以这些代码亮出来后被鄙夷了很久的呢。之所以选择
Web，是有先例的（以前写过一个笔记软件，啊，是个坑，也是 Web
技术的，坑了）。

当时认为 Web App 是未来啊。被 Google 洗脑的，因为当时 Google 的 Web
产品那么多……也许在很多环境下 Web App 还是太前卫了，但是现在我还是相信
WebUI 即使对本地程序也是一个很好的选择。

Web 技术做 UI 不是什么新鲜东西。很早就有人在 Delphi 和 VB 的程序中使用
IE 的控件来画用户介面。现在那个豌豆荚我记得也是用 WebUI 的。

**很精准的把握哦~现在 Hotot Web App
的设计似乎也打开前往移动平台的道路，有没有考虑像 Amazon CloudReader
那样做个 iPad 版本？**

…嗯，我保证会有（如果大家能捐赠我一些设备用于开发的话。其实现在花喵
@shellexy 有在慢慢地做 Hotot 的移动设备版本，但是还没到能用的程度。

**哦？好消息啊~ 很好奇 Hotot 的开发团队的规模，到底有几个人呢？**

唔，我算是发起者吧，目前活跃的开发者是三人，花喵
@shellexy，校内改造器的作者 @xnreformer， 还有我 @shellex 。设计师是
@OickilL 和我。Lanuchpad PPA的维护者是吉米 @jimmy\_xu\_wrk。之前 TX主席
@Tualatrix 也有参与过。另外还有很多朋友直接提交了patch，谢谢（鞠躬

**很紧凑的团队啊！**

呃？是么？但是我们有一半人都没有见过面呢。这种事情也只有在开源世界才会看到什么的吧。

**啊……如果你们举办个 Hotot 开发者和用户会议，一定会很受欢迎呢！**

太抬举了哦...其实Hotot的用户量很少呢——因为一直没有正儿八经地发布过。本来想磨蹭到1.0再说，但是不知道为什么被某西语社区发现了我们的托管站点，于是就慢慢有用户了。

不过也好。。如果没有这批用户，估计这个project又坑了。。所以我希望大家来用哦——来提意见提patch哦。

**说到这里，在 Hotot
的开发过程中，对于用户需求、错误汇报、文档、补丁审核等代码之外的工作，是如何进行的呢？**

目前的 Feedback 制基本上只有两条：直接上 Twitter
@我们，或者去代码托管那地儿去发
Issue。在正式版本发布前期望能提供一条方便的渠道来收集用户需求和错误报告。至于文档和补丁这些就继续沿用现有的方式好了。

**有没有考虑邮件列表 IRC 之类的传统开源项目反馈路线？**

其实有一个 Google Group 啦... 在
https://groups.google.com/forum/#!forum/hotot。IRC
的话不大适用。因为我们都是兼职，Hotot 的用户群体也属于小众，开 IRC
人不会很多的说。

**原来如此。对于 Hotot 下一步的发展有什么样的计划呢？偶找不到路线图……**

唔，确实没有路线图。现在基本上是想到什么就做什么。不过大方向还是有的，某些特性——比如多账户支持啦，多协议支持啦，Mac
独立版本啦——都在计划内。但是没法提供一个保证来说明第几个版本能完成。

不过短期的计划确实有。比如在0.9.8会做一些小优化，主要在用户体验方面。Kismet
的用户介面也计划在下个版本完成。也在想办法减少 Memory
Footprint。当然说不定到时候有什么想法就直接实现了，所以如果届时大家看到什么变化也不要惊讶。。

**什么时候会到 1.0 呢？不要学 Wine 哦~（笑 相比 Chrome 版本帝，Hotot
的保守的多呢**

其实我们的期望是在 2012 世界末日到来之前能让 1.0 见见阳光（笑

**代号 Ark ？ (大笑**

嗯，在 1.0 以前，codename 都会沿用
Ada，为了纪念世界上第一名（女）程序员。当然了，Ada 也可以有别的意义…

但是在 1.0 的时候会有一个特别的 codename，啊，我保留这个权利的。

**哈哈，粉丝们可要记住哦~ 对了，既然你这么喜欢猫咪，为何选用 Hotot
这个兔子样的名称？**

因为作为啮齿动物，兔子是很好吃的。

好吧，因为兔子也很可爱。我也很喜欢兔子。另外就是 Hotot
这个名字看上去挺可爱（虽然读起来不大可爱

**哈哈，的确如此呢~除了 Hotot，还正在参与其他什么开源项目么？**

目前别的开源项目啊，基本上没有参与的了（太忙了呢

有空的话以后也许能帮花喵和计算机科学屠戮者捣鼓下输入法

别的暂时也没啥计划。研究生很累的

**恩恩，YY 下能从输入法直接发推，貌似很有趣哦~**

实现起来倒是很简单，交给 @CSSlayer 几个小时就搞定了吧

**哈哈，小企鹅输入法的用户们注意了哦~**

其实现在 Twitter 客户端基本上饱和了吧，就连 Twitter
自己都不再鼓励大家开发客户端了。

本来使用第三方客户端的用户就已经比较少了吧，我对此的反应是需要给 Hotot
增加一些别人没有的东西。另外就是确实可以放慢一点脚步了。以后说不定会开启一些别的项目。

**哦？会是哪个方向呢？还是社交网络么?**

唔，这个暂时还没什么想法。这种事情都是厚积薄发吧

**好的，很期待看到你的新开源项目 （ 应该会是的 Web App
吧，无责猜测，哈**

这个可不一定哦...我的本职工作是写 Linux C 的...

**更有意思了，本职工作是 Linux C 的，却用 Python + JavaScript
去解决遇到的 Linux 桌面应用问题~**

因为 Linux 桌面太破了嘛。

我觉得语言还是能决定点东西的。如果某语言用起来很麻烦，也许开发者们就懒得去做某些特性了。

**这样子看来，Hotot 算是代表了一个解决 Linux
桌面应用开发难的问题新思路：用 Web App 。可以这样说么？**

嗯，其实 Gnome Shell 和 KDE 也有这样搞的吧。

话说 @shellexy 挖了个大坑那就是一个纯 Web 技术的
DE，该坑还处于理论阶段。

**哈哈，永远欢迎爆料~ 恩，最后，有什么想对 LT 的读者朋友/Hotot
的用户/你个人的粉丝想说的话么？**

呃，希望大家“心里都充满爱与悲伤”这样？

**呃，好吧，Hold 住了……**

恩，那就说这句吧。。希望大家心里都充满爱与悲伤。

（握手

**(握爪**

（蹭蹭

*English Version:*

**Tommy: Good evening, Shellex. Very glad to have a chance to chat with
you on this special day.**

shellex: Evening, Tommy. 9/11 is indeed a special day...

**Well, would you please introduce yourself to the readers?**

I'm @shellex, well, a creature from Kitty-Planet. I'm currently living
in Beijing.

**Still won't say too much about yourself.**

It's not, many people have met me in person.

**I bet it's not as many as the Hotot users. How about talking about
what makes you start the Hotot. I believe many of us are quite curious
about that.**

Yeah, it all began with the words from @doublechou "hey, @shellex, how
about making a twitter client?". So it happened.

Well, the truth is at that time Gwibber, the native Twitter client under
Linux wasn't that good. We had to use AIR-based one. So I think it would
be better to write my own.

**AIR-based one, you mean Spaz?**

I was using twhirl before, haven't used Spaz before.

**I see... Then can you recall anything special during the design of
Hotot, perhaps the things missing from the clients mentioned above?**

Eventually, the Twitter clients spring up like mushrooms. Now we have
much broader options.

As saying, Hotot has experienced several big changes indeed.

**Pray continue.**

At first, GUI of Hotot was completely rely on GTK until we found Webview
provides a better flexibility when dealing with large number of small
widgets. So the list of tweets was rewritten using Webview.

Then we felt that the looking of native GTK so cumbersome. We could
apply the Web technology to all UI elements. Thus all the UI logic were
rewritten with JavaScript. Only the OS specific events were handled by
Python. Oh, network layer, too.

At last, @shellexy and I implemented the HTTP request to Twitter with
JavaScript, further reduce the dependency on Python. A step closer to
port to Chrome. The Chrome port is considered to a) make it accessible
to the users on other platforms; b) express our unsatisfactory against
the performance and feature of WebKitGTK. Chrome suits our needs best.

BTW @shellexy and I mainly use Hotot for Chrome, not the standalone
Hotot.

**Woo, does it mean that the standalone version might be retired some
time in the future?**

Hmm, perhaps not, unless the Linux Desktop is dead.

Currently Hotot is a Web App which can be run under any WebKit
container.

**Well, can I say that we might see a Qt based Hotot some day? :)**

e had discussed it in the early phase of development. There used to be a
big branch named Hotot-Qt. However, this development of this branch was
ceased due to the birth of Hotot for Chrome. (**Editor:** Just before
publishing this interview, @CSSlayer wrote the Hotot-QT.)

Still, we are very welcome to anyone trying to port Hotot to any Web
container because the standalone version on Mac or Windows doesn't exist
at the moment.

**Very Interesting. To be cross-platformed, Hotot chose the path of Web
App, instead of the cross-platform GUI framework. Is it from a technical
consideration, the belief of the tendency, or just the gut of Chrome
fan?**

Actually I'm not THAT good at JavaScript since I hadn't coded Web
before. Not surprised for being mocked when open sourcing the source
code. But I had written a Web based notepad (discontinued after all)
before.

I was brain-washed by Google at that time to believe Web App was the
future. A lot Web Apps Google has! But perhaps in many circumstances Web
App is way too ahead of the time. However, I still believe WebUI is a
wise choice, even for local applications.

Using Web technology to build UI is nothing new. Someone had
demonstrated embedding IE widgets into GUI in Delphi and VB application.
If I'm right, [Wandoujia](http://wandoujia.com/) is drawn in WebUI, too.

**Wise choice. The Web App design seems to make the mobile port quite
feasible. Have you ever consider to develop an iPad version like Amazon
CloudReader?**

It will be, I promise, if someone would like to donate some devices for
development. Actually @shellexy is working on mobile version of Hotot,
but slowly and immaturely.

**That's really good to hear. I'm wondering how many members there are
in Hotot developer team?**

Well, I'm kind of the project initiator, with other two active
developers: @shellexy and @xnreformer (Xiaonei Tweak). Designers are
@OickilL and me. @jimmy\_xu\_wrk is the PPA maintainer. The author of
Ubuntu Tweak, @Tualatrix was once our member, too. Also, many friends
send us patch. Thank you! (Bow

**That's quite small!**

Really? Half of our team members haven't meet in person yet. I guess
this story could only happen in open source world.

**Fans would cheer if you hold something like a Hotot User and Devloper
Night :)**

I'm flattered. Actually the user base of Hotot was relatively small
since we have never officially release yet. I intended to wait until
1.0. But somehow our project host site was discovered by a Spanish
community. Then the number starts to grow gradually.

Don't get me wrong. It turns out to be very well. Without those early
adopters, this project might be dead like my previous one. Suggestion
and Patch are highly welcome!

**Right now, how is the user feedback, bug tracking, documentation and
patch review going on Hotot development?**

Right now, there are only two ways to give us feedback. One is to tweet
us dirtecly, the other is to file a issue on code project host. I'm
looking a way to provide convenient user suggestion and bug report
before official release. The documentation and patches will continue
using the current method.

**Have you considered the traditional way in open source project, such
as mailing list or IRC?**

We actually have a Google Group on
https://groups.google.com/forum/#!forum/hotot. IRC might not suit us
since we're part time and minority.

**Sounds reasonable. What's next for Hotot development? I cannot find
the RoadMap...**

Well, we don't have a RoadMap, it's a "Monkey see, Monkey do" process
now. Ambiguous targets are there: multi-account support, multi-protocol
support, standalone Mac version etc. But I cannot guarantee which
version will have these.

Short term plan exists. You can expect a few UX tweaks on 0.9.8 version
with Kismet interface ready. We're also trying to reduce the memory
footprint. But don't be surprised to see anything BIG...

**When do you plan to release 1.0 version? Don't be another Wine. :)
Compare to the progressive release of Chrome, Hotot is rather
conservative.**

My goal is to release 1.0 before the End of the World on 2012. :)

**With codename Ark? LOL**

Well, we will continue using the codename Ada, to memorize the first
female programmer. Of course Ada could mean something else...

But there will be a special codename for 1.0, I reserve the final
decision.

**Take a note of this, folks~ BTW why use the rabbit-like name Hotot
when you're so fond of kitty?**

Because rabbit is very tasty as a rodent.

OK, the truth is that I am also very fond of the cute rabbit. Moreover,
the word 'Hotot' looks cute, though doesn't sound so.

**Indeed! Do you participate other open source projects besides Hotot?**

Not now, too busy for me.

Perhaps I will assist @shellexy and @CSSlayer on input method if I'm
free.  
Nothing else on plan, being a postgraduate student is not easy.

**It seems to be quite fine to tweet directly from input method!**

Quite easy to implement, @CSSlayer could get it work in a few hours.

**The users of Fcitx, take note.**

The market of Twitter client is almost saturated, even Twitter itself
doesn't encourage client development any more.

Still the number of people using third party clients is relatively low.
My first response is to add something unique to Hotot. I might be able
to slow down a bit. Start something new, probably.

**Which field? Social network?**

Haven't an idea yet. Just wait for the sparkle.

**OK, I'm looking forward to your new open sourced project. I bet it
will be a Web App :)**

You cannot be sure! My day work is Linux C Programming.

**Very interesting, a Linux C programmer turns to Python + JavaScript to
solve Linux desktop appliance problem.**

Because the development for Linux desktop application is not easy.

I think the programming language is an important factor. If the language
is quite difficult to write, perhaps the developers will likely to avoid
it despite of certain good feature set.

**In this way, can I say that the Web App way Hotot goes represents a
possibility to solve the difficulty of Linux desktop application?**

Well, I think GNOME Shell and KDE have something similar. BTW @shellexy
has drafted a pure Web based DE, still in concept though.

**Ha, leak news welcomed! Well, at last, do you have anything else to
say for the LinuxTOY readers/Hotot users/personal fans ?**

Err...How about "wish your heart full of love and grief"?

**Err... Up to you...**

Then here you go:Wish your heart full of love and grief.

(ShakeHand

**(ShakeHand**

(Scratching
