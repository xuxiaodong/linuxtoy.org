Title: PyFetion 0.2 发布
Date: 2009-12-13 18:41
Author: toy
Category: News
Tags: fetion
Slug: pyfetion-02-released

{
撰文/[cocobear](http://cocobear.info/blog/2009/12/12/pyfetion-02-release)
}

[PyFetion](http://code.google.com/p/pytool/) 0.2
版本已经发布，协议根据移动 09.11.04 的飞信版本 Fetion 2008 3.5.2  
(安全加强版)。

更新内容包含：

-   增加查看飞信好友是否隐身功能
-   增加登录时状态的选择[隐身 在线 忙碌 离开]
-   日志改用 Python 的 logging 模块
-   增加对好友状态改变的处理 (如上线等)
-   重写 TCP 方式中的底层通信函数
-   使用对列保存接收到的多余消息 (例如发短信时本来应该返回 200 OK
    却先来了个BN通知消息，以前这样会出错，现在底层会把 BN
    消息放在队列中，返回 200  
    OK)
-   修改了一些异常处理方式
-   增加登出，删除好友函数
-   改写 get\_contactlist 函数，使用一个 dict 保存当前的好友列表
-   增加一个 receive 函数
    做客户端的时候可以在一个线程中主调用该函数，所有的消息都会 yield
    出来 (请参考 fetion.py)
-   修正向 PC 发送消息的命令，飞信新增加了一个 CatMsg 的命令
-   增加接收从最新版本 PC
    端发送的消息功能;这个比较麻烦新版本飞信对每一个新会话使用 fork
    出一个线程的方式;
-   许多清理了修正
-   调整类的结构
-   改用 MIT License
-   增加了一个 CLI 的飞信客户端 跨平台支持
-   Fedora 8 Python 2.5.1 测试;Windowx XP Python 2.6.4测试;Win7 Python
    2.6.2测试;Mac 10.5.7 Python 2.5.1
-   我忘记在这里列出来的

<!-- -->

    ./fetion.py
    ------------------------基于 PyFetion 的一个 CLI 飞信客户端-------------------------

    命令不区分大小写中括号里为命令的缩写

    help[?]           显示本帮助信息
    ls[l]             列出好友列表
    status[st]        改变飞信状态 参数[0隐身 1离开 2忙碌 3在线] 参数为空显示自己的状态
    msg[m]            发送消息 参数为序号或手机号 使用quit退出
    sms[s]            发送短信 参数为序号或手机号 使用quit退出 参数为空给自己发短信
    find[f]           查看好友是否隐身 参数为序号或手机号
    add[a]            添加好友 参数为手机号或飞信号
    del[d]            删除好友 参数为手机号或飞信号
    cls[c]            清屏
    quit[q]           退出对话状态
    exit[x]           退出飞信

fetion.py 特色:

-   多线程支持，同时收发消息
-   添加，删除，好友，判断好友是否隐身功能
-   占用资源少，我正写这博客的时候官方的飞信占我 96.8M 的内存
-   跨平台支持
-   扩展性好，加两行代码就可以实现从手机发命令关机等功能
-   其它我没发现的

{ Thanks cocobear. }
