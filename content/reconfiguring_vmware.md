Title: 系统内核升级后 VMware 不能运行的解决办法
Date: 2006-08-01 15:17
Author: toy
Category: Tutorials
Slug: reconfiguring_vmware

在使用“sudo apt-get dist-upgrade"升级系统内核后，VMware
无法运行了。以下是解决步骤：

1.安装当前版本适合的内核 headers

`sudo apt-get install linux-headers-$(uname -r)`

2.重新配置 VMware

`sudo /usr/bin/vmware-config.pl`

3.采用默认配置即可，只是当问到

`Would you like to skip networking setup and keep your old settings as they are? (yes/no)`

时，回答“yes” 就可以不必重新配置网络了。

注：此方法在 Ubuntu Dapper + VMware 5.5.1 环境测试通过。

参考：[1](https://wiki.ubuntu.com/VmWare?highlight=%28vmware%29)
[2](https://wiki.ubuntu.com/InstallingVMWare?action=show&redirect=VmWare+guide%3A+How+to+install+VMware+in+Breezy)
