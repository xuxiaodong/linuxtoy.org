Title: biabiamiamia
Date: 2013-03-01 09:39
Author: lovenemesis
Category: Funny
Tags: Bash
Slug: biabiamiamia

拥有如此个性名称的脚本是 *yangyang.gnu*
编写的一个[百度音乐网](http://music.baidu.com/)的歌曲下载辅助工具。*3 月
5 日更新版本* *感谢作者 *yangyang.gnu* 来稿*

biabiamiamia 具有如下命令行参数：

-   `--artist`，指定歌手名；
-   `--album`，指定专辑名（默认该歌手 所有专辑）；
-   `--quality`，指定下载歌曲的品质 （320、192、128，默认320kbps）；
-   `--version`，显示版本信息；
-   `--help`，显示本帮助信息。

任何BUG，请告知 `yangyang.gnu AT gmail.com`。

【用例】

-   下载羽泉的所有专辑，歌曲选用 192kbps 码率品质:
    `biabiamiamia --artist="羽泉" –quality=192`
-   下载伍佰的《浪人情歌》专辑，歌曲选用最高码率品质:`biabiamiamia --artist="伍佰" --album="世界第一等"`

【效果】  
下载界面

[![](http://lt-file.b0.upaiyun.com/files/2013/03/biabiamiamia-1-300x186.png "biabiamiamia-1")](http://lt-file.b0.upaiyun.com/files/2013/03/biabiamiamia-1.png)

百度为防机器人，下载过程中可能出现验证码，按界面提示查看并输入验证码即可继续下载。

[![](http://lt-file.b0.upaiyun.com/files/2013/03/biabiamiamia-2-300x79.png "biabiamiamia-2")](http://lt-file.b0.upaiyun.com/files/2013/03/biabiamiamia-2.png)

【下载】  
<http://code.google.com/p/yangyanggnu/downloads/list>

【安装】  
构建系统采用 `cmake`，需要自行提前安装。源码安装步骤如下：

`tar -xv -f biabiamiamia.tar.gz -C .`

`cd biabiamiamia/`

`cmake .`

`make && make install`

【后续】  
考虑借助开源OCR库，自动识别验证码。

【注意】

1.  biabiamiamia内部调用curl进行下载操作，请自行提前安装；
2.  默认下载路径：

        ~/biabiamiamia_music

【V0.1.20130305】

1.  『优化』指定平均下载速度下限为8kbps，低于此自动重新连接，最多重连4次；
2.  『优化』资源不存在时会出现503错误页面，忽略503页面而不再将其当作资源下载；
3.  『优化』为减少出现验证码的几率，下载时伪装成firefox且增加页面引用；
4.  『优化』对于导致下载失败的不同原因进行区别：因网络质量导致下载失败（处理机制，重新下载）、因出现验证码导致下载失败（处理机制，获取BAIDUVERIFY的cookie键值后重新下载）；
5.  『优化』修正部分歌曲名中含有“/”的歌曲无法下载的问题（thanks to Iven
    Hsu）；
6.  『新增』命令行参数错误时，显示帮助信息；
7.  『新增』下载暂停/恢复功能。ctrl+c退出程序，下次若下载先前歌手的所有专辑（指定专辑无效）时，自动从中断歌曲续下；

