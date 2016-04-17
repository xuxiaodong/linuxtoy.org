Title: CMMusic: 小巧而实用的 MPlayer 音乐播放前端
Date: 2011-03-11 08:16
Author: jiqingwu
Category: Apps
Tags: mplayer
Slug: cmmusic

CMMusic 是一个不错的 MPlayer 音乐播放前端，感兴趣的朋友不妨试试。

<!-- PELICAN_END_SUMMARY -->

+ Author: Jiqing (<jiqingwu@gmail.com>)
+ home: <http://hi.baidu.com/jiqing0925>
+ create: 2011-03-10
+ update: 2011-03-10

### 为啥用cmmusic

mplayer是元老级的媒体播放器，到现在依然强大，因为它的“全能”，一直拥有大量的用户。但我们主要用mplayer看电影，其实用mplayer播放音乐也很不错：占用资源很少，而且支持的格式非常多。

如果用xmms2或者mpd听音乐，如果想听wma什么的还要装额外的解码器。而只要装了mplayer，看电影和听音乐只用它就够了。无奈，mplayer没有个好用的前端。不过，现在，小巧的cmmusic来了，为mplayer提供了一个简单实用的音乐播放前端。

作者是咱中国人，可以从 [这个网页](http://bbs.ylmf.net/forum.php?mod=viewthread&tid=1141319&extra=) 看到更多的信息。大家有什么问题或建议可以用中文给他写信啊，方便交流。感谢作者，向作者致敬。

cmmusic是用ncurse库的终端下运行的程序。虽然界面不华丽，但功能全面，很实用，先看个截图吧。

[![](http://linuxtoy.org/img/2011/03/thumb-cmmusic.png)](http://linuxtoy.org/img/2011/03/cmmusic.png)

### 安装cmmusic

现在，cmmusic似乎还没加到各发行版的仓库中。可以从<https://sourceforge.net/projects/cmmusic/>下载源码编译安装。

因为依赖ncurses，所以编译前请安装ncurses的开发库。最好装libncursesw，支持宽字符，这样能支持中文显示。

```
sudo apt-get install libncursesw5-dev
```

应该差不多了，如果提示缺什么库，就安装libxxx-dev吧。然后使出程咬金的三板斧：:

```
./configure
make
sudo make install
```

安装的文件如下：

- cmmusic 核心程序，位于 /usr/local/bin
- cmmusicx 其实是一个脚本，自动打开一个终端运行cmmusic，位于 /usr/local/bin
- cmmusic.xpm 用于在菜单中显示的图标，位于/usr/local/share/pixmaps
- cmmusic.desktop 程序菜单中显示的项目，位于/usr/local/share/applications/

### 使用

- l 载入或存储播放列表lst文件，也用于指定添加音乐文件的目录
- + 添加音乐文件，会给出刚才用 l 指定的目录下的文件列表，空格选中，按回车添加到播放列表
- - 移除播放列表中的项目。
- ] 增加音量
- [ 减小音量
- , 上一首
- . 下一首
- p 播放/暂停
- s 停止
- m 静音
- q 退出
- d 切换播放模式。
    - SING 表示只播放一遍当前选中的文件
    - SILP 重复播放当前选中的文件
    - MULT 顺序播放一遍当前列表中的文件
    - MULP 重复按顺序播放列表中的文件
    - RAND 乱序播放列表中的文件
- r 设置歌词（只支持lrc文件）搜索目录。默认lrc为GBK，如果为UTF8，请使用选项``-lrc UTF-8``

另外，cmmusic同样可以用于播放电影，有播放列表，看电视剧很方便。最后，再次为国人的精彩作品喝彩！
