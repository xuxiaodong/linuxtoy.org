Title: 教程：把Opera的快速拨号引入 Konqueror
Date: 2009-08-30 10:26
Author: gmsh
Category: Apps
Slug: speeddial-for-konqueror

本教程介绍一种借助软件把快速拨号引入 Konqueror 中的方法。

众所周知，快速拨号（SpeedDial）是 Opera
浏览器的特殊功能。读完本教程，你可以和 [John
Smith](http://blog.gmsh.pp.ru/about)一样借助 Tristan
把快速拨号引入Konqueror。

  
*转自[http://blog.gmsh.pp.ru/2009/08/speeddial-for-konqueror/ （Gmsh's
blog）](http://blog.gmsh.pp.ru/2009/08/speeddial-for-konqueror/)*

效果示意

[![](http://i.linuxtoy.org/images/2009/08/speeddial-400x269.jpg)](http://i.linuxtoy.org/images/2009/08/speeddial.jpeg)

OK,Let's go！

1.  从[这里](http://www.unix-ag.uni-kl.de/~fischer/speeddial/tristan-20090828.tar.bz2)下载
    Tristan, 名为`tristan-20090828.tar.bz2`。
2.  解压，并在文件夹下建立名为 `debug` 的文件夹。
3.  进入该文件夹，编译。命令如下`cmake -DCMAKE_INSTALL_PREFIX=/usr \  -DCMAKE_BUILD_TYPE=debugfull ../ \  && make`。
4.  运行`su -c "make install"` 安装
5.  运行`kbuildsycoca4`重建系统配置。
6.  依次进入KDE4 的系统配置>高级>文件关联，新建类型
    appliction/x-tristan , 添加扩展名 `*.trs`,嵌入项按图配置。
    [![](http://i.linuxtoy.org/images/2009/08/tristansettings.jpeg)](http://i.linuxtoy.org/images/2009/08/tristansettings.jpeg)
7.  重启 Konqueror 打开 源码文件夹下的
    example.trs。用右键配置即可。推荐设为主页。

参考资料：http://www.unix-ag.uni-kl.de/~fischer/speeddial/
