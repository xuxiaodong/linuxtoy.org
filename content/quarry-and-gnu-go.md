Title: Quarry+GNU Go：和电脑下围棋
Date: 2007-02-02 10:42
Author: toy
Category: Games
Slug: quarry-and-gnu-go

对于围棋迷朋友来说，应该注意到 Linux 中的
[Quarry](http://home.gna.org/quarry/)+[GNU
Go](http://www.gnu.org/software/gnugo/)
这对组合，该组合不仅可以使你和电脑下围棋，而且也可以和人下围棋。其中，Quarry
主要是提供 GUI 支持，而 GNU Go 则允许你能够与电脑同台竞技。

[![Quarry](http://i.linuxtoy.org/i/2007/02/quarry_s.png)](http://i.linuxtoy.org/i/2007/02/quarry.png)

在 Ubuntu 中，你可以通过执行 `sudo apt-get install quarry gnugo`
指令来安装 Quarry 和 GNU Go。然后，你可以在终端中输入
`/usr/games/quarry` 运行游戏。

在开始玩游戏之前，你还需要进行设置：进入“首选项 -> GTP Engines ->
添加”，在“Command line:”输入“`/usr/games/gnugo --`mode gtp
`--`quiet”，点击确定即可。

(via [Ubuntu Chinese
Forums](http://forum.ubuntu.org.cn/viewtopic.php?t=37051), thanks!)
