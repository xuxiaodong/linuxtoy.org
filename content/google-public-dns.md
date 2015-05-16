Title: 用 Google 免费 DNS 服务加快冲浪速度
Date: 2009-12-04 16:38
Author: toy
Category: News
Tags: DNS, Google
Slug: google-public-dns

{ 撰文/jazzi }

谷歌发布了 [Google Public DNS](http://code.google.com/speed/public-dns/)
服务，利用这个服务我们可以：

1. 加快 DNS 解析速度从而加快网页载入速度；  
2. 谷歌承诺不会给你重定向，避免一般 DNS
服务一打开敏感网页就给你重定向不知道哪里去；  
3. 更安全。

使用的方法是：

网络连接 → 本地连接 → 属性 → Internet 协议 (TCP/IP) → 属性 → DNS
服务器填入  
8.8.8.8 和 8.8.4.4。

**编注：**

以上方法仅适用于 Windows 平台，Linux 系统可将这组 IP 加入
/etc/resolv.conf 文件：


    nameserver 8.8.8.8
    nameserver 8.8.4.4

使用 NetworkManager
的同学，设置方法请参考[这里](http://paste.ubuntu.org.cn/i47496)。

{ Thanks jazzi. }
