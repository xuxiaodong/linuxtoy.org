Title: 快速在 Tiling & Float WM 间切换
Date: 2011-08-24 00:00
Author: lovenemesis
Category: Tips
Tags: Musca, Pekwm, ratpoision
Slug: switching-between-tiling-and-float-wms

在两个 tiling 和 float WM之间自由切换，无须重启
WM，不丢失窗口。*感谢李存金来稿！*

tiling 和 float 两种管理方式都有各自适合的场景，平常我基本上在用
tiling(musca)，但是偶尔会要用到 GIMP 这样的程序， 这时候 tiling
的方式就不方便了。一直在寻找一个WM 能够在 tiling, float
两种方式之间自由切换，并且两种两种方式用起来都比较舒服。例如 musca
虽然能切换到 float 的方式，但是基本上处于半残状态，不具备可用性。

曾经还尝试用 fvwm 模拟 tiling
的管理方式，但不理想，毕竟不是原生的。偶然看到 ratpoision
支持临时调用其它的 WM，然后突发其想是否可用 ratpoision 作为 WM
的切换器，在 ratpoision WM 下自由切换不同的 WM。

想法有了，方案我也初步实现了，我选用的 tiling 是 musca，musca
我一直在用，float 选 pekwm 是由于他对 EWMH/NetWM 支持比较全面，在 musca
pekwm 之间切换时不会丢失窗口。

各位有什么好的其它方案可以提供参考吗？

**ratpoision启动文件**： `~/.ratpoisionrc`

    =====================================
    exec xdotool key 'Escape'
    # ratpoision启动时会弹出一个welcome窗口， 按Escape将其关闭
    exec ~/bin/three-wm

    # 自定义的脚本，负责在musca pekwm之间切换

    =========================================
    command="musca"
    #默认启动musca
    startxpid=$(ps -eo pid,cmd | grep "startx *-- *$(echo "$DISPLAY" | sed 's/.0$//')" | awk '{print $1}')
    #startxpid用于判断在musca pekwm ratpoision是否在同一个DISPLAY下

    if [[ "X$startxpid" == "X" ]];then
    #ratpoision第一次启动，还没有startx进程
       ratpoison -c 'tmpwm /usr/bin/musca'&
       exit 0
    else
       pstree -Apa $startxpid | grep -v "grep" | grep -q "ratpoison" || exit 1;
    #如果不处于ratpoison环境，就退出程序
    fi

    if  wmctrl -m | grep -q 'Name: musca';then
       command="pekwm"
    fi
    if ps aux | grep -v 'grep' | grep -q 'ratpoison -c';then
       ps aux | grep -v 'grep' | grep 'ratpoison -c' | awk '{print $2}' | xargs -I{} sudo kill -9 '{}'
    fi
    #杀死僵死的ratpoison -c
    case "$command" in
       musca)
           #杀死pekwm，在ratpoison下启动musca
           if pstree -Apa $startxpid | grep -v "grep" | grep -q "pekwm";then
               pstree -Apa $startxpid | grep -v "grep" | grep "pekwm" | cut -d',' -f2 | awk '{print $1}' | xargs -I{} sudo kill -9 '{}'
               ps aux | grep -v 'grep' | grep 'xfce4-panel' |  awk '{print $2}' | xargs -I{} sudo kill -9 '{}'
               notify-send -t 3000 'kill pekwm relative thing'
           else
               notify-send -t 3000 'no pekwm runing, run musca direct'
           fi
           ratpoison -c 'tmpwm /usr/bin/musca'&
           sleep 2s
           musca -c "pad 0 0 10 0"
           musca -c "hook on ^(add|use) pad 0 0 10 0"
           ;;
       pekwm)
           #杀死musca，在ratpoison下启动pekwm
           if ps aux | grep -v "grep" | grep -q "/usr/bin/musca";then
               pstree -Apa $startxpid | grep -v "grep" | grep "musca" | cut -d',' -f2 | awk '{print $1}' | xargs -I{} sudo kill -9 '{}'
               ps aux | grep -v 'grep' | grep 'dzen2' |  awk '{print $2}' | xargs -I{} sudo kill -9 '{}'
               notify-send -t 3000 'kill musca relative thing'
           else
               notify-send -t 3000 'no musca runing, run pekwm direct'
           fi
           ratpoison -c 'tmpwm /usr/bin/pekwm'&
           ;;
       *)
           ;;
    esac

**编者注：**偶不是 Tiling WM 使用者，所以还是麻烦了解的朋友尽情拍砖了。
