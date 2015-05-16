Title: Stapler: 从命令行处理 PDF 文档
Date: 2010-05-21 11:47
Author: toy
Category: Apps
Tags: PDF, Python, Stapler
Slug: stapler

Stapler 是一个用于处理 PDF 文档的命令行工具，因其为纯 Python
实现，所以比 Java  
实现的 PDFtk 更轻巧，可作为后者的替代品使用。

目前，Stapler 包括合并 PDF、分割 PDF、删除 PDF
中的页面等功能。兹举一例来说明  
Stapler 的用法。

假设你想要将 1.pdf 和 2.pdf 合并为一个单独的 PDF 文档  
out.pdf，则可以执行以下命令：

stapler cat 1.pdf 2.pdf out.pdf

Stapler 的其他用法可通过执行不带参数的 stapler  
命令获得，大都一目了然，只需依照做即可。

Stapler 的源代码可通过 [github](http://github.com/hellerbarde/stapler)
取得。
