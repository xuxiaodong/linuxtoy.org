Title: Fedora Updates 服务恢复
Date: 2008-09-10 22:36
Author: lovenemesis
Category: News
Tags: Fedora
Slug: fedora-updates

8月28日 Fedora
更新服务器遭到未授权侵入，管理人员及时发现该侵入并停止了受影响的更新服务，于是
Fedora
的软件仓库在这近半个月的时间未有任何更新。对数万个软件包的重新签名过程终于在今天结束了，目前
Fedora 的软件更新服务已经恢复，强烈建议 Fedora 的用户立即执行更新！  

尽管这次入侵导致的具体损害报告还没有放出，为了安全期间， Fedora
社区更改了用于签名的公钥，所以本次更新的过程略有不同：

-   首先，在终端中输入 su -c 'yum update'，或者使用 PackageKit-gnome
    。等待软件仓库列表下载完毕后会提醒有一个名为 fedora-release
    的包需要更新，请确定并安装更新。
-   之后，再次运行 su -c 'yum update'，会发现多了一个软件仓库地址
    updates-newkey。
    依据系统中已安装的软件包数量，会提示有大量的软件包需要更新，此时请确认此更新。
-   在更新的软件包下载完毕后，会提醒有一个新的 GPG Key
    需要导入，此时确认即可开始安装刚下载的更新了。

注意此过程仅对 Fedora 8 和 Fedora 9
的这两个版本有效，对生命周期已经结束的 Fedora 7
及更早的版本将不会重新签名。很快将会有一个更新包负责删除系统中已经废弃不用的
GPG Key 和软件仓库信息。

详细信息请查看[这里](http://forums.fedoraforum.org/showthread.php?t=198892)。
