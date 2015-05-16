Title: 解决 Exaile 音乐播放器中文乱码
Date: 2007-11-25 09:49
Author: toy
Category: Tips
Slug: exaile-chinese

[Exaile](http://linuxtoy.org/archives/exaile.html)
是一个很棒的音乐播放器，有方便的播放列表标签，自动分类、排序，音乐文件浏览和搜索。不过默认的
Exaile 没有考虑国内 GBK 标签的 MP3，我给写了个 [GBK
补丁](http://paste.ubuntu.org.cn/4150)，加了自动转码以支持国内的 MP3
中文。

[![Exaile](http://i.linuxtoy.org/i/2007/11/exaile-thumb.png)](http://i.linuxtoy.org/i/2007/11/exaile.png)

*Exaile 已正常识别 GBK 的 MP3 标签*

**应用补丁**

可以先 apt 或从 [www.getdeb.net](http://www.getdeb.net/) 安装 Exaile
音乐播放器，然后在终端里边执行：

`grep -q gb18030 /usr/share/exaile/xl/media/mp3.py || sudo sed -i '/unicode(id3/a\ \ \ \ try: text = id3[t].text[0].encode('iso-8859-1').decode('gb18030')\n\ \ \ \ except: pass' /usr/share/exaile/xl/media/mp3.py`

再重新导入音乐，就可以看到能自动识别 GBK 的 MP3 标签了。

[撰文/华华]
