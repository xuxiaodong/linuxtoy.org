Title: Docker 0.7
Date: 2013-11-27 15:16
Author: lovenemesis
Category: Virtual Machine
Tags: docker
Slug: docker-0-7

基于 Linux 系统的轻量级容器工具 Docker 发布 0.7 版本，带来了标准 Linux
支持，不再需要特定的内核。

新版本带来七大功能：

-   标准 Linux 支持，提供对 Fedora/RHEL、Ubuntu、Gentoo、Arch
    等发行版的开箱即用支持。
-   实现统一化存储驱动，包含对三种存储方式的支持：AUFS、VFS 和
    DeviceMapper 的支持，正在开发包括 Btrfs 及 ZFS
    在内的更多文件系统支持。
-   支持离线传输，可以将完整的运行时环境原封不动的进行迁移，方便企业级用户进行封包部署。
-   改善了端口映射，允许更复杂的端口映射逻辑，并时代调整了语法。
-   在明确允许的情况下可以在各个容器间搭建连接实现互通。
-   现在终于可以给容器自定义名称了！
-   多方面质量控制上的改善。

[官方发布公告](http://blog.docker.io/2013/11/docker-0-7-docker-now-runs-on-any-linux-distribution/)
