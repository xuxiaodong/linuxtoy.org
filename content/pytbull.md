Title: pytbull：入侵检测/预防系统测试框架
Date: 2016-05-09 17:02:50
Authors: toy
Category: Apps
Tags: ids, python, security
Slug: pytbull
Via: pytbull|http://pytbull.sourceforge.net/

或许当你安装了 IDS/IPS（入侵检测/预防系统）之后就感觉系统安全无忧了，但如何确信？答案是测试。pytbull 是使用 Python 开发而成的 IDS/IPS 测试框架，利用它你可以完成超过 300 多项安全测试，其范围涵盖非常全面。

<!-- PELICAN_END_SUMMARY -->

![pytbull]({filename}/images/pytbull.jpeg)

pytbull 包含 11 个测试模块，它们是：

1. badTraffic：测试如何处理低质流量
2. bruteForce：测试暴力攻击
3. clientSideAttacks：测试客户端攻击
4. denialOfService：测试 DoS 攻击
5. evasionTechniques：测试各种闪避技术
6. fragmentedPackets：测试各种碎片攻击
7. ipReputation：测试服务器的 IP 信誉
8. normalUsage：测试一般用法
9. pcapReplay：启用 pcap 文件重放
10. shellCodes：测试 shell code
11. testRules：基本规则测试
