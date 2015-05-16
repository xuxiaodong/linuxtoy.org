Title: Dijjer：给流媒体插上 P2P 的翅膀
Date: 2006-10-10 20:19
Author: toy
Category: Apps
Slug: dijjer

[Dijjer](http://dijjer.org) 是一个很特别的 P2P 软件。说它特别，是因为
Dijjer 与一般的 P2P 软件有着很大的不同。对于流媒体的发布者来说，使用
Dijjer 可以为他们节省网站的带宽；同样地，流媒体的分享者则可以利用 Dijjer
提高下载速度。使用 Dijjer 具有以下优势：

![Dijjer](http://i.linuxtoy.org/i/dijjerlogo.png)

-   在浏览器中即可下载，无需新开其他的 P2P 下载客户端；
-   边下载边播放，在下载音乐或视频的时候，就可以立即倾听或者观看了；
-   能完美地在 RSS 及 podcasting 中使用；
-   支持 Windows、Mac 和 Linux，人人都可享用 Dijjer。

如果你是一个流媒体的发布者，那么可以这样在你的网站中使用 Dijjer：

    原始链接：http://mysite.com/video.mov
    使用 Dijjer 后的链接：http://dijjer.org/get/http://mysite.com/video.mov

不需要安装 Dijjer，便可直接使用。

而对于想要享受流媒体的用户来说，则可以按以下步骤操作：

1.  下载
    [Dijjer](http://downloads.dijjer.org/dijjer.jar)，将得到一个名为
    dijjer.jar 的文件。
2.  在终端中使用

        java -jar dijjer.jar

    来执行 Dijjer。

3.  在浏览器地址栏中输入

        http://127.0.0.1:9115

    可以访问 Dijjer 状态页面。

4.  要使用的话，只需在 http://127.0.0.1:9115
    后面加上流媒体的实际地址即可，如
    http://127.0.0.1:9115/http://mysite.com/video.mov。

最后，提供一个链接，供大家测试：

    http://dijjer.org/get/http://linuxtoy.org/test.mp3
