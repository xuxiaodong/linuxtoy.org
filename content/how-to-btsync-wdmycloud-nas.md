Title: 玩转 BTSync 与 WD MyCloud
Date: 2016-04-26
Author: lovenemesis
Category: Tutorial
Tags: nas, raspberrypi, btsync, systemd
Slug: how-to-btsync-wdmycloud-nas
Summary: 如果你不堪忍受 NAS 厂商提供的官方客户端，可以尝试配合 Raspberry Pi 将其打造成 P2P 同步利器。

关注本站的读者可能还记得在下分享的 [WD My Cloud NAS](https://linuxtoy.org/archives/wd-mycloud-personal-nas-review.html)和 [BTSync 玩转技巧](https://linuxtoy.org/archives/tips-while-playing-btsync.html)，这篇文章算是将其结合起来，如何通过 Raspberry Pi 使用 BTSync 访问 WD My Cloud NAS。

需求不高，可是要解决的问题零零散散却有不少，在具体解决的过程中，发现网上现存文档有不少过时的地方，所以结合自己的实践加以总结，方便后来者有个参考。

下文使用 OSMC 2016.04.1 + Raspberry Pi 2 + BTSync 2.3.6 

### BTSync 通过 SMB/CIFS 协议访问 NAS ###

WD My Cloud 和其他大多数开箱即用的消费级别 NAS 一样，仅支持通过网口访问数据，哪怕其提供了 USB 接口。而 BTSync 对于 SMB/CIFS 的支持欠佳，尤其是在检测文件变化方面。BTSync 的支持论坛提到它同时运用了监听文件系统通知和主动扫描的方式监视文件夹变动，前者高效且省电，后者缓慢且消耗资源。对于 My Cloud 来言，其固件缺陷导致 NFS 访问速度不佳，SMB/CIFS 是唯一可行的访问方式，而通过 SMB/CIFS 挂载的远程目录是没有 `inotify` 的主动通知的，这样便导致了在 [BTSync 玩转技巧](https://linuxtoy.org/archives/tips-while-playing-btsync.html) 中提及的各类问题：文件损坏，索引停滞等等。经过大量阅读他人经验并结合自己实践，发现可以通过**只读访问**来规避这个问题。

对于使用 systemd 的 OSMC 来说，**忘掉 `fstab`** 吧！配置 SMB/CIFS 挂载最直观的方式莫过于使用 `mount` 文件了：在 `/etc/systemd/system` 目录下创建以挂载点目录结构为命名的一系列 `.mount` 文件。比如若想要其挂载到 `/mnt/Media` 目录下，那么这个文件的名字**必须**是 `mnt-Media.mount`。其具体内容和一般的 systemd 无差别不大，参考 [OpenELEC 的 Wiki](http://wiki.openelec.tv/index.php?title=Mounting_network_shares) 和 [systemd.mount Man 手册](https://www.freedesktop.org/software/systemd/man/systemd.mount.html)。

在这个例子中，在下增加了`iocharset=ut8`、`file_mode=0777` 和 `dir_mode=0777` 三个选项。第一个很直观不用解释，后两者是因为 BTSync 需要在共享的目录中创建 `.sync` 的索引纪录，所以需要**完整的读写执行权限**。注意这里 `DirectoryMode=` 这个控制一般挂载分区权限配置并不适用。

之后给新创建的 `.mount` 文件赋予可执行权限，使用 `sudo systemctl enable`连接至对应的启动级别，重启下即可看到生效。

接下来启动 BTSync，将新挂载的 SMB/CIFS 分区添加到同步目录即可，注意给其他设备分享时选择**Read-Only**。

### 利用 USB 优盘提供临时写入空间 ###

上述的方式可以避免 BTSync 在 SMB/CIFS 运行时可能的文件损坏风险，不过既然是云存储，不能上传总说不过去吧……考虑到 Raspberry Pi 2 的 USB 供电能力，使用了一个 [SanDisk 的 UltraFit 优盘作为临时文件存放点](https://www.amazon.cn/%E7%94%B5%E8%84%91-it-%E5%8A%9E%E5%85%AC/dp/B00YFI1EBC)，大小足以满足一般临时文件的存放。为了延长其寿命，将其格式化为闪存友好的[F2FS](https://en.wikipedia.org/wiki/F2FS) 文件系统。

之后将这个优盘所挂载的目录也添加到 BTSync 同步目录中，这一次可以选择**Read-Write**。

说过了是临时存放，意味其中的文件需要定期转移到 NAS 作为长期备份的，`rsync` 是最佳的选择了。对于使用 systemd 的 OSMC 来说，**忘掉`crond`** 吧！使用 `.timer` 文件，可以按照易懂且可控的方式指定需要定期执行的任务。简而言之需要两个配置文件实现，一个`.service`文件内容包含要做的内容，另外一个**文件名相同**的`.timer`文件指定运行时间和频率。

`.service` 文件的格式和内容可参考中其他的文件，在 `Exec=` 中写入 `rsync` 运行的命令和参数，只是不需要 `[Install]` 字段。而在 `.timer` 文件中，只需要在`[Timer]`字段指定 `OnCalendr=` 便可，这里可以方便的指定 `daily`、`weekly` 等易懂的时间点，具体可以参考[systemd.timer Man 手册](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)。

类似的，赋予可执行权限，使用 `sudo systemctl enable`连接至对应的启动级别，之后便可以通过 `sudo systemctl list-timers --all` 看到它们了。

### 按需挂载 SMB/CIFS 实现节能 ###

在等待 BTSync 索引和备份的过程中，突然想到了节能的问题。家用 NAS 并没有很大的吞吐，适时的进入节能模式不仅降低运行开销且可以延长寿命。WD 的这款 My Cloud 是由自动休眠功能的，但仅在没有设备访问的请求的状态下才会进入。这意味着需要按需挂载 SMB/CIFS。

对于使用 systemd 的 OSMC 来说，**忘掉 `autofs` 吧**！使用 `.automount` 文件，可以非常方便的为现有的 `.mount` 增加按需挂载功能。类似的，和挂载配置 `mnt-Media.mount` 对应的自动挂载文件**必须**是 `mnt-Media.automount`。其中在 `[Where]` 指定挂载点，然后在 `[TimeoutIdleSec]` 指定闲置时间，格式和 `.timer` 中的类似，比如 `10min` 意味着系统会在侦测到连续 10 分钟没有对这个挂载点的访问操作后将其卸载，并在下一次有访问请求时自动挂载。

同样的，赋予可执行权限，使用 `sudo systemctl enable`连接至对应的启动级别即可。

除了设置自动挂载外，还需要调整 BTSync 的*主动扫描时间间隔*。默认情况下 BTSync 会每 10 分钟扫描一下共享目录，这个频率对于两三个用户的家庭 NAS 显然是太高了，而且也使得硬盘无法进入休眠模式。根据 [Sync 官方的帮助文档](http://help.getsync.com/hc/en-us/articles/205449995-Sync-prevents-HDD-from-sleeping-on-NAS-)，将其扫描间隔调整为 5 小时。


### 最终的实现结果 ###

经过这么一番折腾：

1. 在 Android 客户端可以自由选择想要备份的文件夹，支持 Android 6.0 的外置 SD 卡
2. 安全且稳定的通过 AES-128 的通过广域网访问及备份
3. 有效降低了 BTSync 对于 NAS 的使用寿命的影响，保持了绿色节能
4. 使用 systemd 的配置系统，虽然文件个数多了些，但是可读性和结构性得到了显著提高

PS：对于 WD My Cloud Mirror Gen 2 以上更高端的多盘位产品是可以直接使用 [BTSync 为其打包的 Docker 应用](http://help.getsync.com/hc/en-us/articles/205504749)的，WD 也提供了[适用于 Raspberry Pi 的 1TB USB 口低功耗硬盘的套装 PiDrive](http://wdlabs.wd.com/products/wd-pidrive-1tb-kit/)。





