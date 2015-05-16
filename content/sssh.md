Title: sssh - 快速 ssh 登陆脚本
Date: 2008-07-11 12:23
Author: toy
Category: Apps
Tags: Scripts, SSH
Slug: sssh

此脚本对于那些需要经常 ssh
登陆远程服务器的朋友应该有点用处。尤其是需要中转服务器 ssh 2
次以上的。脚本功能包括：将服务器 IP 和密码保存于文本文件中
(明文保存，安全性要自己保证)，方便登陆，支持多次 ssh
中转，支持服务器编码自动转换，支持某个用户名的通用密码。

**使用方法：**

最好将脚本保存在 PATH 变量包含的路径下，建议保存于 ~/bin 并确保此目录在
PATH 中。

编写 ~/.pass 文件，并执行 `chmod 600 ~/.pass`

安装 expect 包。

.pass 文件的写法：

1.  最简单的，可以在文件中写下如下一行：

    `name=hostA usernameA@IP-A passwordA`

    就可以使用 sssh hostA 登陆此服务器了。

2.  中转登陆：  

    ` name=hostA usernameA@IP-A passwordA name-hostA=hostB usernameB@IP-B passwordB`
    执行 sssh hostA hostB 就相对于先登陆 hostA，然后在 hostA 上登陆
    hostB。同理，理论上可以中转 N
    次，hostA->hostB->hostC->hostD……，嘿嘿……
3.  使用通用用户名的密码：

    这是用于这样的例子：有 N 个服务器，都开通了一个通用用户名
    (例如：view 用户，只有很低的权限)，这些 view
    用户的密码都是同一个，而且会定期同步修改。这种情况下，如果修改了
    view 密码的话，.pass 文件就要修改 N
    个密码了，为了避免这样的麻烦，可以使用通用用户名和密码功能：  

    ` usualName view usualPSW password-of-view name=hostA view@IP-A name=hostB view@IP-B name=hostC view@IP-C`

    这样就可以直接用 sssh hostA，sssh hostB
    登陆了。可以看到，这里省略了第 3
    列的密码字段。此法同样适用于多级登陆的服务器。

4.  指定服务器使用的编码：  

    ` usualName view usualPSW password-of-view name=hostA usernameA@IP-A passwordA gbk name=hostB view@IP-B | gbk`
    在某行服务器的后面 (第 4 列)，加上 gbk，就可以指明该服务器使用的是
    gbk，登陆了以后不会出现乱码了。如果某行使用了通用用户名和密码的话，为了不致引起混乱，密码那列需要加个
    | (竖线) 占位。
5.  使用通用编码：

    `usualCODING gbk`

    加上此行，对于没有指定编码的服务器，将默认使用 gbk 编码。

下载：

由于脚本贴在这里会出现半角引号变全角的状况。所以，请直接在[这里下载](http://linuxfire.com.cn/~lily/sssh)。

[撰文/[bones7456](http://bones7456.blog.ubuntu.org.cn/2008/06/29/sssh/)]
