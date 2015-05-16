Title: Pidgin 插件推荐：gSMS
Date: 2008-02-24 14:54
Author: toy
Category: Apps
Tags: Pidgin, Pidgin Plugins
Slug: gsms-plugin-for-pidgin

[gSMS](http://gsms.usajusaj.org/) 是一个
[Pidgin](http://linuxtoy.org/search/pidgin) 插件，当有人通过 Pidgin
联系你时，该插件将向你的移动电话发送 SMS
短消息，以达到通知你的目的。如果你不是每时每刻都挂在网上，如果你担心错过与朋友的重要交谈……那么，gSMS
就是你所需要的。

要使用 gSMS，你必须满足下列条件：

-   一个 Google 帐号
-   开启 Google Calendar 服务的 SMS 短消息提醒功能
-   使用 ntp 进行 PC 同步

gSMS 可用于 Linux 和 Windows 系统，支持 Pidgin 2.2.x 及 2.3.x 版。在
Linux 上，只需将 gsms.so 文件复制到 ~/.purple/plugins
目录即可完成安装。

接着，运行 Pidgin，在插件对话框中可以启用 gSMS，并对其进行配置：

![gSMS 配置](http://i.linuxtoy.org/i/2008/02/gsms.png)

-   Gmail account：你的 Gmail 邮箱地址
-   Password：该帐号的密码
-   Timeout：让 gSMS 等多久发送
-   Calendar feed path：设置 Google Calendar 的 feed 地址

[下载 gSMS](http://gsms.usajusaj.org/) (含源代码及已编译的二进制文件)
