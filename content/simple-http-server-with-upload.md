Title: 一个支持上传的简单 HTTP Server
Date: 2010-05-16 15:48
Author: toy
Category: Apps
Tags: HTTP Server, Python
Slug: simple-http-server-with-upload

{ 撰文/[bones7456](http://li2z.cn/) }

现在，很多人都知道，Python 里有个  

SimpleHTTPServer，可以拿来方便地共享文件。比如，你要发送某个文件给局域网里的同学，你只要  
cd 到所在路径，然后执行这么一行：

python -m SimpleHTTPServer

人家就可以通过 http://你的IP:8000  
来访问你要共享的文件了。像我早已把这个命令做了  

alias。但是，某一天，你需要从同学哪里复制一个文件到本机，然后你就会跟你同学说，XX，共享下某目录。当你以为可以用  
HTTP 来访问他的 8000 端口的时候，他却告诉你，不好意思，我是 Windows  
啦~~当然你可以选择在他 Windows 里装个 Python，也可以选择使用
Samba、FTP  

等其他方式，但是有没有和之前一样简单的方式呢~当然了，这时候，你就需要一个支持上传的简单  
HTTP
Server，也就是我这个：[SimpleHTTPServerWithUpload.py](http://bones7456.googlecode.com/svn/trunk/SimpleHTTPServerWithUpload.py)，哈哈。然后你开个服务，让人家上传即可。

其实这个就是修改自 SimpleHTTPServer
的，只不过我给它加上了最原始的上传功能，安全性方面没有验证过，不过理论上应该不会没人一直开着这个吧？另外，我对
RFC1867 的理解不一定透彻，所以，Use on your own risk!

截图如下：

![simple-http-server](http://i.linuxtoy.org/images/2010/05/simple-http-server.png)

代码[在此](http://bones7456.googlecode.com/svn/trunk/SimpleHTTPServerWithUpload.py)，单文件、零配置，直接用
Python 运行。

{ [Source](http://li2z.cn/2010/05/15/simplehttpserverwithupload/).
Thanks bones7456. }
