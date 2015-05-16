Title: Ansible 1.4 添加 33 个新模块
Date: 2013-11-22 10:51
Author: toy
Category: News
Slug: ansible-14

代号为“Could This Be Magic”的 [Ansible 1.4][b] 现已推出。Ansible
是一个与 Puppet、  
Chef、SaltStack 等类似的配置管理系统，我们曾在 [Ansible
快速上手][a]一文中对其  
进行过介绍。此次发布的新版本包含来自 190 个人的贡献（Ansible
目前的活跃程度由此  
可见一斑），新添了 33
个模块，增强了语言方面的特性，此外还包括一些细微的改进。  

Ansible 1.4 的最大变化表现在模块方面。本次更新加入了 33 个模块，包括：

* 与 Google Compute Engine 交互的模块（由 Google 的 Eric Johnson
编写）  
* 改善了 Rackspace 模块、Amazon EC2 模块  
* 新的 F5 BigIP 模块  
* unarchive 模块可用来部署 tarball 包  
* synchronize 模块是 rsync 的包装  
* copy 模块支持递归复制  
* 适合 openvswitch、JBoss 的模块

语言方面，Ansible 1.4 则加入了新的 `do/until`
循环、能够通过任务失败条件进行更  
好的调控、以及通过 `subelements` 执行循环等等。

另外，Ansible 现在针对遗留特性具有方便的废弃警告提醒。

Ansible 1.4 可通过 `pip` 安装，或直接下载 [Tarball][t] 包。

[b]: http://blog.ansibleworks.com/2013/11/21/ansible-1-4-released/  
[a]: http://linuxtoy.org/archives/hands-on-with-ansible.html  
[t]: http://ansibleworks.com/releases/ansible-1.4.tar.gz
