Title: Cycles Per Instruction (2014) 专辑内核模块版
Date: 2014-04-24 11:29
Author: toy
Category: Funny
Slug: netcat-cpi-kernel-module

最近发生在 Linux 内核社区的一件比较有意思的事情是，netcat  
乐队将 [Cycles Per Instruction (2014)][c] 专辑以[内核模块][n]  
的形式予以发布。这对于同时作为 Linux 和音乐爱好者的同学来  
说，不啻是一次特别的音乐视听体验。

要听到这张 Cycles Per Instruction (2014) 专辑，可按如下步  
骤操作：

**准备依赖**

以 Debian 为例：

# apt-get install build-essential vorbis-tools
linux-headers-$(uname -r)

**构建模块**

% git clone https://github.com/usrbinnc/netcat-cpi-kernel-module.git  
% cd netcat-cpi-kernel-module  
% make

我在编译时，遇到了如下错误：

netcat.c:20:18: fatal error: trk4.h: No such file or directory

在执行 `cp tracks/* .` 后，构建成功。

**安装模块**

# insmod netcat.ko

这将创建 `/dev/netcat`。

**播放专辑**

现在，使用 `ogg123` 就可以播放这张专辑了：

% ogg123 - < /dev/netcat

Audio Device: Advanced Linux Sound Architecture (ALSA) output

Playing: -  
Ogg Vorbis stream: 2 channel, 22050 Hz

[n]: https://github.com/usrbinnc/netcat-cpi-kernel-module  
[c]: http://netcat.bandcamp.com/
