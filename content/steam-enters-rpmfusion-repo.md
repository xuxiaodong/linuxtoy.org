Title: Steam 进入 RPMFusion 仓库
Date: 2013-11-01 16:13
Author: lovenemesis
Category: Games
Tags: steam
Slug: steam-enters-rpmfusion-repo

来自 Valve 的数字分发平台 Steam 现在被收录至 RPMFusion 仓库，方便 Fedora
及 RHEL7 用户安装。

关于 Steam 本站已有诸多报道，不再赘述。

Steam 目前官方仅以 deb 格式发布，但协议允许第三方重分发。本次亦是
Fedora/RPMFusion 打包者的社区结果，相比先前 Fedora People 仓库中的
Steam，本次优化了配置文件，不再依赖 Ubuntu
运行时环境，避免了一些图形和声音问题。

如果您已经安装了之前的版本，**请注销重登录或重启计算机**保证软件包升级生效。此外该软件包也会自动处理
S3TC 材质压缩的问题。

当下该软件包尚处于测试仓库中，Fedora 18/19 中通过以下命令安装：

`yum -y --enablerepo=rpmfusion-nonfree-updates-testing install steam`

[消息博文](http://negativo17.org/steam-is-now-in-rpmfusion/)
