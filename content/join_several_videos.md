Title: 如何合并几个视频片段
Date: 2006-09-01 22:15
Author: toy
Category: Tutorials
Slug: join_several_videos

有时候我们从网上下载的视频为多个片段，在观看时多有不便。如果能够将它们合并到一起，不仅利于我们播放，而且方便我们收藏，何乐而不为呢？使用
Mencoder 将能够满足上述需要。你仅需如下指令：

`mencoder -oac copy -ovc copy -idx -o output.avi video1.avi video2.avi video3.avi`

-   其中，-oac copy 选项告诉 mencoder 要正确拷贝音频流。而 -ovc copy
    选项则是拷贝视频流。
-   如果在视频文件中没有找到索引的话，那么 -idx 选项会要求 mencoder
    建立它。
-   -o 选项指定输出文件的名称。
-   最后几个参数为需要合并的几个视频片段。

怎么样，很简单吧。

（Via
[MisterHowTo](http://www.misterhowto.com/index.php?category=Computers&subcategory=Video&article=join_with_mencoder),
thanks!）
