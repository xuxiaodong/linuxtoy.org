Title: aMule 的安装及配置
Date: 2006-11-16 18:51
Author: toy
Category: Tutorials
Slug: amule_install_and_config

aMule 是一个类似于 eMule 的多平台 P2P 客户端程序。以下将简略叙述 aMule
在 Ubuntu 中的安装及配置 [High ID] 与 [KAD] 的过程。

-   安装：  
    ` sudo apt-get install amule sudo apt-get install amule-utils`
    如果需要将 aMule 与 Firefox 浏览器相关联，可以把
    `network.protocol-handler.app.ed2k` 的字符串设置为 `/usr/bin/ed2k`。
-   配置：

    下载服务器列表可用[这里的](http://i.linuxtoy.org/files/other/server.met)，KAD
    更新地址可用[这个](http://www.emule-inside.net/nodes.dat)及[另一个](http://renololo1.free.fr/e/nodes.dat)。

    ID
    最好设置为：[CHN][VeryCD]XXXX，比如：[CHN][VeryCD]benben。另外，路由器映射端口可设置为：4662,
    4672, 4665。

[撰文/[benben](http://hi.baidu.com/benben)]
