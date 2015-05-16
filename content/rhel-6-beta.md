Title: RHEL 6 Beta 放出
Date: 2010-04-23 08:39
Author: toy
Category: Distros
Tags: Red Hat, RHEL
Slug: rhel-6-beta

Red Hat 于昨日放出了 RHEL（Red Hat Enterprise Linux） 6 的首个 Beta  
测试版本。RHEL 6 作为下一代的 Red Hat Enterprise Linux  
平台，主要包括以下新特性和改进：

+ 电源管理：支持 tickless kernel，并通过 Powertop、Power  
Managemnet（ASPM、ALPM）、Tuned 等应用栈来减少电源损耗  
+ 下一代的网络：全面支持 IPv6，FCoE，iSCSI，以及改进了 mac 802.11
无线栈  
+ RAS（Reliability, availability, and serviceability）：对硬件的 RAS
能力及  
NUMA 架构进行了增强  
+ Fine-grained 控制及管理：改进了调度器，通过内核中的 Completely Fair  
Scheduler (CFS) 及 Control Groups (CG) 来更好的管理资源  
+ 可扩展的文件系统：提供 ext4 及 XFS 文件系统支持  
+ 虚拟化：改进了 KVM 的性能，并添加了新的功能  
+ 企业级安全增强：改进了 SELinux 的易用性、应用沙盒等  
+ 开发及运行库支持：SystemTap 得到改善，加入了新的 ABRT 框架，包含 GCC  
4.4.3、glibc 2.11.1、GDB 7.0.1 等

参阅 [RHEL 6 Beta  

发布公告](http://www.redhat.com/rhel/beta/)及[发行注记](http://www.redhat.com/docs/en-US/Red\_Hat\_Enterprise\_Linux/6-Beta/html/Beta\_Release\_Notes/)可了解详情。你可以从这里[下载  
RHEL 6 Beta](https://inquiries.redhat.com/go/redhat/rhel-6-beta)。

{ Thanks abird. }
