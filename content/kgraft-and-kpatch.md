Title: 两个新的动态内核补丁项目: kGraft 和 kpatch
Date: 2014-03-05 09:46
Author: toy
Category: Kernel
Slug: kgraft-and-kpatch

给 Linux 内核动态打补丁而不必重启系统看来是最近的一项  
热点技术。虽然此前已经有了 [Ksplice][k] 来达到此类目  
的，但最近 SUSE 和 Redhat 却先后推出了类似的项目。其中，  
前者为 [kGraft][g]，后者是 [kpatch][p]。

**kGraft**

为了使 Linux 管理人员更容易的安装重要的 Kernel 安全补丁，  
同时又不让系统当机，SUSE Labs 开发了 kGraft。目前，kGraft  
尚处于功能原型阶段，SUSE 计划在本月将其提交到 Linux  
内核上游，并发布源代码。

**kpatch**

Redhat 目前已经以 GPLv2 许可发布了 [kpatch][s] 的源代码，  
其主要包含以下 4 个组件：

* kpatch-build: 用来将 source diff patch 转换成 hot patch  
module  
* hot patch module: 包含替代函数及原始函数元数据的内核模块  
* kpatch core module: 为 hot patch 注册新的函数以用于替换  
提供接口的内核模块  
* kpatch utility: 允许用户管理 hot patch 模块的命令行工具

感兴趣的朋友不妨参考文中的链接以获得更多信息。

[k]: https://linuxtoy.org/archives/ksplice.html  
[g]:
https://www.suse.com/communities/conversations/kgraft-live-kernel-patching/  
[p]: http://rhelblog.redhat.com/2014/02/26/kpatch/  
[s]: https://github.com/dynup/kpatch
