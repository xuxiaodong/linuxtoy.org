Title: 使用 dd 和 gzip 代替 Ghost 做磁盘镜像
Date: 2006-12-28 18:02
Author: toy
Category: Tutorials
Slug: make_disk_image

在 Linux 下，其实可以使用 dd 和 gzip 命令来代替 Ghost
做磁盘镜像。但缺点是速度不够理想，据实际测试表明，16 GB（实际占用
4GB）可能需要耗费 1 个小时。

要使用 dd 和 gzip 备份，可以执行命令：  
`# dd if=/dev/hda1 | gzip > bw.office.sled.10.hda1.dd.gz`

在还原时，可以执行下列命令：  
`# gzip -dc bw.office.sled.10.hda1.dd.gz | dd of=/dev/hda1`

值得注意的是，还原时需要使用如 Live CD 之类的 Linux 引导系统。

（感谢 pig345 分享此技巧）
