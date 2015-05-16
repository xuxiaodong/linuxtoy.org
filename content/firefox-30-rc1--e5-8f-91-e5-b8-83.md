Title: Mozilla Firefox 3.0 RC1 发布(更新RC2)
Date: 2008-05-13 11:36
Author: lovenemesis
Category: Web Browser
Tags: Firefox
Slug: firefox-30-rc1-%e5%8f%91%e5%b8%83

Mozilla 基金会旗下著名的网络浏览器 Firefox
今天终于发布了最新3.0版本的候选版本RC1。继上月2日发布 Beta5 版本之后
Mozilla 终于有所行动了。

6月5日，发布第二个候选版本RC2。

6月5日，官方正式发布公告放出，见[这里](http://www.mozilla.com/en-US/firefox/3.0rc1/releasenotes/)。

官方32位Linux RC1关于信息：

Mozilla/5.0 (X11; U; Linux i686 (x86\_64); zh-CN; rv:1.9)
Gecko/2008051202 Firefox/3.0

与先前版本的差别：

-   首次运行时会要求MPL协议确认
-   主题变为Default 3.0
-   绝大部分扩展已经到位，如:Adblock Plus, Flagfox, PDF Download, Peral
    Page Saver,DownThemAll。
-   Acid3 Test：71/100，与 RC1
    相比没有提升。（估计Final版本也不会提升了……）

下载地址：  

[45种语言全平台二进制版本](http://www.mozilla.com/en-US/firefox/all-rc.html)[  
](ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/3.0rc1-candidates/build1/firefox-3.0.zh-CN.win32.installer.exe)

[源代码包](ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/3.0rc2-candidates/build2/firefox-3.0rc2-source.tar.bz2)

PS:上面的RC2源代码包编译后，关于如下：

Mozilla/5.0 (X11; U; Linux x86\_64; en-US; rv:1.9) Gecko/2008060500
Firefox/3.0

本人编译选项，仅够参考（强烈建议编译前安装ccache，节省时间好帮手）：

--prefix=/usr --enable-application=browser --enable-update-packaging --enable-optimize --disable-debug --disable-tests --enable-official-branding --enable-system-hunspell --enable-safe-browsing --with-system-jpeg --with-system-zlib --with-system-bz2
