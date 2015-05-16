Title: Google Earth 4.3 beta 界面字体增大术
Date: 2008-04-19 08:55
Author: toy
Category: Tips
Tags: Google Earth, Tips
Slug: change-the-google-earth-ui-font-size

有朋友反映新的 [Google Earth 4.3
beta](http://linuxtoy.org/archives/google-earth-43-beta-released.html)
版默认的界面字体过小。读者 cnc
找到了一个实用技巧，可以根据自己的需要来增大 Google Earth
的界面字体显示。

其方法是使用文本编辑器打开 GoogleEarthPlus.conf
文件，该文件位于用户起始目录下的 .config/Google/
文件夹中。完整的路径为：

`vim /home/sf/.config/Google/GoogleEarthPlus.conf`

注意你需要将其中的 sf 更换成你的用户名。

接着，定位到 [Render] 段，并找到 GuiFontSize=
(如果没有，你可以添加这行)，然后将其更改为所需的字体大小即可。如下图显示
GuiFontSize=10 的效果。

[![Google
Earth](http://i.linuxtoy.org/i/2008/04/google-earth.png "Google Earth")](http://i.linuxtoy.org/i/2008/04/google-earth.png)

[感谢 cnc 朋友的提示]
