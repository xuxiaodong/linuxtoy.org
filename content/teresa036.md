Title: teresa 0.3.6
Date: 2016-02-28  
Modified: 2016-02-28
Category: Python
Tags: ipod, TTS
Slug: teresa
Authors: Chen Meng
Summary: 在 Linux 下同步你的 iPod Shuffle 并开启中文语音播报支持

Linux 下有很多工具可以同步 iPod, 但是多数都不支持播报播放列表名和音频标题。唯一支持 TTS 的 IPod-Shuffle-4g 也不支持中文。

ipodshuffle 是个 Python 项目，主要用于管理 iPod Shuffle 4。
其中的命令行工具 teresa 可用来设置最大音量与同步音乐, vocierss TTS 引擎 支持普通话和粤语。

## 安装

### Gentoo:
添加 两个 overlays: ikelos 和 observer，

然后安装 dev-python/ipodshuffle 

### 其他 Linux 发行版
最简单的方式是先安装 pip3， Debian/Ubuntu/Fedora 里的包名可能是 python3-pip，Archlinux 里可能是 python-pip

然后再通过 pip3 安装 ipodshuffle：
> pip3 install ipodshuffle

### 使用举例
第一次，先打开 VoiceOver 标志：
> teresa set -b /media/ipod_base -v true

再同步：
> teresa sync -b /media/ipod_base -s /media/ipod_src -l en-gb,zh-cn,ja-jp -e voicerss -k d279f919f7384d3bafa516caad0eae56

**sync** 是同步主命令；

**-b** ipod 的挂载路径;

**-s** 源目录，是有[**特定目录结构**](http://ipodshuffle.readthedocs.org/en/latest/tools/sync.html#source-folder-structure)的路径， 路径下面的所有文件夹和文件都可为软链接；

**-l** 指定所用到的语言代码(因为程序自动识别文本语言效果并不完美)，用逗号分割，没有空格。查看引擎支持的语言代码：
> teresa sync --help

**-e** 指定 TTS 引擎， 例子中的 voicerss 是一个 http TTS 引擎， 后面的一大串字符是使用这个 TTS 引擎而需要在此网站注册后获得的 API key，链接： [http://www.voicerss.org/](http://www.voicerss.org/)， 免费注册，每日 350 次免费 TTS 拉取请求。(这是能找到的唯一一个基本免费又好用的 TTS 网站)

teresa sync 会在 ~/.cache/teresa/ 里保存语音音频文件，下次使用到同样的文本和语言的语音文件就会直接从缓存中提供。

程序也会记录音乐文件的修改时间和大小， 所以如果源目录修改不大，下次同步会很快。

查看更多程序用法选项：

> teresa --help

> teresa sync --help

[在线文档](http://ipodshuffle.readthedocs.org/en/latest/)

[项目主页](https://github.com/meng89/ipodshuffle) 