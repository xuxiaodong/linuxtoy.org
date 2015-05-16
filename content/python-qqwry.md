Title: 使用Python查询纯真IP(完整)
Date: 2014-08-09 15:52
Author: jianlee
Category: Apps, News
Slug: python-qqwry

纯真IP是一个非常不错的IP数据库

本文内容有：

1. 解析纯真IP数据库文件格式(即 qqwry.dat
文件格式），可以根据自身需要，使用熟悉的语言去读取IP记录（虽然网络上己有各种语言版本，但动手写一写的必要性还是有的）．

2. 提供一个 Python 语言实现的查询纯真IP数据库版本．

[qqwry.py
源代码](https://github.com/gwind/ylinux/blob/master/tools/IP/QQWry/qqwry.py "使用Python查询纯真IP代码")

[关于 QQWry (纯真IP数据库）->
README](https://github.com/gwind/ylinux/tree/master/tools/IP/QQWry)

测试中用到的
[ip.list](https://github.com/jianlee/ylinux/blob/master/tools/IP/QQWry/ip.list)

使用示例：

1. 重新查询"<https://linuxtoy.org/archives/python-ip.html>中的所有IP"

    $ python qqwry/qqwry.py -q `cut -d' ' -f 1 1.list` -f qqwry/qqwry.dat
      122.224.7.146 浙江省绍兴市上海网宿科技股份有限公司电信CDN节点
     89.163.144.165 德国 CZ88.NET
    211.174.187.161 韩国首尔
     59.166.120.184 日本ATHOME网络
      147.231.70.91 捷克科学院
        85.28.26.66 俄罗斯 CZ88.NET
     218.239.223.77 韩国 CZ88.NET
      216.146.47.37 美国新罕布什尔州曼彻斯特Dynamic Network Services公司
       122.155.0.62 泰国 CZ88.NET
        69.31.5.120 美国弗吉尼亚州费尔法克斯县麦克莱恩社区GTT股份有限公司旗下nLayer通信股份有限公司
      75.109.170.56 美国 CZ88.NET
      69.43.142.150 美国 CZ88.NET
        59.109.6.83 北京市方正宽带
     125.46.248.158 河南省郑州市联通
      201.17.35.128 巴西圣保罗
     212.175.84.152 土耳其 CZ88.NET
     219.134.242.67 广东省深圳市电信ADSL
     213.228.142.42 葡萄牙 CZ88.NET
      85.17.182.198 荷兰阿姆斯特丹LeaseWeb IDC
       218.77.129.6 海南省电信
     61.151.248.152 上海市电信
     210.210.18.218 印度 CZ88.NET
     194.171.247.21 荷兰 CZ88.NET
       59.57.251.57 福建省厦门市电信
      218.56.61.114 山东省济南市联通
     220.130.208.19 台湾省台北市中华电信数据通信分公司
      201.63.218.70 巴西 CZ88.NET
     118.102.25.161 河北省廊坊市华瑞信通网络科技有限公司

 

说明：

2009年我在[LinuxToy](https://linuxtoy.org "LinuxToy")发了一篇贴子:
<https://linuxtoy.org/archives/python-ip.html>
．其主题与本贴一致，但本次更新，内容变化颇大，故另起一篇．另外，我于2009年写的版本有很大错误，但当前网络上查找python版本实现时，还有一些帖子原文引用这个版本的程序．惭愧！

 

资源:

[下载纯真IP库 txt
格式（使用本程序dump）3.4M(xz)](https://github.com/gwind/ylinux/blob/master/tools/IP/QQWry/ip.txt.xz)
