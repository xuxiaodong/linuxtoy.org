Title: Fedora 18: Yum 与 PackageKit 和谐共处
Date: 2012-10-30 11:50
Author: lovenemesis
Category: News
Tags: Fedora, packagekit, yum
Slug: yum-no-longer-collides-with-packagekit-in-fedora-18

在 Fedora 18 中，在终端单独运行 yum 将不再会遇到需要等待 PackageKit
结束任务的困扰。

PackageKit 作为 yum
的前端，常常会依据系统设置在后台执行诸如检测安全更新等操作。若在此时在终端再单独运行
yum，会被提示 yum 被 PackageKit 锁定，需要等待。根据 PackageKit
后台执行任务的不同，等待时间从几秒钟到几分钟不等。迫不及待的用户常常会因此
kill 掉 PackageKit 进程。

在 Fedora 18 中最新的 Yum 和 PackageKit 改进了这个状况。现在 PackageKit
守护进程在收到来自终端的 yum
运行请求时，**会暂停正在执行的后台任务，释放 yum
锁，交还给终端单独运行的 yum** 。当终端的 yum 运行命令结束后，再重新恢复
PackageKit 的后台任务执行。

[消息来源](http://kparal.wordpress.com/2012/10/22/fedora-18-yum-no-longer-collides-with-packagekit/)

[补丁及 Bugzilla
追踪](https://bugzilla.redhat.com/show_bug.cgi?id=812938)
