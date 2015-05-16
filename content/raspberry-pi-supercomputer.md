Title: Raspberry Pi 超级计算机
Date: 2012-09-13 09:22
Author: lovenemesis
Category: Gadget
Tags: Raspberry Pi
Slug: raspberry-pi-supercomputer

南安普敦大学的计算机工程师们使用 64 个 Raspberry Pi
构建了一个廉价“超级计算机”。

[![](http://lt-file.b0.upaiyun.com/files/2012/09/engineersbui.jpg "engineersbui")](http://lt-file.b0.upaiyun.com/files/2012/09/engineersbui.jpg)

如上图所示，64 块 Raspberry Pi 采用如乐高积木一般的方式累加而成，使用
[MPI(Message Passing
Interface)](http://www.mcs.anl.gov/research/projects/mpi/)
标准通过高速以太网实现连通。

该“超级计算机”拥有 64 块处理器，具备 1TB 的内存（每块 Raspberry Pi
装备了一张 16GB SD 卡 PS 本人同样迷惑中），总造价在 2500
英镑以下，命名为 Iridis-Pi，取自该校的另外一台[超级计算机
Iridis（全欧洲最快的运行 Win Server
的计算机）](http://www.southampton.ac.uk/research/new_boundaries/supercomputer.shtml)。

Simon Cox 教授表示他们尝试了在该超级计算机上运行 Pi
测试，不过没有公布运算测试用时。本人对于 Raspberry Pi 所用的 ARMv6
指令集处理器的浮点运算能力并不持乐观态度，64 块加起来恐怕还不如一块 AMD
HD7970……

当然，该设备的主要目的是为了**启发学生们进行高性能计算方面的研究**，甚至在自家屋里也可以轻松构建！感兴趣的童鞋可以查看[详细构建指南和对应源代码](http://www.southampton.ac.uk/~sjc/raspberrypi/pi_supercomputer_southampton.htm)。

[图片及消息来源](http://phys.org/news/2012-09-raspberry-pi-supercomputer.html)
