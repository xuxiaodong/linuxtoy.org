Title: 解决 Flash 视频无声问题
Date: 2006-07-27 21:13
Author: toy
Category: Tutorials
Slug: flash_no_sound

如果在 Firefox 中观看 Flash 视频没有声音，可以尝试通过以下办法解决：

1.安装 alsa-oss 包：

`sudo apt-get install alsa-oss`

2.编辑 firefoxrc 文件：

`sudo vim /etc/firefox/firefoxrc`

将其中的 `FIREFOX_DSP=""` 修改为 `FIREFOX_DSP="aoss"`。

3.Enjoy!
