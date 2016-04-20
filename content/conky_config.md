Title: Conky 的配置
Date: 2006-11-06 09:33
Author: toy
Category: Tutorials
Tags: Conky
Slug: conky_config

[Conky](http://conky.sourceforge.net) 不仅十分小巧，它不会消耗多少系统资源空间；而且可以很漂亮，本身支持伪透明特性，能够嵌入到桌面中。用于实时监视系统，了解系统运行之状况，实在是不二之选。

<!-- PELICAN_END_SUMMARY -->

![Conky](http://i.linuxtoy.org/i/2006/11/conky.png)

Conky 的安装是非常简单的，一句 `sudo apt-get install conky` 就可搞定，以 Debian/Ubuntu 为例。Conky 默认并不会创建配置文件，需要使用下列命令手动生成：

`zcat /usr/share/doc/conky/examples/conkyrc.sample.gz > ~/.conkyrc`

但 Conky 默认的配置也许并不能满足我们的需要，所以就让我们来定制它吧。我配置的
Conky 最终效果如右图所示，主要是简洁，仅查看必要的系统信息。看了你是不是有点心动了呢？

关于 Conky 的配置，主要注意下面几点：

1. 定义字体：使用 `xftfont Luxi Sans:size=8` 这行可以定义 Conky 的全局字体，其格式为字体名称:大小，也可使用字体样式，如粗体可用 `style=Bold` 来表示。

2. 显示位置：假如我要让 Conky 在右上角显示，就去掉 `alignment top_right` 这行的注释符，相应的注释其余的行，如下所示。  

        #alignment top_left alignment top_right #alignment bottom_left #alignment bottom_right #alignment none

3. 大小及边框：分别由 `minimum_size` 和 `border_width` 来确定，前者的设置格式为宽x高，不要边框的话，可将后者设置为 0。

4. 显示信息：在 Conky 配置文件的最后部分可以定义具体显示什么内容。这里主要是了解一些变量的使用，比如，显示系统从开机到现在所运行的总共时间，可以使用 `uptime` 变量，变量前面要用 `$` 表示。更多变量的含义可以查看 Conky 主页的 [Conky Variables](http://conky.sourceforge.net/variables.html)。

在 Conky 网站上提供了大量的[配置文件示例](http://conky.sourceforge.net/screenshots.html)可以参考。也可看看我的[配置文件](http://linuxtoy.org/dls/conkyrc)。
