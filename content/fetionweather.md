Title: FetionWeather: 利用 Crontab+Libfetion 预报天气
Date: 2009-04-27 17:31
Author: toy
Category: Apps
Tags: fetion, LibFetion
Slug: fetionweather

[QReadBook](http://linuxtoy.org/archives/qreadbook.html) 和
[ZhuaShuShell](http://linuxtoy.org/archives/zhuashu-shell.html) 的作者
[fangvv](http://sites.google.com/site/fangvv) 今天给我们发来了他的新作
FetionWeather── 使用 Libfetion
发送天气预报到自己和飞信好友的移动手机上。

**要求**

Linux 机器，crontab，g++，[Libfetion
0.9.2](http://linuxtoy.org/archives/linux-libfetion-092-released.html)，Bash
Shell，有效的飞信帐号，网络连接

**步骤**

1. 在系统中创建 fetion 目录，假设前面的路径为 PATHTOFETION。  
2. 下载 linux\\\_fetion\_0.9.2.tar.gz 到 fetion 目录。  
3. 使用 tar 解压 linux\\\_fetion\_0.9.2.tar.gz 压缩包。  
4. 提取 FetionWeather.zip 中的 weather.cpp 和 getweather 到 fetion
目录。  
5. 注意修改 weather.cpp 中的 CHANGE\\\_THIS\\\_WITH\_FETIONID
为你要发送的好友的数字 id，必须已经是飞信好友。  
6. 注意修改 Shell 脚本 getweather 中的预报 URL：可以从 查找你所在的城市
24 小时天气预报 URL。  
7. 编译：`g++ weather.cpp linux\_fetion\_0.9.2/lib/libfetion\_32.a -o
weather -I"linux\_fetion\_0.9.2/" -lcurl -pthread`  
8. 修改 getweather 运行权限 `chmod 755 getweather`  
9. 在 fetion 目录下测试一下运行情况:

./weather YOURID YOURPASSWORD "`./getweather`"

10. 可以正常接收预报短信后，加入到 Crontab:

0 19 * * * /PATHTOFETION/fetion/weather YOURID YOURPASSWORD
"`/PATHTOFETION/fetion/getweather`"

(每晚 19 点时发送天气预报，因数据源 wap.weather.com.cn 每天 18：00
之后给出第二天天气预报，因此请该时刻之后再发送天气短信)

**说明**

主要短信发送函数为 fs\\\_send\\\_sms 和
fs\\\_send\\\_sms\\\_to\\\_self。0.9.3 版本的 libfetion
因使用起来有问题，因而现在我选择使用的是
0.9.2。自己用的小程序，注重功能，代码简陋，可以根据您的需要自己修改使用。该程序亦可用来循环发送垃圾内容给飞信好友，本人对此引发的后果概不负责。

[下载 FetionWeather](http://i.linuxtoy.org/files/FetionWeather.zip)
