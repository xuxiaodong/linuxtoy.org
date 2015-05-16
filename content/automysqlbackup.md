Title: AutoMySQLBackup——自动备份 MySQL 数据库的脚本
Date: 2006-08-01 14:55
Author: toy
Category: Apps
Slug: automysqlbackup

[AutoMySQLBackup](http://sourceforge.net/projects/automysqlbackup/)
是一个功能强大的脚本，它调用 mysqldump 来备份 MySQL
数据库，具有如下特点：

-   每天、每周、每月自动备份；
-   支持一次备份多个数据库；
-   对备份数据进行压缩，以便节省占用空间；
-   本机、远程皆可备份；
-   可以发送到指定的邮箱。

在使用之前进行简单设置即可：

    USERNAME=设置 MySQL 数据库用户名
    PASSWORD=设置 MySQL 数据库密码
    DBHOST=设置 MySQL 数据库地址（使用 IP）
    DBNAMES=设置 MySQL 数据库名称（放在""中），多个数据库使用空格分开
    BACKUPDIR=设置 MySQL 数据库备份路径（默认为"/backups"）

做好之后，把它丢到/etc/cron.daily吧，这样系统就会每天帮你自动备份 MySQL
数据库了。

如果要还原的话，在解开压缩文件之后，使用下面的命令：

`mysql --user=username --pass=password --host=dbserver database < /path/file.sql`

注意：你需要根据自己的实际情况来填充命令中的相应内容。另外，如果想要获得更详细地设置的话，请阅读脚本文件中的注释。
