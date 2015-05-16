Title: Cacti：网络流量监测工具
Date: 2008-08-26 17:42
Author: MDZ
Category: Apps
Tags: cacti, 监测, 网络, 流量
Slug: cacti

Cacti 是一款基于 PHP 的网络流量监测工具，与 ntop 相比功能更强大。它通过
snmpget 获取数据，用 RRDtool 绘制图形。

[![Cacti](http://i.linuxtoy.org/i/2008/08/cacti_promo_main-300x223.png)](http://i.linuxtoy.org/i/2008/08/cacti_promo_main.png)

[![Cacti
Demo](http://i.linuxtoy.org/i/2008/08/get_imagephp-281x300.png)](http://i.linuxtoy.org/i/2008/08/get_imagephp.png)

使用 Cacti 需要 PHP、MySQL、snmp、rrdtool
等环境和工具。在安装前保证它们的正常运行。

Ubuntu 用户可通过 apt-get 来获得。安装完后在浏览器中输入
http://localhost/cacti 就可监测网络流量。

官方网站：<http://www.cacti.net/>  
下载地址：<http://www.cacti.net/downloads/cacti-0.8.7b.tar.gz>  
截图：<http://www.cacti.net/screenshots.php>
