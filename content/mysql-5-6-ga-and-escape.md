Title: MySQL 5.6 GA 及逃亡潮
Date: 2013-02-06 14:56
Author: liangsuilong
Category: Apps
Tags: Fedora, mariadb, MySQL
Slug: mysql-5-6-ga-and-escape

今日，Oracle 公司宣布 MySQL 5.6 GA，正式版为 5.6.10。

MySQL 5.6.10 GA 主要是修复了之前 RC 版本中的 Bug。MySQL 5.6 新增特性有：

-   改进的 InnoDB 存储引擎，增加全文索引能力。
-   提升子查询性能。
-   同步复制功能增强，引入多线程复制特性。
-   引入 NoSQL 特性，可直接使用 Memcached API 操作 InnoDB 数据。

官方[Release
Note](http://dev.mysql.com/doc/relnotes/mysql/5.6/en/index.html) 和 [下载地址](http://dev.mysql.com/downloads/mysql/)

本来本篇新闻就要完结。不过近日，各大 Linux 发行版的 MySQL
逃亡潮越演越烈，继 Mageia 2（原 Mandriva 社区衍生版）和 OpenSUSE 12.3
以后，Fedora 社区宣布将会在即将发布<span
style="color: #000000">~~跳票~~</span>的 Fedora 19 使用 MariaDB 替代
MySQL。MariaDB 是原 MySQL 创始人 [Michael 'Monty'
Widenius](http://en.wikipedia.org/wiki/Michael_Widenius "Michael Widenius") 创建的一个
MySQL 社区分支，为避免 MySQL 落入 Oracle
收后存在的闭源风险，同时提供更多特性及更强的性能。

[MariaDB 取代 MySQL 被列入 Fedora 19
的已确认特性内](https://fedoraproject.org/wiki/Features/ReplaceMySQLwithMariaDB)，而且完成度极高，相信
Fedora 19 不会在发布时放弃该项特性。但该项特性还是引起了争议。支持者以
Tom Lane 和 Remi Collet 等 Fedora 的 MySQL 维护者为首，认为 Oracle
缺乏对 MySQL 和 Linux 发行版支持，缺少 MySQL 文档，提交 Bug Report
也缺乏 Oracle 员工跟踪。反对者担心 MariaDB 替代 MySQL 以后会影响 RHEL
后续维护和升级，毕竟 RHEL 是获得 Oracle MySQL 认证的 Linux
发行版。当中有负责 MySQL 开发维护的 Oracle 员工参与讨论，并举例 MySQL 跟
Ubuntu 和 Debian 社区合作的成果，结果使用公司邮箱的 Oracle
员工肯定还是被围观吐槽了。[详细讨论在 Fedora
开发者列表](http://lists.fedoraproject.org/pipermail/devel/2013-January/176584.html)

MariaDB 最新稳定版本为 5.5.29，开发版本为 10.0.1 Alpha。MariaDB 10.0
依然基于 MySQL 5.5 开发，但会引入 MySQL 5.6 部分特性。MariaDB
提供以下特性：

-   XtraDB 替换 InnoDB，XtraDB 是 Percona 开发维护的 InnoDB
    威力加强版，整合 Google、Facebook 等公司和 MySQL 社区的补丁。
-   Aria 存储引擎和 Sphinx 存储引擎
-   基于 Galera Cluster 的 MariaDB 集群方案
-   多主复制（将在 MariaDB 10.0 实现，由淘宝贡献）
-   Cassandra NoSQL 存储引擎（将在 MariaDB 10.0 实现）

在 Fedora 17 和 Fedora 18，用户已经可以安装和测试 MariaDB。而在 Fedora
19，依赖 MySQL 的软件包会转为依赖 MariaDB。

`yum remove mysql mysql-libs mysql-devel mysql-server`

`yum install mariadb mariadb-libs mariadb-devel mariadb-server`

[![](http://lt-file.b0.upaiyun.com/files/2013/02/Screenshot-from-2013-02-06-132743-300x198.png)](http://lt-file.b0.upaiyun.com/files/2013/02/Screenshot-from-2013-02-06-132743.png)

你使用的 Linux 发行版，已经逃离或计划逃离 MySQL 了吗？

**补充一：**2009 年 Oracle 收购 Sun 时，Oracle 在反垄断审查中向欧<span
style="color: #000000">~~罗巴抢钱联~~</span>盟承诺继续保持 MySQL
开源并持续改进，另外一方面 Oracle 也需要 MySQL 抢占 Microsoft SQL Server
的市场份额。Oracle 这三年对 MySQL
改造所做的动作，我想读者心里早已有答案。

**补充二：**即使 MariaDB 取代 MySQL 以后，Fedora 19 依然会包含 MySQL
的软件包，用户依然可以继续选择安装使用。但用户并不能通过软件库同时安装
MariaDB 和 MySQL，因为两者间有文件冲突。而 Fedora 18 升级到 Fedora 19
的用户，系统原有的 MySQL 将会自动替换成 MariaDB。类似的情况也会出现
Apache OpenOffice，Fedora 19 有可能重新引入 OpenOffice，但 OpenOffice
会因为文件冲突而不能和 LibreOffice 共存。Fedora 19 依然使用 LibreOffice
作为默认的办公套件。
