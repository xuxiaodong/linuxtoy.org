Title: 让 Linux 更好用: Ailurus 10.04.2 发布
Date: 2010-04-25 09:08
Author: toy
Category: Apps
Tags: Ailurus, Fedora, Ubuntu
Slug: ailurus-10042

{ 撰文/[Homer](http://ailurus.cn) }

Ailurus 是让 Linux 更好用的程序。现在 10.04.2 版已经发布了。

[![ailurus-10042](http://i.linuxtoy.org/images/2010/04/thumb-ailurus-10042.png)](http://i.linuxtoy.org/images/2010/04/ailurus-10042.png)

主要改进是，可以单独启动特定功能。除了“安装软件”功能外，其它功能都能在一秒钟内启动。快捷方式在“应用程序”菜单->“系统工具”项->“Ailurus  
- 快速启动”项中。

其它的改进是:

系统信息方面:  
增加 OpenGL 版本号

系统设置方面:  
说明了一键更改字体大小的原理  
修正了“加速Firefox”的错误  
改变登录窗口图片  
取消清理操作时，不会出错

软件安装方面:  
优化了软件安装流程  
显示所装的软件的发行协议  
增加“硬件”, “语言支持”, “嵌入式系统”, “Nautilus  
右键菜单”分类  
增加 Acire，一个管理 Python 代码片段的工具  
增加 Eclipse VEditor，写 Verilog 的工具  
增加编辑视频的软件 PiTiVi  
增加 World of padman，一个3D射击游戏  
增加 Firefox Stylish 插件，可以改变网页外观  
增加 ImageMagicK，一个图片编辑程序  
增加 OSD-Lyrics，显示歌词的程序

系统清理方面:  
增加清空最近的文档，清空APT缓存，清理内核，清空Ailurus缓存功能

搜索最快的源方面:  
显示大约剩余多少秒

其它改进:  
修正了上一版中的 bug  
改进了“快速安装热门软件”，减少界面点选次数  
载入图标失败时不会异常退出  
修正了Fedora上，检查新版本的代码

Ailurus 可以在 Ubuntu 8.04~10.04, Fedora 11~13 上使用。

Ubuntu 用户这样安装

sudo add-apt-repository ppa:ailurus  
sudo apt-get update  
sudo apt-get install ailurus

Fedora 用户这样安装

su -c 'wget http://homerxing.fedorapeople.org/ailurus.repo -O
/etc/yum.repos.d/ailurus.repo'  
su -c 'yum makecache'  
su -c 'yum install ailurus'

项目主页

源代码在这

欢迎您的参与

{ Thanks Homer. }
