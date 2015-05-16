Title: Fedora 15 的两项新功能
Date: 2010-11-10 11:30
Author: lovenemesis
Category: News
Tags: Fedora, wayland, yum
Slug: two-new-possible-features-on-fedora-15

今天 Fedora QA 负责人 rahulsundaram 透露了两条 Fedora 15
可能包含的新功能！

首先，**Wayland 也将被打包并入 Fedora 15**，但是不会做为默认 X
服务器，此举只为方便测试。不过具体的工作安排也尚未成型。

*消息来源：*[Fedora 邮件列表](http://cut.gd/2z0U)

其次，**Yum 增加自动移除无用依赖包功能**。和已经存在一段时间的
`remove-with-leaves` 插件不同，此次合并入 Yum
本身的无用依赖包移除功能直接通过 Yumdb
的信息获取依赖关系，无需进行常常出错的额外依赖性检验。包含该功能的
`Yum 3.2.28-13` 已推送 Fedora Rawhide 仓库，安装后在 `/etc/yum.conf`
中添加 `clean_requirements_on_remove = 1` 选项即可体验。

*消息来源：* [skvidal 博客](http://cut.gd/1F4b)
