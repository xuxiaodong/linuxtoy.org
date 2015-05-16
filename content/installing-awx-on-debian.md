Title: 在 Debian 上安装 AWX
Date: 2013-12-12 15:03
Author: toy
Category: Tips
Slug: installing-awx-on-debian

AnsibleWorks AWX 是 Ansible 的收费版本，它可以免费使用，但最多只能管理
10  
台主机。AWX 提供基于 Web 的界面，包含 REST API、角色访问控制、Job
模板等  
功能。

AWX 默认只支持安装到 RHEL/CentOS 6 及 Ubuntu 12.04 以上版本上。因为 AWX
本  
身也是由 Playbook 来部署的，所以我们只需稍加修改就可以用来安装到 Debian
上。

在[下载 AWX 的安装包][a]后，首先解包备用：

tar zxvf awx-setup-latest.tar.gz

接着，获取下列修改文件：

* ：对应  
roles/packages\_ubuntu/tasks/main.yml 文件  
* ：对应  
roles/postgres/tasks/main.yml 文件  
* ：对应  
roles/misc/tasks/main.yml 文件  
* ：对应  
site.yml 文件

同时，根据需要修改 `group\_vars/all`，并设置密码。

然后，执行：

./setup.sh

就开始 AWX 的安装过程了。

待安装完成，进入 `/etc/apache2/sites-enabled`，创建两个符号链接：

ln -s ../conf.d/awx.conf .  
ln -s ../conf.d/awx-plain.conf .

另外，需要将 `/etc/apache2/apache2.conf` 中的 `Require all denied`  
注释掉。

即，将：

  
Options FollowSymLinks  
AllowOverride None  
Require all denied  

改成：

  
Options FollowSymLinks  
AllowOverride None  
#Require all denied  

再重启 Apache 服务，就可以通过 访问了。AWX 默认  
用户为 admin，密码为 `group\_vars/all` 中设置的密码。

[a]: http://www.ansibleworks.com/ansibleworks-awx/
