Title: MyPHPdumpTool：MySQL 数据库备份解决方案
Date: 2006-11-01 19:19
Author: toy
Category: Apps
Slug: myphpdumptool

[MyPHPdumpTool](http://sourceforge.net/projects/myphpdumptool/)（简称
mpdt）是一个不错的 MySQL 数据库备份解决方案。它使用 PHP
所写，可直接在命令行执行。无论是本机的，还是远程的 MySQL 数据库，mpdt
都能胜任。它除了能够将所备份的 MySQL
数据库保存到当前的机器上之外，也可以将其上传到 FTP 服务器。结合
Cron，使用 mpdt 还可以实现按照计划自动备份，十分方便。

由于 mpdt 是通过在 CLI 执行的应用，所以首先要确保系统中存在 PHP
命令行程序。如果没有，则可以通过 `sudo apt-get install php5-cli` 安装。

在下载了mpdt 之后，使用 `tar xvzf mpdt*.tar.gz` 解包。mpdt 的用法如下：

`php mpdt.php [1] [2]`

其中，[1] 为需要备份的 MySQL 数据库配置信息，[2] 为要上传的 FTP
服务器配置信息。二者可以在 lib/config.inc.php 文件中配置。

对于 MySQL 数据库来说，主要配置以下四个方面：

` "DBHost"=>"xxx.xxx.xxx.xxx", "DBUser"=>"dbuser", "DBPasswd"=>"dbpasswd", "DBName"=>"dbname"`

DBHost 可以为 localhost，也可以为确定的 IP 地址；DBUser
即所备份的数据库的用户名；DBPasswd 为需备份数据库的密码；DBName
是要备份的数据库名称，如果是备份所有的数据库，则填写“all”。

与 MySQL 数据库类似，FTP 服务器的配置包括：

` "FTPHost"=>"xxx.xxx.xxx.xxx", "FTPUser"=>"ftpuser", "FTPPasswd"=>"ftppasswd"`

依次为 FTP 服务器的 IP、用户名及密码。

需要说明的是，无论是 MySQL 数据库还是 FTP
服务器，都可以保留多个配置信息，如 profile1、profile2 等等。

在备份时，如下调用配置信息即可：

`php mpdt.php profile1 profile1`

如果不需要备份到 FTP 服务器，则将 `$ftp_bool=1;` 设为
0。默认会将文件备份到 archive 目录。

要按照计划自动完成备份的话，执行 `crontab -e`，在其中添加下列内容：

` 50 23 * * * /usr/bin/php [dir_path]/mpdt.php [db_profile_name] [ftp_profile_name]`

这将会在每天的 23 点 50 分执行备份任务。注意，请根据实际情况酌情修改。
