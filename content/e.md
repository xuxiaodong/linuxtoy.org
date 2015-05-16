Title: e：可以解包多种存档格式的小工具
Date: 2007-07-11 17:17
Author: toy
Category: Apps
Slug: e

[e](http://martin.ankerl.com/2006/08/11/program-e-extract-any-archive/)
是一个使用 Ruby
语言写成的小工具，它可以对下列存档文件格式执行解包操作：zip、rar、7zip、gzip、bzip2、rpm、deb、cab、arj、ace、ppmd、lzo、tar.bz2、tar.gz、tlz、tar.lzma、ar、cpio、dar、uharc、zzip
等等，其支持的格式可谓非常广泛。

**安装 e**

由于 e 需要依赖 Ruby，所以你必须先行安装 Ruby（如果你没有安装的话）。以
Debian/Ubuntu 为例，你可以通过执行以下指令来安装 Ruby:

`sudo apt-get install ruby`

然后，你需要下载 e：

`wget http://martin.ankerl.com/files/e`

再给 e 加上可执行属性：

`chmod a+x e`

为方便使用，可将其移到 /usr/local/bin 目录：

`sudo mv e /usr/local/bin`

**使用 e**

比如，你要提取一个 zip 文件，可以执行：

`e file.zip`

你也可以同时提取多个存档文件：

`e a.tar.gz b.tar.bz2 c.cab d.deb e.rpm`

你甚至可以直接提取当前目录中的所有存档文件：

`e *`
