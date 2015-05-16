Title: Oracle Linux: CentOS 的更好替代品？
Date: 2012-07-19 13:44
Author: lovenemesis
Category: News
Tags: CentOS, Oracle
Slug: is-oracle-linux-real-better-alternative-of-centos

最近 Oracle 宣称旗下的 Oracle Linux 是比 CentOS
更好的免费替代品，且提供了一个切换脚本。不过，事实真的是这样子么？

在 [Oracle 的宣传页面](http://linux.oracle.com/switch/centos/)上，Oracle
大力强调 Oracle Linux 的优势：

-   相比 RHEL，Oracle Linux 提供免费的软件更新。
-   相比 CentOS，Oracle Linux 更快的提供安全更新。
-   雇佣有专业的工程师和 QA 团队。
-   如果需要付费支持的话，价格比 RHEL 便宜。

难道 Oracle (良心发现)决定回馈 Linux 用户了？醒醒吧，亲，这是 Oracle！

[CentOS
社区的开发者在博客](http://www.bashton.com/blog/2012/oracle-spreading-fud-about-centos/)上给出了和
Oracle 在宣传页面上故意忽略的内容：2012 年的安全更新时间表。

  Red Hat Bug ID   Red Hat 修复发布   CentOS 修复发布   Oracle 修复发布   差异 (天)
  ---------------- ------------------ ----------------- ----------------- -----------
  2012-0743        18-Jun-2012        19-Jun-2012       21-Jun-2012       2
  2012-0571        15-May-2012        16-May-2012       21-May-2012       5
  2012-0481        17-Apr-2012        17-Apr-2012       23-Apr-2012       6
  2012-0350        6-Mar-2012         7-Mar-2012        12-Mar-2012       5
  2012-0124        13-Feb-2012        14-Feb-2012       14-Feb-2012       0
  2012-0052        23-Jan-2012        24-Jan-2012       25-Jan-2012       1

从表中可以明显看出实际上 **CentOS 在 2012 年中几乎都比 Oracle Linux
更早获得安全更新**，这也是创建的 CentOS 持续更新仓库带来的改善。

值得指出的是如果企业用户真的关心获得安全更新的时间点的话，应该去订阅
RHEL 的支持服务，而不是 Oracle 的。**Oracle Linux 永远不会比 RHEL
更快获得安全更新。**

[TechCrunch
对于此事件的报道(评论中包含很多内容)](http://techcrunch.com/2012/07/18/oracle-spreads-fud-about-centos-but-misses-the-mark/)
