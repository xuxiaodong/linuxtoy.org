Title: emacs 新手必看: undo-tree
Date: 2011-10-25 21:54
Author: Kardinal
Category: News
Slug: emacs-undo-tree

火星人都知道，emacs 只有 undo ，没有 redo ……或者说它有
redo，但是相当的诡异，套用一句经典台词就是: 猥琐，非常的猥琐

简单的说，emacs 的 redo 就是 undo undo ，也就是传说中的负负得正。

可能有些 emacs 新手，还不知道怎么去操作，因为一般情况下，无论你 undo
多少次，都不会发生 redo 的现象。

这是因为 emacs
把相同类型的操作，合并为一个事件。比如说往缓冲区里打字，也就是
self-insert-command，如果每次 undo
，只是撤消掉一个字符，那就太僵硬了，所以 self-insert-command
的操作，每20次合并为一个事件，一次 undo ，撤消掉20个字符。

而 undo 的猥琐之处在于，只要连续的 undo
，无论多少个，都是一个事件……当然，这也是必需的，不然你 undo
了20次之后，又突然开始 redo ……而恰巧这时又是夜深人静的话……

undo 之后想要 redo
，就要进行一个其它类型的操作，随便输入一个字符或者移动一下光标都可以，不过标准答案是
C-g 。

这种模式有其强大之处，比如普通的编辑器中，输入 a ，undo，再输入 b
，然后无论你如何 undo redo，都不可能把 a 再召唤回来，因为它不保存上一次
undo 的状态。以下是普通编辑器中的  
s1,s2,s3,s4,undo,undo,s5,s6,s7,s8,s9,undo,undo,undo,undo,undo,s10……  
最后保留的状态是 s1 , s2 , s10  

    s1--s2--s10
         |
         +s3--s4
         |
         +s5--s6--s7--s8--s9

  
好了，下面是 emacs
中同样的操作，所有的状态都可以保留，只不过中间的步骤可能有点多……  

    s1--s2--s3--s4
                  )
        s3  u3--u4
       / | (
      |   \ s5--s6--s7--s8--s9
      |    \                  )
      |     u5--u6--u7--u8--u9
       \ 
        s10----sn

  
假设 u3 表示 undo s3 。从 s9 开始 undo，顺着 emacs
的“undo蛇”往回走，到了 u3 的时候，就是 undo undo s3，也就是 s3
了，而这一串 undo，也成了“undo贪吃蛇”的一部分。虽然 emacs
保留了全部的操作状态，但是从 s10 返回 s1
却要将近20步，而普通的编辑器只要两步。

这个必需得动手实验后才能有一个直观的印象，按以下步骤操作: (g C-g) (u
undo)

1g2g3g4guu5g6g7g8g9guuuuuu10(可以把end-of-line绑到空格代替C-g)

其实这种“undo蛇”完全可以表示成 undo tree。s10 到 s1 ，两步;再到
s4，四步(有一步是切换分支)……  

              s10----sn
             /
    s1--s2--s3--s4
               
             s5--s6--s7--s8--s9

  
不知道 emacs
为什么没有使用这种方式，可能是因为选择分支之类的操作很难描述吧。

好了，不提这么伤感的事，现在有一个扩展叫作 undo-tree
，基本解决了这个问题。  

[undo-tree](http://www.dr-qubit.org/download.php?file=undo-tree/undo-tree.el)  
安装使用都很简单:  

    ;放到load-path中，配置文件中添加
    (require 'undo-tree)
    (global-undo-tree-mode)

  
由于篇幅所限，就不截图了

C-x u 进入 undo-tree-visualizer-mode , p n 上下移动，在分支之前 b f
左右切换，t 显示时间戳，选定需要的状态后， q
退出。这是主要的操作，其它的自己摸索好了……
