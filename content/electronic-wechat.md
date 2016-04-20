Title: Electronic WeChat：在 Linux 下使用微信
Date: 2016-04-20 10:03:38
Authors: toy
Category: Apps
Tags: im, wechat
Slug: electronic-wechat

Electronic WeChat 是利用 [Electron][e] 开源框架而打造的一款第三方微信客户端，目前支持 Linux 和 Mac OS X 系统。

<!-- PELICAN_END_SUMMARY -->

[![Electronic WeChat]({filename}/images/e-wechat.thumb.png)]({filename}/images/e-wechat.png)

Electronic WeChat 具有一些不错的特性，包括拖入图片、文件即可发送，能够阻止他人撤回消息，可以显示贴纸消息，以及直接打开重定向的链接等等。

要在 Linux 下安装 Electronic WeChat，可以下载 `linux-x64.tar.gz`（64
位，选择适合自己系统的架构）后执行：

```
tar zxvf linux-x64.tar.gz
cd dist/Electronic\ WeChat-linux-x64
./Electronic\ WeChat
```

然后使用手机扫描二维码即可登录。

&rarr; [Electronic WeChat](https://github.com/geeeeeeeeek/electronic-wechat)

[e]: https://github.com/atom/electron

{ Thanks Iven. }
