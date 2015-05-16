Title: Fedora 12 下安装 Nvidia 官方驱动
Date: 2009-10-24 22:52
Author: lovenemesis
Category: Tutorials
Tags: Fedora, nouveau, NVIDIA
Slug: howto-install-nvidia-official-driver-under-fedora-12

Fedora 12 引入了 Nouveau 的 KMS
支持，系统启动在视觉上平滑很多，不再有闪屏或者黑白字符的出现。遗憾的是
Nouveau 目前不支持 3D 加速，想使用 Compiz 或者玩 3D 游戏的朋友只能求助于
Nvidia 的官方驱动。

目前 Fedora 12 尚处于 Beta 阶段， rpmfusion 里 rpm 格式的 nvidia
驱动尚未就绪，本文介绍以目前 Nvidia 最新的 190.42 驱动在 Fedora 12 Beta
32 位下的安装为例。该版本驱动经过修正，不需要打补丁即可在 Fedora 12 Beta
下使用。

***首次安装***

**1.**到
[nvnews](http://www.nvnews.net/vbulletin/showthread.php?t=122606) 上下载
190.42 版驱动。得到一个以 run 结尾的安装文件，赋予它可执行权限。

`chmod +x NVIDIA-Linux-x86-190.42-pkg0.run`

**2.**重新启动，由于显卡驱动的安装无法 X
服务运行时进行，所以需要进入运行级别 3 。在品牌 Logo 出现后按 ESC 键进入
GRUB 界面，在选择内核，按 e 键进行编辑，在 kernel 行未添加 `3`
这个参数。

比如我的 kernel 行就是从

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet`

修改成

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet 3`

完成后按 Enter 退出编辑模式，按 b 键引导。

**3.**在字符终端下登录，进入放置安装文件的目录，使用以下命令启动安装文件。

`su -c './NVIDIA-Linux-x86-190.42-pkg0.run'`

按照提示一步步进行。

**4.**编辑 /etc/modprobe.d/blacklist.conf 文件，以阻止 nouveau
模块的加载。

`su -c 'vi /etc/modprobe.d/blacklist.conf'`

在文件末尾添加

`blacklist nouveau`

保存退出。

**5.**编辑 /etc/grub.conf 文件，禁止 nouveau KMS 的使用。

`su -c 'vi /etc/grub.conf'`

将

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet`

修改成

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet nouveau.modeset=0`

保存退出。

**6.**如果看见 Nvidia 的 Logo 表明 Nvidia 运行正常。

至此 Nvidia 官方驱动安装完成。

***启用 Plymouth 图形化引导***

Nvidia 官方驱动本身是不支持 KMS 的，所以只能在引导时指定使用 MESA
的驱动来达到图形化 Plymouth 的效果。

**1.**在品牌 Logo 出现后按 ESC 键进入 GRUB 界面，在选择内核，按 e
键进行编辑，在 kernel 行未添加 `vga=ask` 这个参数。

比如我的 kernel 行就是从

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet nouveau.modeset=0`

修改成

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet nouveau.modeset=0 vga=ask`

完成后按 Enter 退出编辑模式，按 b 键引导。

**2.** 此时会屏幕上会提示按 ENTER 查看可选显示模式，敲击 ENTER 进入。

此时会显示一个表格，显示的是代码和分辨率色深的对应值，从中找到适合自己屏幕分辨率和色深的值。比如我的本本分辨率色深是
1280*800*32，在表上查到对应值是 361。此时输入 361，然后敲击
ENTER，就可以看到图形化的 Plymouth 引导界面了。

**3.**下来需要将这个值做为每次引导的参数。编辑 /etc/grub.conf 文件，添加
vga=?????，将
?????替换成刚才得到的值。注意刚才得到的值其实是个16进制数，要在前面添加
0x 才行，比如我的 361 此时就变成 0x361。

`su -c 'vi /etc/grub.conf'`

将

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet nouveau.modeset=0`

修改成

`kernel /vmlinuz-2.6.31.1-56.fc12.i686.PAE ro root=UUID=0a86cf1f-ea02-4016-9c15-c9c537489eaf  LANG=zh_CN.UTF-8 KEYBOARDTYPE=pc KEYTABLE=us rhgb quiet nouveau.modeset=0 vga=0x361`

这样，每次都会使用 0x361 对应的分辨率去启用 Plymouth 了。

***内核升级后编译内核模块***

使用官方驱动的一大缺陷就是每次更新内核时都要重新编译内核模块。简单的讲就是执行上文首次安装的第2和3步，只是在第3步时将运行驱动文件的方式有些差异。

`su -c './NVIDIA-Linux-x86-190.42-pkg0.run -K'`

在运行时添加 -K
参数代表只编译内核模块，而不再进行驱动程序文件的安装。执行完后，重新启动即可。
