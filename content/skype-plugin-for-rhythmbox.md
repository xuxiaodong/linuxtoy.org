Title: 听我的音乐：Rhythmbox 的 Skype 状态插件
Date: 2009-09-06 21:58
Author: lovenemesis
Category: Instant Messenger, Music Player
Tags: rhythmbox, Skype
Slug: skype-plugin-for-rhythmbox

Rhythmbox 做为 GNOME
系统默认的音乐播放器，具有不错的插件扩展功能。今天介绍的这款插件可以让
Rhythmbox 正在播放的歌曲信息显示在 Skype 的个人状态里。

以 Fedora 11 i686 为例：

**首先**，安装访问源代码树需要的 subversion：

`su -c 'yum install subversion'`

**之后**，在计划放置源代码的目录（比如
$HOME/Build）的终端中输入以下命令：

`svn checkout http://skype-plugin.googlecode.com/svn/trunk/ skype-plugin-read-only`

**然后**创建必要的 Rhythmbox 插件目录：

`su -c 'mkdir -v /usr/lib/rhythmbox/plugins/skype-plugin'`

**接着**拷贝相应文件到刚才创建的插件目录：

`su -c 'cp -v skype-plugin-read-only/src/* /usr/lib/rhythmbox/plugins/skype-plugin/'`

**最后**，启动 Rhythmbox 和 Skype，在 Rhythmbox 的“编辑”-“插件”里找到
Skype notifier ，打勾。

此时 Skype 会弹出如截图提示，询问是否允许 Rhythmbox 访问
Skype，在“记住该选择“前打勾，点击确定即可。

[![](http://i.linuxtoy.org/images/2009/09/screenshot-skype-api-authorisation-request.png)](http://i.linuxtoy.org/images/2009/09/screenshot-skype-api-authorisation-request.png)

大功告成，这些你的 Skype 好友就可以知道你正在听什么音乐了～
