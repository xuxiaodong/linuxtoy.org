Title: 解决 VMware 在 2.6.24 内核下的问题
Date: 2008-02-12 10:07
Author: toy
Category: Tips
Slug: vmware-and-kernel-2624

昨天，系统将内核升至 2.6.24，除了 VMware Server
停止响应外，其他一切尚好。根据以往的经验，只需重新配置 VMware
Server，并编译适应新内核的 VMware 模块即可。于是遂调用 VMware Server
配置程序 vmware-config.pl，无奈在编译模块时却无法通过。

后想起原来在安装 VMware Server 时使用过 VMware-any-to-any-update
补丁，就找来最新版一试，果然灵验。该 VMware-any-to-any-update 最新版为
116，可从[这里下载](http://i.linuxtoy.org/files/vmware-any-any-update-116.tgz)。其使用方法如下：  

` tar zxvf vmware-any-any-update-116.tgz cd vmware-any-any-update116/ ./runme.pl`

在执行补丁操作后，runme.pl 将调用
vmware-config.pl，按提示操作即可，此不赘述。

另外，要补充的是，此 VMware-any-to-any-update 补丁无论对于 VMware
Server，还是对于 VMware Workstation
都是适用的。希望以上提及的对遇到同样问题的朋友有所帮助。
