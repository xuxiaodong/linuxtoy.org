Title: du/ncdu 的结果和 df 不一致！
Date: 2010-03-12 23:32
Author: ihipop
Category: AskLinuxtoy
Slug: different-of-du-df

{ 文/[ihipop](http://ihipop.gicp.net/2010/03/802.html)}

还记得 LinuxTOY 介绍过得 [ncdu](http://linuxtoy.org/archives/ncdu.html)
么

今天发现了一个问题，du/ncdu 和 df 显示的结果不一致！  
  
我的磁盘结构如下（sda6 mount 到了 opt/attachements 目录下面）  
  

[![](http://i.linuxtoy.org/images/2010/03/112.png)](http://i.linuxtoy.org/images/2010/03/112.png)  
  
我一看，根目录已经 50% 了  
就 cp apache 的日志到 /blog/ 里面去了，然后<span style="#ff0000;">**用
sftp 删除了原来 apache 的日志（用 cp 复制，但是用 sftp
删除的）**</span>，结果一个 df -h 发现 /blog
目录的占用是上去了。但是根目录还是占用 50%  
于是我用 ncdu 来 exclude 掉 blog 和 attachments
两个目录，发现实际占用只有到 8GB

> `ncdu --exclude blog --exclude attachments /`

运行结果:

[![](http://i.linuxtoy.org/images/2010/03/11.png)](http://i.linuxtoy.org/images/2010/03/11.png)  
  
我还是不相信，就用 du 计算了一下

> `du` `-h  --summarize --exclude=attachments --exclude=blog /`

得到的结果 8.1G，和 ncdu 相差无几  
我还是不敢相信自己的眼睛

> 8G/26G=50%？？？？？？？？？

> 13-8=5GB

那个 5GB 那里去了？  
不是被我删除的那个日志么？》  
怎么还没释放？??  
于是我

> `cat` `/dev/null  >/blog/acces_log`

结果运行 df -h 一看，blog 的占用是下去了，可是根目录的占用还是没掉

咋回事？

是我脑残了还是我对 Linux 的磁盘占用理解有误？？？
