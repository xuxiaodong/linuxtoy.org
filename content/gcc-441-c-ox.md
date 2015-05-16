Title: GCC  4.4.1 发布在即，C++ 0x 标准实验性支持大幅进步
Date: 2009-04-23 11:35
Author: toy
Category: News
Tags: GCC
Slug: gcc-441-c-ox

{撰文/guest}

前些日 GCC 4.4 版发布，对 C++ 0x
标准的支持有了大幅的提升，但是没看到有什么消息报道。今日到 GCC
网站看，得知 4.4.1 版本发布在即，故投稿一封。

请注意，以下所有特性都需要在命令行指定 `-std=gnu++0x` 或
`-std=c++0x` 来启用!!

GCC 4.4 相对于 4.3 版最大的变化就是对 C++ 0x
标准支持有了大幅提升（当然，还有很多其他方面的改变，不过我个人比较关注
C++），已支持的 0x 特性中，thread 已经可用，api 方面基本上与 pthread
规范相一致，熟悉 pthread 的人能很快上手。因为 pthread
规范已经非常成熟，所以在 C++ 中支持 thread 只是标准方面的问题（看 4.4
的头文件可知，在支持 pthread 的平台上，mutex 和 condition\\\_variable
等直接映射到 pthread 相应类型），不过，C++
作用域之后变量被析构，使得程序员可以直接在临界区的作用域内声明
lock\\\_guard<mutex>lock(mutex)，而无需手动释放互斥锁。得益于 4.4
版中对于其他 C++ 新特性--变长模板参数的支持，也可以一次性在
std::lock(LockableType1&m1,LockableType2&m2...)中锁定多个锁。对于 thread
编程中相关的时间问题，如 pthread 中的 pthread\\\_cond\_wait，由另一个 0x
标准的库--chrono
支持，这个库抽象了时间点，时间间隔等概念，而且借助运算符重载，对时间点-时间点=时间段，时间点＋时间段=时间点
等常用逻辑进行了封装。另外使用了模板技术在编译期对声明的类型精度进行保护，比如说
1hour+1second，只能得到更高精度的 second 类型，而不能得到 hour 类型。与
pthread 相关的还有 cstdatomic，其中包含了常用的基本类型对应的 atomic
类型，而且使用 atomic 也可以生成自定义的 atomic 类型。

容器方面，forward\\\_list 被加入，vector 等已有的容器增加了 cbegin,cend
来返回 const\\\_iterator，并且最重要的，是对 Initializer
lists--初始化列表的支持。以往对容器一些初始元素的置入，只能是声明容器后用
push\\\_back 等方法调用，而现在，你可以这样用 vector<int>
container{1,2,3,4,5,6,7}。而且初始化列表可以嵌套，比如: set>
tuple\\\_container{{2,3.2},{4,5.8}};(测试发现一个问题，如知道请赐教。经测试，
GCC 自带的 std::tr1::tuple 支持初始化列表，但是不能嵌套，boost::tuple
可以)。这方便了使用，也提高了可读性。

另一个好东西就是 auto，你可以不必写 map>>::const\_iterator
it=container.begin()(当然只是举例子...)，而直接用 auto
it=container.begin()，类型推导就交给编译器吧。另一个小的但是方便的变化是你可以这样写
vector > 而不用写 vector 空格>。

对于构造函数，拷贝构造函数等的一些方便性的问题上，default 和 delete
已被支持。过去，自定义了构造函数后，默认的构造函数便不再自动生成，带来些语法上的麻烦，但是现在你可以这样写:
constructor()=default:仍然有默认的构造函数。类不可复制:constructor(const
xx&)=delete。诡异的“模板函数不能有默认模板参数”问题已解决。

以上这些只是我稍有了解的部分，相对 4.3 的全部变化，请看原页面
。比较可看出，4.4 相对 4.3 只增加了一些 tr1 的扩展来说，改变还是很大的。

为了第一时间尝鲜，我没有在 Linux 下编译 4.4，而是使用了别人编译的 GCC
4.4 win32 版，页面 ，我实验的这些特性中，win32 版的 GCC 是不能使用
thread 的，我加入了 pthread-for-win32，又定义了 GCC 头文件中几个控制
thread 库是否被支持的宏，仍然没有成功将 thread 带入 std
命名空间，最后一次成功带入，链接时却报错与 pthread-for-win32 中一个 time
结构冲突，故想完全体验 4.4 thread 好处的同志们请使用 Linux
版。另外，我个人声明，我使用
c/c++/java/c#(样样稀松)，所以希望这个贴不要成为各个语言 fans 的 pk
场...喜欢 C++ 的同志看看，不喜欢的，也可以彼此借鉴借鉴。此次 0x
标准中借鉴了其他语言的长处，如契约概念(类似于 java 中
comparable,xxxable)lambda 表达式(C＃已支持)而 java 的泛型，java7
的初始化列表等概念也从 c++
中得到经验和教训(或许这些所说只是谁先有了实现的问题)，语言的不断进步，我们也可得到更好的编程体验。
