Title: 如何查找 Linux 死机原因？
Date: 2011-10-28 16:13
Author: lovenemesis
Category: Tips
Tags: Crash, Panic
Slug: how-to-determine-the-freeze-under-linux

Linux
内核虽然号称“不死族”，几乎不会崩溃或者死机，但是特殊情况下，还是有一定几率会宕机的。*转载自
[deleak.com](https://www.deleak.com/blog/2011/10/28/y-it-crash/)*

因为 Linux 广泛用于生产环境，所以每一次宕机都会引起相当大的损失。它
Uptime 达到上百天也许你习以为常，但是只要 Down
十几秒，就会立即急的满头大汗。真的很难以想象证交所宕机会怎么样，也许全国股民会闹翻天。所以我们需要一些小技巧来查找死机的原因，从而避免死机或者内核崩溃。（话说
windows 天天蓝屏也没感觉呀 :-o 难道已经麻木了 :oops: ）

**请注意：以下方法可能不适用于 Server，因为桌面环境和 Server
还是有很大区别的。**

**X Crash**

事实上 Linux 内核很少出错，平常我们所遇到的“死机”都是 X
无响应造成的错觉。那 X 没响应了应该怎么处理呢？

通常套路是 `Ctrl + Alt +F7 (F8)` 切换到某个 tty，然后用 root 登陆，执行
`top` 查看吃资源最多的程序，然后使用 `pkill/kill/killall`
等命令杀死该程序。或使用组合键 `Ctrl + Alt + Backspace` 重启 X
（**黑日白月注**：这个快捷键组合在最新的 Ubuntu 和 Fedora 中关闭）。

如果偶遇切换 tty 失败或者没响应，可以试着使用 SSH
登陆此电脑，然后再杀死程序。也许只是 X 不响应，而内核和 SSH daemon
仍然工作，故此可以实施此法。

[arch 配置 SSH
daemon](https://wiki.archlinux.org/index.php/Secure_Shell#Daemon)

万一 X 不给力，各种方法试了无效，又没有办法通过 SSH 登陆到此
pc，那怎么办呢？别着急，我们还有万能的 “reisub”
大法。不过在启用前先要激活内核 sysrq 功能 (via)
。系统启动时执行：` echo "1" > /proc/sys/Kernel/sysrq ` 或者修改
`/etc/sysctl.conf ` 文件，设置 Kernel.sysrq = 1。系统异常时依次按下
Alt+sysrq+{reisub} ，然后系统会自动重启。（有关 sysrq 请看：[Linux
死机了怎么办？](http://linuxtoy.org/archives/what-to-do-if-Linux-crash.html)）

**不建议长按 Power
按键强制关机，有可能损坏硬件或者丢失数据，甚至导致磁盘坏道！**

**X
崩溃而内核完好**常见的症状有：程序无响应，花屏，鼠标移动指针无动作，键盘输入没有识别等。但后台的音乐可以正常播放，或者键盘
Caps Lock/Num Lock/Scroll Lock 按键按后对应 LED
可以正常亮灭。遇到此种情况可以使用上述方法重启 X 或者电脑即可恢复正常。

**Application Crash**

这个比较常见，但是也是相当难解决的。因为 Linux
上的应用软件大部分都是开源的，所以可能没有超高的稳定性。也许由于库的缺少或者版本错误，或者代码的
Bug，都有可能导致程序出现异常。

一般遇到这种问题，建议检查配置文件是否正确，对配置文件的错误修改可能导致程序的运行失败。如果您确信配置文件没有错误但是程序仍然异常，可以尝试把配置文件删除（注意备份！），然后再次打开软件尝试。通常程序的配置文件在：

-   `~/.[APPNAME]`
-   `~/.config/[APPNAME]`
-   `/etc/[APPNAME].conf`

或者有可能是库的错误，您可以在终端输入程序名或者程序路径运行程序，根据终端的提示信息除错。由于导致程序崩溃的可能性多种多样，在此不能一一列举，所以建议您根据出错信息去
google 搜索并找到解决方案。

**Kernel Panic**

X 的问题还好办，可是如果 RPWT 碰到 Kernel
Panic，那可真是上天无路入地无门，撞墙的心都有 :evil: 。

一般引起 Kernel Panic 的原因很多，但是都比较罕见。例如硬件问题 (irq
confilct, bad block, high temperature)，软件问题（错误的 mod，内核的
Bug），或者文件系统不支持（没有内建 ext4 支持却挂载 ext4 的 root
分区），硬件的变动（如添加/更换内存，不支持架构的cpu），错误的驱动。

Kernel Panic 的表现形式也是多种多样：启动失败，不正常的长时间 io
操作，键盘灯的不正常频闪，wireless 等指示灯错误闪烁，无响应（请区别 xorg
crash 情况），彻底锁死，黑屏，reisub 大法不灵 等等。

一般情况下，秉承 KISS 原则的 Linux
内核，会尽力解决一切错误并正常运行，如果遇到极端情况发生
Panic，它会尽可能把所有相关信息显示在屏幕上——至于多少，别奢求，Kernel
已经尽力了。

因为 Kernel Panic 是一种很极端的情况，有的人可能自从使用 Linux
就没有遇到过。所以我们要收集所有相关的信息来解决问题。发生错误后的各种输出是最直接的最有效的（
Dump 在 tty。请关闭 x）。因为 Kernel 已经崩溃，不一定能找到完整的
Log。您可以根据以下线索尝试：

1.  `/var/log/messages` —— rp
    爆发的时候，也许会记录下很多相关信息。按照时间戳查找。
2.  回溯操作 —— 回忆 Kernel Panic
    之前所做的所有事，并回滚。（如安装了某个程序，可以在
    /var/log/pacman.log 找到安装日志）
3.  Dump 信息 ——
    屏幕输出信息是系统最后的“遗言”，请使用数码相机或者笔纸记录。（tty
    only）

接下来就应该根据错误发生的可能原因进行排除。将内核启动参数化为最简形式，不应附加任何不必要参数，并
BIOS 中禁用掉所有无关硬件。相关日志文件：

-   `/var/log/boot`
-   `/var/log/xorg` 所有相关（仅参考）
-   `/var/log/messages`

如果可以，您应该记录下所有屏幕输出信息，并查看 `/var/log/messages `。

可能遇到的问题，和解决方法：

1.  irq conflict （还好我没碰到），可以尝试从 bios 修改硬件irq，或者升级
    bios，都不生效就换电脑或者禁用冲突硬件；
2.  bad balock，尝试修复坏道或者屏蔽坏道分区，建议更换磁盘；
3.  io
    error，同上，也有可能是没有内建文件系统支持的原因，重新编译内核或者找最新版的内核安装；
4.  mod，删除可能导致错误的内核模块（如 vboxdrv），涉及到的命令有：
    -   lsmod: 列出已载入的模块
    -   modprobe: 载入模块（**黑日白月注：**在这里和其他命令对应的为
        insmod + depmod 比较好，modprobe 更类似于 XXXmod
        系列命令的升级整合版本。）
    -   rmmod: 移除内核中模块，效果等同于 modprobe -r
    -   modinfo: 显示模块相关信息

5.  driver，a卡或者n卡驱动，也容易造成问题；
6.  硬件本身的问题导致，建议检测硬件可用性和兼容性（例如 memtest+）；
7.  内核 bug，如果您有能力，建议使用 KDB (Kernel debugger)
    排错，或者重新编译内核；
8.  不负责任的告诉您，最好的方法是换 windows :mrgreen:

**为了方便作者集中回复，请[前往原文](https://www.deleak.com/blog/2011/10/28/y-it-crash/)评论**

[消息来源](https://twitter.com/#!/ghosTM55/status/129730117118341120)
