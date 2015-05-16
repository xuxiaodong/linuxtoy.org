Title: Hotpatch
Date: 2011-10-10 14:41
Author: lovenemesis
Category: Development
Slug: hotpatch

Hotpatch 是一个允许正在运行的进程动态加载一个 so 库的 C 库，类似于 Win32
上的 CreateRemoteThread() API。

和其他现有的动态加载方案相比，Hotpatch 的优点是在**加载 so
库之后将会恢复原先进程的运行状态**。

开发者可以利用 Hotpatch 实现：

-   加载 so 库到一个已经运行的进程中。
-   调用该 so 库中的自定义函数。
-   向该函数传递序列化的参数。

它包含三部分： `hotpatch.h` 头文件，`libhotpatch.so` 库和命令行辅助程序
`hotpatcher`。

目前的局限有：

-   用户只能向拥有权限的进程注入 so 库（当然 root
    用户可以向所有进程注入）。
-   目前仅支持 64 位 Linux，32 位支持将在下一个版本中完成。
-   在编译共享库时需要加上连接器参数 `-fPIC -nostartfiles`。
-   对于一个正在运行进程仅能动态加载一次 so 库文件。

[详细说明及 API 列表](https://github.com/vikasnkumar/hotpatch#readme)

[Github 仓库](https://github.com/vikasnkumar/hotpatch)

[消息来源](http://identi.ca/notice/84509249)
