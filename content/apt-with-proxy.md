Title: 让 Apt 使用代理
Date: 2007-01-08 10:17
Author: toy
Category: Tutorials
Slug: apt-with-proxy

在 Ubuntu 中使用 apt-get
时，为了获得访问或者较好的速度，我们可以通过使用代理来解决这个问题。apt-get
有一个配置文件 apt.conf，它位于 /etc/apt/
目录下，我们只需对它稍作更改即可。

执行的步骤为：

1.  打开终端，并输入
    `gksudo gedit /etc/apt/apt.conf`。这里，你也可以使用自己喜好的编辑器来代替
    gedit。另外，如果 apt.conf 文件不存在，你可以创建一个。
2.  添加下列内容：  
    ` Acquire {`

    http::proxy “http://user:pass@yourProxyAddress:port”

    }  
     

    你必需调整引号中的内容以适应自己的需要。如代理地址、帐号、密码、端口。另外，如果不需要帐号或密码，则可以省略不写。

3.  假如你只想临时让 Apt 使用代理的话，则可以这样做：  
    ` export http_proxy=”http://user:pass@youProxyAddress:port/”`

(via [OSSGeeks](http://www.ossgeeks.co.uk/?p=66),thanks!)
