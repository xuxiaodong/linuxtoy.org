Title: 使用 rtop 监视远程服务器
Date: 2015-05-23 18:22:12
Authors: toy
Category: Apps
Tags: rtop
Slug: rtop

[rtop][r] 是一个基于 SSH 的远程系统监视工具。通过 `rtop`，你可以远程监视
CPU、内存、磁盘、以及网络的使用情况。

<!-- PELICAN_END_SUMMARY -->

![rtop](/images/2015/05/rtop.png)

`rtop` 使用 Go 语言编写而成，可按如下步骤获取源码并编译：

```bash
git clone --recursive https://github.com/rapidloop/rtop
cd rtop
make
```

要运行 `rtop` 则可执行：

```bash
rtop user@host:port
```

其中：

- user：SSH 用户
- host：SSH 主机或 IP
- port：SSH 端口，可选

稍等片刻，便可看到如上图所示的系统概要信息。

[r]: http://www.rtop-monitor.org/
