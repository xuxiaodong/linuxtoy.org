Title: Exaile-cn 091231 发布
Date: 2010-01-01 13:28
Author: toy
Category: Apps
Tags: Exaile, Exaile-cn
Slug: exaile-cn-091231-released

{ 撰文/[billma](http://exaile-cn.googlecode.com/) }

Exaile-cn 是一个对 Exaile 进行扩展的项目，通过对 Exaile 进行扩展，使
Exaile  
功能上更加丰富，更加符合中国用户的使用习惯，给国内 Linuxer  
提供一个更加本土化的播放器。

**更新说明**

+ 修复了播放音乐时无法启用歌词插件的 bug  
+
修改了歌词文件分析方式，解决无法正确读取一行歌词有多个时间标签的歌词的
bug  
+ 修复了不能保存歌词修改的 bug  
+ 添加了歌词插件透明度、歌词目录、歌词颜色的选项

**下载地址**

**安装方法**

Exaile-cn 现在只支持 Exaile 0.3.0.2，如果你的 Exaile 不是  
0.3.0.2，可能会无法正常使用。

1. 解决乱码问题方法：将 id3.py 覆盖到 /usr/lib/exaile/xl/metadata 目录下
(需要 root 权限）

注：如果这样做仍不能解决乱码问题，请尝试把所有 Collection 删除，然后
Rescan Collection

2. 豆瓣封面插件安装方法：将 doubancovers
复制到～/.local/share/exaile/plugins/
(如果没有目录，先创建目录）下，然后启动 Exaile，选中插件选项即可  
3. 歌词同步显示插件安装方法：先把 engine\\\_unified.py 和
engine\\\_normal.py 覆盖到 /usr/lib/Exaile/xl/player（也有可能是
/usr/lib/Exaile，再将 LyricDisp 目录复制到
~/.local/share/exaile/plugins 下，然后启动 Exaile，选中插件选项即可

{ Thanks billma. }
