Title: DocBook配置指南
Date: 2008-08-15 13:42
Author: Kardinal
Category: Apps
Tags: docbook
Slug: docbook%e9%85%8d%e7%bd%ae%e6%8c%87%e5%8d%97

其实DocBook配置本来是很容易的，但是你在网上查阅了各种资料之后，它就变成了不可能完成的任务  

本人搜遍千山万水，经过分析、整理、试验、大胆假设、小心求证……总之是不容易，终于实践出一个可行的方案  

**配置运行环境**

在Archlinux中配置DocBook` pacman -S docbook-xml docbook-xsl libxslt libxml2 `

在Ubuntu中配置DocBook` apt-get install xsltproc docbook-xsl `

**生成Html文件**

写好一个DocBook.xml文件之后，使用这个命令检查一下是否有错误  
`xmllint DocBook.xml`

生成单页面Html文档  

`xsltproc /usr/share/xml/docbook/xsl-stylesheets-xxxx/xhtml/docbook.xsl DocBook.xml > DocBook.html `

生成多页面Html文档  

`xsltproc /usr/share/xml/docbook/xsl-stylesheets-xxxx/xhtml/chunk.xsl DocBook.xml`

将下面的代码保存为DocBook.xml试验一下吧

> <?xml version="1.0" encoding="UTF-8"?>  
>  <!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
> "http://docbook.org/xml/4.2/docbookx.dtd">  
>  <article>  
>     <title>My first Docbook document</title>  
>     <sect1>  
>        <title>The greeting</title>  
>        <para>  
>          Hello world 你好  
>        </para>  
>     </sect1>  
>  </article>
