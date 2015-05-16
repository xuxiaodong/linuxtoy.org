Title: 最小化安装 Ubuntu
Date: 2007-01-06 19:19
Author: toy
Category: Featured
Slug: minimalist-install-of-ubuntu

[Ubuntu](http://www.ubuntu.com/)
的默认安装方式或许并不为所有用户所接受。譬如说吧，有的用户并不想使用
GNOME
桌面环境，也有的用户并不需要预先安装的所有软件。为了解决上述诸如此类的问题，在安装最小化的
Ubuntu 的基础上，根据各人之喜好执行定制化安装，可能是较好的折中方案。

在安装之前需要确定的一件事情是，如何选择安装 CD。根据本文的要求，下载
Alternate install CD 是比较适合的。为了便于安装，应该将下载后的 ISO
文件烧录成光盘。

首先，安装 Ubuntu 基本系统。以 Ubuntu 6.10
为例，当插入安装盘后，计算机从光盘引导系统，这时在初始安装菜单中选择“Install
a command-line system”，之后与一般的安装过程并无二致。

在基本系统安装完成后，会要求重新启动一次系统，使用在安装过程中设置的帐号及密码登录。

现在，执行指令 `sudo vim /etc/apt/sources.list`，以便对 sources.list
文件进行编辑。在 VIM 打开文件后，将 `deb http://` 或 `deb-src http://`
前面包含的注释符号（#）删除。然后保存所作的修改。

为了完成后续的安装过程，需要继续执行指令 `sudo apt-get update`。

至此，最小化的 Ubuntu 安装已经就绪。

如果需要安装桌面环境，那么还可以执行以下的选择：

1.  安装 X 窗口系统：`sudo apt-get install x-window-system-core`。
2.  安装登录管理器：`sudo apt-get install xdm/gdm/kdm`[[注](#comment)]。最常见的图形化登录管理器包括
    XDM、GDM、KDM，用户可根据自己的需要选择其中之一。
3.  安装桌面环境或窗口管理器：`sudo apt-get install ubuntu-desktop/kubuntu-desktop/xubuntu-desktop`。这将分别安装
    GNOME、KDE、XFCE 桌面环境。对于 GNOME、KDE、XFCE
    这些桌面环境来说，为了获得更强的定制效果，也可仅安装最基本的组件，如：`sudo apt-get install gnome-core/kde-core/xfce4`。当然，如果不需要桌面环境，也可选择安装窗口管理器代替。那样的话，可以执行指令
    `sudo apt-get install fluxbox/icewm/enlightenment/fvwm`。
4.  安装软件：`sudo apt-get install firefox/gaim/xmms`。这将安装 Firefox
    浏览器、Gaim 聊天程序、XMMS
    音乐播放器。同样，不必拘泥于此处的示例，完全可以按自己的喜好来安装。

一旦完成上述过程的安装，重启系统，将会享受到一个完全自由的系统。

注释

类似 xdm/gdm/kdm 这样的写法需要读者选择其中一项才能无误地执行命令。
