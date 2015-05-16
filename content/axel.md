Title: Axel－加速下载工具
Date: 2006-09-02 17:55
Author: toy
Category: Apps
Slug: axel

[Axel](http://wilmer.gaast.net/main.php/axel.html) 通过打开多个 HTTP/FTP
连接来将一个文件进行分段下载，从而达到加速下载的目的。对于下载大文件，该工具将特别有用。

-   安装：`sudo apt-get install axel`
-   一般使用：`axel url（下载文件地址）`
-   限速使用：加上 -s 参数，如 -s 10240，即每秒下载的字节数，这里是 10
    Kb
-   限制连接数：加上 -n 参数，如 -n 5，即打开 5 个连接

[[via](http://www.cyberciti.biz/tips/download-accelerator-for-linux-command-line-tools.html)]
