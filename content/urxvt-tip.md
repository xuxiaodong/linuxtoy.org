Title: URxvt 技巧一则
Date: 2009-08-27 09:39
Author: vern
Category: Tips
Tags: Urxvt
Slug: urxvt-tip

你在编译一个程序，结果某个未知错误导致编译失败。这时你希望把错误信息复制并粘贴  

到网页浏览器中。碰到这种情况，基本上都是用鼠标选择错误信息，然后切换到浏览器用  
中键粘贴。

这个技巧就是教你省略鼠标只靠键盘完成上述动作。操作很简单，但是我想大多数人都没  
留意。在 make 命令执行结束，你看到 error/failed  
等关键字的时候，按下 M-s，输入  
error/failed 等错误关键字，Up/Down  
用于检索关键字位置，通过正则表达式匹配你感  
兴趣的错误信息，然后按下  
Shift-Enter，此时高亮显示的字符串就被复制下来了。

剩下的交给 Shift-Insert 粘贴就可以了。

参考: man urxvtperl

while "Enter" or "Return" stay at the current position and additionally
stores  
the first match in the current line into the primary selection if the
"Shift"  
modifier is active.
