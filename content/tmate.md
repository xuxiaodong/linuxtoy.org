Title: tmate: 即时分享终端会话
Date: 2013-07-02 20:48
Author: toy
Category: Apps
Tags: tmate, tmux
Slug: tmate

[tmate][t] 为你提供即时的终端会话共享，使用起来特别容易，在此强烈推荐给需要结对的朋友。

<!-- PELICAN_END_SUMMARY -->

![tmate](http://lt-file.b0.upaiyun.com/files/2013/07/tmate.png)

tmate 构建在 [tmux][m]、libssh、以及 msgpack 的基础之上，它可以与 tmux 共存，同时会使用 tmux 的配置。

目前，tmate 针对 Ubuntu 提供有[安装源][u]、Arch Linux 用户可以通过 [AUR][a] 安装，其他 Linux 用户可通过以下命令从源代码编译安装：

```
% git clone https://github.com/nviennot/tmate.git  
% cd tmate  
% ./autogen.sh  
% ./configure  
% make  
# make install
```

注意在编译时需要 cmake、pkg-config、libtool、libevent-dev、libncurses-dev、libssl-dev、zlib1g-dev 等依赖。

假设 A 同学想把自己的终端会话分享给好友 B，那么他在启动 `tmate` 后，使用 `tmate show-messages` 可得到两个类似如下的 SSH 登录指令（其中一个为只读）：

```
ssh ro-@sf.tmate.io  
ssh @sf.tmate.io
```

现在，B 同学只要使用这些指令登录 SSH 便可进入 A 的终端。

[t]: http://tmate.io  
[m]: http://linuxtoy.org/tag/tmux  
[u]: http://tmate.io/#ubuntu  
[a]: https://aur.archlinux.org/packages/tmate/
