Title: 使用 Wine 在 Linux 上运行 Google Chrome
Date: 2008-09-05 08:55
Author: toy
Category: Tips
Tags: Google Chrome, Wine
Slug: running-google-chrome-on-linux-with-wine

虽然 Google 表示 [Google Chrome
浏览器](http://linuxtoy.org/archives/google-chrome.html)会提供 Linux
平台的版本，但是仍然需要假以时日。如果你身边既没有 Windows
系统，又想要急着体验 Chrome，不妨考虑在 Linux 上通过 Wine 来运行它。

以下是在 Linux 上运行 Google Chrome 的步骤：

1.  安装 Wine，确保使用 [1.1.3
    最新版](http://linuxtoy.org/archives/wine-113.html)。
2.  下载并安装 winetricks：  

    ` wget http://www.kegel.com/wine/winetricks sudo cp winetricks /usr/sbin`
3.  安装依赖和 Flash 插件：  
    `winetricks riched20 riched30 flash`
4.  安装字体（可选）：  
    `winetricks allfonts`
5.  下载 Chrome 安装程序：  

    `wget http://gpdl.google.com/chrome/install/149.27/chrome_installer.exe`
6.  安装 Chrome：  
    `wine chrome_installer.exe`
7.  在安装完成后，先不要运行 Chrome，使用文本编辑器编辑 Google
    Chrome.desktop 文件：  

    `Exec=env WINEPREFIX="/home/mimir/.wine" wine "C:\\windows\\profiles\\mimir\\Local Settings\\Application Data\\Google\\Chrome\\Application\\chrome.exe"`

    将上面的内容改成：  

    `Exec=env WINEPREFIX="/home/mimir/.wine" wine "C:\\windows\\profiles\\mimir\\Local Settings\\Application Data\\Google\\Chrome\\Application\\chrome.exe" --new-http --in-process-plugins`

    注意，你需要将其中的 mimir 更换成你的用户名。

8.  回到桌面，点击 Google Chrome 运行程序。

截图：

[![Google Chrome on
Linux](http://i.linuxtoy.org/i/2008/09/chrome-on-linux-thumb.png)](http://i.linuxtoy.org/i/2008/09/chrome-on-linux.png)

[via [My Science Is
Better](http://www.myscienceisbetter.info/2008/09/install-google-chrome-on-linux-using-wine.html)]
