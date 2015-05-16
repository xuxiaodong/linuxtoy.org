Title: Kimpanel 加入搜狗云输入法的讨论
Date: 2009-11-11 14:48
Author: toy
Category: News
Slug: kimpanel-and-sougou-cloud-ime

{ 撰文/linooxlee }

KDECN 的 Mail List 里对给 KDE 4 的 Kimpanel  
加入搜狗云输入法进行了讨论。

搜狗云输入法的接口简单：

API：

比方说

返回


    ime_query_res="%E6%B5%8B%E8%AF%95%EF%BC%9A5%09+
    %E4%BE%A7%E5%AE%A4%EF%BC%9A5%09+
    %E4%BE%A7%E8%A7%86%EF%BC%9A5%09+
    %E7%AD%96%E5%A3%AB%EF%BC%9A5%09+
    %E6%B5%8B%E6%97%B6%EF%BC%9A5%09+
    %E4%BE%A7%E8%9A%80%EF%BC%9A5%09+
    %E5%86%8C%E8%B0%A5%EF%BC%9A5%09+
    %E7%AD%96%E7%AD%AE%EF%BC%9A5%09+
    %E7%AD%96%E4%B8%96%EF%BC%9A5%09+
    %E6%B5%8B%EF%BC%9A2%09+
    %E5%86%8C%EF%BC%9A2%09+
    %E4%BE%A7%EF%BC%9A2%09+
    %E7%AD%96%EF%BC%9A2%09+
    %E5%8E%95%EF%BC%9A2%09+
    %E6%81%BB%EF%BC%9A2%09+
    %E5%A4%A8%EF%BC%9A2%09+
    %E6%86%A1%EF%BC%9A2%09+
    %E5%8E%A0%EF%BC%9A2%09+
    %E8%8D%9D%EF%BC%9A2%09+
    %E7%AE%A3%EF%BC%9A2";ime_query_key="ceshi";

URL 解码后就是关于拼音"ceshi"的 20
个候选字符。它的模式很简单，用搜狗云输入法和用 Google
搜索道理是完全一样的--你发个字符串给服务器，服务器返回若干查询数据，因此应用软件使用搜狗云输入法在版权上没问题的。

但是 Kimpanel 毕竟只是图形显示的前端，没有和  
Xserver 通信模块，要和 Xserver 通信相当于写一个 iBus
之类的引擎了，因此还不如就借助 iBus（个人觉得 SCIM 太依赖 GTK 了，iBus
稍好一点但对 KDE 也不太友好，希望能把 Kimpanel 改造成 KDE
独立输入法--我是 KDE 饭)。

其实已经有人为以 iBus 为基础做了一个搜狗云输入法：

这还有两段录像：

*  
*
