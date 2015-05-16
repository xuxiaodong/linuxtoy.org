Title: Wayland 增加客户端淡出功能
Date: 2012-04-17 12:14
Author: lovenemesis
Category: Window Manager
Tags: wayland
Slug: wayland-add-client-fading-support

程序失去响应了？Wayland 让它退散掉～

Scott Moreau 提交了一组 Wayland
补丁，允许客户端调整表面渲染器的亮度和对比度，并且允许对客户端发送 Ping
指令。

由此带来的典型应用是当作为应用程序的客户端由于某种问题无法响应 Ping
指令时，达到设定阈值后将触发淡出事件，将该程序的窗口淡出，从而提示用户该程序运行不正常。当程序恢复响应后，可以取消淡出效果。

或许这是一个实用的 Eye Candy?

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTA4ODM)
