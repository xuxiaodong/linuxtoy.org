Title: Sabre: 懒人最爱的 Amarok 脚本
Date: 2008-03-08 19:39
Author: toy
Category: Apps
Slug: sabre

想想你出门前要做的事情：暂停 Amarok、设置 Konversation
为暂离、然后锁定机器；回家以后又要解锁、开始 Amarok、设置
Konversation，是不是觉得很麻烦？如果你也觉得这样很烦人的话，那么你一定会欣赏
Sabre 这个脚本。

Sabre 是一个简单的 Amarok
脚本，通过检测指定蓝牙设备是否在范围内来决定自己的动作。简单的说，如果指定的蓝牙设备出现在范围内，那么，Sabre
就会将电脑解锁、让 Amarok 开始播放、取消 Konversation
的暂离状态；相反，如果没有检测到指定的蓝牙设备，那么 Sabre
就会锁定电脑、停止歌曲播放、指定暂离状态。

只要将手机设定为需要监控的设备，那么出门和回家所需的操作就自动化了，也不会有忘记锁定机器之类的烦恼，实在是懒人福音。

你可以在
[kde-apps.org](http://www.kde-apps.org/content/show.php/Sabre:+Bluetooth+Proximity+Plugin?content=75746&PHPSESSID=8876f9a25aef5b239ef84526a4914e61)
找到这个脚本，下载以后解压缩，修改 install.sh
里面的安装路径，指定到自己的 Amarok 的 scripts 目录，Ubuntu
系统应该不用改，其他就看情况了。然后
./install.sh，会询问几个小问题，想要绑定的蓝牙设备的 mac
地址、在使用什么桌面环境、有没有设置
sudoer，按照自己的情况设定以后，编辑 /etc/sudoers，加入下面这行：user
ALL = NOPASSWD: /usr/bin/l2ping，因为这个脚本使用 l2ping
来检测蓝牙设备，而这个命令需要 sudo。

好了，这些都做完以后，重启 Amarok，脚本管理器中运行 sabre 和
sabre-backend.sh，打开手机蓝牙，就可以享受 sabre 带来的便利了！

[撰文/Matri Ning]
