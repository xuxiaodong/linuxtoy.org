Title: 直接 Paste 代码到网络上的好东东
Date: 2010-05-04 20:54
Author: toy
Category: Tips
Slug: paste-code

{ 撰文/UNKNOWN }

是不是很郁闷 QQ  
里面贴代码的时候会自动转换成很多奇怪的表情，是不是比较长的代码一贴 QQ  
就不能贴上去？是不是传软件很麻烦，还要登
E-mail，还要手选？还要等？现在都已经不是问题了，直接命令行下面 pipe
就可以完成。

主要介绍 3 个同类软件，可以自由选择:

+ [dpaste](http://dpaste.com)  
+ [pastebin](http://pastebin.com)  
+ [pastie](http://pastie.org)  
+ wgetpaste

软件作用:

直接把管道里面的文字内容传到网站上面，然后反馈一个地址可以读取内容。  
看一个 wgetpaste 例子，就很清楚了:

[![wget-paste](http://i.linuxtoy.org/images/2010/05/thumb-wget-paste.jpg)](http://i.linuxtoy.org/images/2010/05/wget-paste.jpg)

[![dpaste](http://i.linuxtoy.org/images/2010/05/thumb-dpaste.jpg)](http://i.linuxtoy.org/images/2010/05/dpaste.jpg)

现在来比较一下 pastebin，pastie，wgetpaste:

(dpaste 没有具体用过，所以还希望大家补一下，别说我懒哦，Linux
正在重装，估计看见 emerge -pv kdebase-meta 说还要 200
多个包谁都会*\_*吧，现在在 Win 下面先快活一下!)。

+ dpaste: 官网介绍说默认是保存 7 天，如果点 hold 的话，会在 30
天都没人看的情况下删除。  
+ pastie: 站点没上去，笔者电信的网络(原因嘛，自己去想)。  
+ pastebin: 支持 x 种代码高亮，保存的数据限制是 1024000 Bytes
以内，保存时间默认是"天"，还有"月"，"永久"可选。[详见这里](http://pastebin.com/help)
为测试，传输过 /bin/ls，结果下载下来是个空文件(那干嘛叫 bin 啊？)。但是
`cat /bin/ls | base64 | pastebin` 是 OK 的。  
+ wgetpaste: 传输大小未知，时间未知。传输 /bin/ls，传到一半就提示错误。

最后的疑问，为什么可以方便上传但是不能利用 id 值来方便下载到管道呢？

{ Thanks UNKNOWN. }
