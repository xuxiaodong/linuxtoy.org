Title: 中国公司为 Wine ARM 实现申请专利并获批准
Date: 2014-04-01 17:26
Author: lovenemesis
Category: Featured
Tags: Wine
Slug: chinese-applied-patent-about-wine-arm-and-granted

在 [Wine 项目于 1.3.4 版本实现 ARM
平台支持](https://linuxtoy.org/archives/wine-134.html)后的 8
个月，浙大网新科技股份有限公司的五个人宣称“发明了在 ARM 处理器上实现
Wine
构建工具移植的方法”并为此申请了专利，更可笑的是，这条专利获得批准并于今年
1 月公开。  

别以为 [COS
操作系统](http://en.wikipedia.org/wiki/COS_%28operating_system%29)已经让你看到了中国
IT
圈的下限，你总会被它会震惊的。来自浙大网新科技股份有限公司的毛德操、王承志、徐鼎鼎、陈天洲、马建良在
2011 年 6
月[申请专利](http://www.google.com/patents/CN102364433B?cl=zh)，宣称自己的发明首度提供了在
ARM 处理器上实现 Wine 构建工具移植的方法。实际上这个方法其实是 WineHQ
项目来自德国的主要贡献者 André Hentschel 于 2010 年 10 月就已实现并随着
[Wine 1.3.4
版本发布](https://linuxtoy.org/archives/wine-134.html)并开发源代码的。此外根据代码仓库记录，这五位中国人未给
Wine 项目做出任何贡献。

大致浏览了下专利说明文档，浙大网新五人所作的事情仅仅是1）下载老版本 Wine
源代码并按照 ARM 构建的要求修改了交叉编译配置文件；2）针对 ARM
处理器重写了一些接口方法。而这两点都是 André Hentschel 已经在 1.3.4
版本中做过的事情。客气点儿说是他们会看文档，实际点儿说是纯抄。接下来，毫不意外的，这项**专利在国内获得批准**，并于今年
1 月份正式公开。这意味着在国内交叉构建 ARM 版 Wine
的行为都有可能涉嫌侵犯此项专利！

4 月 1
日在西方是愚人节，一个充满玩笑和欢乐的日子。现在玩笑有了，只是一点儿都不欢乐了……

在此希望能引起 CodeWeavers
在华员工和诸多开源爱好者的关注，最好能有所行动。~~扫除败类，才能有发展空间。~~

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTY0ODI)

[WineHQ 项目相关记录](http://www.winehq.org/wwn/366#Bad%20Patents)

**4 月 3 日更新报道**：

发明者之一徐鼎鼎及其团队[提供了一系列视频](http://www.youku.com/playlist_show/id_22122332.html)，希望能证明自己的确是独立开发的。此外得知其公司上层也在处理此事情，本站会继续跟进后续报道。

[龙井论坛相关帖子](http://www.longene.org/forum/viewtopic.php?f=2&t=16201)

**4 月 4 日更新报道**：

Wine 项目主要支持商业公司 CodeWeavers 中国区员工 Qian Hong
已经在评论中给出回应。目前仍无专利持有人浙大网新的正面回应。

**4 月 16 日更新报道**

距离本次事件批露已经两周了，尽管浙大网新官方依然无动于衷，不过 Qian Hong
兄则得到了来自[台湾 Open Foundry](http://www.openfoundry.org/tw/about)
的林诚夏老师从法律角度对于该事件的回答。现全文转载如下：

关于您提出来的二个讨论问题，我简要就我所知来提供资讯如下。

1、对于Wine项目这样的LGPL开源项目，假如浙大网新基于Wine on
x86独立完成了Wine on  

ARM的移植并且是唯一的实现者（假设Andre等人不曾存在），那么他们是否可以为Wine
on ARM的移植方式申请专利？

可以的，若是浙大网新是Wine on
ARM實作的唯一實現者，那浙大网新很有機會可以依此移植方式來申請專利。因為追根究柢，專利適格(patentability)的三個要素，就是論：A、技術性(technicality)，B、商用性(Industrial
applicability)，以及C、新穎性(Novelty)，所以只要符合這三個要素，各國的專利審核權責機構，就可以據此來核發專利，這個原則不論中國大陸、台灣，或是美國、歐盟都是一樣的。而依專利法的架構來論，其實法律上並沒有關於「軟體專利(Software  

Patent)的個別解釋，應該是說，軟體專利也是專利，不過這類的專利是本質上大量透過軟體程式的方式，來實現它的技術方法，所以這類的專利才會被簡稱為軟體專利，實則軟體專利就是專利，目前美國、歐盟看待軟體專利的態度是，盡量嚴格審核，但若是其確實是符合專利適格的三要素，其專利權的保護／實踐範圍也可以具體說明，或是透過與硬體裝置的結合運用來限縮到一定的範圍的話，就可以核可。基於上述的這些專利核發的基本原則，若是浙大网新基於Wine  
on
x86，另行完成了WINE在ARM平台上的移植，且這樣的移植技術在資通訊(Information
and Communication
Technology)領域裡，並不為其他技術人員所熟知(non-obviousness)，那麼它就很有可能具有專利適格，而可以被合法申請並獲得。

2、对于Wine项目这样的LGPL开源项目 ，如果浙大网新为Wine on
ARM的移植方式申请专利，那么他们是否需要公开他们改动过的Wine项目的代码？（我可以理解如果浙大网新分发了基于Wine的产品，那么根据LGPL他们需要同时提供改动过的代码；但我不理解“申请专利”算不算一种“分发”，算不算“公开分发”，该不该提供代码）

要回覆第二個問題，首要討論的是：「申請專利併專利公報的發布，算不算是一種程式碼散布的方式。」第二個要討論的重點則是，倘若浙大网新之後確實有散布Wine
on
ARM移植實作的程式碼，那麼此一申請核過的專利，要不要一併依LGPL的授權規則，提供給後手使用者來使用。

第一個討論重點：“申请专利”算不算一种“分发”，算不算“公开分发”。依我個人對專利法與自由開源軟體授權條款的解釋，應該是不列入程式碼的散布或分發行為的。因為專利公報上被述明的，僅是此一專利的實踐方法，其重點描述內容為技術的實踐步驟，雖然說如果是軟體專利的公報，會約略描述到軟體程式的層級架構，但畢竟不是程式碼全部份或一部份的公開披露，故依照多數的自由開源軟體授權條款的文義解釋，程式碼的散布／分發行為，原則上應該是要程式碼的傳遞與增殖(convey  
&
propagation)，而若僅為技術方法的展示與披露，應該還沒有到達程式碼已然傳遞或增殖的要件。

然而！雖然浙大网新的專利申請與核可專利之後的專利公報，不必然充足了程式碼散布的條件，但之後其將這個WINE
on  

ARM的移植，實作在商業產品時，必然會用到某些軟體工具組，併合實作後的WINE程式碼一併散布，此時，依照LGPL的解釋，不論是LGPL-2.1版或LGPL-3.0版的條款，都明訂完整的程式源碼(Source
Code)包括軟體元件的安裝資訊與編譯腳本(Installation Information &
Compiling Script)，從這個角度來看，日後浙大网新在WINE on
ARM移植實作併商業散布時，就會有提供程式源碼的義務和要求。

但最後一個要討論的爭議點，也是最難解決的爭議就是：如果浙大网新聲稱其後WINE
on
ARM的移植實作，是採用LGPL-2.1的授權方式來利用的話，那麼其所申請的這個專利，會不會併合程式碼的實作而提供給後手使用者，則有一些解釋上的爭議！因為依照WINE的授權聲明(https://www.winehq.org/license)，WINE
HQ是採用LGPL-2.1+(under the terms of the GNU Lesser General Public  
License as published by the Free Software Foundation; either version
2.1 of the License, or (at your option) any later
version.)的方式向外釋出，也就是說，浙大网新可以自主主張，其打算用LGPL-2.1或LGPL-3.0，或其後更新版本的方式來利用WINE  
HQ。

而倘若浙大网新表示其就是採用LGPL-2.1，不欲以更新版本的方式來利用WINE
HQ，那其所申請的專利會不會一併在實作中提供給後手，就會產生爭議。這是因為LGPL是在3.0的版本，才明訂程式開發者所自主寫入軟體程式的軟體專利技術，必須一併依LGPL-3.0的授權方式，提供給後手使用者來利用；但在LGPL-2.1的版本，因為是1991年便撰寫完成，對於專利授權方式的安排，就沒有LGPL-3.0(2007年)這般完整與考究。依照LGPL-2.1的原始規定，專利權人對於其寫入軟體專利技術的運用，僅是「不能與LGPL-2.1的授權模式產生衝突」，而不會產生衝突解釋起來的灰色與模糊地帶太大，實用上便會有解釋不清的困擾。

進一步的相關資訊，可以參照我在2007年與葛冬梅小姐合作撰寫的專文，GPL-2.0
第 7 條淺評：http://www.openfoundry.org/tw/legal-column-list/894-gpl2-7-

其實在這篇文章裡，我們的觀點是依照GPL-2.0第7條，以及LGPL-2.1第11條(If,
as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this
License.)，可以導引出專利授權的意涵，使用者是有機會引用這二條條款，做為專利授權的依據。不過，這是延伸性的「目的性解釋」，是否實務上能夠如此比附援引，仍然有待日後的司法判解給予論理上的支持。

所以說，簡要回覆您第二個問題，我是認為基於LGPL-2.1條款內容的論理解釋，一旦浙大网新將WINE
on  

ARM進行商業實作之後，其後手是可以依LGPL-2.1或LGPL-3.0的授權規則，來向其要求改作後的程式源代碼，並且一併得到專利權使用的地位，只要使用者的使用方式不違背LGPL-2.1或LGPL-3.0的授權規則，則浙大网新就不能對他們進行專利侵權的訴訟。

不過，根據您轉錄的新聞連結，其實André
Hentschel在德國社群的討論網站，已經公開過WINE on
ARM的實作資訊了，所以日後若真的有個別的使用者，被浙大网新控以專利侵權的責任，則在法庭上，被控者亦可舉證該技術已經André
Hentschel披露而成為一個在ICT領域已公告週知的先前技術(Prior
Art)，並從此立場要求承審法庭一併廢棄浙大网新申請的此號專利，因為據專利申請的三要件中，若該技術已然在該領域被熟知，則新穎性適格已然喪失，而不具專利適格。

大致是這樣的法律論理邏輯，希望有助於您釐清疑惑。若後續還有別的想法，再歡迎隨時與我接續討論。

20140415 12:05 中研院 资创中心 林诚夏
