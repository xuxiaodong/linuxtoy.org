Title: Ubuntu 蓝牙全攻略
Date: 2010-03-28 18:28
Author: ivan_wl
Category: Tutorials
Tags: Bluetooth, Ubuntu
Slug: ubuntu-bluetooth-guide

Ubuntu 的蓝牙支持相信很多同学都在使用吧，插上就用，连个手机传个文件啊什么的非常方便。但是你有没有想过压榨出其更大的潜能呢？有没有想过坐到电脑前，打开蓝牙连上手机，戴上耳麦，直接就通过电脑来接打电话了呢？或者连上你的 iPod touch，音乐声就从电脑的音箱中飘出了呢？当然，Windows 系统下有诸如 IVT 之类的商业驱动和配套软件可以实现，而在 Linux 下呢？当然也是可以的，而且都是自由免费的哦！

<!-- PELICAN_END_SUMMARY -->

下面就跟我来，压榨下 Ubuntu 的潜能吧！我使用的是 Ubuntu 9.10，其他的版本没有测试过，大家可以自己试试。另外先说明一点，Ubuntu 自带的 gnome-bluetooth 工具不是很好用，而且后面设置蓝牙立体声支持的时候用 gnome-bluetooth 会非常的不方便，所以建议大家安装使用 [Blueman](http://linuxtoy.org/archives/blueman.html) 这个管理工具。当然不要在新立德中直接安装 Blueman，直接装的话它不会替换 gnome-bluetooth，结果两个冲突起来会很悲剧的…建议添加 Blueman 的 PPA 源

<https://launchpad.net/~blueman/+archive/ppa>

然后安装 Blueman 就好了，它会自动替换掉 gnome-bluetooth。然后建议也更新一下与蓝牙有关的所有软件包，经我测试，更新后的兼容性和性能都会更好一些。当然，如果你不想使用 Blueman，也是完全可以的，就是麻烦一些。后面我会详细说明。

另外如果你是外置的 USB 蓝牙适配器的话，插在电脑上开机可能会出现蓝牙管理器无法管理的情况，解决的办法就是拔了再插一下，或者终端中运行

    sudo /etc/init.d/bluetooth restart

来重启蓝牙服务即可。

首先让我们来看如何把 Ubuntu 打造成一个蓝牙免提设备。这里就要请出我们的主角 - [HFP for Linux](http://nohands.sourceforge.net/) 了。

HFP for Linux 是一个在 Linux 下提供蓝牙 HFP（就是免提支持）的工具。看一眼主页中的图片大家就明白是怎么回事了。

[![HFP](http://i.linuxtoy.org/images/2010/03/thumb-hfconsole.png)](http://i.linuxtoy.org/images/2010/03/hfconsole.png)

下面我们就来编译安装。首先安装编译时需要的一些包

    sudo apt-get install subversion g++ autoconf libtool libspeexdsp-dev libasound2-dev libbluetooth-dev libaudiofile-dev libdbus-1-dev

然后用 svn 获得源代码

    svn co https://nohands.svn.sourceforge.net/svnroot/nohands/trunk

进入源代码的文件夹下，就可以开始编译安装了。

    ./autogen.sh  
    ./configure  
    make  
    sudo make install

编译安装完成。然后运行 hfconsole，一个拨号盘的界面就出现了。我们在里面配对好手机，等界面上的信号和电量指示出现，就成功了！

[![hfconsole](http://i.linuxtoy.org/images/2010/03/thumb-sendpix0.jpg)](http://i.linuxtoy.org/images/2010/03/sendpix0.jpg)

拨个电话试试？怎么，电脑的喇叭中没有声音？别急，点右下角的设置按钮，Audio device 选项卡，Driver 中换 OSS 试试。可以点下面的 Feedback test，如果能传出话筒的声音，那就正常了。如果 OSS 没有弹出什么错误提示，但是仍然没有声音怎么办啊？别急，首先到声音设定程序中去，确定你的话筒设置好了么？打开录音机程序，录一段试试看？也可能是话筒音量太小了，运行 alsamixer，把 mic boost 调大些。至于 alsamixer 可能无法保存音量设置，下次开机就没了，解决方法大家就自己 Google 下吧。不知道为什么，我这儿只有 OSS 能用。但是 OSS 是独占声卡的，所以，用的时候，把你的那些音乐播放器什么的都退了吧……或者你也可以尝试用 aoss 包裹一下，我就不多废话了。

如果一切正常的话，我们就可以把手机扔一边，用电脑来打电话了！如果你是强人，可以试试利用平板电脑啊上网本啊高级MP4啊什么的打造一个自己的车载蓝牙免提系统。折腾 Linux 真是其乐无穷啊～

~~~~~~~~~~~~~分割线~~~~~~~~~~~~~

接下来我们来开启 Ubuntu 中的 A2DP audio source stream 支持。就是把电脑打造成一个立体声蓝牙耳机。

这里有一个[详细的英文说明](http://jprvita.wordpress.com/2009/12/15/1-2-3-4-a2dp-stream/)，洋文好且翻墙能力高的同学可以直接去看看～

进入正题。首先要确定你的系统中有 pulseaudio-module-bluetooth 模块，没有的话自行 apt-get 新立得安装。然后加载模块

    pactl load-module module-bluetooth-discover

Ubuntu 9.10 中好像默认就有这个模块，而且是自动加载的，这部分就略过吧。

然后修改 /etc/bluetooth/audio.conf 文件，打开 audio source 支持。在

    # If we want to disable support for specific services  
    # Defaults to supporting all implemented services  
    #Disable=Control,Source

这几行字下，加入一行

    Enable=Source

保存，关闭。重启蓝牙服务，就是 `sudo /etc/init.d/bluetooth restart` 了。

然后，如果你使用的是 Blueman 的话，效果就立竿见影了。重新搜索、配对一下你的手机啊什么的，如果你的手机支持蓝牙立体声耳机的话，在你的设备列表上点右键，你就会看到 Connect to 下有 Audio source 的字样。点上去连接，用手机放首音乐，怎么样，电脑的喇叭响起来了吧～下面是连接到我的 iPod touch 上的效果。

[![ipod](http://i.linuxtoy.org/images/2010/03/thumb-ipod1.png)](http://i.linuxtoy.org/images/2010/03/ipod1.png)

[![ipod](http://i.linuxtoy.org/images/2010/03/thumb-ipod2.png)](http://i.linuxtoy.org/images/2010/03/ipod2.png)

但是如果你实在不想用 Blueman，执意要用 Ubuntu 默认的蓝牙管理器呢？好吧，也不是没有办法……首先你可能需要 d-feet 这个 d-bus 调试工具。apt-get 或新立得安装。

在蓝牙管理器中重新配对好你的设备，运行 d-feet，左侧栏中点 org.bluez，右侧找到和你的蓝牙设备 mac 地址对应的项目，展开 org.bluez.AudioSource / Methods 项，双击 Connect()，如图。

[![d-feet](http://i.linuxtoy.org/images/2010/03/thumb-d-feet.png)](http://i.linuxtoy.org/images/2010/03/d-feet.png)

接下来出现一个框，点 execute。你可能需要多试几次。然后打开声音设置，看硬件一栏，是不是有个 A2DP 设备出来了？

[![Sound](http://i.linuxtoy.org/images/2010/03/thumb-sound.png)](http://i.linuxtoy.org/images/2010/03/sound.png)

蓝牙 A2DP 流已经成功输入到 Pulseaudio 中了，接下来你可以把这个选作输入设备，然后录一段音看看…但是如何让声音直接从喇叭中播放出来呢？让你用 Blueman 来着，要不然会有这么麻烦么…

打开 pacmd，进入 pulseaudio 控制台。用命令 list-sources 找到你蓝牙设备对应的输入源，注意 mac 地址，记下名字。然后用 list-sinks 找出你需要的输出设备的名字。一般情况下只有一个，就是它了。然后用命令 `load-module module-loopback source= sink=` 将其连接，这回出声了吧！费这么大劲，还是赶快换 Blueman 吧，都自动帮你做好了！

另外说一点，蓝牙立体声的音质可能不像你想象的那么好，有点破音…可能是因为我用的是几十块的杂牌蓝牙适配器的原因吧。另外，我的电脑的蓝牙立体声和黑莓手机的兼容极差，完全无法使用，不知道为什么…

怎么样，一个小小的蓝牙，我们就压榨出了 Ubuntu 这么多的潜能。还有，如果你是强人的话，可以试试用平板电脑啊上网本啊高级 MP4 啊什么的打造一个自己的蓝牙车载娱乐系统。怎么样，折腾 Linux 是不是其乐无穷啊～

本文作者：ivan_wl ( twitter: [@ivan_wl](http://twitter.com/ivan_wl) ) 投递并授权 [linuxtoy.org](http://linuxtoy.org) 网站发表，欢迎转载，转载请保留作者信息。

{ Thanks ivan_wl. }
