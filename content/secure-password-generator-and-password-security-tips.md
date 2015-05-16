Title: Secure Password Generator 及密码安全小技巧
Date: 2012-09-05 17:39
Author: lovenemesis
Category: Firefox Extension
Tags: Firefox
Slug: secure-password-generator-and-password-security-tips

面对近年来频繁爆出的网站用户密码数据库被黑客袭击的问题，很有必要为在线网站使用独立健壮密码保护。这款
Firefox 扩展即可帮助您。

在过去的一两年里，众多知名站点如 Last.fm, Battle.net, Dropbox
被爆掉，黑客们前所未有的掌握了大量被散列化了的密码暗文（采用明文密码的
CSDN
之流不再赘述）。而由于现实中很多人会为了方便记忆多个站点共用一个密码，这些暗文可能包含的巨大潜在价值（银行账户、个人隐私、商业机密等）让更多的黑客蠢蠢欲动。

在今年的密码破解大赛上，一台装备了[8 块 AMD Radeon HD7970
GPU](http://cdn.arstechnica.net/wp-content/uploads/2012/08/project-erebus-v2-51.png)的机器可以**在
12 小时内暴力破解任意 8 位数的字母数字符号组合密码**，而它的造价仅为
$12000。此外云计算的发展更进一步降低了门槛， Amazon
云计算服务让更多的人有了廉价获得高性能计算能力的途径。

另一方面，得益于某些脑残网站的明文密码和不断增长的密码破解清单，**黑客们对于现实中人群的密码设定习惯有了更深入的了解**，比如常见的单词首字母大写、数字后缀等。此外在算法上的一些研究如彩虹表等，也大幅度缩短了从暗文到明文所需用时。

有朋友可能会觉得自己的[密码严格遵循安全建议](http://support.mozilla.org/en-US/kb/create-secure-passwords-keep-your-identity-safe)，相当复杂，应该不会有问题。但是由于现在社交网络的丰富，个人的兴趣爱好男女关系什么的太容易被全天下获知了，纵使单纯的暴力破解无法快速找出，别有用心的针对性黑客也可能会从社会工程的角度推测出受害者所用密码。

[Secure Password
Generator](https://addons.mozilla.org/en-US/firefox/addon/secure-password-generator/)
既是这样一款可以快速生成随机组合复杂密码的软件。

[![](http://linuxtoy.org/img/2012/09/secure-password-generator.png "secure-password-generator")](http://linuxtoy.org/img/2012/09/secure-password-generator.png)

它提供如下功能：

-   丰富的自定义选项，精确控制长度、字母、符号、数字等，并且可指定不需要的字符。
-   支持生成适用于左手输入、右手输入或者双手输入的密码。
-   和浏览器紧密结合，支持在密码框右键点击生成密码，或者插入上一次生成密码。

如果想知道生成密码的安全程度，可以使用这个[在线密码强度检测站点](http://howsecureismypassword.net/)进行测试，它会给出大约用一般桌面电脑破解你的密码所用时间。假使您微调这个小扩展无论如何也无法达到的密码健壮性需求，那么可以使用
[GRC 提供的超高强度在线密码生成器](https://www.grc.com/passwords.htm)。

之后与 [Firefox
内置的密码管理器](http://support.mozilla.org/en-US/kb/password-manager-remember-delete-change-passwords)配合，即可实现对多个网站分别采取独立的高健壮随机密码而又无需担忧记忆。

如果也使用 Firefox Sync 服务的话，那么也可以无缝的在 Firefox for Android
上使用。Firefox Sync
使用加密钥[本地和远端双重加密的手段](https://docs.services.mozilla.com/sync/overview.html)，保证存储密码库的安全，若配合主密码使用更加。

当然此外，还可以使用如 [LastPass](https://lastpass.com/)
之类的独立软件+浏览器插件的方式实现。不过它的**移动版本和智能手机上的浏览器整合性不好**，仅能在其内嵌浏览器中执行需要密码的操作。

**强力推荐阅读**：[Ars Technia
关于近期密码破解的专题报道](http://arstechnica.com/security/2012/08/passwords-under-assault/)
