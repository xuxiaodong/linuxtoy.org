Title: Morphu U — 制作人脸渐变动画
Date: 2007-08-28 09:29
Author: toy
Category: Apps
Slug: morphu-u

[Morphu U](http://morphu.cosoft.org.cn/) 是一个很有意思的程序。据作者
goldolphin 介绍，它原是 Win32 程序，后来利用 gtkmm 界面库移植到了 Linux
平台下。由于 Morph U 通过采用 Field-Morphing
技术来实现图像的变形效果，所以你可以使用它在将两幅图像按一定比例融合生成中间图像或是改变一幅图像中某些形状的基础上制作连续的人脸渐变动画。

[![Morphu
U](http://i.linuxtoy.org/i/2007/08/morphu_s.png)](http://i.linuxtoy.org/i/2007/08/morphu.png)  
*Morphu U 屏幕截图*

**编译 Morphu U**

Morphu U
没有提供二进制包，因此，如果你打算使用它，就必须亲自动手编译它。不过，不用担心，这个过程并不难。在编译
Morphu U 之前，你需要准备 gtkmm2.4-dev 或以上版本。然后[下载 Morphu U
的源代码](http://morphu.cosoft.org.cn/miscs/morphu-0.11a.tar.gz)（目前最新版本为
0.11a），执行以下命令：  
` tar zxvf morphu-0.11a.tar.gz cd morphu ./configure cd src make`

**运行并使用 Morphu U**

编译完成后，可以执行 ./morphu 来运行 Morphu U 程序。 关于 Morphu U
的使用方法在程序主页已经说得非常详细了，建议大家参考一下，此不赘述。例如下图的效果就是由
Morphu U 所带的示例文件生成的。

![Morphu U](http://i.linuxtoy.org/i/2007/08/morphu-result.gif)  
*使用 Morphu U 制作的人脸渐变动画*

[感谢 Morphu U 的作者 goldolphin 推荐]
