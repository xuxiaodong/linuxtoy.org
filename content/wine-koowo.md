Title: wine + 酷我音乐盒
Date: 2008-09-14 17:46
Author: toy
Category: Tips
Tags: Koowo, Wine
Slug: wine-koowo

[撰文/nihui]

测试平台：Magic Linux 2.1-rc2(KDE 3.5.10)  
日期：2008/9/14 戊子中秋  
wine 1.1.4  
酷我音乐盒 v2.0.6  
已安装的 windows 软件：ies4linux，flashget，flac

**详细步骤：**

1.  下载 [winetricks](http://www.kegel.com/wine/winetricks)
2.  执行 winetricks wmp9，安装 Windows Media
    Player(安装需要两遍，安装时鼠标会失效，需要用键盘的 Enter 或
    Alt + * 操作，之后还会同时安装 wmp7 codecs)
3.  执行 winetricks
    allcodecs，安装编解码器(xvid，intelcodec，ffdshow)(注意，在安装
    ffdshow 的时候最好把解码器全部选上，并选“no limit”)
4.  从[酷我音乐盒网站](http://mbox.koowo.com/)上下载酷我音乐盒并安装(安装完成后不要立即启动)
5.  将 devenum.dll 和 quartz.dll 分别拷贝到 Windows Media Player 和
    KWMUSIC 安装目录中，并执行 regsvr32 jscript.dll
6.  运行 winecfg -> 增加程序设置 ->
    wmplayer.exe，在“函数库”选项卡中新增 devenum 和
    quartz，并选择“原装先于内建”
7.  运行 winecfg -> 增加程序设置 ->
    KwMusic.exe，在“函数库”选项卡中新增 devenum，quartz 和
    msvcr71，并选择“原装先于内建”
8.  双击桌面上的快捷方式即可运行酷我音乐盒啦

**能够正常使用的有：**

播放本地歌曲、播放网络资源歌曲(mp3/wma)、进度条和音量控制、播放模式控制、同步歌词显示/调整/保存、在线MV播放、网络资源库、搜索功能、今日推荐、皮肤、系统托盘支持(托盘菜单/最小化至托盘)、歌曲下载功能、播放列表控制、迷你模式(移动/拉伸等控制)、窗口置顶和移动

**不能够正常使用或不稳定的有：**

窗口最大化和拉伸、网络资源列表没有滚动条(但是键盘可以)、分割条不可伸缩、歌手图库、卡拉OK

**缺陷：**

退出后kwmv.exe不能自动退出，需要杀掉进程，否则下次启动可能启动不来

**未测试功能：**

会员积分功能

截图：

[![Koowo](http://i.linuxtoy.org/i/2008/09/koowo-thumb.jpg)](http://i.linuxtoy.org/i/2008/09/koowo.jpg)

[[原文链接](http://shuizhuyuanluo.blog.163.com/blog/static/778181200881452338557/)]
