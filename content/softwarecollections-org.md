Title: SoftwareCollections.org
Date: 2014-04-15 14:16
Author: lovenemesis
Category: Productivity
Tags: CentOS, Fedora, RHEL
Slug: softwarecollections-org

在实际生产环境中，有一些时候你不得不在一台服务器上部署不同版本的应用环境，比如想在
RHEL6 上安装 Python 3.3，但又不想影响系统中现有的 Python 2.7。使用
SoftwareCollections(SCL) 可以方便的达成这个目的。

SoftwareCollections 方案的特点有：

-   可以将预编译的软件包安装的独立位置，不会覆盖系统中已有的版本。
-   可以同时运行多个不同版本的应用，每个运行在独立环境中，互不干扰。
-   无需自己手动编译及处理依赖关系，使用熟悉的 yum/rpm 软件包管理工具。
-   支持 RHEL、CentOS 和 Fedora。
-   提供 `scl` 命令行工具快速切换和管理软件包集合。
-   提供 [SoftwareCollections.org](https://www.softwarecollections.org/)
    在线查询站点。

**SCL 快速上手**

1. 以在 CentOS 上安装 PHP 5.4 为例，第一步当然是安装 SCL
命令行工具：`su -c "yum install -y centos-release-SCL scl-utils"`

2. 就可以通过 `yum` 安装 php54 了：`su -c "yum install -y php54"`  
使用 SoftwareCollections
的最大不同就是这一步的安装位置不一样，从而和系统默认的不会产生冲突。

3. 启动一个使用 php54 的新对话：`scl enable php54 'bash'` 其中 'bash'
代表打算使用来自 SoftwareCollections
中版本所要执行的程序，注意根据具体需要换成对应的名字。

目前 SoftwareCollections 提供的软件有包括 Ruby 1.9.3/2.0，Python
2.7/3.3，MariaDB 5.5、Node.js 0.10、PHP 5.4
等在内的常见语言以及应用环境。具体列表可以查看 [SoftwareCollections.org
站点](https://www.softwarecollections.org/)。

[官方发布公告](http://developerblog.redhat.com/2014/04/08/announcing-softwarecollections-org/)
