Title: Supertux 修改存档的方法
Date: 2010-10-14 21:38
Author: lovenemesis
Category: Games
Tags: SuperTux
Slug: supertux-saved-file-cheats

最近很无聊，装了supertux来玩，无奈 bonus
levels2第一关始终玩不过，就研究了下supertux的存档，那是相当简单，原来开源的游戏，修改起来那么简单。*感谢
squeeze 来稿！*

在用户目录下有个文件夹".supertux"打开后可以看到save，里面有三个文件：

1.  slot1.stsg //"start
    game"的存档，可以有5个存档，slot2.stsg,slot3.stsg...
2.  bonusisland1.stsg //"bonus levels"中"bonus island1"的存档，仅一个
3.  bonusisland2.stsg //"bonus levels"中"bonus island2"的存档，仅一个

**基本格式**

    (supertux-savegame
      (version 1)
      (title  "Icyisland - 28/32")   #存档标题,改不改无所谓，正常的是28/32表示有32关，存档在28关
      (lives   5)      #企鹅的数量，玩不过？改300试试。
      (score   17820)  #成绩
      (distros 74)     #金币数
      (tux (x 50) (y 33)  #企鹅所在的位置，坐标
           (back "west")   #不清楚
           (bonus "iceflower"))  #不清楚
      (levels            #这里是已经过关的记载
         (level (name "bonus2/level1.stl")  #过关的名字，我在/usr/share/games/supertux/levels/worldmaps里查找出来的，
                                                            #其中bonus1的比较特殊，数字开头的字母不同，呵呵
                (solved #t))   #过关标志，如果没这个，有上面的名字，运行游戏会退出
         ...
         (level (name "bonus2/level28.stl")  #同上，bonus2里面的比较简单，从1-28.
                (solved #t))   #同上
       )
     )

    ;; EOF ;;

下面介绍下/usr/share/games/supertux/levels/worldmaps的文件，这个是具体每关的坐标，名字  
world1.stwm "start game" 地图坐标，名称  
bonusisland1.stwm "bonus levels"中"bonus island1"地图坐标，名称  
bonusisland2stwm "bonus levels"中"bonus island2"地图坐标，名称

文件格式

    ;; Generated with Flexlay Editor
    (supertux-worldmap
      (properties
        (name  "Bonus Island I")  #名字
        (start_pos_x 35)          #开始时企鹅的坐标
        (start_pos_y 2))          #开始时企鹅的坐标
      (tilemap
        (width  70)              #地图总宽带
        (height 50)              #地图总高带
        (data   #下面很多9 啥的数字省略
        ...
    (levels
         (level (name "bonus1/bonus-level1.stl")  #每个小关的名字，对应存档里的
               (x 35)                         #坐标，如果你想要跳过某关就直接输入这个到你的存档
                (y 4))                        #同上
         (level (name "bonus1/bonus-level2.stl")
               (x 32)
                (y 41))   
         (level (name "bonus1/bonus-level3.stl")
               (x 30)
                (y 39))
         (level (name "bonus1/bonus-level4.stl")
                  (extro-filename "extro-bonus.txt")
               (x 32)
                (y 46))
         (level (name "bonus1/bonus-level5.stl")
               (x 44)
                (y 39))
         (level (name "bonus1/abednego-level1.stl")
               (x 12)
               (y 33))
        (level (name "bonus1/abednego-level2.stl")

对游戏过关修改就看这点够了，注意看上面的，**不是连续的**，这是bonus1的不同处。
