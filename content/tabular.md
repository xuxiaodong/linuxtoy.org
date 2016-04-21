Title: Tabular: 在 Vim 中对齐文本
Date: 2011-02-22 20:12
Author: toy
Category: Vim plugins
Tags: Vim
Slug: tabular

Vim 插件 [Tabular](https://github.com/godlygeek/tabular) 允许你在 Vim 中按等号、冒号、表格等来对齐文本，对于经常写代码的朋友来说，有 Tabular 将会非常方便。

<!-- PELICAN_END_SUMMARY -->

![Tabular](http://linuxtoy.org/img/2011/02/tabular.png)

如上图所示，假如我想让其中的两行按等号对齐，则将光标定位到有等号的那行，执行 `:Tab /=` 即可。

又如，若想将下面的

```
|1|2|  
|one|two|
```

变成

```
| 1 | 2 |  
| one | two |
```

可执行 `:Tab /|`。
