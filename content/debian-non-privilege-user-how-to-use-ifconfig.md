Title: 解决 Debian 非特权用户无法使用 ifconfig
Date: 2011-10-02 10:48
Author: shuge.lee
Category: Cli
Slug: debian-non-privilege-user-how-to-use-ifconfig

如何配置让 Debian 非特权用户也可以使用 ifconfig 。

ifconfig 在 /sbin 目录下，新建一个用户时， Debian 默认从 /etc/skel/
复制配置文件，

/sbin 并不在 $PATH 中，所以导致默认非特权用户无法使用 ifconfig
（terminal 会提示说找不到该命令）。

解决方法：

在 ~/.profile 修改 $PATH 环境变量，在末尾加上一行

```  
export PATH=$PATH:/sbin  
```

或者，修改 /etc/skel/.profile，这个会影响所有新创建的用户。

（完）
