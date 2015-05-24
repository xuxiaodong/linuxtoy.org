Title: blecat: 蓝牙传输小工具
Date: 2015-05-24 16:37:52
Authors: toy
Category: Apps
Tags: cli, bluetooth
Slug: blecat

[blecat][b] 是利用蓝牙协议编写的命令行小工具，它支持管道操作，也能用来传输文件。

<!-- PELICAN_END_SUMMARY -->

通过一行 `npm install -g blecat` 命令即可安装 `blecat`。

比如，在开启蓝牙的两台电脑上，若在其中一台执行：

```bash
echo hello world | blecat
```

那么在另一台只要直接敲入 `blecat` 就会输出 `hello world`。

传文件的话，则可利用 shell 重定向按如下方式操作：

```bash
blecat < myfile.txt # 发送端
blecat > myfile.txt # 接收端
```

感兴趣的朋友不妨一试。

[b]: https://github.com/mafintosh/blecat
