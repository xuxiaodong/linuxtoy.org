Title: Flash Player 9 beta for Linux
Date: 2006-10-19 17:25
Author: toy
Category: Apps
Slug: flash_player_9_beta_for_linux

Linux 用户等了许久的 [Flash Player
9](http://labs.adobe.com/downloads/flashplayer9.html)，终于发布了 beta
版。这次发布的版本号为
9.0.21.55，包括独立的播放程序和插件两部分。值得注意的是，beta
版并没有完全实现所有的功能，如 Web 播放器中的全屏模式支持，完整的 SSL
支持等。不过，这些在最终发布时会包括进去。

如果你想要为 Firefox 浏览器提供 Flash Player 9
的支持，那么可按以下步骤执行：

![flash player](http://i.linuxtoy.org/i/flash_player.png)

` wget http://download.macromedia.com/pub/labs/flashplayer9_update/ FP9_plugin_beta_101806.tar.gz tar xvzf FP9_plugin_beta_101806.tar.gz mkdir ~/.mozilla/plugins cd flash-player-plugin-9.0.21.55/ cp libflashplayer.so ~/.mozilla/plugins/`

假如你先前曾打开过 Firefox 的话，那么就重新启动它吧。

另外，还包括一个 Flash Player 9 的独立播放程序，其安装过程如下：

` wget http://download.macromedia.com/pub/labs/flashplayer9_update/ FP9_standalone_beta_101806.tar.gz tar xvzf FP9_standalone_beta_101806.tar.gz cd flash-player-standalone-9.0.21.55/ chmod +x gflashplayer sudo cp gflashplayer /usr/bin/`

使用 gflashplayer 就可以启动 Flash Player 9 的独立播放程序了。

[![flash player
9](http://i.linuxtoy.org/i/flash_player_9_s.png)](http://i.linuxtoy.org/i/flash_player_9.png)

（非常感谢血色眼泪朋友提供消息）
