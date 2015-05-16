Title: GitCafe 结束 Alpha 阶段内测，Beta 版正式公开上线
Date: 2012-09-20 13:03
Author: lovenemesis
Category: News
Tags: Git, gitcafe
Slug: gitcafe-leaves-alpha-enters-beta

2012年1月1日GitCafe正式上线内测，在经历了三个季度的内测与持续研发后，我们向所有开发者在[这个特殊的日子](http://softwarefreedomday.org/)推出我们的beta版本。现在，无需邀请码，所有人都能够开始[注册](http://gitcafe.com/signup)使用我们的代码托管服务。*[转载自
GitCafe 官方博客](http://blog.gitcafe.com/92.html)*

相对于GitCafe
Alpha，Beta版本完善并推出了许多重要的基础服务，我们相信正是这些基础服务的推出与有效利用，才能够真正盘活中国开源社区的开发与贡献氛围。

**组织(Organization)**

我们可以看到，现在在国内有许多大大小小的开源社区与全力研发并支持开源项目的企业，在技术活动中，开发者们往往很乐意介绍自己所实现的好玩的项目，作为企业也希望能够尽可能有效地推广他们的开源技术，但是我们却一直没有这样的平台能够很好的来协助这些辛勤的开发者有效的让目标用户与其他感兴趣的开发者了解自己项目的存在与使命。

组织功能就是为了解决这一问题而诞生，我们允许任一用户自行创建组织，以一个官方的名义去发起一些项目来让开发者们关注和参与。在用户的首页与右上角下拉菜单中，都可以看到创建组织的按钮。

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-organization.png "gitcafe-organization")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-organization.png)

组织创建完成后，您可以看到一个与众不同的组织首页，在首页您可以添加展示图片、介绍并开始创建属于组织的项目，让您的组织看起来生气蓬勃。

**私有项目与私有协作人员(Private Repo & Private Collaborator)**

让大家久等了！自从内测上线后，就陆陆续续有朋友发送邮件给到我们咨询何时能够公开上线并推出私有项目托管服务。

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-create.png "gitcafe-create")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-create.png)

在Beta中，您已经可以创建私有项目并且添加私有项目协作人员，我们的私有项目服务将会持续免费至2012年年底，现在是时候来看看我们从2013年开始的收费策略了。

**极特币(GitCoin)与收费服务策略**

嗯，如果2012年年底人类没有灭绝，那么恭喜您，您将有机会在2013年为GitCafe更为茁壮的发展给到财力上的支持，我们的私有项目托管等付费服务将从2013年1月1日开始收取费用。

我们引入了虚拟货币概念极特币(GitCoin)，与人民币的兑换汇率是30:1，也就是1元人民币能够兑换30枚GitCoin。这看似是一个很奇怪的汇率，30这个数字看上去也不是很geek，为什么我们会这么做呢？这是因为我们的收费服务并不是按月付费，而是按天，以下是我们目前付费服务的收费策略：

-   单个私有项目: 4极特币/天
-   添加单个私有项目协作人员: 4极特币/天
-   256MB免费托管空间使用额度超出每256MB: 8极特币/天

现在您应该理解为什么我们使用1:30这样的汇率了，方便按月的换算，您每天账户余额上因使用付费服务而扣除的极特币数量，基本就是每月真实的人民币开销额度。

举个例子，作为一个GitCafe用户我如果现在有两个私有项目，三个私有项目协作人员，那么我每天将会使用(2+3)*4共20极特币，每个月支出约20块人民币。

GitCafe的收费服务弹性极大并且价格低廉，现在就开始试用我们的这些付费服务吧，我们将免费近一整个季度，直至2012年年底。

**一些细节**

为了提供更好的用户体验，GitCafe在细节上的打磨也是全倾全力，用户可以根据自己的喜好来调整访问GitCafe后首页的显示模块，默认的显示模块为用户的关注动态(Activity)，您可以将其他板块拖动至第一位来设置首页默认显示模块，在以后GitCafe开放出更多新奇好玩的特性后，相信这个功能能够为您带来极大的便利。

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-activity.png "gitcafe-activity")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-activity.png)

在对于一次性push多个commit至GitCafe服务器后，动态(Activity)的时间轴会为您与您的粉丝更好地显示您push上去提交信息：

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-activity-02.png "gitcafe-activity-02")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-activity-02.png)

在创建工单(Ticket)与私信(Message)等用户可以提交评论、消息与其他内容的对话框中，GitCafe提供了Markdown语法支持以及方便好用的快捷键：

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-message.png "gitcafe-message")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-message.png)

在创建了组织或者成为一个组织的管理员后，您可以直接在创建项目中选择项目的拥有者：

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-new.png "gitcafe-new")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-new.png)

您可以在项目主页的代码浏览区域(Code
Browser)的右上角看到分享至各社交网络的链接图标，为分享自己或者他人优秀的项目而带来极大的便利：

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-share.png "gitcafe-share")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-share.png)

最后需要介绍的一个细节是您可以在创建项目时补充上中文名或者全名：

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-fullname.png "gitcafe-fullname")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-fullname.png)

这样在展示项目主页时，您将可以更好的向本地社区用亲切的母语来命名和介绍您的作品：

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-projecticon.png "gitcafe-projecticon")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-projecticon.png)

邀请更多好友加入GitCafe，免费获得GitCoin

[![](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-invite.png "gitcafe-invite")](http://lt-file.b0.upaiyun.com/files/2012/09/gitcafe-invite.png)

对于一个开发项目来说，积极并且高质量的参与者必不可少，这也是GitCafe想要为大家打造的社区氛围，我们在提供基础的项目托管服务同时，也提供了工单(Ticket)以及基础的fork与pull
request功能， 有了这些基础服务，一个项目能够更规范地管理与协作起来。

现在，点击您首页的邀请好友按钮，将您的邀请链接通过各大社交网络发送给您的朋友与粉丝们，每成功邀请一位好友将免费获得20个极特币！

致谢

GitCafe从项目成立开始研发至今已经近一年，在这一年中我们经历过坎坷，也获得过许多朋友的帮助，在此特别感谢[上海联合创业办公社](http://people-squared.com/)，我们在这里办公，也在这里找到了家的感觉。更感谢在Alpha内测阶段协助我们测试与汇报问题与改进建议的近1000位内测用户以及来自各众多开源社区与企业的支持与关心。

目前Beta版本仍然是一个非常基础的服务平台，我们不会停下脚步，将持续推出新功能与特性，对细节进一步打磨，为打造一个优秀的开发者服务平台而奋斗。您可以关注GitCafe的[新浪微博](http://weibo.com/gitcafe)以及[Twitter](http://twitter.com/gitcafe)来获取我们的最新资讯，也欢迎点击GitCafe右上角的[反馈](http://gitcafe.com/feedback)来提交Ticket给到我们问题与建议。

谢谢。

Thomas Yao ( [@ghosTM55](http://weibo.com/ghostm55) )
