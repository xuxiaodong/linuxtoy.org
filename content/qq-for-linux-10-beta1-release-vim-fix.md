Title: QQ for Linux 1.0 Beta1 发布(Vim冲突修复)
Date: 2009-01-04 16:13
Author: lovenemesis
Category: Instant Messenger
Tags: QQ
Slug: qq-for-linux-10-beta1-release-vim-fix

腾讯公司的即时通讯软件 QQ for Linux 今日发布了最新的 1.0 Beta1 版本。

该版本主要改进为：

-   支持好友备注功能
-   支持代理服务器登录
-   支持热键（提取消息：Ctrl+Alt+Z ；截屏：Ctrl+Alt+A）
-   优化皮肤的细节
-   优化代码运行效率，再次降低系统开销
-   2009-1-6 替换版本文件，修正Esc和vim冲突的问题(版本号未变)

发布说明见[这里](http://support.qq.com/cgi-bin/beta2/content_new?tid=2467867&start=0&num=20&order=0&pn=1&fid=361)。  
下载见[这里](http://im.qq.com/qq/linux/download.shtml)。

~~PS: 和Vim ESC 热键冲突的问题已经向腾讯提交
Bug，感谢各位的测试。对于已经安装的朋友可以参照41楼 xeoc 朋友的方式用
Ctrl+[ 替代。~~

PS: **Vim
的问题已经解决**，请前往官网重新下载即可。这次腾讯解决问题的速度值得表扬！

*Fedora 用户替换 2009-1-6 版本的方法：*  
在新的 RPM 包所在目录使用命令：
`su -c 'rpm -Uvh --replacepkgs --replacefiles linuxqq-v1.0.2-beta1.i386.rpm '`
