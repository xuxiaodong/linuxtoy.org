Title: OilRush for Linux 0.6 Preview
Date: 2011-03-13 11:23
Author: lovenemesis
Category: Featured
Tags: OilRush
Slug: oilrush-for-linux-06-preview

Unigine 的[OilRush for Linux
的预售活动](http://linuxtoy.org/archives/oil-rush-linux-pre-order.html)已经进行一段时间了。在这里与诸位分享下这一段时间的试玩后的体会。

**以下所有的截图和内容均基于 OliRush for Linux 0.6
早期预览版本，可能和正式发布时的内容存在不同。**

**测试环境**

-   CPU: AMD Phenom II X3 P820
-   内存：2GB DDR3 1066
-   显卡：ATI Mobility Radeon HD 5470 512 VRAM
-   系统：Fedora 14 i686 2.6.35.11-83.fc14.i686
-   驱动：Catalyst 11.2

**故事背景**

气候灾难后地球，绝大部分区域被海洋覆盖。恶劣的生存环境使得海洋中蕴藏的石油成为各路势力争夺的焦点。你的目标就是占领石油钻井，击败对手！

[![](http://linuxtoy.org/img/2011/03/main-menu.png)](http://linuxtoy.org/img/2011/03/main-menu.png)

主菜单

[![](http://linuxtoy.org/img/2011/03/options-menu.png)](http://linuxtoy.org/img/2011/03/options-menu.png)

设置菜单：**抗锯齿关**，其余保持默认（高）。

**游戏界面**

[![](http://linuxtoy.org/img/2011/03/game-control-screen.png)](http://linuxtoy.org/img/2011/03/game-control-screen.png)

1.  初始建筑：摩托快艇生产平台。
2.  摩托快艇：脆弱但速度快，具有基本的对地和对空能力。
3.  雷达：显示当前场景地形及各个平台分布。
4.  撤销：取消对当前部队部队下达的指令。
5.  信息：不知道有什么特殊用途，可能多人游戏才有效。
6.  部队分配：制定该指令对驻守当前平台中25%、50%或者100% 的单位有效。
7.  科技点：显示可以用来投放在科技升级上的点数。
8.  单位数量：当前单位/最多拥有单位。
9.  石油量：当前拥有的石油桶数。
10. 消息框：显示当前选中的建筑、单位或者科技的详细信息
11. 菜单：暂停并唤出游戏菜单。

部分科技升级会增加**战场支援能力，会在屏幕左侧显示**。

[![](http://linuxtoy.org/img/2011/03/defense-build.png)](http://linuxtoy.org/img/2011/03/defense-build.png)

**建筑修建**

游戏中主要的建筑就是各类生产平台，而每个**生产平台可以添加防御工事**，分为三种：

-   机枪：基本对空对地能力，适合对付各类小型单位。
-   炮塔：强力对地，适合对付大型水面单位。
-   导弹塔：强力对空，适合对付各类空军单位。

**修建防御工事需要耗费石油**，它们在受到伤害时都会慢慢自动维修，可以进行升级强化耐久和威力，也可以变卖以回收一部分石油。

注意**生产平台本身是不可以修建的**，只能**靠单位去占领地图上中立的平台或者抢夺对手**的。

除了生产平台以外，另外一个重要的平台就是**钻井平台**，只有它才可以提供石油资源以维持防御工事和，同样也是需要去占领或抢夺的。

**作战单位**

目前所见到的作战单位有：

-   摩托快艇：脆弱但速度快，具有基本的对地和对空能力。
-   导弹巡逻艇：速度中等，强力对空，对地一般。
-   大型炮艇：速度慢，对抗防御工事和大中型舰艇十分有效。
-   滑翔翼侦察机：速度快，对付小型舰艇和地方工具效果不错，但面对导弹防空火力时生存力低。
-   武装直升机：速度中等，对地导弹对付大型舰艇和防御工事效果显著，生存力也较高。

每种**作战单位由其专属的生产平台产出**，分布在地图上各个区域。

毫无疑问的是正式版本必将有更多单位加入。

**单位控制**

OilRush
中**无法单独微操某个单位**，而是**以平台为单位操纵周围其驻守的部队**。当然在这个过程中可以通过指定某类驻守部队（譬如只选定摩托快艇）以及百分比控制（譬如只选定50%的摩托快艇）的方式实现一定程度上的微调。

鼠标**左键选择平台，右键指定目标平台**。可以通过撤销按钮取消对部队下达的指令。

期间单位的 AI
还是不错的，当**组合编队包含移动速度各不相同的海空单位时，所有单位会先集合在一起然后再前往目的地**，避免了轻型单位成炮灰的情况。

**单位的生产无需耗费石油**，自己占领的生产平台会以固定的速率生产单位，直到达到单位上限。

**科技天赋树**

[![](http://linuxtoy.org/img/2011/03/tech-talents.png)](http://linuxtoy.org/img/2011/03/tech-talents.png)

科技树分为三类：

-   作用于敌方平台的：探测，降低生产效率，降低守军作战效率、防御破坏等等，以及**核弹**。
-   作用于乙方平台的：强化防御、增加生产效率、增加守军作战效率等等。
-   作用于乙方单位的：增加移动速度、增加威力、舰艇装备升级、特殊能力升级等等，以及快速自动修复。

科技树上的投资需要耗费科技点数，而**科技点数是通过和敌方交战的激烈程度获得**的。

需要主动释放的技能会在屏幕左侧以工具条形式显示，**使用时会耗费石油数**。

**更多截图**

[![](http://linuxtoy.org/img/2011/03/capture-oil-tower.png)](http://linuxtoy.org/img/2011/03/capture-oil-tower.png)

抢夺钻井平台

[![](http://linuxtoy.org/img/2011/03/capture-frigate-platform.png)](http://linuxtoy.org/img/2011/03/capture-frigate-platform.png)

抢夺导弹快艇平台

[![](http://linuxtoy.org/img/2011/03/captureing-platform.png)](http://linuxtoy.org/img/2011/03/captureing-platform.png)

抢夺中，可以从建筑上红色的指示灯看出进度

[![](http://linuxtoy.org/img/2011/03/against-gun-tower.png)](http://linuxtoy.org/img/2011/03/against-gun-tower.png)

和机枪塔交火

[![](http://linuxtoy.org/img/2011/03/destroy-gun-tower.png)](http://linuxtoy.org/img/2011/03/destroy-gun-tower.png)

显然它不是对手

**总结**

OilRush 借鉴了[独立游戏获奖作品 Eufloria
(真菌世界)](http://www.eufloria-game.com/)的操作模式和 Red Alert 3
的科技升级，通过 Unigine 效果惊人的图形引擎加以表现，还有有趣 **Tower
Defense 塔防地图**，可以说是 2011 年在 Linux
平台上的最强游戏作品了，强烈推荐。

另外在官方论坛上，[开发人员表示](http://www.oilrush-game.com/forum/index.php?/topic/13-why-two-version-of-the-game-are-sold/page__view__findpost__p__110)在考虑在**最终版本销售时不再区分版本，一个帐号将可以下载全部平台客户端**。同时，[OS
X
版本](http://www.phoronix.com/scan.php?page=news_item&px=OTE5OQ)也正在开发中。

目前 OilRush 预售价
$19.95（**￥131**），支持**支付宝**/信用卡/PayPal等方式付款。
