Title: Apache 2.2.15 发布
Date: 2010-03-09 15:24
Author: toy
Category: Apps
Tags: Apache, HTTP Server
Slug: apache-2215

最近，Apache 软件基金会和 Apache HTTP 服务器项目发布了 Apache HTTP  
Server（"httpd"）的 2.2.15 版本。Apache 2.2.15  
主要解决了一些安全方面的问题，并修正了之前版本中的缺陷。

![Apache](http://i.linuxtoy.org/images/2010/03/apache\\\_logo.png)

Apache 2.2.15 将 openssl 库更新到了 0.9.8m，解决了 CVE-2009-3555  
(cve.mitre.org) 和 TLS renegotiation
前缀注入攻击问题。另外，该版本也修正了  
mod\\\_proxy\\\_ajp、mod\\\_isapi、mod\\\_headers 等方面的问题。

查看[官方公告](http://www.apache.org/dist/httpd/Announcement2.2.html)了解详情。Apache  
2.2.15 可从[这里下载](http://httpd.apache.org/download.cgi)。
