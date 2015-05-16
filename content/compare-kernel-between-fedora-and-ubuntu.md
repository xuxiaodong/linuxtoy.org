Title: Fedora 与 Ubuntu 内核比较
Date: 2013-05-10 10:30
Author: lovenemesis
Category: Kernel
Tags: Fedora, Kernel, Ubuntu
Slug: compare-kernel-between-fedora-and-ubuntu

红帽的 Josh Boyer 充满好奇心的比较了 Fedora 18 和 Ubuntu 13.04 所搭载的
Kernel 3.8 在配置上的不同，发现了一些有趣的地方。

**注意：**下文为意译

[Josh Boyer](http://jwboyer.livejournal.com/) 分别选用当下 Fedora 18
中的 3.8.11-200.fc18 和 Ubuntu 13.04 中的 linux-image-3.8.0-19-generic
在 X86 64 位环境下进行比较，两者使用相同的上游内核。

**底层设置**

Ubuntu 将最大可使用内核数设定为 256 而 Fedora 仅为 128；同时 Ubuntu
启用了更多
[NUMA](https://en.wikipedia.org/wiki/Non-Uniform_Memory_Access)(非一致性内存访问)支持，并且设定了更高
NUMA 可支持数。考虑到 Canonical 打算统一 Ubuntu
桌面版和服务器版中的内核，Ubuntu 启用这些 SMP 相关的选项完全可以理解。

在计时器中断唤醒次数上 Fedora 设为 1000，而 Ubuntu 设为
250。通常来说较大的值意味着能提供更快的交互响应，更适用于桌面应用；较小的值则更便于服务器能更加专注的完成工作，而非响应中断。不过两者都启用了按需响应，CPU
在空闲时不会被无用的计时器唤醒打扰。未来估计两者都会逐步迁移到 3.10
内核引入的零计时器唤醒，更好的降低休眠时能耗。

同时 Ubuntu 也默认启用了快速无 HZ
选项，增加了内核进入空闲状态的机会，可以减少能耗。Fedora
曾在该选项刚刚引入上游时启用过，但是后续的诸多问题又使其被禁用了。经过几个内核的修订该功能相比当初稳定许多，值得重新考虑。

**默认选择**

Ubuntu 的默认 I/O 调度器为 deadline 而 Fedora 为 CFQ (Completely Fair
Queueing)。

默认 CPU 频率控制策略方面，Fedora 遵循常规的为按需调控，而 Ubuntu
则稍显异类为性能优先。

不过这两项都是可以在运行时调整的，这里所说的只是默认设置。

**Linux 安全模块**

Fedora 毫不惊讶的仅仅在内核中启用了对 SELinux 的支持。

Ubuntu 则更为“友好”的启用了所有安全模块的支持，而不仅仅是它默认支持的
AppArmor。尽管这不会带来任何安全性上的提升，不过这给予了系统管理员在默认安全模块之外更多的选择。

**模块签名**

Fedora 和 Ubuntu 都使用了模块签名，不过在具体应用上则有差异。

Fedora 使用了 SHA256 进行模块签名，因为这是 UEFI 通常使用的校验方式。

Ubuntu 则使用了模块版本，通过在载入模块时比较它的 CRC
与内核中的记录来判断模块是否安全。同时 Ubuntu
也启用了“来源版本”域，在一定程度上允许针对不同的内核版本编译模块并载入，如果明确知道其对应关系的话。

**遗留系统支持**

相比 Fedora，Ubuntu
启用了更多对异常少见或遗弃的设备、分区和网络的支持，比如 atari 和 sysv68
分区、DECNET 和 ARCNET 网络以及并行 IDE 接口(编者注：Linux 大概在 8
年前就使用 SATA 驱动实现 IDE 支持了)。不过 Fedora
也启用了一些遗留系统的支持，比如 OSS，而 Ubuntu 已经完全禁用它了。

此外 Ubuntu 内核也默认启用了更多的 SoC
支持，比如各种嵌入式领域才能见到的键盘、GPIOLIB、MFD 驱动等，以及 JFFS2
和 F2FS 文件系统等。这似乎和 Canonical
所说的合并桌面版和服务器版不符（编者注：或许也想涉足 X86
嵌入式？），不过这也意味着 Ubuntu 或许能在某些少见的 X86 SoC
设备上启动起来。

在开源显卡驱动支持方面，Fedora 仅启用了支持 KMS 的那些和少量 FB 驱动，而
Ubuntu 则默认启用了几乎全部。

最后 Ubuntu 默认启用不少处于 Staging 状态的内核驱动。Staging
保存那些由于质量问题而无法进入主线维护的开源驱动，启用它或许带来更广泛的硬件支持，但是其由于质量也对系统稳定性引入了隐患。

**总结**

两者内核在配置上并不存在能导致性能明显差异的部分，不过其中的部分细节值得双方重新审视。

[英文原文](http://jwboyer.livejournal.com/47022.html)

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTM2OTE)
