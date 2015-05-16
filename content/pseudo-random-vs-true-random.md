Title: 伪随机和真随机
Date: 2011-10-15 00:00
Author: lovenemesis
Category: Funny
Tags: random
Slug: pseudo-random-vs-true-random

相信每个计算机相关专业的人都理解伪随机和真随机的差别，那么它们到底“看起来”有什么差别呢？

下面是来自 [Random.org 的随机数位图](http://www.random.org/bitmaps/)：

[![](http://linuxtoy.org/img/2011/10/randbitmap_true.png "randbitmap_true")](http://linuxtoy.org/img/2011/10/randbitmap_true.png)

下面是在 Windows 系统上调用 PHP 的 rand() 方法生成的：

[![](http://linuxtoy.org/img/2011/10/randbitmap_computer.png "randbitmap_computer")](http://linuxtoy.org/img/2011/10/randbitmap_computer.png)

看起来并不随机是吧？

代码如下：

    // Requires the GD Library
    header("Content-type: image/png");
    $im = imagecreatetruecolor(512, 512)
        or die("Cannot Initialize new GD image stream");
    $white = imagecolorallocate($im, 255, 255, 255);
    for ($y=0; $y<512; $y++) {
        for ($x=0; $x<512; $x++) {
            if (rand(0,1) === 1) {
                imagesetpixel($im, $x, $y, $white);
            }
        }
    }       
    imagepng($im);
    imagedestroy($im);

同样这段代码在 Linux 系统上运行时并没有出现这样的规律，换用 Mersenne
Twister 的 mt\_rand()
方法也没有这样的规律。为神马呢？[请看这篇文章](http://www.boallen.com/random-numbers.html)。

[原文博客](http://www.boallen.com/random-numbers.html)

[消息来源](http://identi.ca/notice/84559479)
