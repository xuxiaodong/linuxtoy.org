Title: OpenPCTV 1.0
Date: 2014-08-28 09:08
Author: lovenemesis
Category: Distros
Tags: openpctv
Slug: openpctv-1-0

在经过15个月的开发周期后，OpenPCTV 终于迎来了第一个正式版本。*感谢作者
Henry Liu 来稿*

OpenPCTV 是基于开源项目 openbricks 的 Linux
交叉编译平台，她集电视、高清视频、IPTV
的采集、录播于一体，致力打造全方位的 HTPC
多媒体平台。同时具有基于多个不同的架构的版本，如 PC 平台有 i386 与
x86\_64，ARM 平台有基于 Freescale IMX6Q 的 TBS2910、Raspberry
Pi、基于全志 A20 的 cubietruck 等（此次发布的 1.0 Release
暂时只有基于i386的版本）。

其主要功能及特点有：

1. 支持 DVB-S2 卫星、DVB-C 有线、DVB-T2 地面波、ATSC
美国有线高清信号的采集与录播。  
2. 提供对全球多种语言的支持，目前 OpenPCTV 的用户遍及全球。  
3. 你可以任意选择 Enigma2、VDR、XBMC 三种不同的播放平台。  
4. 全面支持 AMD、Nvidia、Intel 三家显卡硬解码高清播放。  
5. 易于安装、配置及使用。你无需使用 Linux 命令行，以 dialog
对话框的方式完成大部分的配置。你可以简单地将系统安装到U盘即可正常使用（当然也可以使用
USB Live
或刻录光盘安装至硬盘）。如果安装至SSD硬盘使用将会获得更佳的体验。

目前通过测试的PC平台有（包括 Enigma2、VDR、XBMC
三个播放平台的硬解码高清播放能力）：

style='margin-left:2.75pt;border-collapse:collapse;border:none'>  

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>主板

lang=EN-US style='font-size:11.0pt'>Acer Aspire 4830TG
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>笔记本电脑

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>映泰
lang=EN-US style='font-size:11.0pt'>TA75MH2

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>映泰
lang=EN-US style='font-size:11.0pt'>TA75MH2

lang=EN-US style='font-size:11.0pt'>Gizmo 10.16cmx10.16cm
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>的迷你主板，
lang=EN-US style='font-size:11.0pt'>APU<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">功耗为</span><span
lang="EN-US&lt;br"></span> style='font-size:11.0pt'>6.4w

lang=EN-US style='font-size:11.0pt'>DB-FT3b-LC AMD
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>官方
lang=EN-US style='font-size:11.0pt'>2014<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">最新测试主板，同样为迷你</span><span
lang="EN-US&lt;br"></span> style='font-size:11.0pt'>10cmx10cm

lang=EN-US style='font-size:11.0pt'>CPU

lang=EN-US style='font-size:11.0pt'>Intel I7 2720QM

lang=EN-US style='font-size:11.0pt'>AMD A4 5300

lang=EN-US style='font-size:11.0pt'>AMD A4 5300

lang=EN-US style='font-size:11.0pt'>AMD G-Series G-T40E

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>单芯片
lang=EN-US style='font-size:11.0pt'>SoC 4<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">核</span><span
lang="EN-US" style="font-size:&lt;br /&gt;
  11.0pt">1.2G</span><span
style="font-size:11.0pt;font-family:&quot;Droid Sans Fallback&quot;">，</span>
lang=EN-US style='font-size:11.0pt'>TDP<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">功耗</span><span
lang="EN-US&lt;br"></span> style='font-size:11.0pt'>4.5w<span
style="font-size:11.0pt;font-family:&lt;br /&gt;
  &quot;Droid Sans Fallback&quot;">，工程测试版，型号未知</span>

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>显卡

lang=EN-US style='font-size:11.0pt'>Intel HD3000
style='font-size:11.0pt;font-family:"Droid Sans
Fallback"'>第二代核芯显卡

lang=EN-US style='font-size:11.0pt'>AMD Radeon HD7480D APU
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>集成显卡

lang=EN-US style='font-size:11.0pt'>Nvidia 520GT 1G DDR3
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>显存

lang=EN-US style='font-size:11.0pt'>AMD Radeon HD6250 APU
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>集成显卡

lang=EN-US style='font-size:11.0pt'>AMD Radeon R6 APU
style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>集成显卡

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>遥控设备

lang=EN-US style='font-size:11.0pt'>MCE

lang=EN-US style='font-size:11.0pt'>CIR(<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">主板自带）</span>

lang=EN-US style='font-size:11.0pt'>CIR(<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">主板自带）</span>

lang=EN-US style='font-size:11.0pt'>MCE

lang=EN-US style='font-size:11.0pt'>MCE

lang=EN-US style='font-size:11.0pt'>DVB<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">设备</span>

lang=EN-US style='font-size:11.0pt'>TBS6982,TBS5980,TBS5881,DVBSky  
S850,DVBSky S960

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>备注

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>正常
lang=EN-US style='font-size:11.0pt'>VAAPI<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">硬解码</span>

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>正常
lang=EN-US style='font-size:11.0pt'>VDPAU<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">硬解码（</span><span
lang="EN-US&lt;br"></span> style='font-size:11.0pt'>mesa r600<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">驱动）</span>

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>正常
lang=EN-US style='font-size:11.0pt'>VDPAU<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">硬解码（官方驱动）</span>

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>正常
lang=EN-US style='font-size:11.0pt'>VDPAU<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">硬解码（</span><span
lang="EN-US&lt;br"></span> style='font-size:11.0pt'>mesa r600<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">驱动）</span>

style='font-size:11.0pt;font-family:"Droid Sans Fallback"'>正常
lang=EN-US style='font-size:11.0pt'>VDPAU<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">硬解码（</span><span
lang="EN-US&lt;br"></span> style='font-size:11.0pt'>mesa radeonsi<span
style="font-size:11.0pt;&lt;br /&gt;
  font-family:&quot;Droid Sans Fallback&quot;">驱动）</span>

部分截图展示：

[caption width="1920"
align="alignnone"][![Enigma2PC](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screen_20140827233927.png)](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screen_20140827233927.png)
Enigma2PC[/caption]

[caption width="1920"
align="alignnone"][![XBMC](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screenshot001.png)](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screenshot001.png)
XBMC[/caption]

[caption width="1920"
align="alignnone"][![VDR](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screen_20140827234448.png)](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screen_20140827234448.png)
VDR[/caption]

[caption width="1920" align="alignnone"][![VDR with
EPG](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screen_20140827234245.png)](http://openpctv.sourceforge.net/wp-content/uploads/2014/07/screen_20140827234245.png)
VDR with EPG[/caption]

[下载](http://sourceforge.net/projects/openpctv/files/release/openpctv-1.0-release-i386.iso/download)

[主页](http://www.openpctv.com)

[SF主页](http://sourcefoge.net/projects/openpctv)

感谢 [TBS](http://www.tbsdtv.com) 提供测试设备
