Title: Fedora 又开始开发新概念的东东了
Date: 2008-11-25 08:34
Author: toy
Category: News
Tags: Fedora
Slug: developing-new-features-for-fedora

[作者：guest]

[Fedora 10](http://linuxtoy.org/tag/fedora-10) 还没正式发布，就又有 5
个新特性提上 Fedora 11 的特性表了。具体内容请见 [Fedora
Wiki](https://fedoraproject.org/wiki/Features/Dashboard#Fedora_11_Feature_Dashboard)。我个人比较感兴趣的是其中的
DeviceKit。这个软件的开发者在页面中提到了 HAL
的某些不足（这个我不大懂，有兴趣的去看[原文](http://lists.freedesktop.org/archives/hal/2008-May/011560.html)），最终决定发布这个
DeviceKit，他的目标是：

> It is designed to partially replace hal and overcome some of the
> design limitiations of hal.

即针对 HAL 设计上的不足而设计，以部分替代
HAL（翻译水平有限请见谅）。光是这一个 DeviceKit 也不算什么，但是最近
Fedora 开发（当然不完全是 Feodra 开发，Fedora
是主导开发）的几个新概念的库都是针对相关领域的短处进行开发的，而且还都是些非常底层的东东，比如一般性音频输出的
PulseAudio，针对各个发行版软件包管理器差异开发的
Package-kit，针对桌面用户权限认证开发的 PolicyKit，针对 X 和 Kernel
开发的 KMS，以及最近的小型图形服务器 Wayland（虽然 FAQ 说是与 X
共存，但我认为就是要在本地运行的 Linux 上替代 X），Wayland
的长期计划可能包括 GTK 和 QT 的后端移植，而需要迁移 HAL 代码到 DeviceKit
的软件列表就有一页半（还仅仅是主要的），觉得 Fedora 还真是有活力啊。
