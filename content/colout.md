Title: Colout: 给命令输出来点颜色
Date: 2013-06-28 21:57
Author: toy
Category: Apps
Slug: colout

[Colout][c]
是颇为好玩的小工具，她能够对别的命令输出进行着色处理。Colout  
本身支持正则匹配，目前具有 8 色及 256 色模式，此外还支持  
colormap、主题、以及源代码语法着色等特性。

![Colout](http://lt-file.b0.upaiyun.com/files/2013/06/colout.png)

Colout 的一般用法为：

| colout [颜色]

例如，执行 `ls -l ~ | colout "^(d*)-*(rwx)(rwx)(r-x)"
blue,red,yellow,green`  
后的效果如上图所示。

更多示例，可参考 Colout 的[使用说明][c]。

[c]: http://nojhan.github.io/colout/
