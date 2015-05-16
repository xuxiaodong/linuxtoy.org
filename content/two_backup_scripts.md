Title: 两个备份的脚本
Date: 2006-11-13 08:26
Author: toy
Category: Apps
Tags: MySQL
Slug: two_backup_scripts

下面两个脚本用于备份 MySQL
数据库和文件夹（比如你的网站和系统配置文件夹）。因为其中包括了密码等安全信息，所以请将脚本文件的权限设置为其他人不可读。定期调用请使用
crontab。

备份文件中可能包含一些敏感信息，所以使用 GPG 加密是明智的选择。关于 GPG
见我的文章 《[GnuPG 简介](http://huichen.org/8)》。

1.  备份数据库  

    ` DBPASS=your db password DBUSER=your db user name DBNAME=your db name GPGUID=your gpg uid EMAIL=”your@email.com”`  
    ` mysqldump $DBNAME --`opt -u $DBUSER -p$DBPASS >
    /home/you/db.sql  
    gpg -r $GPGUID -e /home/you/db.sql  
    rm /home/you/db.sql  
    gzip /home/you/db.sql.gpg  
    DATE=`date +%Y%m%d` ; mv /home/you/db.sql.gpg.gz
    /home/you/db.$DATE.sql.gpg.gz  
    echo ‘MySQL Backup is attached’ | mutt -a
    /home/you/db.$DATE.sql.gpg.gz $EMAIL -s “MySQL Backup “$DATE  
    rm /home/you/db.$DATE.sql.gpg.gz  
   这个脚本会将你的数据库 dump 到一个文件，然后用 GPG 将其加密（你的
    pub key 的 UID 为
    GPGUID），压缩，最后发送到你的信箱保存。注意将其中的 DBPASS, DBUSER,
    DBNAME, GPGUID, EMAIL, /home/you 等修改掉，DBUSER 用户并不需要对
    DBNAME 数据库有完全的权限，只要 select 和 lock
    权限即可，所以你可以建立一个 MySQL 用户专门用来备份。
2.  备份文件夹  

    ` GPGUID=your gpg uid EMAIL=”your@email.com” tar -cf /home/you/folder.tar /the/local/dir/ --`absolute-names
    `--`ignore-failed-read  
    chmod go-rwx /home/you/folder.tar  
    gpg -r $GPGUID -e /home/you/folder.tar  
    rm /home/you/folder.tar  
    gzip /home/you/folder.tar.gpg  
    DATE=`date +%Y%m%d` ; mv home/you/folder.tar.gpg
    /home/you/folder.$DATE.tar.gpg.gz  
    echo ‘Folder Backup is attached’ | mutt -a
    /home/you/folder.$DATE.tar.gpg.gz $EMAIL -s “Folder Backup
    “$DATE  
    rm /home/you/folder.$DATE.sql.gpg.gz  
   工作原理和第一个脚本类似。

~~需要注意的是，上面两个脚本的双减号在 wordpress
中无法正常显示，所以我用两个减号中间加空格来代替。~~

更新：根据 [Citygrit
网友的提示](http://blog.citygrit.cn/?p=94)，已顺利解决了 `--`
的显示问题。

[撰文/[Hui](http://huichen.org)]
