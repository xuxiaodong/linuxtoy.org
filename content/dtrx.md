Title: dtrx: 懒人的存档提取之道
Date: 2013-01-05 11:22
Author: toy
Category: Apps
Slug: dtrx

提取存档最令人困惑的莫过于面对不同的存档格式，不仅得选择合用的存档提取程序，有时还得搭配各种不同的选项。有了
[dtrx][d] 的帮助，则可以使我们变得更懒一点，只要记住一个命令就够了。

dtrx 能够提取
tar、zip、cpio、deb、rpm、gem、7z、cab、lzh、rar、gz、bz2、lzma、xz
等多种存档格式，甚至还包括递归提取功能。

要使用 dtrx 提取存档，只要在其后跟存档文件名称即可，如：

dtrx file\_name.tar.gz

dtrx 的重要选项包括：

* -l：列出存档中的文件  
* -r：递归提取存档文件  
* -m：提取元数据（如 deb）  
* -o：覆写模式  
* -f：将所有文件提取到当前目录

dtrx 为 Python 程序，可从其[项目主页][d]获取。

[d]: http://brettcsmith.org/2007/dtrx/
