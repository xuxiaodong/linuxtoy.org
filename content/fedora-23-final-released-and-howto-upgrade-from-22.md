Title: Fedora 23 正式发布及如何从 22 升级
Author: lovenemesis
Date: 2015-11-04
Category: Distros
Tags: fedora
Slug: fedora-23-final-released-and-howto-upgrade-from-22
Summary: 经过一周的延期 Fedora 23 正式发布啦！本次发布引入了新的升级机制，老版本用户可以更加有效的完成升级工作。

关于本次发布的改善，可以参考本站早先关于 [Beta 版](https://linuxtoy.org/archives/fedora-23-beta-released.html) 或 [Alpha 版](https://linuxtoy.org/archives/fedora-23-alpha.html) 的报道。

随着 Fedora 23 引入了更为健壮的跨版本升级机制，充分使用了 `dnf` 和 `systemd` 引入的特性。若您当下正在使用 Fedora 22，仅需三步即可升级到新版本：

1. 安装 dnf 插件：`sudo dnf install dnf-plugin-system-upgrade`。该插件将替换先前的 `fedup`。
2. 运行 system-upgrade 插件，下载升级软件包：`sudo dnf system-upgrade download --releasever=23`。注意仔细检查待下载列表中最下端那些由于不满足依赖关系而无法升级的软件包，若是它们不重要，可以继续等待升级过后再解决。
3. 带上述软件包全部下载完成且校验过后，重新启动开始执行升级：`sudo dnf system-upgrade reboot`

是不是很简单？具体所花的时间取决于您的网速和安装的软件包数量。

**关于 Fedora 的跨版本升级（hei）历史**

和其它发行版相比，Fedora 更加追求最新的开源技术，随着带来的一个负面影响既是跨版本升级的难度。比如最早期官方跨版本升级工具 `preupgrade` 采取类似软件包升级的热升级方式，时不时会由于新旧版本之间配置文件较大的差异导致升级后的系统行为诡异。

在引入固定化 `/usr` 的时候，不得不利用开发新的使用 `systemd` 的升级工具 `fedup`。`fedup` 将实际执行升级的过程交由 `systemd` 在重新启动后执行，大大提升了可靠性。
然而由于 `systemd` 也处于早期应用阶段，`fedup` 的 Hack 方式也导致了少量说升级后行为诡异的。同时基于 yum 实现的依赖关系分析过程相当的漫长。

本次 Fedora 23 引入的 system-upgrade 理论上讲更加健壮，一方面使用公开 API 以 dnf 插件形式存在，其依赖关系分析速度得到了极大的提升；另一方面转而使用 `systemd` 稳定的 API，行为的一致性得到了保证。

另一方面，Fedora 倒是一直有使用 `yum` 或 `dnf` 的非官方的跨版本升级途径，不过这种更是风险自担的咯。

