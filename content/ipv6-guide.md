Title: GNU/Linux 环境 IPv6 简明应用指南
Date: 2010-02-07 16:54
Author: toy
Category: Tutorials
Tags: IPv6
Slug: ipv6-guide

{ 撰文/聚焦深空 }

IPv6 是什么，与 IPv4 有什么不同？请参考[1]。  
深层问题请参考 IPv6 相关 RFC 文档，特别是参考[1]提及的 RFC  
文档。

**原生 IPv6 环境**

需要加载 ipv6 内核模块，或编译到内核。

方法一、静态 IPv6，手工配置 IPv6 地址和路由。

方法二、启用 IRDP 让系统自动配置，要求 IPv6 路由器支持  
IRDP。

方法三、启用 DHCP client 自动配置，要求 DHCP server 支持  
IPv6。

ISC dhcp-4.1+ 支持 IPv6。

**原生 IPv4 环境**

需要加载 ipv6、tun、sit 内核模块，或编译到内核。  
由于使用 IPv6 tunnel，性能较原生 IPv4 有微量下降。

方法一、手工配置 IPv6 tunnel。

方法二、启用 6to4 tunnel，要求有公网 IPv4 地址。

假设公网 IPv4 地址为 192.0.2.19。  
对应 6to4 地址为：

$ printf "2002:%02x%02x:%02x%02x::1\\n" `echo 192.0.2.19 | tr . ' '`
2002:c000:0213::1

配置命令如下：


    ip tunnel add tun6to4 mode sit remote any local 192.0.2.19
    ip link set dev tun6to4 mtu 1472 up
    ip -6 addr add 2002:c000:0213::1/16 dev tun6to4

    ip -6 route add ::/96 dev tun6to4 metric 1
    ip -6 route add 2000::/3 via ::192.88.99.1 dev tun6to4 metric 1

自动配置脚本可参考[2]。

方法三、启用 tunnel broker，要求有公网 IPv4 地址。

优点是可以长期拥有公网固定 IPv6 地址，缺点要注册。  
建议使用自动配置工具 aiccu，此工具也支持 NAT  
环境，及穿越防火墙。

方法四、启用 teredo tunnel，要求使用于 NAT 环境，对 NAT  
类型有限制。

特别适用于以 NAT  
方式访问网络的虚拟机，不适用于桥接方式。  
建议使用自动配置工具 miredo。

方法五、启用 isatap tunnel。

公网不常用，可参考[3]手动配置。

**DNS**

查询对应域名 IPv6 地址，需要查询 DNS AAAA record。  
查询对应域名 IPv4 地址，需要查询 DNS A record。  
DNS root server 早已全面启用 AAAA record，且可通过 IPv6  
地址访问；为减少 root server 压力，使用时请自觉架设 dns relay  
server。

当前 opendns，遇到无 A record 情况会返回 opendns 地址，不适宜  
IPv6 环境使用；google public dns 无此问题，推荐使用。

**iptables、ip6tables**

主机上，完全放行外出访问，并且接受返回的连接即可。  
限制外出访问的情况，请放行 "iptables -t filter -A OUTPUT -p ipv6  
-j ACCEPT"，请根据自己需要适当调整。

**IPSEC**

误解：IPv6 默认使用 IPSEC，不用担心安全问题。  
对 Linux 来说，加载 ipv6 内核模块时，会自动加载 ipsec  
内核模块，编译到内核时类似。  
IPSEC 要配置才有效，配置工具  
ipsec-tools，且暂无简单配置方法。  
IPSEC 可实现 host to host、host to router、router to router  
加密，且可选择加密 报头、报文、报头＋报文  
中任一方式。

**总结**

配置好 IPv6 环境，接着可以玩出许多花样。  
比如，可以在原生 IPv4 环境下，配置一个纯 IPv6  
子网，子网内仅使用 IPv6，并可正常访问互联网。  
比如，可以用 IPv6  
实现公司和家庭主机直接互联，即使主机均在 NAT  
后，不需借助 vpn 之类东东。  
比如，可以给主机添加 dns AAAA record，配置 IPv6  
就绪的服务器。

欢迎指正！

参考资料：

[1]  
  

  

[2]  
  
  
  
  

[3]

  

  

  

{ Thanks 聚焦深空. }
