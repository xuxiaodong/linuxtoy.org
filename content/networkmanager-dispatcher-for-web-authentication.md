Title: 使用 NetworkManager 搞定网页验证
Date: 2011-09-19 13:06
Author: lovenemesis
Category: Tips
Tags: NetworkManager
Slug: networkmanager-dispatcher-for-web-authentication

学校基机房不知什么时候开始，上网要通过验证系统登陆。之前写了一个 bash
脚本执行登陆，但是每次开机后仍要手动运行，不方便。逛 Archlinux Wiki
的时候偶然看到了 NetworkManager 的 dispatcher
用法，就用此实现了自动登陆和登出。*感谢 Hexchain 来稿*

方法如下：

1. 创建 passport 脚本

使用 Firebug 或 Chrome Inspector 抓出登陆时的
postdata，写出脚本（对不同的网络，登陆服务器和 postdata
不同。此处以我的网络环境为例）：

    #!/bin/bash

    POSTLOGIN="username=hexchain&password=hexchain&password_enc=aGV4Y2hhaW4K&login=1&login_type=login&password_type=normal"
    POSTLOGOUT="logout=1"

    if [[ "$1" == "logout" ]]
    then
        wget -O- http://192.168.200.254:81/ --post-data=$POSTLOGOUT -T2 -t2
    else
        wget -O- http://192.168.200.254/ --post-data=$POSTLOGIN -T2 -t2
    fi

由于这个验证系统十分
buggy，登陆后连接登陆页面将收不到任何回应，因此指定了 `-T2` 和 `-t2`
参数。

将以上内容保存在 `/path/to/passport`

2. 创建 dispatcher:

    #!/bin/sh

    INTERFACE=$1
    STATUS=$2

    case "$STATUS" in
        up)
            /bin/bash /path/to/passport login
            ;;
        down)
            /bin/bash /path/to/passport logout
            ;;
    esac

将以上内容保存为 `/etc/NetworkManager/dispatcher.d/10_authenticate`
(不同发行版文件位置可能不同，此处以 Arch 为例) 并设立 +x 属性。

最后，确保 NetworkManager 网络配置正确且自动启动。

参考资料：[Arch
Wiki](https://wiki.archlinux.org/index.php/NetworkManager#Use_dispatcher_to_connect_to_a_vpn_after_a_network-connection_is_established)

**评论请前往[作者博客原文](https://hexchain.org/home/post/290)，以便统一回复。**
