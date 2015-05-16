Title: 小熊猫 Ailurus 10.07.6 发布
Date: 2010-07-28 04:35
Author: Homer Xing
Category: Apps
Slug: ailurus-10076

小熊猫 Ailurus 是一个简单的软件安装工具和 GNOME 调节工具，支持 Ubuntu,
Mint, Fedora 和 Arch Linux。  
  
现在 10.07.6 版本发布了，带来了以下新的特性:

-   减少了安装软件时的内存消耗
-   如果设置了 http\_proxy 环境变量，那么就使用代理服务器
-   支持将软件条目保存到文件、以及从文件加载
-   “打印计算机信息” 对话框减少了缩进
-   可以禁用 GNOME 登录声音
-   建议执行 apt-get remove ubuntu-docs 包，以便释放 270M 磁盘
-   软件不能安装时，显示更加友好的信息
-   消除了 10.06 版本的恼人的不能安装软件的 bug
-   其它一些 bug 得到修正

新版本增加了一些优秀的开源软件, 见
[这里](http://github.com/homerxing/Ailurus/raw/master/ChangeLog)。

您可以这样安装:

`sudo add-apt-repository ppa:ailurus sudo apt-get update sudo apt-get install ailurus`

也可以从这下载代码和安装包:
<http://code.google.com/p/ailurus/downloads/list>
