Title: Fail2ban: 自动扳掉恶意 IP
Date: 2013-01-04 14:33
Author: toy
Category: Apps
Slug: fail2ban

[Fail2ban][f]
通过解析日志文件并根据恶意行为（如多次口令失败）来自动扳掉特定的 IP
地址，从而加固 Linux 服务器的安全性。

![fail2ban](http://lt-file.b0.upaiyun.com/files/2013/01/fail2ban.jpg)

Fail2ban 支持 apache、sshd、vsftpd
等多种服务，能够自定相应操作，如更新防火墙规则、发送 Email
等。其源码可从 [Fail2ban][d] 官网获取，或通过所用发行版的包管理器安装。

[f]: http://www.fail2ban.org  
[d]: http://www.fail2ban.org/wiki/index.php/Downloads
