Title: Ubuntu 削减非 LTS 支持周期
Date: 2013-03-20 10:00
Author: liangsuilong
Category: Distros
Tags: systemd, Ubuntu
Slug: ubuntu-cut-down-non-lts-support

昨日的 Ubuntu 技术委员会讨论了 Ubuntu 非 LTS
版本的支持周期和滚动更新的版本发布模型。

会后技术委员会确定了 Ubuntu 非 LTS 版本的支持周期，从现在的 18
个月削减到 9 个月。也就是说，新的非 LTS 版本发行 9
个月后，用户就无法获得该版本的任何更新。用户如果需要获取软件更新，即需要升级到新版本
Ubuntu。Canonical
此举是为了腾出更多的公司资源，以开发和维护他们认为更迫切更有价值的项目。缩短后的支持周期政策将会在
Ubuntu 13.04
以及未来发行的版本中实施。滚动更新的详细技术细节，依然在规划与制定中，暂时没有更多的消息透露。

[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTMzMTE)  [IRC
会议记录](http://irclogs.ubuntu.com/2013/03/18/%23ubuntu-meeting.html#t21:00)

另外[早前的消息](http://www.phoronix.com/scan.php?page=news_item&px=MTMyMDE)指出，Ubuntu
13.04 将会用 systemd-logind 替代已经不再维护的 ConsoleKit
用于用户会话管理，但 Init System 依然使用自家开发的 Upstart，
