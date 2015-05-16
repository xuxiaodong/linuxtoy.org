Title: 使用 WiFi ESSID 更新 Pidgin 状态信息
Date: 2010-01-11 11:47
Author: toy
Category: Apps
Tags: Pidgin
Slug: essid-based-pidgin-status

{ 撰文/[lvyi](http://lvscar.info) }

不知道大家是怎么使用 IM
工具状态信息的，万年不变的签名档抑或当前播放歌曲名？

最近的习惯是把 IM
状态信息用来显示当前俺在哪，例如在家时显示"@home"，在公司时显示"@office"。虽说
Pidgin 更换状态信息很方便，但咱死 coder
的一个特征就是对这种简单重复的事不爽。周末得空研究了下 Pidgin
的状态切换机制，写个了小脚本在上线时根据当前无线网络的 ESSID
自动更换状态栏内容。

使用方法很简单，用文本编辑器打开，变更一下 Pidgin 状态信息和其匹配的
ESSID。  
把这脚本设置为可执行，放入桌面环境的启动自动运行列表里。登出，登入就 OK
了。

该脚本依赖 python-dbus，最近一两年的 Linux 系统基本都会默认安装吧。

下载：[essid\_based\_pidgin\_status.py](http://svn:svn@svn.lvscar.info/4fun/essid-based-pidgin-status/essid\_based\_pidgin\_status.py)

{
[Source](http://blog.lvscar.info/2010/1/11/essid\_based\_pidgin\_status/).
Thanks lvyi. }
