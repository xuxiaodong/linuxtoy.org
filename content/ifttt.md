Title: IFTTT: 好玩又实用的自动化服务
Date: 2013-12-02 11:51
Author: toy
Category: Apps
Slug: ifttt

我觉得 [IFTTT][i] 是那种只干一件事且干得特别好的网站。IFTTT 即 if this
then  
that
的简称，其意图十分明显，就是如果满足某个条件，那么就执行某个动作。如下  
图所示。

![IFTTT](/img/2013/12/ifttt.svg)

利用
IFTTT，我们可以把很多事情自动化，从而使我们解脱重复的羁绊。例如，当我  
在 LinuxTOY 上发布一篇新文章时自动在 Twitter 上发一推。

在开始使用 IFTTT 之前，让我们先来了解几个基础概念：

* Channel：渠道，它是烹制 IFTTT
食谱的基本材料。每个渠道都有其触发器和动作。  
IFTTT 目前支持许多渠道，包括 RSS、Email、SMS、Twitter、Facebook 等等。  
* Trigger：触发器，if 语句的条件块，如发布新文章时。  
* Action：动作，if 语句的执行块，如在 Twitter 上创建推。  
* Recipe：一条完整的 if 语句就是一道食谱，它包括触发器和动作两个部分。

接下来我们看看 IFTTT 的用法。首先，注册并登录 IFTTT
网站。然后，激活要使用的  
Channel。这样，就可以开始创建或使用别人的 Recipe 了。IFTTT  
被设计得很好用，创建 Recipe 的过程十分容易。我们以“if Feed then
Twitter”来加以  
说明：

1. 点击 this 后，选择 Feed 作为触发器渠道；  
2. 选择 New feed item 作为触发器；  
3. 输入 Feed URL，如 https://linuxtoy.org/feed；  
4. 点击 that，选择 Twitter 作为动作渠道；  
5. 选择 Post a tweet 作为动作；  
6. 可根据需要更改动作模板，如标题、网址等；  
7. 添加 Recipe 说明。

这样就建好了一道 Recipe。IFTTT 会每隔 15
分钟去检查一次触发器，若条件满足则执行  
相应的动作。

[i]: http://ifttt.com
