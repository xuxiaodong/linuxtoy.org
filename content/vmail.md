Title: Vim + Gmail = Vmail
Date: 2012-12-17 11:28
Author: toy
Category: Apps
Tags: Gmail, Vim
Slug: vmail

简言之，[Vmail][v] 是 Vim + Gmail 的结合体，她允许你在 Vim
这一经典的文本编辑器中处理一切 Gmail
事务，诸如收发、阅读、星标、存档、删除、搜索邮件等等。体验一番下来，Vmail
给我的感觉是操作流畅，速度不错。

[![vmail](http://lt-file.b0.upaiyun.com/files/2012/12/vmail-thumb.png)](http://lt-file.b0.upaiyun.com/files/2012/12/vmail.png)

**安装及配置**

Vmail 需要 Ruby 1.9.0 以上版本（包含 SSL
支持）、sqlite3/libsqlite3-dev、及 lynx（用于查看 HTML
邮件）等使用依赖，通过以下指令可安装：

% gem install vmail

在安装完成后，给 Vmail 添加配置信息：

% vim ~/.vmail/defaults/.vmailrc

其中新添内容主要为：

username: yourusername@gmail.com  
password: yourpassword  
name: Your Name

现在，你可以执行 `vmail` 来启动它了。

**使用简述**

Vmail 启动后，默认将载入 100 封邮件，在其条目上按
Enter（回车）即可打开新的分隔窗口来阅读该邮件。Vmail 的其他操作包括：

* ,c - 撰写新邮件，完成后可用 ,vs 发送  
* ,* - 星标邮件  
* ,# - 删除邮件  
* ,e - 存档邮件  
* ,! - 标记为垃圾邮件  
* U 和 I - 分别标记为未读和已读  
* ,u - 检查新邮件  
* ,m - 切换邮箱  
* ,r - 回复  
* ,a - 回复全部  
* ,f - 转发  
* ,s - 搜索

更完整的使用说明，可参考 [Vmail 主页][v]。

[v]: http://danielchoi.com/software/vmail.html

{ via [Hacker News](https://news.ycombinator.com/item?id=4922542) }
