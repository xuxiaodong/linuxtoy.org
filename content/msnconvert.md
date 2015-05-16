Title: msnconvert — 转换 MSN 的聊天记录到 Pidgin 格式
Date: 2007-11-02 10:06
Author: toy
Category: Apps
Slug: msnconvert

msnconvert 是一个可将 MSN 的聊天记录转换成 Pidgin
格式的小程序。该程序使用 C++ 编写，并以 GPL3 许可发布。msnconvert
需要依赖 libxml++2.6（Debian/Ubuntu 可通过 sudo aptitude install
libxml++2.6c2a 安装），目前最新版本为 0.1。

msnconvert 在 Ubuntu Gutsy
平台上开发，若你使用其他平台，需要自己重新编译，编译命令可以参考包里的
make 文件。

msnconvert 的使用方法如下：

1.  若你的 Pidgin 已经使用了 log reader（日志读取器）插件，则在
    blist.xml 就包含了对应了信息，可以直接使用 log reader
    的对应信息进行转换，但你需要告诉程序你的 MSN
    聊天记录存放位置，这个目录下应该是一系列的 XML 文件。
    `./msnconvert -u /path/to/msn/history/`
2.  转换一个具体的 XML 聊天记录文件。比如，已经有一个 XML
    文件，是和某个朋友产生聊天后的记录。

    `./msnconvert -f /path/to/user00234234.xml`

    注意：xml
    文件的名称必须保持原始名称，因为这里面包含了你朋友帐号的部分信息。

    而且此处有一个理论上的 BUG：若你的朋友里有几个非常相似的帐号，如
    love9@mail1、love91@mail2，这时系统就有可能判断错误。因为 MSN
    产生的聊天记录名称是 love9
    再加一串数字，而我现在还不知道这串数字的规律，因此就无法进行更明确的判断。

- [下载 msnconvert 0.1 source
code](http://wlx.westgis.ac.cn/uploads/2007/11/msnconvert-0.1-src.tar.gz)  
- [下载 msnconvert 0.1
可执行文件](http://wlx.westgis.ac.cn/uploads/2007/11/msnconvert-0.1-i386.tar.gz)

[作者/[LiangXu Wang](http://wlx.westgis.ac.cn/442/)]
