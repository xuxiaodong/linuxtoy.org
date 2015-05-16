Title: inxi: 获得完整的系统信息
Date: 2012-10-31 11:36
Author: toy
Category: Cli
Slug: inxi

虽然在 Linux
下我们可以通过各种命令来获取系统的相关信息，但若要一次性得到全部系统信息该法就显得较为麻烦了。从某种程度上说，[inxi][i]
这个 Bash 脚本则恰好满足了我们在这方面的需要。

要安装 inxi，只需执行下列命令即可：

% mkdir ~/bin  
% cd ~/bin  
% wget https://inxi.googlecode.com/svn/trunk/inxi  
% chmod +x inxi

在我的虚拟机（Debian）中执行 `./inxi -c0 -v7` 后，其输出结果如下，包括
CPU、图形、音频、网络、磁盘、分区等各方面的信息：

System: Host: debiantoy Kernel: 3.2.0-3-686-pae i686 (32 bit, gcc:
4.6.3)  
Desktop: N/A dm: (startx) Distro: Debian GNU/Linux wheezy/sid  
Machine: System: innotek product: VirtualBox version: 1.2  
Mobo: N/A model: N/A Bios: innotek version: VirtualBox date:
12/01/2006  
CPU: Single core Pentium CPU E5700 (-UP-) cache: 6144 KB flags: (nx sse
sse2 sse3 ssse3) bmips: 5753.32 clocked at 2876.661 MHz  
Graphics: Card: InnoTek Systemberatung VirtualBox Graphics Adapter
bus-ID: 00:02.0 chip-ID: 80ee:beef  
X.Org: 1.12.3 drivers: ati,vboxvideo (unloaded: fbdev,vesa) Resolution:
800x600@60.0hz  
GLX Renderer: Gallium 0.4 on llvmpipe (LLVM 0x209) GLX Version: 2.1
Mesa 8.0.4 Direct Rendering: Yes  
Audio: Card: Intel 82801AA AC'97 Audio Controller  
driver: snd\_intel8x0 ports: d100 d200 bus-ID: 00:05.0 chip-ID:
8086:2415  
Sound: Advanced Linux Sound Architecture ver: 1.0.24  
Network: Card: Intel 82540EM Gigabit Ethernet Controller  
driver: e1000 ver: 7.3.21-k8-NAPI port: d010 bus-ID: 00:03.0 chip-ID:
8086:100e  
IF: eth0 state: up speed: 1000 Mbps duplex: full mac:
08:00:27:b4:54:2d  
WAN IP: 119.255.59.90 IF: eth0 ip: 10.0.2.15 ip-v6:
fe80::a00:27ff:feb4:542d  
Drives: HDD Total Size: 21.5GB (16.4% used)  
1: id: /dev/sda model: VBOX\_HARDDISK size: 21.5GB serial:
VB0e8748e0-f06c0cac  
Optical: /dev/sr0 model: VBOX CD-ROM rev: 1.0 dev-links: cdrom,dvd  
Features: speed: 32x multisession: yes audio: yes dvd: yes rw: none
state: running  
Partition: ID: / size: 5.2G used: 2.4G (48%) fs: ext3 dev: /dev/dm-0  
label: N/A uuid: 9ef1b35c-68a0-43c9-8ed0-20f4c0325ecd  
ID: /boot size: 228M used: 19M (9%) fs: ext2 dev: /dev/sda1  
label: N/A uuid: 821abb0e-09c6-4b66-8ae2-a6aebdd51426  
ID: /home size: 14G used: 976M (8%) fs: ext3 dev: /dev/dm-2  
label: N/A uuid: 728fd07a-9f87-4b78-81c8-d904065b7577  
ID: /media/sf\_wind size: 200G used: 45G (23%) fs: vboxsf dev:
/dev/none label: N/A uuid: N/A  
ID: /home/xuxiaodong/share size: 200G used: 45G (23%) fs: vboxsf dev:
/dev/none label: N/A uuid: N/A  
ID: swap-1 size: 0.70GB used: 0.00GB (0%) fs: swap dev: /dev/dm-1  
label: N/A uuid: b9213b7a-1cf9-44d1-b6b1-2b4c8277caf7  
RAID: No RAID data available - /proc/mdstat is missing - is md\_mod
kernel module loaded?  
Unmounted: ID: /dev/sr0 size: 0.05G label: VBOXADDITIONS\_4.1.8\_75467
uuid: N/A  
ID: /dev/sda5 size: 21.22G label: N/A uuid: N/A  
Sensors: None detected - is lm-sensors installed and configured?  
Info: Processes: 106 Uptime: 1:12 Memory: 165.3/1010.0MB Runlevel: 2
Gcc sys: 4.7.1 alt: 4.4/4.6  
Client: Shell inxi: 1.8.20

[i]: https://code.google.com/p/inxi/
