Title: Google Chrome for Fedora
Date: 2009-11-10 03:01
Author: lovenemesis
Category: Web Browser
Tags: chrome, Fedora
Slug: google-chrome-for-fedora

谷歌最近将 Google Chrome Linux 版本推送到自己的 Linux RPM 仓库里了，使用
Fedora 的铬粉可以方便的使用 yum 安装 Chrome 浏览器了。

如果已经通过 Google Linux 软件仓库安装过 Picasa for Linux 或者 Google
Desktop Search 那么，只需要简单的使用以下命令即可。

`su -c 'yum install google-chrome-unstable'`

如果没有启用的话可以使用谷歌提供的脚本添加该仓库，然后再使用以上命令：

`su -c 'wget https://dl-ssl.google.com/linux/google-repo-setup.sh && bash google-repo-setup.sh'`

更多详细内容（包括64位的诡异现象，也是我迟迟未发布的原因）请移步至
[liangsuilong](http://www.liangsuilong.info/?p=484#content) 兄的博客。
