Title: Simple Mail: Firefox 上的 E-mail 客户端
Date: 2010-03-25 18:26
Author: toy
Category: Firefox Extension
Tags: Firefox, Mail
Slug: simple-mail-for-firefox

{ 撰文/Gunn }

最近一直在为 Ubuntu 下面的邮件 App 烦恼。用了很长一段时间的  
Evolution，界面很清爽，对 GNOME  
相当友善，但是有一个非常大的问题就是体积和占用资源。

这个大怪物在 home
下面会生成非常大的文件夹，即使在界面上删除了邮件，目录的体积并不会减少。倒腾了半天，写了一个脚本，勉强解决了这个问题，但是无奈
Evolution 就是
Evolution，即使删除了所有邮件，这个玩意还是忒大...资源的占用就更不用说了，何况我用的还是
Netbook。

这几天还尝试了不少其他的邮件软件，都放弃了，原因如下:

+ Thunderbird -- 我知道它很好用，有很多的插件，但是要像 Firefox
那样重新个人化起，我就没有耐心了  
+ Claws / Sylpheed -- 反正就是用不惯，中途出现两次崩溃  
+ Balsa -- 貌似 Ubuntu 官方和 PPA
里面都没有新版本，所以能安装的版本都不能支持 Gmail 的 SMTP

主角请出场：[Simple
Mail](https://addons.mozilla.org/en-US/firefox/addon/5593)

[![Simple  

Mail](http://i.linuxtoy.org/images/2010/03/simple-mail-thumb.png)](http://i.linuxtoy.org/images/2010/03/simple-mail.png)

这个插件非常的小（废话），不到 200k，优点:

+ POP、IMAP、SMTP 全支持，而且对 Gmail 自动补全 Port  
+ 邮件存放位置可以自定义  
+ 界面清爽，新创作的邮件单独 Tab  
+ 自动补全邮件地址（这个好的功能，Evolution 竟然没有）  
+ 有 Filter（大加分，特别是当邮件特别多的时候，非常需要的一个功能）

缺点:

+ 读邮件的时候不能新建 Tab  
+ 2 个 Gmail
帐户不能同时使用（似乎是这样的，我建立两个之后收发邮件就开始报错，非
Gmail 邮箱也许可以）

{ Thanks Gunn. }
