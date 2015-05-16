Title: 提醒：改变 Steam Library 位置有风险
Date: 2015-01-16 10:24
Author: lovenemesis
Category: Tips
Tags: steam
Slug: reminder-risk-when-changing-steam-library-location

友情提醒：在更改 Steam Library 的位置是请留心且注意备份。

昨日有用户反映似乎 Steam for Linux 的启动脚本有一些问题，若是您更改了
Steam Library 的位置的话，可能会进入 Steam `reset` 流程；而由于
`reset` 中的的环境变量处理问题，可能导致跟 Steam Library
位于同一文件树下的东西全部被删除。

比如：Steam Library 新移动到 `/run/media/user1/SteamDisk/steam
`，那么**整个 `/run` 下的东西被删除**。

该问题已经[汇报至 Steam for Linux 官方
Github](https://github.com/ValveSoftware/steam-for-linux/issues/3671)，正在进一步核实。  
由于潜在损失较大，所以先提前通知下诸位童鞋。

[消息来源](https://twitter.com/ivenvd/status/555897188350308352)
