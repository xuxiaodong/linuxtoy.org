Title: 使用 pydf 查看磁盘空间占用情况
Date: 2009-01-11 17:32
Author: toy
Category: Apps
Tags: df, pydf, Python
Slug: pydf

pydf 是一个 df 克隆，因其使用 Python 语言编写而成，故名为 pydf。使用
pydf，你可以查看磁盘的空间占用情况，比如已经用了多少，还剩下多少。与 df
相比，pydf 输出的信息更加具有可读性（当然，这个 df
加上必要的选项也可以做到），另外就是 pydf 包含色彩化的输出。

![pydf](http://i.linuxtoy.org/images/2009/01/pydf.png)

上图为执行 pydf 后的默认输出结果。

你也可以给 pydf 增加选项来改变输出行为。具体的 pydf 选项可通过
`pydf --help` 查询。

[pydf](http://kassiopeia.juls.savba.sk/~garabik/software/pydf/)
