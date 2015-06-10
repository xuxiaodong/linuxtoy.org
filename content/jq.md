Title: jq: 从命令行处理 JSON
Date: 2014-03-11 10:42
Author: toy
Category: Apps
Slug: jq

因为最近要处理一些 JSON 数据格式，所以在经过一番搜索后最终找到了 [jq][j] 这个很棒的工具。jq 允许你直接在命令行下对 JSON 进行操作，包括分片、过滤、转换等等。

<!-- PELICAN_END_SUMMARY -->

让我们通过几个例子来说明 jq 的功能：

**漂亮打印**

如果我们用文本编辑器打开 JSON，有时候可能看起来会一团糟，但是通过 jq 的 `.`（点）过滤器就可以立马让 JSON 的格式规整起来。

    % jq . soundtag.json

![jq](/img/2014/03/jq01.png)

*用文本编辑器打开后的样子*

![jq](/img/2014/03/jq02.png)

*用 jq 显示的结果*

**快速查询**

利用 jq 能够以 `key` 作为关键字来对 JSON 作出快速查询，例如：

    % jq .cn soundtag.json

这将仅仅显示 `cn` 键对应的值。

jq 的键查询也支持链式调用，如：

    % jq .cn[0].pNum soundtag.json

**管道操作**

熟悉命令行的朋友可能都知道 | （管道）是一个非常强大的武器。幸运的是，jq 也提供了对管道的支持。

    % jq '.cn[] | { pNum }' soundTag.json

在这里，我们使用管道过滤并构造出 pNum 对象。

**总结**

如果你需要在命令行下处理 JSON，我强烈推荐 jq。jq 不仅能够满足一般性的常见需求，更包含运算、内置函数、条件比较、  变量声明、自定函数等强大功能。对此感兴趣的朋友，不妨通过 [jq 的官方手册][m]进行学习。

[j]: http://stedolan.github.io/jq/  
[m]: http://stedolan.github.io/jq/manual/
