Title: 基于 AutoYaST 自动化安装 SuSE 实践
Date: 2015-05-28 22:09:37
Authors: wsgzao
Category: Tutorials
Tags: suse, autoyast
Slug: autoyast

本文主要介绍基于 AutoYaST 实现半自动化 SuSE 定制光盘和PXE网络全自动化安装 SuSE 的实践过程，希望对大家有用。

<!-- PELICAN_END_SUMMARY -->

### 前言

在金融行业中我所接触的操作系统主要是AIX和SLES(SuSE Linux Enterprise Server)，也许大家平时用得更多的是CentOS，虽然有部分差异但原理都是相通的，SMIT和YaST也是灰常实用的功能，推荐大家有机会尝试体验下。因为网上关于SuSE自动化部署的参考文章较少，这套自动化部署方案已经被验证并在生产系统使用了1年半，配置相对成熟和稳定。遵循Don't Repeat Yourself原则，本文主要介绍基于AutoYaST实现半自动化SuSE定制光盘和PXE网络全自动化安装SuSE的实践过程，如需了解更加详细的参数说明可以参考扩展阅读中的SuSE官网。

> AutoYaST是自动化部署SuSE的黄金搭档

### 更新历史

2015年05月28日 - 初稿 [阅读原文](http://wsgzao.github.io/post/autoyast/)

扩展阅读

- [SuSE](https://www.suse.com/zh-cn/)
- [AutoYaST](http://doc.opensuse.org/projects/autoyast/)

## SuSE自动安装光盘

### 定制版本

> SUSE Linux Enterprise Server 11 (x86_64)
> VERSION = 11
> PATCHLEVEL = 2

[下载地址](https://www.suse.com/zh-cn/download-linux/)

### AutoYast简介

AutoYast是SuSE Linux的自动安装工具。通过AutoYast，在DHCP、TFTP、PXE服务的支持下，通过FTP、NFS等网络安装源可以实现SuSE Linux的完全无人值守自动安装。但是，这种方式必须建立独立的服务器且客户端支持PXE网络启动，在现场没有网络或者系统不支持客户端网卡的场景下不适合，通过AutoYast制作的SuSE Linux一键安装光盘可以满足上述场景。本文主要介绍SuSE Linux Enterprise Server 11（简称SLES11）一键安装光盘的制作， 其他SuSE Linux仅供参考。

### 生成AutoYaST配置文件

AutoYast配置成功后，生成一个名为autoinst.xml的XML配置文件，SuSE Linux通过这个文件控制操作系统的安装。AutoYast生成配置文件有3种方式：

1. 系统安装时自动生成
2. 系统安装后通过运行命令生成
3. 直接编辑生成（偷懒最佳姿势）

> 系统安装时生成配置文件

按照正常步骤安装SLES11，把必须的软件全部安装。运行到最后一步“安装已完成”，勾选“为AutoYast复制此系统”，系统开始克隆系统生成配置文件，并弹出提示窗口。生成配置文件用时约2分钟左右，生成的配置文件位于/root目录下。

[![suse](/images/2015/05/thumb_qdkqiuvj20m80goad3.jpg)](/images/2015/05/qdkqiuvj20m80goad3.jpg)

> 运行命令生成或者修改配置文件

如果在系统安装时没有生成配置文件，可以运行命令生成。在系统中打开终端，以root用户运行命令`yast2 autoyast`，打开AutoYast配置窗口，选择“工具”->“创建参考配置文件”，弹出“创建参考控制文件”窗口。勾选需要配置的项目，如软件包选择、语言、分区、键盘布局、防火墙、网络设置等，AutoYast根据选择的项目从系统获取相关配置信息。选择“文件”->“保存”，弹出“另存为”窗口，输入文件名“autoinst.xml"，选择“保存”，系统提示文件保存到指定目录下。

[![suse](/images/2015/05/thumb_qdlady7j20mc0hd413.jpg)](/images/2015/05/qdlady7j20mc0hd413.jpg)

有时我们需要对模块做些调整，比如磁盘分区、软件包等。以调整磁盘分区为例介绍配置文件的修改。以root用户运行`yast2 autoyast`，打开AutoYast窗口，选择“文件”->“打开”，选择autoinst.xml文件，等系统读取配置后，在AutoYast窗口显示配置配件名称，修改后保存即可。

### 制作安装光盘

> AutoYast配置文件生成后，可以开始制作一键安装光盘了。制作一键安装光盘需要用到SLES11的原安装光盘的数据。

``` bash
#首先复制SLES11原安装光盘的数据到指定目录
mkdir /tmp/sles11
cp -R /media/S*/* /tmp/sles11
#复制autoinst.xml
cp /root/autoinst.xml /tmp/sles11
#编辑isolinux.cfg文件，找到# install所在位置
cd boot/x86_64/loader/

vi isolinux.cfg

# install
append initrd=initrd autoyast=file:///autoinst.xml splash=silent showopts 
:x!

#运行mkisofs命令生成自动安装光盘
cd /tmp/sles11

mkisofs -R -o /tmp/SLES11-SP2-64-AUTO.iso -b boot/x86_64/loader/isolinux.bin -c boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table .
```

### 我的配置文件

> 预设分区

名称|格式|大小
----|----|----
swap|swap|16G
boot|ext3|120M
|LVM|
root|ext3|5G
usr |ext3|10G
var |ext3|5G
opt |ext3|10G
home|ext3|15G
tmp |ext3|10G
总计||71G

> 预装软件包

``` bash
KDE Desktop Environment
Oracle Server Base
C/C++ Compiler and Tools
nmap
java-1_6_0
libstdc++43-devel-32bit
```

> 预设语言

``` bash
主要：英语
添加：中文
```

> 预设用户名/密码

``` bash
root/如果你直接复用我的配置文件请私信我获取密码
```

> 预设网络配置

``` bash
禁用服务：防火墙，IPv6
```

> autoinst.xml

[查看 autoinst.xml]({filename}/files/autoinst.xml)

## SuSE自动化PXE网络安装

### PXE基本原理

> 什么是PXE

PXE(Pre-boot Execution Environment)是由Intel设计的协议，它可以使计算机通过网络启动。协议分为client和server两端，PXE client在网卡的ROM中，当计算机引导时，BIOS把PXE client调入内存执行，并显示出命令菜单，经用户选择后，PXE client将放置在远端的操作系统通过网络下载到本地运行。
PXE协议的成功运行需要解决以下两个问题：

1. 既然是通过网络传输，那么计算机在启动时，它的IP地址由谁来配置；
2. 通过什么协议下载Linux内核和根文件系统。

对于第一个问题，可以通过DHCP Server解决，由DHCP server来给PXE client分配一个IP地址，DHCP Server是用来给DHCP Client动态分配IP地址的协议，不过由于这里是给PXE Client分配IP地址，所以在配置DHCP Server时，需要增加相应的PXE特有配置。

至于第二个问题，在PXE client所在的ROM中，已经存在了TFTP Client。PXE Client使用TFTP Client，通过TFTP协议到TFTP Server上下载所需的文件。

这样，PXE协议运行的条件就具备了，下面我们就来看看PXE协议的工作过程。

> 工作过程

在下图中，PXE client是需要安装Linux的计算机，TFTP Server和DHCP Server运行在另外一台Linux Server上。Bootstrap文件、配置文件、Linux内核以及Linux根文件系统都放置在Linux Server上TFTP服务器的根目录下。

PXE client在工作过程中，需要三个二进制文件：bootstrap、Linux 内核和Linux根文件系统。Bootstrap文件是可执行程序，它向用户提供简单的控制界面，并根据用户的选择，下载合适的Linux内核以及Linux根文件系统。

[![suse](/images/2015/05/thumb_qdlpssej20j50luq4o.jpg)](/images/2015/05/qdlpssej20j50luq4o.jpg)

> 方案介绍

这种方案需要首先设置一个启动服务器和一个安装服务器（可以配置在同一台物理机上），然后通过网络启动存放在启动服务器上的安装程序。安装程序会自动访问存放在安装服务器上的安装配置文件和安装介质来完成安装。

涉及到的技术

该方案主要应用了三种技术：

1. 在PC上从网络启动SLES安装程序的PXE协议
2. SLES安装程序提供的网络安装功能（即指通过网络访问安装介质）
3. SLES安装程序提供的无人值守安装功能（SuSE称为AutoYast）

软硬件需求

要按本文介绍的方法完成自动化安装，你需要如下软硬件资源：

- 一台PC机器作为启动和安装服务器（其它架构机器也可以）
- 一台待安装的PC机器，它的网卡必须带有PXE支持
- 一个建好的局域网，上述两台机器已经连接入同一子网
- 待安装的SLES安装介质

### 配置tftpd

> 为了简化步骤，我们在XP虚拟机下搭建DHCP和TFTP服务端，用tftpd工具来整合实现PXE网络引导，注意服务端与客户端要在同一局域网内。在Linux下配置服务的原理类似，具体方法可参考互联网。

(1)[下载tftpd](http://tftpd32.jounin.net/)

(2)启动tftpd32程序，选择【Settings】

[![suse](/images/2015/05/thumb_qdmb0dcj20b809imz6.jpg)](/images/2015/05/qdmb0dcj20b809imz6.jpg)

(3)按需勾选，这里我们仅选择【TFTP】和【DHCP】

[![suse](/images/2015/05/thumb_qdmsu8tj20a90eyab7.jpg)](/images/2015/05/qdmsu8tj20a90eyab7.jpg)

(4)TFTP设置如下

- Base Directory：对应存放Linux的引导文件
- PXE Compatibility：增强对不同型号网卡的网络启动支持
- Show Progress bar：在网络引导过程中显示进度
- Translate Unix file names：转化Unix文件名
- Allow "\" As virtual root：允许虚拟路径
- 其它高级选项：设置包括兼容性以及一些细节

[![suse](/images/2015/05/thumb_qdnb9j3j20aa0eytax.jpg)](/images/2015/05/qdnb9j3j20aa0eytax.jpg)

(5)DHCP配置

重点注意Boot File引导文件的设置和DHCP绑定地址

[![suse](/images/2015/05/thumb_qdntup0j20ac0ev762.jpg)](/images/2015/05/qdntup0j20ac0ev762.jpg)

(6)tftpboot目录结构

``` bash
file://D:\tftpboot (2 folders, 3 files, 35.86 MB, 36.46 MB in total.)
│ INITRD 32.20 MB
│ LINUX 3.64 MB
│ pxelinux.0 16.04 KB
├─pxelinux.cfg (0 folders, 1 files, 193 bytes, 193 bytes in total.)
│ default 193 bytes
└─tftpd32 (0 folders, 4 files, 620.33 KB, 620.33 KB in total.)
EUPL-EN.pdf 33.51 KB
tftpd32.chm 346.96 KB
tftpd32.exe 200.50 KB
tftpd32.ini 39.36 KB
```

- initrd和linux提取自linux启动引导镜像
- pxelinux.0是pxe启动引导镜像
- pxelinux.cfg文件夹下的default文件为启动菜单配置项
- 编辑`tftpboot\pxelinux.cfg`，可以自定义autoinst.xml文件的访问方式和路径

``` bash
default linux

# Install Linux
label linux
kernel linux
append initrd=initrd autoyast=ftp://198.15.0.106/suse/autoinst.xml install=ftp://198.15.0.106/suse splash=silent showopts
```

### 配置FTP

(1)下载[Filezilla Server](http://filezilla-project.org/)

(2)设置ftp 

允许匿名访问帐户即可，配置好ftp路径。提取SLES镜像内的安装目录至ftp目录下。

### 配置AutoYaST

> 使用SuSE中的AutoYaST工具生成autoinst.xml，复制到ftp任意目录下，注意文件路径与default配置相吻合

网络启动机器

前面的配置工作完成后，下面我们就在待安装机器上通过网络以无人值守的方式来安装

(1)启动待安装机器，选择从网卡启动。具体方法因BIOS版本不同而异。下图是从VMWare虚拟机上得到的选择网络启动的屏幕截图。

[![suse](/images/2015/05/thumb_qdo92xij209b05oaaa.jpg)](/images/2015/05/qdo92xij209b05oaaa.jpg)

(2)网卡中的PXE代码会联系DHCP服务器来获取IP地址以及启动镜像，然后启动镜像被载入并运行。

[![suse](/images/2015/05/thumb_rhjsgthj20k20b7wgw.jpg)](/images/2015/05/rhjsgthj20k20b7wgw.jpg)

(3)开始全自动安装

[![suse](/images/2015/05/thumb_rhlmbe2j20sg0lcdnj.jpg)](/images/2015/05/rhlmbe2j20sg0lcdnj.jpg)

### 安装后添加自定义模块

> 我这里以添加Kernel内核补丁为例

``` xml
<scripts>
<init-scripts config:type="list">
<script>
<filename>instkernel.sh</filename>
<debug config:type="boolean">true</debug>
<location></location>
<interpreter>shell</interpreter>
<source><![CDATA[
#!/bin/bash
#
# After installation, the logfile from this script can be found in
# /var/adm/autoinstall/logs
#
echo "========================================="
echo "... Starting AutoYAST included script ..."
echo "========================================="
rpm -ivh --root=/ ftp://144.131.254.206/update/3.0.74-0.6.8/kernel-default-base-3.0.74-0.6.8.1.x86_64.rpm 
rpm -ivh --root=/ ftp://144.131.254.206/update/3.0.74-0.6.8/kernel-default-3.0.74-0.6.8.1.x86_64.rpm 
rpm -ivh --root=/ ftp://144.131.254.206/update/3.0.74-0.6.8/kernel-source-3.0.74-0.6.8.1.x86_64.rpm 
rpm -ivh --root=/ ftp://144.131.254.206/update/3.0.74-0.6.8/kernel-default-devel-3.0.74-0.6.8.1.x86_64.rpm
]]>
</source>
</script>
</init-scripts>
</scripts> 
```

### 小结

[![suse](/images/2015/05/thumb_rhkbs4ej20dd081mxf.jpg)](/images/2015/05/rhkbs4ej20dd081mxf.jpg)

其实在研究自动化部署的过程中我们会遇到各种坑，只有踩过的人才能够体会其中的不容易，如果大家在测试和使用SuSE自动化安装时遇到任何问题，欢迎直接在原文下方留言，我们一起学习和成长^_^。
