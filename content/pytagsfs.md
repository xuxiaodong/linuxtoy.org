Title: 有趣的 FUSE -- pytagsfs
Date: 2010-04-20 10:25
Author: toy
Category: Apps
Tags: FUSE, pytagsfs
Slug: pytagsfs

{ 撰文/guest }

在 Linux 下有很多的音乐管理软件，但是这个基于 FUSE  

的软件更强，能按照指定的格式字串和过滤器将文件系统中的音乐挂载到一个文件夹中！看看他的例子吧。

pytagsfs -o format='/%g/%a - %t.%e' source(原始音乐文件夹)
by-genre(要挂载到的目录)

将音乐先按风格分成文件夹，每个风格文件夹下的音乐显示成 artist -  
title.extension 的格式。

更强的是原始文件系统的任何变化都会反映至挂载的目录中(如 tag
修改将令虚拟文件系统中的文件位置变更)，而挂载目录中的文件重命名、移动、修改都相当于对原始音乐文件的
tag 修改！

假如音乐文件没有对应的标签，将会被排除。不过也可以手动添加至挂载文件夹。

本人简单尝试了几个 mp3，发现程序默认是读取 ID3v2 标签(只有 APE
标签时音乐都被排除了)，若只使用中文的 ID3v1 标签则乱码。推荐用 Foobar 把
mp3 的标签统一成 ID3v2+APE 标签之后再使用。

对于标签的支持，pytagsfs 基于 [Mutagen  
库](http://code.google.com/p/quodlibet/wiki/Development/Mutagen)。  
Mutagen 库在 QuodLibet、Exaile、Listen 等多个音频软件中被使用。

主页：

PS：假如源目录中文件有一个相同拷贝，则挂载后只显示了一个文件。不过我没有尝试的是，假如原始文件不是拷贝，但是按标签生成的文件名一样改是什么效果？

{ Thanks guest. }
