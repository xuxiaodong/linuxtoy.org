Title: 批量创建缩略图
Date: 2006-10-27 23:04
Author: toy
Category: Apps
Slug: batch_create_thumbnail

平时在创建缩略图时，经常用到 ImageMagick 中的 convert
程序。不过，仅限于创建单张图片的缩略图。今天，读到 *[CLI tricks:
Creating image
thumbnails](http://polishlinux.org/apps/cli-tricks-creating-image-thumbnails/)*
一文时，其中一段可以批量创建图片缩略图的代码相当受用，兹录于后。  

` for file in *.png do   convert -resize 200 "$file" thumb_"$file" done`

这段代码将对目录中的所有 png 文件生成对应宽度为 200px
的缩略图。如果需要对其他图像文件格式进行操作，那么可以修改代码中的
png。与此同时，对于最终生成缩略图的大小也可根据自己需要进行修改。

如何使用这段代码呢？相当简单，创建个新的文件，粘贴上这段代码，然后在文件之前加上
#!/bin/bash。保存后，chmod +x 该文件即可。

完整的代码可从[这里](http://linuxtoy.org/dls/createthumb)看到。
