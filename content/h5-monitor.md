Title: h5-monitor: 文件修改监控软件
Date: 2010-03-17 10:37
Author: toy
Category: Apps
Tags: Go, h5-monitor
Slug: h5-monitor

{ 撰文/[lvscar](http://lvscar.info) }

h5-monitor 是一个适用于 Linux  
的文件修改监控软件，它能在文件发生变更时把最新的文件内容通过 websocket  
实时广播到多个浏览器，h5-monitor  
部署非常方便，只需要在服务器上运行单独的可执行文件，即可同时响应 html
页面和  
websocket 内容请求。

环境依赖:

+ Server: Linux 2.6.13+  
+ Client：Chrome 4.0.249+

适用于 Linux (i386&amd64)的二进制可执行文件:  
[下载](http://svn:svn@svn.lvscar.info/4fun/h5-monitor/h5-monitor)

使用方法:

$touch /tmp/h5-monitor\_test  
$./h5-monitor --listen=127.0.0.1:12345 [--access=YOUR\_PROXY\_DOMAIN]
[--debug] /tmp/h5-monitor\_test  
google-chrome access http://127.0.0.1:12345  
$echo "hello world" > /tmp/h5-monitor\_test

项目主页:  
发布手记:

h5-monitor 使用 GO 语言开发而成。

{ Thanks lvscar. }
