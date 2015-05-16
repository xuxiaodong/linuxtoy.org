Title: 让 Karmic 启动再快 5 秒
Date: 2009-11-03 17:00
Author: Yunkwan
Category: Tips
Tags: Karmic, Ubuntu 9.10
Slug: karmic-boot-up-reduce-5-sec

{ 撰文/[Yunkwan](http://kwanlife.yo2.cn) }

是真的! Karmic 开机已经很快了，可是还可以再快 5 秒!  
5 秒当然只是大约大部分人得到的结果~  
可能已经习惯了 Karmic 启动的快速吧~ 我自己就感觉不太明显~  
我升级前也忘记了先把启动时间记下~  

不过既然[原文](http://www.omgubuntu.co.uk/2009/10/get-dramatically-faster-boot-times-in.html)的评论这么多人都得到了
5 秒的结果，也不会假吧~

好吧~ 方法就是加入一个 ppa 源，然后更换内核~

请注意哦~ 我不保证这一内核能在你的电脑上稳定使用哦~
系统挂掉了可不要找我算账哦~  
我是一个负责人的人

这毕竟有风险哦~ 如果你是很新手或不想折腾的话~ 还是劝告你不要尝试了~  
因为就提升那一点启动速度，对你实际使用没有太明显，毕竟 5
秒，喝口水，白日梦还没法完就过去了~  
况且，用电脑也不是整天重启的啊~

Step1:

sudo add-apt-repository ppa:ubuntu-boot/ppa

或者

ppa:ubuntu-boot/ppa

Step2:

sudo apt-get update && sudo apt-get dist-upgrade

完成后重启，据说第一次启动是感觉不出的~ 可能是因为要 readahead 需要
profile 一下吧~  
不过，如果真是 profile 的话，貌似时间和以前 9.04 相比，耗时也太短了~  
了解真相的朋友请相告知哦~

Hope you guys enjoy it!!

{
[Source](http://kwanlife.yo2.cn/articles/karmic-boot-up-reduce-5sec.html).
Thanks Yunkwan. }
