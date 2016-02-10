Title: Talos安全工作站
Author: mytbk
Date: 2016-02-10
Category: Gadget
Tags: Server freesoftware
Slug: talos-secure-workstation
Summary: Talos安全工作站是Raptor Engineering开发的一款POWER8计算机，使用完全自由的固件，具有非常强大的性能。

几天前 [Phoronix](http://phoronix.com/vr.php?view=22801) 介绍了 Raptor Engineering 推出的 [Talos安全工作站(Talos Secure WorkStation)](https://raptorengineeringinc.com/TALOS/prerelease_info.php) 并进行了评测。

Raptor Engineering是个从事硬件和固件开发的公司，为[coreboot](https://www.coreboot.org/)社区贡献了好几个主板的coreboot移植。此前有几款移植了[libreboot](https://libreboot.org/)的主板和笔记本，它们能满足从系统固件到系统软件都自由的要求，但是都已经落后于时代。Talos安全工作站的性能不但强于现在支持libreboot的计算机，而且能和搭载Intel高端芯片的系统相比。

从Raptor Engineering给出的[specification](https://raptorengineeringinc.com/TALOS/prerelease_specs.php)看，这个工作站有一个8/10/12核心的POWER8处理器，TDP为190W(8核或10核的芯片有130W版本)，支持硬件虚拟化，向量计算加速和AES加速。它有8个DDR3 RDIMM内存槽，最大支持256G内存。在接口方面，有PCIe,PCI,SATA3,USB 3.0,HDMI,千兆网口等主流接口，还有RS232和GPIO接头。此外，它还使用开放工具链的FPGA.

根据Phoronix给出的跑分结果，在Debian GNU/Linux 8.3下，C-Ray,bzip2的成绩均不错。但由于软件对POWER8的优化还不够，OpenSSL的跑分比较糟糕。在软件还可以进一步优化的情况下，可以期待有更好的表现。

至于价格，搭载8核处理器的入门级主板大约为3100美金，相对性能接近的Intel平台还是比较贵。
