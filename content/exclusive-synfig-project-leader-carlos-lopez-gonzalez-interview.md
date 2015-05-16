Title: 独家：Synfig 项目领导 Carlos López González 专访
Date: 2012-02-28 15:02
Author: lovenemesis
Category: Featured
Tags: synfig
Slug: exclusive-synfig-project-leader-carlos-lopez-gonzalez-interview

我们 LinuxToy 最近对 Synfig 项目的领导人 Carlos López
González，做了一次非常有趣的采访。*感谢 jcome 来稿*

*Scroll to the end for the English version.*

[![](http://linuxtoy.org/img/2012/02/synfig-00-synfig-logo.jpg "synfig-00-synfig-logo")](http://linuxtoy.org/img/2012/02/synfig-00-synfig-logo.jpg)

Synfig Studio
是开源的二维矢量动画软件，通过它，在有限的人力和物力情况下就能制作出具备电影品质的动画电影。最近我们联系到了
Synfig 项目的领导者 Carlos López González， 让他就 Synfig
的开发，使用以及社区建设等方面情况和我们分享。

**LinuxToy (LT): 您能自我介绍下吗？**

Carlos López (CL): 我是 Carlos López
González，西班牙人，过去的十七年里，我生活在加的斯（Cádiz），它是一个位于安达鲁斯亚（Andalucía）
自治区南部的古老城市。我出生并成长在塞维利亚，并在那里度过了我的主要的学校学习生活，获得了工业工程师学位。到目前为止，我在汽车制造行业工作八年了，而在这之前的九年里，我为安达鲁斯亚政府工作。我排行老五，是家里最小的，离异，有两个儿子。目前我和我的伴侣一起住，希望过上更加幸福生活。

**LT：相比 Blender，GIMP 或者 Inkscape，Synfig
不是个被人所熟知的开源图形图像软件。您能给我们介绍一下吗？Synfig
后面有什么故事？**

CL：站在 [Synfig](http://synfig.org)背后的是一小群热心人，他们致力于把
Synfig 打造为权威的开源动画应用程序。

Synfig 项目（现在是一个开源项目）的诞生是为了把 [Robert Quattlebaum（aka
darco）](http://wiki.synfig.org/wiki/User:Darco)和他的已经关闭的动画公司（[Voria
Studio，LLC](http://www.deepdarc.com/category/voria/)）的成果延续下去而出现的。Synfig
项目的基根是程序代码本身。围绕着它，贡献者们添砖加瓦，努力把它打造成一个完整的产品套件。我们有网站，[论坛](http://synfig.org/forums)，[Wiki](http://wiki.synfig.org)，[邮件列表](http://sourceforge.net/mail/?group_id=144022)，博客，等等。

Synfig
项目的维护者小团队（领导者，合作者，或者任何其他叫法）随时间也在自然的变化着。并没有任何特别的指定角色，而且每个部分的责任也是没有特别指定的。

Synfig
经历过的时光也是有好有坏。我认为现在它正处在一个好的时刻。虽然去社区看上去不是非常活跃，但当前的基础设施条件是最好的。我们有备份脚本可以备份整个基础设施，这让我们在迁移到其他服务器上时可以不受任何影响。特别感谢
Konstantin Dmitriev (aka zelgadis)
的工作，如今我们的网站和论坛放在一个付费的服务器上，可以自动更新论坛数据库和
CMS 引擎。Wiki 还在 TuxFamily 的服务器上，程序代码和 trackers 则在
Sourceforge 上。对于复杂的开发任务，Konstantin 和我采用 Pivotal Tracker
作为追踪开发问题（功能和缺陷）的系统。

**LT：除了开源的许可，相比其他商业动画工具，Synfig 有什么优势？**

CL：Synfig
有几个功能让它显得独一无二。有个专业动画师在经过测试后，曾经对其渲染引擎出色的抗锯齿渲染结果赞不绝口。它的每个内部参数都是采用浮点计算的，这给它带来非常棒的渲染结果。对我而言，最主要的是浮点计算给用户带来了真正的与时间无关，与空间无关的分辨率。

另一个非常有趣的能力是值节点（value node
system）系统和这个系统带来的无止境的可能性。这里有个例子，是我以前通过值节点系实现的[粒子模板](http://wiki.synfig.org/wiki/Particles_V2.0)。

它也有一些创新的功能，比如，[曲线渐变](http://wiki.synfig.org/wiki/Curve_Gradient_Layer)和[高级轮廓](http://wiki.synfig.org/wiki/Advanced_Outline_Layer)，这些在动画世界的任何其他地方都找不到的（至少我们没有发现）。

[![](http://linuxtoy.org/img/2012/02/synfig-01-e9949b_particle-demo-reel.png "synfig-01-particle-demo-reel")](http://linuxtoy.org/img/2012/02/synfig-01-particle-demo-reel.png)

[粒子系统模板视频](http://youtu.be/YJV3xMP24fc)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzEwODE2.html)）

**LT：您是怎么加入到这个项目的？在浏览了论坛后，我们发现您在很短的时间里就从新手成长为大师。：）能给我们分享一下这个过程吗？**

CL：我是通过报告 bug 的方式开始对这个项目的贡献的。那时候，我们已经有
wiki 页面了，而且 [Chris Moore（aka
dooglus）](http://dooglus.rincevent.net/synfig/)已经做了非常多的工作，但是，还是有很多地方不完整，也没文档。所以，在报告
bug 的期间，我开始尝试掌握如何使用 Synfig Studio，这幫助我写下了很多
wiki 页面。在我开始学习这个程序时，我保持着和
Chris（那时他是主要的代码和 wiki 贡献者）之间非常活跃的沟通。先是在 IRC
里聊，后来转到一个聊天客户程序里。我们一起工作，或者实现我提出的一些功能需求，或者修复我报告的
bug。那是一个非常流畅和活跃的沟通时光。之后论坛问世了，我有它的部分管理权限。后来
dooglus 决定暂时离开 Synfig
项目（现在这个他的假期还在没结束），我接过了贡献代码的火炬。大概是在同一时间，那时另一个非常棒的贡献者，[Paul
Wise（aka pabs3）](http://bonedaddy.net/pabs3/)为了能专心致力于其他的
FOSS 项目，决定移交 wiki，论坛的管理给我，同时移交的还有 Sourceforge
的程序代码管理。最后，感谢
[Zelgadis](http://zelgadis.profusehost.net/blog/)的努力和帮助，基础设施从
darco 的私人服务器迁移到了 Sourceforge，稍后又迁移到
Tuxfamily，再后来是他自己的私人服务器。  
因此，从新手到大师（LOL）的故事基本是在 IRC 聊天纪录里纪录着。

**LT：除了对代码的贡献，您也被 Synfig 社区称为最友善的人。您对 FOSS
社区文化的建设有什么想法？**

CL：我认为每个人都可以做贡献的。新人有利的一面在于他的还没有形成偏见。人们（特别是写代码的）在为某个项目工作了一段时间后，就会拒绝关注那些和已有形态不太相符的新问题。在执行关键性的项目时坚持这条原则是有利的。但多数时候，缺乏相关知识会导致管理者对新人咆哮：它能运行，不要动它。如果有这个发生，则需要对这个项目的运转（代码，网站，论坛）做更深入的了解，因为用户，特别是没有偏见思想作祟的，总有他正当理由的。

对我而言，FOSS
项目最重要的是聆听用户。这是我努力要做的（当然要继续学习如何做得更好）。我将和
Zelgadis
保持联系，讨论如何实现一些他所要求的具体的功能。Zelgaids，作为优秀的动画师，很擅于转述修改需求，转述他发现的阻碍动画流程的
bug 。不只是简单报告 bug
和要求功能，而且要和程序员（或者管理员）坐到一起，实现功能，解决
bug，这点非常重要。  
理想的状态是，这类沟通最好有个公开的频道。我们过去有用 IRC
或论坛，但我认识到了多数是使用邮件和私聊。狡辩下，这可能是因为没有足够时间，大家所处得时区也不不尽相同。也许我们应该多用邮件列表来公开我们的对话交流。另外，Pivotal
Tracker 是公开和开放给任何人的，我们（也）在那里做事务交流。

[![](http://linuxtoy.org/img/2012/02/synfig-02-curve-gradient.png "synfig-02-curve-gradient")](http://linuxtoy.org/img/2012/02/synfig-02-curve-gradient.png)

[曲线渐变截屏](http://www.youtube.com/watch?v=z6PBpJf46dg)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzEwNjA0.html)）

**LT：Yu Chen（aka jcome）在本地得 Linux
用户组做过两次的演示，但是收效甚微。然而，在 LT 上发布的，新 [Demo Reel
的 Spiderboat
动画渲染求助](http://linuxtoy.org/archives/need-help-to-render-synfig-studio-demo-reel.html)却非常的成功。按照您得经验，推广这个专业的软件的正确方法是什么？**

CL：推广的第一个方法是用它，用它并创作好的动画。这是可能的！第二个方法是铲除它当前发展的两个主要障碍：没有
Mac
平台的包维护者；还有因为它当前的渲染引擎没有很好的对实时播放进行优化导致得界面响应速度慢的问题。我相信一旦这两个问题得到修复，这个应用程序的普及度会大大提高。

**LT：Synfig 的教程和文档情况怎么样？您能给我这样的新手一些建议吗？**

CL：我们的 Wiki 还有很多地方要完善。虽然，在 2010
年我们做了卓有成效的努力更新 Wiki，但仍有很多文章需要扩展，进行内容充实
。

关于 wiki
上的[开发者园地](http://wiki.synfig.org/wiki/Developer_Documentation)，目前“占地面积”非常的小，需要更多的文章来充实。这是时间和资源的问题，因为，特别是在这个领域，并没多少人能写相关文章。

要了解代码，唯一的方法是代码本身。刚开始阅读代码时，要多花时间和精力，但，一旦您了解了整个思路之后，事情会变得容易许多。

如果您真的想要掌握
Synfig，我觉得步骤应该和我所经历过的一样：学习软件的使用，报告发现的
bug，写 wiki，发送补丁，然后变成官方的 coder。还有就是要滥用当前 Synfig
贡献者的耐心和友善。。。；）

**LT：既然“使用”是第一步，您觉得如果我只是动画爱好者，没有动画专业知识，想在业余做些动画找点乐趣，我可以学
Synfig 吗？从哪里开始比较好？**

CL：我的第一条建议是要乐在其中。动画是个归属于时间和空间的问题，不是说用个软件就能学会的。弄本动画书，按照它的指引做练习。复制他人的作品。不要一开始就试图找出自己的风格，要对自己的作品感到满意，享受做动画过程。从别人的评价中进步，不停的改进作品。做动画是很耗时的，也要求你做事专注。没有耐心，就没有好成绩。

[![](http://linuxtoy.org/img/2012/02/synfig-03-advanced-outline-demo1.png "synfig-03-advanced-outline-demo1")](http://linuxtoy.org/img/2012/02/synfig-03-advanced-outline-demo1.png)

[高级轮廓视频](http://youtu.be/boM_ZC9VZ54)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzEwMTA0.html)）

**LT：在 2012 年，Synfig 有什么计划？哪方面是您觉得最需要获得帮助的？**

CL：短期的计划是发布一个新版本（目前没有决定是小版本还是中版本）。我有和
[David Rylander（aka
rylleman）](http://rylanderanimation.se/)讨论过和您提的同样的事情。我想成立一个小小的团队做个头脑风暴，看看我们下一个要开发的新功能是什么。我们要在第一下就要瞄准目标。因为手头可利用的资源非常有限，在和我们拥有的时间、知识水平相匹配的前提下，选择开发一个最有影响力的功能。我们也试着探寻请求某些特定社区的帮助，让他们帮忙完成某个指定的编程任务，比如
OpenGL 实现，但这个还没有最终决定。

可以说我们目前正处在一个非常关键的时刻。编写代码方面，我也感觉自己比之前更加熟练了。现在正是做出成绩能在
FOSS 世界引起反响的改变的时候。  

这些都是我的愿望，至于会发什么，我自己也不知道的。我能保证的是：只要还能从中找到乐趣，我就会一直坚持做下去.

**LT：您能推荐一两个使用 Synfig 的动画艺术家和他们的动画视频吗？**

CL：

[![](http://linuxtoy.org/img/2012/02/synfig-04-morevnaproject-production-cuts_512kb.png "synfig-04-morevnaproject-production-cuts_512kb")](http://linuxtoy.org/img/2012/02/synfig-04-morevnaproject-production-cuts_512kb.png)

Konstantin Dmitriev - [The Morevna Project: Production
Cuts](http://www.youtube.com/watch?v=ZNUtgBoeGko)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzA4MzYw.html)）

[![](http://linuxtoy.org/img/2012/02/synfig-05-ra-bumper-b.png "synfig-05-ra-bumper-b")](http://linuxtoy.org/img/2012/02/synfig-05-ra-bumper-b.png)

David Rylander - [Rylander Animation bumper
2009](http://vimeo.com/8713234)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzA5NTk2.html)
）

[![](http://linuxtoy.org/img/2012/02/synfig-06-convite-de-casamento.png "synfig-06-convite-de-casamento")](http://linuxtoy.org/img/2012/02/synfig-06-convite-de-casamento.png)

Quadro Chave -[Convite de
casamento](http://vimeo.com/12275509)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzA5MTMy.html)
）

**LT：最后我想看看您的动画大作来结束我们的采访：）可以吗？（看，我在滥用当前
Synfig 领导者的耐心和友善了。。。；）**

CL：呵，我沒有多少可以给大家 show
的东东，有的只是此类的小故事，一些功能演示和测试用的视频。我也只是处于入门级别的！

[![](http://linuxtoy.org/img/2012/02/synfig-07-mr-tip-toe-adventures-spanish.png "synfig-07-mr-tip-toe-adventures-spanish")](http://linuxtoy.org/img/2012/02/synfig-07-mr-tip-toe-adventures-spanish.png)

Carlos López González - [Mr Tip Toe Adventures
Spanish](http://youtu.be/uHCpbMmT5GE)（[天朝镜像](http://v.youku.com/v_show/id_XMzU0NzA4ODA4.html)
）

**LT：非常感谢 Carlos 花时间和我们聊这些。**

CL：谢谢（Cheers）！

*English Version Start from Here*

**Interview of Synfig project leader, Carlos López González**

We, LinuxToy held an interesting interview with Carlos López González,
the leader of the Synfig Project:

Synfig Studio is a free and open-source 2D animation software, designed
as powerful industrial-strength solution for creating film-quality
animation using a vector and bitmap artwork. It eliminates the need to
create animation frame-by frame, allowing you to produce 2D animation of
a higher quality with fewer people and resources.

**LinuxToy (LT): Would you please talk a bit about yourself?**

Carlos López (CL): My name is Carlos López González. I’m Spanish and for
the past 17 years I live in an ancient city of the southern part of
Andalucía: Cádiz. I was formed in Seville where I was born. There, I did
my primary school studies and completed my formation obtaining the
Industrial Engineer’s Degree. I've worked in the automotive industry for
eight years and now, for the past nine years, I’m working for the
Andalusian government. I’m the youngest son of five children.  I’m
divorced and have two sons. Now I live with my partner, looking for a
happy life together.

**LT:  Comparing with Blender, GIMP or InkScape, Synfig is not quite a
well-known open sourced graphical application. Can you please introduce
Synfig a bit? What's behind its name?**

CL: Behind Synfig there is a small and enthusiast group of people that
is decided to make Synfig the definitive open source animation
application.

Synfig Project (as it is now, one open project) is the result of the
effort of keep alive the inheritance we received from [Robert
Quattlebaum](http://wiki.synfig.org/wiki/User:Darco) (aka darco) and
its, now closed, animation company ([Voria Studios,
LLC](http://www.deepdarc.com/category/voria/)). The basis of the Synfig
project is the code itself. Around it, people who has been contributing
to this software, has supported the project by adding the resources to
make it a complete suit. One website, a
[forum](http://synfig.org/forums), a [wiki](http://wiki.synfig.org),
[mailing lists](http://sourceforge.net/mail/?group_id=144022), social
blogs, etc. conform the core of the protect.

The group of Synfig Project maintainers (leaders, collaborators, or
whatever you like to call them) has changed along the time, naturally.
There is not any special rule to participate and the “responsible” of
each area is not particularly decided, just it is.

Synfig has passed good and bad times. I think that now is a good moment.
Although apparently the community is not very active, the current
infrastructure is better than ever. We have backup scripts for the
entire infrastructure that would allow us migrate to other servers
without effort. Thanks to Konstantin Dmitriev (aka zelgadis) the hosts
of the website and the forum are supported in a paid server that has
automatic updates of the forum database and CMS engines. Wiki is still
on TuxFamily servers and the code and trackers are hosted on
Sourceforge. Konstantin and I use Pivotal Tracker as system to keep
track of development issues (features and bugs) on complex developments.

**LT: Besides being open sourced, is there any other advantages over
other commercial animation tools?**

CL: Synfig has several features that makes it unique. One professional
animators that has tested it has applauded the antialiasing results of
the render engine. It gives great results thanks to the float point
calculations of every parameter it makes internally. For me the main
advantage is the floating point calculation that gives real time and
space independent resolution.

Another very interesting ability is the value node system and its
endless possibilities. One example is the [particles
template](http://wiki.synfig.org/wiki/Particles_V2.0) I did using value
nodes.

It has also some innovative features like [Curved
Gradients](http://wiki.synfig.org/wiki/Curve_Gradient_Layer) and
[Advanced Outlines](http://wiki.synfig.org/wiki/Advanced_Outline_Layer)
that are not seen elsewhere in the world of animation. (at least we
aren’t aware of them).

[particle demo reel](http://youtu.be/YJV3xMP24fc)

**LT:  How did you join this project? After browsing the forum, we found
you had a very short time from noob to master. :)  Can you share some
insights on this?**

CL: I started to contribute to the project by reporting bugs. At that
time the wiki already existed and there were a lot of work already done
by [Chris Moore (aka dooglus)](http://dooglus.rincevent.net/synfig/) but
many areas were incomplete and not written. So meanwhile I reported some
bugs I started to try to understand how to use Synfig Studio which
helped me to write a good set of wiki pages. When I started to
understand how the program works I keep a active communication with
Chris (who was the main code and wiki contributor those days) with the
IRC chat first and with a one to one talk client later. We were working
together on implementing some of the features I requested or fixing the
bugs I reported. It was a very fluid and active communication time. Then
the forum was born and I got some of the administrator privileges for
it. Later dooglus decided to take vacations from Synfig Project (that
still last to this day) and I took the torch of the code contribution.
More or less a the same time [Paul Wise (aka
pabs3)](http://bonedaddy.net/pabs3/), the other great contributor of
that time, decided to pass to me the administration rights of the wiki
and forum as well as the code admin on Sourceforge to dedicate to the
maintenance of other FOSS project he is involved in. Finally, thanks to
the efforts and help of
[zelgadis](http://zelgadis.profusehost.net/blog/), the infrastructure
were migrated from a private server run by darco to Sourceforge, lately
to Tuxfamily and finally to his own private server.

So, the period of transition from noob to master (LOL) is registered
basically on IRC chat logs.

[curve gradient](http://www.youtube.com/watch?v=z6PBpJf46dg)

**LT: Besides significant contribution to the code, you have a
reputation of being "Kind and Nice" within Synfig community. What do you
think of breeding a culture in FOSS community?**

CL: I think that everyone can contribute. The greatness of the newcomer
is that his mind is empty of prejudices. People (especially coders) that
has worked with the same project for some time, tends to reject new
focus of the problem that don’t conform with the already established
formats. It is good have some kind of discipline when dealing with a
project of some importance but most of the time the lack of knowledge
makes administrators loud out to the newbie: If it works, don’t touch
it. If that happens then there is needed a more deeper knowledge of how
the Project works (code, website, forums) because the user, especially
the one with a non biased mind, always has a reason.

So for me the most important achievement of FOSS project is to listen
the users. This is what I’m trying to do (as well as continue learning)
lately. I’m in continuous contact with zelgadis in discussion to how to
implement some certain feature he requested. Zelgaids, as good animator
he is, transmits very well the needs of the modifications or the bugs
found that blocks work flow. It is very important to not only report
bugs or request features but work together with the coder (or
administrator) to the completion and resolution of it.  
Ideally this communication is better to have in a public channel. We
have used in the past the IRC and the forum but I recognize that we are
using more the email and private chat. It is probably the lack of time
and the difference of time what justify it. Maybe we should use more the
mailing lists to make public our conversations. On the other hand,
Pivotal Tracker is public and open to join to anyone and there we talk
about those things.

**LT:  Yu Chen (jcome) had presented the Synfig in local Linux user
group twice but received few response. However, the [rendering request
for
spiderboat](http://linuxtoy.org/archives/need-help-to-render-synfig-studio-demo-reel.html)
(part of new demo reel) published on LT is a huge success. Based on your
experience, what is the proper way to promote this relatively
professional software?**

CL: The first way to promote is to use it and create good animations
with it. And it is possible! The second way is to correct the two main
blocking problems it has by now: There is not Mac maintainer and has a
slow responsive interface due to its current render engine is not
optimized for real time playing. I believe if both problems were fixed
the popularity of the application would increase a lot.

**LT: How is the tutorials and other documents about Synfig? Could you
please give me some suggestions for a starter like me?**

CL: The wiki needs lot of work. Although there was a great effort during
2010 to make it up to date, there are still many articles that need
expansion and that are just a little stub. Also good tutorials and video
tutorials are needed.

Regarding to [Developer
area](http://wiki.synfig.org/wiki/Developer_Documentation) of the wiki,
it is really small and needs more articles. It is just a question of
time and resources, because, especially in this area, there are so few
people that can write articles.  
The code itself is the only way to understand the code. It takes time
and effort to understand at first, but once you get the whole idea, the
things look easier.

If you really want to master Synfig I think that the steps would be the
same than I followed: Learn to use, report bugs, work on wiki, send
patches, and become official coder. Always abusing of the patience and
friendship of any of the current Synfig contributors... ;)

**LT: As a hobbyist who lacks professinal knowladge for animation and
not a coder at all, would be possible to be a user of Synfig Studio? The
purpose is just to have fun with it. What is the best way to start
with?**

CL: My first reccomendation is to just have fun. Animaiton is a question
of time and spacing and that cannot be learned with just a software.
Warp a animation book and follow the recipes it has. Copy others. Don't
try to find your own style from start, just be happy with your artwork
and have fun doing animations. Learn from others critics and form time
to time refine your works by trying to do better some aspects of the
animation. Animation is time consuming and needs lots of concentration.
If there is not patience, there wont be good results.

[advanced outline demo](http://youtu.be/boM_ZC9VZ54)

**LT:  What is the plan for Synfig in 2012? Which part do you think that
needs a hand most?**

CL: The short term plan is to release a new (minor or medium we haven’t
decided yet) version. The other day I was talking to [David Rylander
(aka rylleman)](http://rylanderanimation.se/) about the same thing you
mention. I would like to setup a micro team to have a brainstorming to
see what’s the next feature in development. We need to hit the target at
the first shot. Since the resources are very limited, we need to select
to develop a new impacting feature that could be feasible within a
normal time and using the current knowledge we have. We can explore the
possibility of ask for help on some particular community for a specific
task of coding (like opengl implementation) but that’s not decided yet.

Let’s say that we are now in a key moment. I feel that I can code more
fluidly than in the past and now is the precise moment to give a effect
hit on the FOSS world with a impacting change.

Those are my wishes but I don’t know what would happen. What I’m sure is
of one thing: I’ll continue with this as long as I get some fun out of
it.

**LT:  Can you name one or two animation artists using Synfig? Any video
clips to show?**

Konstantin Dmitriev - [The Morevna Project: Production
Cuts](http://www.youtube.com/watch?v=ZNUtgBoeGko)

David Rylander - [Rylander Animation bumper
2009](http://vimeo.com/8713234)

Quadro Chave -[Convite de casamento](http://vimeo.com/12275509)

**LT: Those video you mentioned above are so impressive. Your Mr Tip Toe
Adventures Spanish clip is so great. May we have another of your great
aniamtion clip to end the interview :) (We're abusing of the patience
and friendship of the current Synfig leader... ;)**

CL: Oh, I haven't so much apart of that small story and some demos and
tests. I'm just a beginner!

[Mr Tip Toe Adventures Spanish](http://youtu.be/uHCpbMmT5GE)

**LT: Thank you for your time Carlos, has been a pleasure talking to
you.**

CL: Cheers!
