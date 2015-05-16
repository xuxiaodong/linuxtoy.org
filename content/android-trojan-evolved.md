Title: Android Trojan 进化
Date: 2011-03-11 09:39
Author: lovenemesis
Category: News
Tags: Android, Security
Slug: android-trojan-evolved

[Android
恶意软件事件](http://linuxtoy.org/archives/android-malware-%e8%ad%a6%e5%91%8a.html)进一步演化，景德镇再度成为焦点！

在[上次事件的末尾](http://linuxtoy.org/archives/android-malware-%E8%AD%A6%E5%91%8A.html)，Google
祭出 Android Market （**注意不是 Android 系统！**）的Remotely Uninstall
远程删除功能，将已经安装包含恶意代码软件从用户手机上删除并邮件通知。同时还放出安全检查工具(**Android
Market Security Tool**)以期修复恶意软件造成的破坏。

然而通过
[Symantec](http://www.symantec.com/connect/ko/blogs/androidbgserv-found-fake-google-security-patch)
和
[F-secure](http://www.f-secure.com/weblog/archives/00002116.html)的报道发现，被**恶意代码感染的
Android Market Security Tool 已经出现在景德镇的某第三方软件市场**中。

被感染的该程序，会在后台的控制下向指定服务器发送
SMS，造成开销；同时在安装后也会将用户信息发送到服务器。

在此提醒诸位使用 Android 手机的朋友：

-   特别留心**中文第三方软件市场**里提供的各类软件。
-   从非 Android Market 里下载包含“ Android Market
    ”关键词的软件时要注意。
-   安装时对于请求“会造成开销(Service that Cost your
    money)”的权限的软件要格外留心！

*消息来源：* [H
Open](http://www.h-online.com/open/news/item/Google-s-security-tool-infected-with-trojan-1205886.html)
