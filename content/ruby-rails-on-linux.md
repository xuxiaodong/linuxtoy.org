Title: 一个 Ruby Rails 程序员在 Linux 下的工作环境
Date: 2008-08-24 13:43
Author: toy
Category: Development
Tags: Rails, Ruby
Slug: ruby-rails-on-linux

[撰文/地藏]

我是一个程序员，我希望我的 PC 工作环境易用，稳定，简洁，高效，个性化。从
Windows -> Debian -> Ubuntu -> Xubuntu -> Fluxbox -> Awesome
我想我走过了一个漫长的道路。目前我使用 Ubuntu 系统，Awesome
窗口管理器，它们基本满足了我的需求，所以我想现在应该是和大家一起来分享一点经验的时候了。

不用 Windows 的理由很简单，在 Linux
系统上感觉更自由，学习提高自己的编程水平更容易，而且基本不会有重装系统这种烦心的事情。选择
Ubuntu 的理由，它很易用，而且保持稳定，比较其他我用过的发行版本，Debian
易用性和稳定性稍差（stable 老了点，testing
稳定差了点，unstable？那你就等着折腾吧），Arch
易用性更差（当然很多人喜欢它的简洁，快速，方便学习 Linux
系统底层机制和应用包的快速更新。但这些对我来讲不是那么重要，我不是 Linux
玩家，也不是 Linux 系统管理员，而只是一个 Web developer）为什么不用
Xubuntu？恩，Xubuntu 是比 Ubuntu 快，但是用了 Awesome
基本一样快了，而且我很多常用的应用也都基于 Gnome，所以就没那个必要了。

然后，我说的个性化不是界面上弄些漂亮的图片，或者换个很 cool
的主题，它们对泡妞也许很重要，但对工作没有什么帮助的。我所指的是使用方法上的可定制性，每个人都有自己的习惯，思考方式，解决问题的方法。因此适合我的未必适合你，这就需要有足够的灵活。

好了，基本我选择的理由就是上面的了。在发行版本的选择上，我想每个人都有各自的需求和个人特点，从中找到一个平衡点是非常重要的。所以我写这些也就是提供一点借鉴。

[Awesome](http://linuxtoy.org/archives/awesome.html) 在 LinuxTOY
上已经有文章介绍过了，我也是看了那篇文章才开始用它的，感谢那篇文章的作者。

其他我日常开发工作使用的软件基本就下面这些：

**Vim**

Vim 开发 Rails 很方便，不太习惯现在 Eclipse、Netbeans 那些大而全的
IDE，它们有很多的优点值得借鉴，不过基本而言它们的启动速度都比较慢，运行后的反应速度也慢。下面是一些我用的
plugin：

-   bufexplorer.vim - buffer 切换，console 下面常用
-   lookupfile.vim - 找文件，很不错
-   matchit.vim - 匹配成对的语句或符号，很有用
-   mru.vim - 最常用文件列表，经常用
-   NERD\_commenter.vim - 快捷来加删 comment，不错
-   project.vim - 基本我没用
-   rails.vim - 开发 Rails
    需要，但大部分好像我都不怎么用，恩，应该再看看它的帮助
-   SimpleFold.vim - 它的折叠方法和 Vim
    里面自带的那个语法文件不太一样，我个人觉得不错
-   snippetsEmu.vim - 缩写代码自动生成，很不错，好用，但是自带的
    Rails，Html 的少了点，需要自己再补充一些
-   supertab.vim - 好用，常用
-   surround.vim - 好用，常用
-   taglist.vim - 不怎么用
-   tailminusf.vim - 不怎么用

**Xterm 或 Urxvt + Screen**

Screen 是个好东西，通常我写一个 config 文件放在正在开发的 Rails
应用的目录下，然后 screen -c xxx.config  

` chdir some_workspace defutf8 on screen  -t server 0 select 0 exec ruby script/server -u --debug screen  -t console 1 exec ruby script/console screen  -t log 2 exec tail -f log/development.log screen  -t fastri 3 exec fastri-server fastri-server screen  -t mysql 4 exec mysql mysql -uname -ppassword screen  -t terminal`

**loop\_qri.sh**

我自己写的一个简单的 Bash 脚本，基于 fastri，用来查 Ruby Rails
以及其他所有 gem package 里面包的 api 方法帮助的小工具。


    #! /bin/bash
    function select_method()
    {
                   select method in ${keywords}
           do
                   if [[ "$REPLY" =~ ^[1-9][0-9]* ]]
                   then
                           history -s "$method"
                           history -w ~/.loop_qri_history
                           echo
    "============================================================================================="
                           qri ${method}
                           echo
    "============================================================================================="
                     have_select=1
                           break
                   else
                           keywords="$REPLY"
                     have_select=0
                           break
                   fi
             done

    }

    history -r ~/.loop_qri_history
    read -e  -p "Please input some keywords of method:" keywords
    have_select=0
    while true
    do
            case "$keywords" in
                                   -stop)
                                                   break
                                                   ;;
                                   -history)
                                                   history
                                                   ;;
                                   *)
                                                   COLUMNS=20
                                                   PS3="Choice a method or input other keywords: "
                                                   if [ $have_select -eq 0 ]
                                                   then
                                                                   match_result=`qri ${keywords}`
                                             fi
                                                   if [[ "$match_result" =~  "Multiple choices" ]]
                                                   then
                                                           keywords=`echo  "$match_result" | sed /--/d  | sed '/,/ s/,/ /g'`
                                                           echo
    "============================================================================================="
                                                           select_method
                                                   else
                                                           echo
    "============================================================================================="
                                                     qri ${keywords}
                                                           history -s "$keywords"
                                                           history -w ~/.loop_qri_history
                                                     have_select=0
                                                           read -e  -p "Please input some keywords of method:" keywords
                                                   fi
                   esac
    done

**Firefox + Firebug**

Firefox 是个好东西，就是感觉它没有 Opera 快，尤其是打开很多 tab
以后不但慢而且不稳定，所以就只用它和 Firebug 来调试网页了。

**Opera**

速度很快，即使打开了很多 tab 也是如此。虽然经常因为 Flash
的插件而失去反应，但还是可以接受。

**Pidgin**

MSN、QQ 都能用了，文字信息交流基本就够我用了。

**Git**

很好用的版本控制软件，我推荐到的
LinuxTOY，请[参考以前的文章](http://linuxtoy.org/archives/git.html)。

**Xmodmap**

我的用法很简单，只是用来把 capslock 和 ctrl
互换个位置。下面是切换这两个键的 xmodmap 配置文件。  

` ! Switch caps lock and left control remove Lock = Caps_Lock remove Control = Control_L keysym Control_L = Caps_Lock keysym Caps_Lock = Control_L add Lock = Caps_Lock add Control = Control_L`

**Awesome**

它的使用方法原来文章已经说的很详细了，不行看它的 Wiki
也行：<http://awesome.naquadah.org/wiki/index.php?title=Main_Page>

下面介绍一点我自己的小窍门。我每天的日常工作要用的软件无非就那么几个，而且我习惯把这些程序放在固定的
viewtag 上，比如 Gvim 和 xterm 在 tagview 1，而 Firefox 和 Gvim 在
tagview 2。但是每天都要逐个启动这些程序把他们放到那些不同的 view
下面是一件非常无聊的事情。所以我找了一个办法来自动完成这些工作。

下面的程序需要你有 Ruby 解析器，你可以：  

` sudo apt-get install ruby1.8 sudo apt-get install rubygems sudo gem install awesomer`

然后仿照下面的代码写一个你自己的程序启动器。


    require 'rubygems'
    require 'awesomer'

    `xmodmap ~/.Xmodmap`
    #注意这里不是单引号，而是 tab 上面那个键
    Awesomer.contact do |a|
       a.tag_view 1

       a.spawn :xterm
       sleep 3
                   a.client_toggletag 3
                   a.client_toggletag 4

       a.spawn :gvim
       sleep 3
                   a.client_toggletag 2
                   a.client_toggletag 5

       a.tag_view 2

       a.spawn :firefox
       sleep 16
                   a.client_toggletag 3
                   a.client_toggletag 6

       a.tag_view 9
       a.spawn :opera
       sleep 20

       a.tag_view 5

     end

