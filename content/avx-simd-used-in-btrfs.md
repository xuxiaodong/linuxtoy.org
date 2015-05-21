Title: AVX 指令集于 Btrfs 的应用
Date: 2015-04-19 21:33
Author: lovenemesis
Category: Tips
Tags: Btrfs
Slug: avx-simd-used-in-btrfs

每一次新品 X86
处理器发布时都会增添以两个名字拗口的新指令集，[AVX](https://en.wikipedia.org/wiki/Advanced\_Vector\_Extensions)
即是这两年引入又在不断得到改善的新指令集之一。可惜大多数新的指令集并不能为一般日常使用带来太多提升。不过若是您打算使用
Btrfs 文件系统的话，需要留意下 AVX 的支持程度了。  

<!-- PELICAN_END_SUMMARY -->

[Btrfs
文件系统](https://en.wikipedia.org/wiki/Btrfs)的一大特性就是针对数据和元数据都会校验和，在这个过程由内核的
`xor` 模块提供支持。而目前 `xor`
具备自动选择最快方式的功能，若是系统 CPU 支持 AVX
扩展指令集的话，则会大大提高 Btrfs
文件系统执行校验和操作的效率。从另一个角度说，沉睡的 AVX
指令集终于有了一个无需特定编译又能在日常使用中发挥用途的机会了。

`xor` 会作为依赖随着 `btrfs`模块的加载引入，这时在 `dmesg`
输出中可以看到类似下面的内容：

>xor: automatically using best checksumming function:  
> avx : 4736.000 MB/sec

作为参考，列出我手头几个设备的 `xor` 输出信息：

* A10-5800K: AVX : 4748.000 MB/sec  
* Athlon 5350: AVX: 6128.000 MB/sec  
* A6-6310: AVX: 5912.000 MB/sec

从上面的列表来看，较新的处理器 AVX 性能都比较好。所以若是打算用爽 Btrfs
文件系统，似乎选择一颗 AVX 性能强劲的 CPU 时较为明智的。

不过这也仅是理论上，尚未作文件系统性能测试，**仅供参考**。
