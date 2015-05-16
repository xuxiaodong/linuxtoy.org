Title: oVirt: 基于 KVM 的虚拟机软件
Date: 2008-06-21 10:10
Author: toy
Category: Virtual Machine
Tags: KVM, oVirt, VM
Slug: ovirt

Red Hat
在本周宣布了一个新的虚拟化~~平台~~管理软件──[oVirt](http://ovirt.org/)。oVirt
是基于 [KVM](http://kvm.qumranet.com)
项目的开源软件，该虚拟机软件支持主流的 x86 硬件，并允许用户在其上运行
Linux 及 M$ Windows 操作系统。

![oVirt](http://i.linuxtoy.org/i/2008/06/ovirt.png)

oVirt 提供基于 Web
的虚拟机管理控制平台，无论是一台主机上的几个虚拟机，还是管理数百台主机上的成千个虚拟机，它皆能胜任。

目前，oVirt 所发布的最新版本为 0.91-1
beta，可从这里[下载](http://ovirt.org/download.html)到适用于 i386 和
x86\_64 架构的安装文件。值得注意的是，运行 oVirt
除了要求硬件具有虚拟化支持外，还应事先安装好
kvm、libvirt、virt-manager、virt-viewer 等软件。
