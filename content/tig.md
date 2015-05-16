Title: 使用 tig 方便的提交代码片断
Date: 2010-05-15 18:56
Author: vern
Category: Cli
Slug: tig

tig 是一款命令行界面的 git 版本仓库工具。用 tig 作 commit in
时，它方便你作代码片断的提交。

打开 status view，移动光标到希望提交的代码行附近

[![](http://i.linuxtoy.org/images/2010/05/2010-05-15_1440x900_origin-7046121.png)](http://i.linuxtoy.org/images/2010/05/2010-05-15_1440x900_origin-7046121.png)

按 u 后提交了 -143,6 +144,7 附近的代码片断

[![](http://i.linuxtoy.org/images/2010/05/2010-05-15_1440x900_partof-7027401.png)](http://i.linuxtoy.org/images/2010/05/2010-05-15_1440x900_partof-7027401.png)

关闭 status view 后，按 u 就提交了整个文件

[![](http://i.linuxtoy.org/images/2010/05/2010-05-15_1440x900_completely-701396.png)](http://i.linuxtoy.org/images/2010/05/2010-05-15_1440x900_completely-701396.png)

想了解 tig 的更多信息请浏览它的主页 <http://jonas.nitro.dk/tig/>
