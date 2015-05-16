Title: CoreAVC 1.9 for Linux 安装指南
Date: 2009-03-03 13:51
Author: lovenemesis
Category: Featured
Tags: coreavc, mplayer
Slug: coreavc-19-for-linux-installation-guide

随着高清视频的逐渐流行，对于 H264 解码器的性能要求也越来越高。
由于缺乏厂商支持，FFmpeg 中的 ffh264 解码器由于解码效率不高，使得一些
CPU 配置较低的机子无法播放高清视频。如果你为此困扰，请参看[Linux 下使用
MPlayer
观看高清电影的三种解决方案](http://linuxtoy.org/archives/play-hd-movies-with-mplayer.html)
一文。本文将介绍如何将介绍其中的第三种： CoreAVC for Linux 。

如果您的显卡不支持 nVidia 显卡独有的 GPU 解码
VDPAU（或者由于各种错误无法使用，如本人），而且 FFmpeg-mt 的 git
慢如牛速（怨念……还是本人……），此时 CoreAVC for Linux
成为了唯一的选择。全文将以 CoreAVC for Linux 维基为基础， 以Fedora 10
i386 系统为例介绍如何在 Linux 下使用 CoreAVC 解码器（亦可用于 X86\_64
架构）。

**需求条件：**

1. CoreAVC 1.7 以上专业版及注册码

需要在 [CoreAVC](http://www.coreavc.com/) 购买，花费$15，可以拜托有
PayPal 的朋友代购……

2.Mplayer 的近期 SVN 版本，1.0rc2 不行。

推荐下载 MPlayer 每日更新的 [SVN
export](http://www.mplayerhq.hu/MPlayer/releases/mplayer-export-snapshot.tar.bz2)
版本，速度比 svn 快。

3.必要的工具和开发包

`su -c 'yum install subversion gcc make p7zip-plugins libXv-devel libX11-devel pulseaudio-libs-devel alsa-lib-devel ccache'`

最后的 ccache 不是必须，但强烈推荐！

假设与该过程有关的 CoreAVC 安装文件和 MPlayer
源代码包都放在一个目录下，比如用户主目录下的 Build 目录下：

`mkdir -pv $HOME/Build`

其他目录也可以，只要自己别找不到东西了～

1.在 Build 目录下使用 svn 获得最新的 CoreAVC for Linux ：

`cd $HOME/Build`

`svn checkout http://coreavc-for-linux.googlecode.com/svn/trunk/ coreavc-for-linux`

2.上一步完成后会在当前目录下生成一个名为 coreavc-for-linux
的目录，进入它：

`cd coreavc-for-linux`

3.安装 dshowserver。

i386 平台可以直接：

`make -C dshowserver`

如果没有提示错误的话就可以安装：

`su -c 'cp -v dshowserver/dshowserver /usr/local/bin'`

`su -c 'cp -v dshowserver/registercodec /usr/local/bin'`

X86\_64
平台的建议从[这里](http://code.google.com/p/coreavc-for-linux/downloads/list)下载已经编译好的，解压缩后同样使用上面的命令复制到
/usr/local/bin 下。

4.安装 CoreAVCDecoder.ax 解码器。  
返回 Build 目录，假设 CoreAVC 安装文件保存在此目录下：

`cd $HOME/Build`

使用 7z 解压 CoreAVC 安装文件

`7z x coreavc_professional_edition-setup.exe CoreAVCDecoder.ax`

无错误的话可以在当前目录下找到名为 CoreAVCDecoder.ax 的文件。  
现在 MPlayer 等播放器对于附件的二进制编码器的默认安装目录是
codecs，为了和官方维基尽量保持一致，在此创建由 codecs 指向 win32
的符号联结：

`su -c 'ln -vs /usr/lib/codecs /usr/lib/win32'`

复制 CoreAVCDecoder.ax 到此目录。

`su -c 'cp -v CoreAVCDecoder.ax /usr/lib/win32/'`

5.注册 CoreAVCDecoder.ax  
如果之前没有使用过 MPlayer
的话，需要创建用户配置文件目录，使用过的话可以跳过：

`mkdir -pv $HOME/.mplayer`

将保存 MPlayer 配置信息的 $HOME/.mplayer 目录关联为注册表：

`export REGISTRY=$HOME/.mplayer/registry32`

输入注册码，用你获得的注册码替代下面命令中的
55555-55555-CORE-55555-55555，注意双引号需要保留：

`registercodec -r $REGISTRY -k "HKLM\\Software\\CoreCodec\\CoreAVC Pro\\Serial" -v "55555-55555-CORE-55555-55555"`

6.用 dshowserver 测试是否注册成功：

`dshowserver -c CoreAVCDecoder.ax -s 1280x720 -g 09571a4b-f1fe-4c60-9760de6d310c7c31 -b 12 -f 0x34363248 -o 0x30323449`

得到的输出结果应该是：

`No id specified, assuming test mode`

`Opening device`

`len: 992`

`ProductVersion: 1.7.0`

`Decoder supports the following YUV formats: YUY2 UYVY YV12 I420`

`Decoder is capable of YUV output (flags 0x2b)`  
`Setting fmt`  
`Starting`

`Initialization is complete`

如果使用的是 1.9.0 版本的 CoreAVC 的话，输出结果应该是：

`No id specified, assuming test mode`

`Opening device`

`Called unk_IsDebuggerPresent`

`len: 992`

`ProductVersion: 1.9.0`

`Win32 LoadLibrary failed to load: nvcuvid.dll, /usr/lib/win32/nvcuvid.dll, /usr/local/lib/win32/nvcuvid.dll`

`Decoder supports the following YUV formats: YUY2 UYVY YV12 I420`

`Decoder is capable of YUV output (flags 0x2b)`

`Setting fmt`

`Starting`

`Initialization is complete`

此时你可以选择在[这里](http://neuron2.net/dgmpgdecnv/dgmpgdecnv100b.zip)下载它提示缺失的
nvcuvid.dll，然后复制到 /usr/lib/win32 目录下

`7z x dgmpgdecnv100b.zip nvcuvid.dll`

`su -c 'cp -v nvcuvid.dll /usr/lib/win32/'`

不过经个人测试这个 dll 文件没什么用处：它是 CoreAVC 1.9 在 Windows
平台下利用 CUDPA GPU 计算加快解码速度的接口，在 Linux
平台下不会起什么作用的……

7.编译并安装 MPlayer  
首先当然是解压缩源代码包：

`tar xf mplayer-export-snapshot.tar.bz2`

之后进入所在MPlayer 源代码目录：

`cd mplayer-export-*`

生成编译配置文件：

`./configure --language=zh_CN`

如果没有提示错误的话，就打上 CoreAVC for Linux 的补丁：

`patch -p0 < ../coreavc-for-linux/mplayer/dshowserver.patch`

如果没有提示错误的话，就可以开始编译了，首次编译大概需要15分钟左右，以后源代码包更新时有
ccache 帮助就会快很多：

`make`

如果没有提示错误的话，就可以安装了：

`su -c 'make install'`

8.配置解码器预置文件  
将默认配置文件复制到MPlayer用户配置文件目录下，**注意是
etc/codec.conf**（也就是当前MPlayer 源代码下的 etc 目录），而不是
/etc/codec.conf （这个是系统etc目录）：

`cp -v etc/codecs.conf $HOME/.mplayer/`

使用任意文本编辑器修改此文件，比如 gedit：

`gedit $HOME/.mplayer/codecs.conf`

之后将以下内容

`videocodec coreserve`

`info "CoreAVC DShow H264 decoder 1.3 for x86 - http://corecodec.org/"`

`status working`

`format 0x10000005`

`fourcc H264,h264 H264`

`fourcc X264,x264`

`fourcc avc1,AVC1 AVC1`

`fourcc davc,DAVC`

`fourcc VSSH`

`driver dshowserver`

`dll "CoreAVCDecoder.ax"`

`guid 0x09571a4b, 0xf1fe, 0x4c60, 0x97, 0x60, 0xde, 0x6d, 0x31, 0x0c, 0x7c, 0x31`

`out YV12,IYUV,I420,YUY2`

添加到

`;=============================================================================`

`;                   VIDEO CODECS`

`;=============================================================================`

之后，并且与下一个 videocodec 之间空一行。保存退出。

**至此， CoreAVC for Linux 应用于 MPlayer 的过程结束**

9.（可选）配置 SMPlayer  
（1）确定使用正确的 MPlayer 版本：

“选项“-”首选项“-“常规”，在“常规”选项卡的“选择 MPlayer
的可执行文件“中输入

`/usr/local/bin/mplayer`

（2）取消 Draw video using slices：

“选项“-”首选项“-“常规”，在“视频“选项卡中取消"Draw video using slices"。

（3）取消 CoreAVC 不支持的反拉丝，并让 CoreAVC 自己决定后期处理级别：

“选项“-”首选项“-“常规”，在“视频“选项卡中将反拉丝设为“无“，取消“为所有视频启用后期处理”。

（4）关闭会导致错误的 Correct PTS 选项：

“选项“-”首选项“-“高级”，在“高级“选项卡中取消“Correct PTS“。

点击“确定“保存退出。

当播放高清视频时点击“信息“后，若是显示在“视频“-”选择编码器“中显示”coreserve“，恭喜你，成功了！

**ffh264 与 CoreAVC 解码效率对比：**  
根据 MPlayer man 手册的建议，对手头的
[辐射3官方720P](http://prepareforthefuture.com/) 宣传片进行测试。

使用 ffh264 时:

`mplayer -benchmark -vo null -nosound -vc ffh264 fallout3_HD.mp4 `  
原始输出：  

`MPlayer SVN-r28764-snapshot-4.3.2 (C) 2000-2009 MPlayer Team 137 audio & 297 video codecs mplayer: could not connect to socket mplayer: No such file or directory Failed to open LIRC support. You will not be able to use your remote control. Playing fallout3_HD.mp4. libavformat file format detected. [lavf] Audio stream found, -aid 0 [lavf] Video stream found, -vid 1 VIDEO:  [avc1]  1280x720  24bpp  29.970 fps    0.0 kbps ( 0.0 kbyte/s) Clip info: name: Fallout 3 Official Trailer ========================================================================== Forced video codec: ffh264 Opening video decoder: [ffmpeg] FFmpeg's libavcodec codec family Selected video codec: [ffh264] vfm: ffmpeg (FFmpeg H.264) ========================================================================== Audio: no sound Starting playback... VDec: vo config request - 1280 x 720 (preferred colorspace: Planar YV12) VDec: using Planar YV12 as output csp (no 0) Movie-Aspect is undefined - no prescaling applied. VO: [null] 1280x720 => 1280x720 Planar YV12 V: 193.7   0/  0 41%  0%  0.0% 0 0 BENCHMARKs: VC:  80.627s VO:   0.023s A:   0.000s Sys:   1.091s =   81.741s BENCHMARK%: VC: 98.6373% VO:  0.0278% A:  0.0000% Sys:  1.3349% = 100.0000% Exiting... (End of file)`

使用 CoreAVC 时:

`mplayer -benchmark -vo null -nosound -vc coreserve fallout3_HD.mp4`  
原始输出：  

`MPlayer SVN-r28764-snapshot-4.3.2 (C) 2000-2009 MPlayer Team 137 audio & 297 video codecs mplayer: could not connect to socket mplayer: No such file or directory Failed to open LIRC support. You will not be able to use your remote control. Playing fallout3_HD.mp4. libavformat file format detected. [lavf] Audio stream found, -aid 0 [lavf] Video stream found, -vid 1 VIDEO:  [avc1]  1280x720  24bpp  29.970 fps    0.0 kbps ( 0.0 kbyte/s) Clip info: name: Fallout 3 Official Trailer ========================================================================== Forced video codec: coreserve Opening video decoder: [dshowserver] DirectShowServer video codecs Opening device Called unk_IsDebuggerPresent len: 992 ProductVersion: 1.9.0 Decoder supports the following YUV formats: YUY2 UYVY YV12 I420 Decoder is capable of YUV output (flags 0x2b) Setting fmt Starting Initialization is complete VDec: vo config request - 1280 x 720 (preferred colorspace: Packed YUY2) [PP] Using codec's postprocessing, max q = 4. VDec: using Planar YV12 as output csp (no 0) Movie-Aspect is undefined - no prescaling applied. VO: [null] 1280x720 => 1280x720 Planar YV12 Found DirectShow filterSelected video codec: [coreserve] vfm: dshowserver (CoreAVC DShow H264 decoder 1.3 for x86 - http://corecodec.org/) ========================================================================== Audio: no sound Starting playback... Dshowserver Connected to host pts value < previous ??% ??,?% 0 0 V: 193.6   0/  0 22%  0%  0.0% 0 0 BENCHMARKs: VC:  43.521s VO:   0.024s A:   0.000s Sys:   1.697s =   45.241s BENCHMARK%: VC: 96.1975% VO:  0.0525% A:  0.0000% Sys:  3.7499% = 100.0000% Destroying filter Exiting... (End of file)`

根据[此文](http://blog.openrays.org/blog.php?do=showone&tid=357)中对各项结果的说明，可以看出使用
CoreAVC 可以使用户空间上解码所用时间从 ffh264 的 80.627s 下降到
43.521s，**也就是说速度提升了46%**（(80.627-43.521)/80.627）！只是在内核空间上有小幅度的提升，从ffh264
的 1.091s 升高到1.697s。据此可见 CoreAVC 的解码效率还是相当惊人的。

**总结**  
个人使用了一些 720P
的片子测试，做为一款需要掏钱的解码器，画面效果相当出色，也没有跳帧的现象发生，但是
CPU 占有率并没有明显下降，是由于 CoreAVC 会在能保持流畅的时候使用剩余
CPU 资源去做画质后处理。在本人 Turion 64 X2 TL-58 /DDR2 800 2*2GB /
GeForce 8400M G 128M 的机子上 CPU 占有率在 40% 至 90% 间浮动。没有 1080P
的资源，不知道此时的 CPU 占有率如何。

如果你的 CPU 性能不错但是显卡不被 VDPAU 支持，并且无法忍受 ffmpeg-mt git
1b/s 的下载速度，那么 CoreAVC 的确是目前在 Linux
播放高清视频的最佳选择。

**附：如何在 Windows 平台上的 SMPlayer 中使用 CoreAVC**

1.到[这里](http://kovensky.project357.com/)下载带有 CoreAVC 支持的
MPlayer 可执行文件。

2.用上面下载的 mplayer.exe 覆盖掉 SMPlayer for Windows 安装时附带的
mplayer.exe。

3.将 CoreAVC 安装目录下的 CoreAVCDecoder.ax 文件复制到 SMlayer 目录下的
codec 目录中。

4.执行上文 SMPlayer 配置中(2)(3)(4)。

5.在 SMPlayer 的
“选项“-”首选项“-“高级”，在“MPlayer选项“选项卡中的“选项“处填入

`-vc coreavc,`

注意不要漏掉最后的逗号！
