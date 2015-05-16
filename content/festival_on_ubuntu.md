Title: Ubuntu 之玩转语音合成（Festival）
Date: 2007-01-21 22:34
Author: toy
Category: Tutorials
Slug: festival_on_ubuntu

也许已经有一部分人早就知道 Festival 这个语音合成软件，也就是所谓的 TTS
(text to speech)。不过网上相关的安装资料大同小异，基本上是在 Gentoo
上安装的心得。我发现 Ubuntu 只有 Festival，而没有相关的 speechd
软件。我经过一晚上的探索，终于可以把这个 Festival
玩转起来，而且有了一些比较好的效果，下面共享自己的经验出来。

1.  安装
    基本上 Ubuntu 的库里就有 Festival 软件。  
    `$sudo apt-get install festival`
2.  使用

    Festival 的基本用法：

    -   交互模式：
        直接输入 festival 进入它的命令行界面。  

        ` $festival festival 〉 (SayText ” hello , festival is coming “) festival 〉 (tts myfile)`  
        第二行是读取 myfile 文件里的内容。
    -   命令行模式：  
        `$festival –tts myfile`

        直接读取 myfile 里的内容。  
        `$ echo “hello , festival is coming ” | festival –tts`

        读取字符串。

3.  配置

    Festival 默认用的是 oss，在一些系统会独占音频。这里我们将配置成使用
    alsa 发音。

    新建文件 ~/.festivalrc ， 输入以下内容:  

    ` (Parameter.set ‘Audio_Command “aplay -q -c 1 -t raw -f s16 -r $SR $FILE”) (Parameter.set ‘Audio_Method ‘Audio_Command)`  
    如果想提高音量，可添加：  

    ` (set! default_after_synth_hooks (list (lambda (utt) (utt.wave.rescale utt 1.6 t))))`  
    至此 festival
    应该比较好的工作了。在集成声卡中会出现音速过快的问题。[LinuxSir](http://www.linuxsir.org/bbs/showthread.php?s=&threadid=89626)
    上有一篇关于 Festival 的帖子，其中 wguzgg
    网友曾经把网上的方法贴了出来。

    我找到了如何将语速恢复正常的方法，原文在[这里](http://www.cstr.ed.ac.uk/cgi-bin/lis…val/speed.html)。  
    主要是集成在主板上的声卡会出现语速过快的问题，解决方式是：

    在 /usr/lib/festival/ 目录下创建一个文件 siteinit.scm，内容如下：  

    ` (Parameter.set ‘Audio_Method ‘Audio_Command) (Parameter.set ‘Audio_Command “sox -t raw -sw -r $SR $FILE -c2 -t ossdsp /dev/dsp”)`  
    这个参数写在 ~/.festivalrc 上也是有效的。不过就和前面我设置用 alsa
    发音的设置冲突了。那个 alsa
    的设置好像也能把语速减慢一点吧。我这里提供方法。你自己看着选择了。

4.  安装新语音

    这部分才是我写此文章的重要目的。因为在 Gentoo
    的帖子，安装一个新的女声，只需要 emerge mbrola。而在 Ubuntu
    的库中并没有收录此包。（也许是我不知道，谁知道告诉我）另一个原因是，默认的美国男声似乎有些含糊不清。所以我找了
    mbrola 的女声来安装（注意，不得用于商业用途，他说的）。

    手动安装 festival mbrola
    的信息，原[网页](http://www.cstr.ed.ac.uk/projects/festival/mbrola.html)。

    -   安装 festival voice wrapper (这个咋翻译偶拿不准）
        下载 festvox\_us1.tar.gz，把它解压到 festival
        的安装目录下，Ubuntu 下为 /usr/share/festival。
    -   获取 MBROLA 声音文件和它的执行文件

        跳到 http://tcts.fpms.ac.be/synthesis/mbrola.html ，点击
        download，下载 MBROLA binary
        和你需要的声音文件。这里选择美国英语女声（for us1）。

        安装 MBROLA binary，这里你应该下载到一个名为 mbr301h.zip
        的文件。解压后把其中名为 mbrola-linux-i386 的文件改名为
        mbrola，再复制到 /usr/local/bin 目录中。

        安装声音文件，这里你下载到的声音文件的文件名应该类似
        us1-980512.zip，把它解压到  
        `[festival_install_dir]/festival/lib/voices/english/us1_mbrola`  
        [festival\_install\_dir]为 festival 的安装目录。在 Ubuntu
        下应为 /usr/share/festival。

5.  测试新的声音
    在执行完上面步骤后新的美国英语女声应该安装完毕。进入 festival
    命令行测试一下：  

    ` festival) (voice_us1_mbrola) festival) (SayText ” hello , american english female voice is coming”)`  
    在这里你应该听到优美的美国英语女声了吧。
6.  更换默认声音
    如果想把上面的女声变成默认的声音，请在 ~/.festivalrc 文件中添加：  
    ` (set! voice_default ‘voice_us1_mbrola)`  
    到这里比较完美了吧。
7.  其它玩法

    当然你会因为一时好奇而装它。不过过一会之后就会想它会有什么用呢？我这里提供自己的一些玩法。

    -   集成词典发音

        在我之前的 vim 技巧中有提到过 sdcv
        这个词典翻译软件。它是星际译王的命令行版本。自从有了它之后我就再也没有打开过星际译王了。因为有需要就直接
        sdcv “word”
        就行了。当然默认它是没有将单词的读音读出来的。星际译王也有个 100
        多 M
        的语音库，但那个库是一个单词一个文件。只能读库里有语音文件的单词。所以我们可以写个脚本，让
        sdcv 和 festival 绑定，这样学习英语来不是更形象嘛。  
        ` $cat dict #!/bin/sh`

        echo “$1 ” |festival –tts >/dev/null 2>&1 &  
        sdcv -n $1  
         
        使用 dict 代替 sdcv，查询的单词无论怎样都会有读音。爽吧！

    -   读中文
        你在开玩笑吧。是的，基本上是个玩笑。中文语音合成国内 863
        好象有项目。不过似乎没有给公共平台提供什么软件接口。这里你可以让
        festival
        读中文拼音，有外国人读中文的味道。（linuxsir上的网友发现的）  
        ` $echo “ni hao, huan yin lai dao linux” |festival –tts`
    -   读文章
        用它来读英文文章。但我想，对于我这程度，大概会把我逼疯。

当然如果你还有什么好的主意，欢迎告诉我。

后记：以上内容部分参考 Gengoo 里的
[HOWTO](http://gentoo-wiki.com/HOWTO_speechd)，对于转贴我很欢迎，但希望能保留原始出处。上面提到的下载
mbrola
文件的网站我用代理才能上。为免大家下载麻烦，我把下载的三个文件[打好包](http://www.51files.com/?UDANGFOEJAMOWSM)了。

（撰文／[lerosua](http://my.donews.com/lerosua/2007/01/21/festival_for_ubuntu/)）
