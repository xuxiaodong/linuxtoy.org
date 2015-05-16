Title: 如何在教育网内上 Freenode 的 IRC 聊天室
Date: 2009-10-18 21:01
Author: JimHu
Category: Tips
Slug: freenode-cernet

由于某些原因，教育网内并没有办法连接到 Freenode 的 IRC 服务器。  

其实解决方案无非就是这么几个。一是，找一个 HTTP、VPN 或者 Socks
代理服务器即可。但是，免费的代理服务其是非常难找的，而且并不能保证稳定运行。

因此，我们可以用到教育网的另一个特性，即 IPv6 支持。Freenode 是提供 IPv6
支持的，而教育网在 IPv6 上并没有封闭 IRC
端口。所以，我们只需要找一个支持 IPv6 的 IRC 客户端，就可以了。这里推荐
Xchat。  
注意：Pidgin 的 IRC 插件不支持 IPv6。

在服务器里面填上 ipv6.chat.freenode.net，端口
6667。然后设置上昵称就可以不受束缚的上 IRC 聊天了，而且绝对稳定：）
