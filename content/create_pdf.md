Title: 创建 PDF 文档
Date: 2006-08-01 15:30
Author: toy
Category: Tutorials
Slug: create_pdf

原文在[这里](http://ubuntu.wordpress.com/2006/03/23/print-to-pdf-using-cups-pdf/)，但需要代理才能访问。简单记录下过程备用。

1.安装 cups-pdf：

`sudo apt-get install cups-pdf`

2.编辑/etc/cups/cupsd.conf：

`将 RunAsUser Yes 更改为 RunAsUser No`

3.重启 cupsys：

`sudo /etc/init.d/cupsys restart`

4.添加新的打印机：

到 System->Administration->Printing，新建打印机，第一步选择“Local
Printer”和“PDF
Printer”选项，第二步选择“Generic”，并在下面选择“Postscript Color
Printer”。

最后，简单执行 `sudo chmod +s /usr/lib/cups/backend/cups-pdf` 即可。

至此，你可以通过打印来创建 PDF 文档了。

注：生成的文件在用户主目录的 PDF 文件夹中。完美支持中文！
