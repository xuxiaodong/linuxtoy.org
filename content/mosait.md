Title: Mosait：制作马赛克效果的拼图
Date: 2008-08-22 09:02
Author: toy
Category: Apps, Cli
Tags: Mosait
Slug: mosait

Mosait 是一个颇有意思的命令行小程序。使用
Mosait，你可以将一幅图片转换成具有马赛克效果的拼图。即便原图片再平常不过，经过
Mosait 的处理，也变得饶有趣味起来。

**编译 Mosait**

在使用 Mosait 之前，你需要从源代码编译它。Mosait 要求
[freeimageplus](http://freeimage.sourceforge.net/)
库，在准备好之后，只需执行下载、解包、make 等步骤即可。

**Mosait 用法**

要使用 Mosait
制作拼图，首先你需要建立一个图片数据库。这可以通过执行以下命令完成（假设你的图片都保存在
images 目录中）：

`mosait -c images/ -o images.db`

接着，我们就可以使用 Mosait 制作具有马赛克效果的拼图啦：

`mosait -d images.db -i src_image.jpg -o my_mosaic.jpg`

上述指令中的 src\_image.jpg 为原图，my\_mosaic.jpg
为输出后的图片，你需要使用自己的图片名称替换。

例如，名画《蒙娜丽纱的微笑》经过 Mosait 处理后，其效果如下图所示：

[![joconde-mosaic](http://i.linuxtoy.org/i/2008/08/joconde-mosaic-thumb.jpg)](http://i.linuxtoy.org/i/2008/08/joconde-mosaic.jpg)  
*点击可放大*

[Mosait](http://mosait.tangui.eu.org/)
