Title: bbmail－小巧的邮件提醒程序
Date: 2006-08-26 11:32
Author: toy
Category: Apps
Slug: bbmail

bbmail 是 bbtool
中的一个邮件提醒程序，非常小巧，易于配置，具体配置参数可参考这个
[manual](http://manpages.debian.net/cgi-bin/display_man.cgi?id=d1078577c96360f2d288860f3d2378f3&format=html)。

1.安装 bbmail

`sudo apt-get install bbmail`

2.编辑配置文件

` 　　mkdir ~/.bbtools 　　cd ~/.bbtools 　　vim bbmail.bb 　　`

把下面的文件贴进去：  

　　` 　　bbmail.numberOf.mailboxes: 1 　　bbmail.mailbox.*.type:maildir 　　bbmail.mailbox.*.filename:/home/jazzihong/Mail/inbox/ 　　bbmail.mailbox.*.newmail.color:green 　　bbmail.mailbox.*.newmail.textColor:blue 　　bbmail.mailbox.*.newmail.pressed.runCommand:xterm -ls -fn -misc-fixed-medium-r-normal--18-120-100-100-c-90-iso10646-1 -e mutt 　　bbmail.pressed.runCommand:xterm -ls -fn -misc-fixed-medium-r-normal--18-120-100-100-c-90-iso10646-1 -e mutt 　　bbmail.show.newmail.counter:yes 　　`

［提醒］  
　　这里用到了
mutt，具体配置请看[这里](http://forum.ubuntu.org.cn/viewtopic.php?p=115871#115871)。

[参考资料］  
　　1.[bbtool](http://bbtools.windsofstorm.net/index.phtml)  
　　2.[bbmail
manual](http://manpages.debian.net/cgi-bin/display_man.cgi?id=d1078577c96360f2d288860f3d2378f3&format=html)

（注：此文为 [jazzi](http://hi.baidu.com/jazzi) 投稿，感谢。）
