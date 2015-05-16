Title: apt-proxy：apt 代理, 缓存
Date: 2008-09-04 18:06
Author: hmy
Category: Apps
Tags: apt-proxy
Slug: apt-proxy

[撰文/hmy]

假如有多台机器需要从 debian（or
ubuntu）的库里面下载软件来安装，如果每个机器都去网上下载一遍，肯定不划算。用
apt-proxy
可以解决这个问题。会把你现在的软件缓存起来。以后的机器安装这个软件就是从本地下载了。

另外有一个通用的解决方法是本地安装 squid，不过要做一些调整，因为 squid
默认缓存小于 4M 的文件。

**参考**

<http://apt-proxy.sourceforge.net>
