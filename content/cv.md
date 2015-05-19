Title: cv: 显示 cp、mv 等命令的进度
Date: 2014-07-14 22:57
Author: toy
Category: Apps
Slug: cv

在 Linux 系统中，大多数命令从来都是信奉“沉默是金”的准则，所以当我们利用 `cp` 复制文件的时候并不能看到所谓的进度条。如果你在意这一点，那么不妨来用用 [cv][c]。

![cv](https://linuxtoy.org/img/2014/07/cv.png)

cv 是 Coreutils Viewer，它能够显示传输数据的进度，包括百分比、大小、以及速率等信息。cv 支持 coreutils 中的基本命令，比如 cp、mv、rm、dd、tar 等等。

cv 的源代码可从 [GitHub][g] 获取，需要自行编译。

[c]: https://github.com/Xfennec/cv  
[g]: https://github.com/Xfennec/cv
