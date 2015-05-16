Title: KDE 下使用 Dropbox
Date: 2009-12-04 11:31
Author: toy
Category: Tips
Tags: Dropbox, KDE
Slug: using-dropbox-under-kde

{ 撰文/[Yandy Ding](http://open-idea.blogbus.com) }

Dropbox 是个非常优秀的文件网络同步工具，不需多加介绍。Dropbox
的默认包是与 GNOME 桌面整合的，这给喜欢 KDE 的朋友带来了麻烦。其实
Dropbox 官方给出了非 GNOME 用户使用 Dropbox 的方案，这里我特地为 KDE
(KDE 4) 的使用者介绍一下如何在 KDE 下使用 Dropbox。

我主要分两部分进行，第一部分介绍剥离 GNOME 的 Dropbox
的安装，第二部分介绍在  
KDE 中如何添加相关右键功能 (比如获取 public url 等)。

**第一部分：**

安装剥离 GNOME 的 Dropbox 其实很简单，说白了就是不要下默认的 Dropbox
包，而下个专门的。下载地址为：

* 32 位系统：  
* 64 位系统：

用 KGet 就行，当然如果喜欢用终端的也可用 wget 命令，例如 32 位的：

wget -O dropbox.tar.gz http://www.getdropbox.com/download?plat=lnx.x86

然后就是安装啦，安装就更简单了，就和 Windows  
的绿色软件一样，只要解压了就能运行 (程序名叫 dropboxd)。

所以只要解压后，把解压出来的文件夹找个合适的地方移过去，然后点 dropboxd
的文件（或是用终端运行）运行一下初始化向导就好了。

这里有个小注意点，解压出来的文件夹默认名是".dropbox-dist"，是个隐藏文件，所以很多朋友可能解压完了找不到解压到哪里了。

这样 Dropbox
就算安装完了，很简单吧？呵呵，当然很多人还是不能满足到此的，比如想进桌面就运行，而不是每次都要手动运行
dropboxd。只要在 KDE 的 Autostart 中建一个指向 dropboxd
的链接就行。具体方法是:

图形界面方法：控制中心 → (高级)标签 → Autostart，然后点击添加脚本（add  
scripts），选择你的 dropboxd，如下图所示：

[![Dropbox  

setting](http://i.linuxtoy.org/images/2009/12/dropbox\_kde-thumb.jpg)](http://i.linuxtoy.org/images/2009/12/dropbox\_kde.jpg)

到这里，Dropbox
就算安装配置完了，你的网络文件夹可以完全与网络同步更新了。下面的第二部分是添加右键功能的高级设置，如果你不需要可以完全不要。不过这一步同样是非常简单的，所以何不稍微“麻烦”一下呢？

**第二部分：**

这个原理其实很简单，就是用 Dropbox 的 CLI
工具，不过不要担心要去学习这个工具，因为在 KDE-Apps
中已经有人做好了现成的"GUI 壳"了:

下载这个包，解压，如果你的网络文件夹是 ~/Dropbox，就直接运行
install.sh  
就行了。如果不是，要用编辑器打开 install.sh 和 dropbox.desktop  
两个文件，把里面的 ~/Dropbox 替换成你的目录，然后再运行 install.sh。

这样第二部分就完成了，很简单吧？当然这只是基本的功能啦，CLI  

工具还是很强大的，如果感兴趣，可以研究下更多功能的使用，不过对于我来说这些基本的功能就够啦。

{ Thanks Yandy Ding. }
