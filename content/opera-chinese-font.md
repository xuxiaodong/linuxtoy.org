Title: 解决英文环境 Opera 中文字体问题
Date: 2009-10-18 09:12
Author: Yunkwan
Category: Tips
Tags: Opera
Slug: opera-chinese-font

{ 撰文/[Yunkwan](http://kwanlife.yo2.cn) }

这是我遇到的问题，具体情况  

[ClickHere](http://forum.ubuntu.org.cn/viewtopic.php?f=73&t=232306)，看看截图。这问题缠绕我几天了~  
今天 @Thruth 在 Gtalk 技术支持~ 终于解决问题~

**解决方法:**

修改 /usr/share/opera/defaults/font.ini

找到 `; Chinese fonts` 这项，然后把字体改为你要的中文字体。

family:WenQuanYi Micro Hei=chinese-s excellent try-first  
 (只需要修改这个)

下面这两行都在开头，加 ";" 来注释掉

;family:WenQuanYi Zen Hei=chinese-s verygood try-first  
;family:文鼎ＰＬ简报宋|AR PL UMing*|AR PL SungtiL GB=chinese-s good
try-first

然后，还有一件必需要做的事!!!就是把下面的日文、韩文都用" ; "注释掉。

;Japanese fonts  
;family:IPA*=japanese excellent try-first  
;family:kochi*=japanese good try-first  
;family:VL*=japanese verygood try-first  
;Korean fonts  
;family:baekmuk gulim|undotum=korean sans-serif excellent try-first  
;family:baekmuk batang|unbatang=korean serif verygood  
;family:baekmuk dotum=korean sans-serif good  
;family:ungungseo|unshinmun=korean serif good  
;family:baekmuk*|un*=korean

然后，保存，重启 Opera 就可以了。

**现象的原因:**

Opera 把中文用韩日字体显示出来，那么字体当然会怪怪的喇~ Opera  
本身的缺憾是分不出中日韩字体，所以，如果没有注释掉韩日字体，  
即便你设置好了中文字体，字体奇怪的问题也会照样出现。

我 Google 了一下，没有什么人在 Opera 9
以后，遇到中文字体的问题，是因为，Opera  
默认是能够使用系统的中文字体。

但为什么我却会遇到这个问题呢? 原因说不清，但可能性有以下几个:

1. 英文环境

2. 系统默认字体使用英文字体。

3. 系统默认字体为 Sans，然后，通过 ~/.fonts.conf
来调配字体使用的优先级~  
首选是纯英文字体，次选才是中文字体

再次感谢 @Thruth。

{ [Source](http://kwanlife.yo2.cn/articles/operachinesefont.html).
Thanks  
Yunkwan. }
