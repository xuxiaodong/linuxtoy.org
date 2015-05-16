Title: Nautilus Mod! 给 Nautilus 再换新面孔
Date: 2010-04-11 10:58
Author: toy
Category: Tutorials
Tags: FM, Nautilus
Slug: nautilus-mod

{ 撰文/[Yunkwan](http://yunkwan.wordpress.com) }

这次 Nautilus Mod 不再单单是个主题。文字太抽象了！ 先上图！

[![Nautilus](http://i.linuxtoy.org/images/2010/04/thumb-nautilus.jpg)](http://i.linuxtoy.org/images/2010/04/nautilus.jpg)

再上一个原版的 Nautilus 对比。

[![Nautilus](http://i.linuxtoy.org/images/2010/04/thumb-lighttheme.png)](http://i.linuxtoy.org/images/2010/04/lighttheme.png)

变动不是太大，但是减少了不必要的东西。一句话： Less is more，but still
less。  
但是 split mode 会有 bug，不过不会 crash，所以放心：

[![Nautilus](http://i.linuxtoy.org/images/2010/04/thumb-nautilusmodsplit.png)](http://i.linuxtoy.org/images/2010/04/nautilusmodsplit.png)

就是 location bar 一高一低… 当然，要正常使用 Nautilus Mod
几个条件是必备的：

1. 适合的主题一个(暂时只有两个)  
2. GNOME 2.30 (Ubuntu Karmic 上很可能不行！！)  
3. 掌握基本的手动编译能力。(其实，门槛很低，只要会复制粘贴都可。)  
4. 一颗好奇的心(这个是重点，呵呵)

好啦！ 来吧！

安装依赖：

sudo apt-get install build-essential  
sudo apt-get build-dep nautilus

[下载 Nautilus
Mod](http://docs.google.com/leaf?id=0B6DKpoTQFXuHMTNhMmJhM2UtNjdjZS00MDNiLWI2NTAtMmUyNjQ1NDViODI2&hl=en)，然后解压，切换到解压后的目录下。

编译：

./configure –prefix=/usr  
make  
sudo make install

重启 Nautilus：

nautilus -q (普通用户权限即可)

换支持 Nautilus Mod 的主题：

暂时有两个：  

[Osliner-Mod](http://gnome-look.org/content/show.php/Osliner-mod?content=122990)，[Elementary-Mod](http://gnome-look.org/content/show.php/Elementary-mod?content=119715)。

Osliner-Mod 就是之前和我介绍过的  

[RadienceOsliner](http://yunkwan.wordpress.com/2010/03/27/%e4%b8%bb%e9%a2%98%e6%8e%a8%e8%8d%90-radienceosliner/)
的改版。  
至于 Elementary-Mod 就不用多说，大家都认识。

Nautilus 设置：

我看 GNOMe-Look 的截图用 width 400 是可以的，但是我这边用 400
会无法显示那个切换 View Moded 的 box，必须把 width 设置为 300 才行。

P.S： 字体是 [Luxi
Sans](http://yunkwan.wordpress.com/2009/12/11/luxi/)，可以看我之前介绍
Luxi Sans 的文章。(Ubuntu 下安装 ttf-xfree86-nonfree 这个包就能装上)  
P.S.2： 建议换上新的 Elementary Icon 2.4 版

{
[Source](http://yunkwan.wordpress.com/2010/04/10/nautilus-mod-给nautilus再换新面孔/).
Thanks Yunkwan. }
