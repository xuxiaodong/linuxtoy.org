Title: 小补丁 大改善
Date: 2010-11-17 00:07
Author: lovenemesis
Category: News
Tags: Kernel
Slug: small-patch-but-huge-improvement

由于一个仅有200余行代码的补丁，未来的 Linux Kernel 2.6.38
或许会成为**下一年度最受期待 Linux 内核版本**。

这个小小的补丁仅为 Linux Kernel 增加了 233
行代码，却将**高负荷下桌面响应最大延迟降低到原先的十分之一，平均延迟降低到六十分之一！**该补丁的作用是为每个
TTY 动态地创建任务分组。

根据 Linus 本人的在 `make -j64`
的负荷下测试表明，该补丁有效的改善了高负荷情况下窗口相应和浏览器页面载入速度。Linus
称赞其为 '**a killer feature**'。

由于目前 2.6.37 的合并窗口已经关闭，**该补丁只能随着 2.6.38
进入内核**。目前该补丁打上后**默认启用**，或者使用将
`/proc/sys/kernel/sched_autogroup_enabled`
动态开关，若是增加`noautogroup` 内核引导参数的话则会关闭此功能。

*消息来源及视频演示：*[Phoronix](http://www.phoronix.com/vr.php?view=15455)

包含该补丁的 [Fedora
内核下载](http://kyle.fedorapeople.org/kernel/2.6.35.8-59.xsched1/)
