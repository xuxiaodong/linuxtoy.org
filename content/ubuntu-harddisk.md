Title: Ubuntu中的Load/Unload Cycle Count问题及解决方案
Date: 2008-09-17 09:09
Author: toy
Category: Tips
Tags: Ubuntu
Slug: ubuntu-harddisk

[撰文/bread]

**说明：**请大家注意，本文所描述的问题只有笔记本电脑才会出现。

**1. 问题描述**

几周前收到soldiers童鞋的短信说，Ubuntu伤硬盘？我说没事，好多人都用呢。过了一周，soldiers童鞋又问，Ubuntu伤硬盘？我说我查查看....

# 安装smart参数查看工具，由此可以查看硬盘的smart信息  
`$ sudo apt-get install smartmontools`

# 查看/dev/sda这块硬盘的smart参数,
你可能需要把/dev/sda这部分修改成你的硬盘设备地址  
# grep 193是只查看 Load Cycle Count这项  

` $ sudo smartctl -a /dev/sda | grep 193 193 Load_Cycle_Count        0x0012   090   090   000    Old_age   Always       -       109989`

这样就可以看到Load/Unload Cycle
Count数目了。用Windows的童鞋可以借助Everest工具，查看存储器->SMART信息，也可以找到相应项的数据。

不看不知道，一看吓一跳，我的是华丽的11W!!! T.T
据说到了60W，就离挂掉不远了。我才用了4个月，算下来照这个速度用下去的话，只能用4*60/10/12=2年....
同寝的Acrest童鞋的也过了10W大关哈哈哈。

`$ while true; do sudo smartctl -a /dev/sda | grep 193; sleep 300; done; `

这样可以每隔5分钟查询一下LCC，一般来说每小时增长在15上下应该是正常的。这样的话即便你每天24小时开着本子，硬盘也可以坚持4年(当然是从理论上来讲)。

**1.1 这个Load/Unload Cycle Count到底是什么？**

Load/Unload Cycle
Count(以下简称为LCC)就是Load/Unload的次数，那么什么叫做Load/Unload呢，下面是一段非常罗嗦的解释，建议不感兴趣的同学出门右转，直接看下一节吧。

大家都知道，硬盘的数据传输是通过磁头读写磁盘上的数据来完成的。在工作过程中，磁头并不与磁盘的盘面直接接触，两者之间有一层很薄的空气薄膜，这层空气薄膜是由于磁盘的高速旋转产生的。如果磁盘停止旋转，空气薄膜消失，磁头则会直接接触到盘片，更详细一点说，会接触到盘片的landing
zone，或者叫做start/stop
zone，这无疑对盘片的寿命以及对存储在这块区域的数据造成不好的影响。因此在早期阶段，硬盘制造商一般会在对盘片的表面或landing
zone部分做特殊的处理，并尽量避免在landing zone存储数据。

但是随着人们对于硬盘传输速度和硬盘容量需求的不断增加，制造商需要不断提高硬盘的面密度，同时要求盘片表面尽可能地平滑，这无疑与之前采用的技术产生了冲突，再加上其他的一些因素，硬盘制造商迫切地需要一种新的方式来替代之前采用的磁头直接接触盘面的行为。这时IBM的工程师们提出了一种叫做Load/Unload的技术。简单来说，Load/Unload技术有点像老式的点唱机，当盘片转速降低无法再产生空气薄膜的时候，就将磁臂以及磁头旋转一下，停靠到磁盘旁边的一个小斜坡上。这样就完全避免了磁头与盘片的直接接触。

总体来说，Load/Unload技术是有利的，比如可以提高硬盘的可靠性：硬盘遭到撞击的时候磁头不会划伤盘面；可以提高硬盘的面密度：不再需要对盘片表面做特殊的处理，可以提供平滑的盘面；以及可以有效地降低功耗：低功耗的程序可以通过多次请求Load/Unload来减少盘片的旋转时间，或者设置旋转超时时间(spin
down timeout)来让磁头定期的做Load/Unload等等。

**1.2 这个参数值高了有啥危害？**

虽然Load/Unload技术有很多优点，但毫无疑问频繁的Load/Unload操作会造成磁头的磨损，严重的话会造成数据读写失效，也就说，硬盘挂了。

那么到底Load/Unload多少次会挂呢？最流行的说法是到60W次，西部数据的一份产品规格说明书上也明确标示出了这一数字。

但也有人指出SMART参数根本就是扯淡，好多坏掉的硬盘SMART值很低好的硬盘SMART值超标，因此根本不能成为评判标准以至于现在好多新机器都直接屏掉。但无论如何，频繁地卸载/挂载总不是什么好事。尤其是当你已经了解到Load/Unload次数过多有可能造成硬盘挂掉的时候，我想无论再有人辟谣，你也不会高枕无忧了。毕竟相对于硬盘本身来说，上面的数据可是要重要的多。

**1.3 LCC为啥会那么高？**

简单来说，可能有下面几个原因：

1)
硬盘厂商在固件中制定的节能策略过于苛刻，以至于为了节能，硬盘频繁地Load/Unload  
2) 操作系统的电源策略过于苛刻。

**1.4 其他的发行版有没有这个问题？Windows呢，MAC OS呢？**

各大linux发行版好像就Ubuntu被报告有这个问题，但这实际上并不是Ubuntu的电源策略太变态，恰恰相反，默认情况下Ubuntu会直接沿用硬件固件里面的设定。其他的发行版中SUSE也有类似的电源管理的BUG，除此之外的发行版似乎默认会忽略硬盘的这个节能功能，所以不会有类似的问题。

至于Windows，也会出现类似的现象，比如说我宿舍的Acrest童鞋，但我的没有。MAC
OS也有报告出现类似的问题。

总体来说这个并不是个别现象，也并不应该算是操作系统的问题。感觉由于Windows下硬盘几乎会一直不停地运作，所以硬件厂商不太重视硬盘固件中的初始设定，比如说我的日立硬盘，电源管理级别被设置为128，结果由于Linux并不像Windows那样频繁读盘，磁头为了节能会频繁地做
Load/Unload操作。

**2. 如何修复这个问题？**

**2.1 硬件修改法 (***推荐使用***)**

正如上面所说，如果你的硬盘在Ubuntu下有这个问题，那么有可能是硬件本身的节能策略太激进了。最简单也是最根本的方法，就是用厂商提供的固件修改工具对出厂的默认设置进行修改，比如说日立的Feature
Tools。

在Feature Tools中，有一项"Change Advanced Power
Mode"，默认是128，可以选择从1到254不同的数值。

简单来说，数字越小越节能，数字越大性能越好。Feature
Tools中将1－254分成三段并分别做了简单的说明，一般来说，设置到192-254则表示不允许Load/Unload操作，而255则表示禁用APM()。这个数字也就是后文提到的APM级别。

**2.2 软件修改法**

修改硬盘固件是最根本的解决方案，除此之外，关于在Ubuntu中修改相关策略，网上有很多种不同的解法，有兴趣的童鞋可以看关于这个Bug的讨论,
Ubuntu
Wiki上关于这个Bug的介绍，起因分析以及解决方案的总结等。基本上流传的方法有这么两种：

**2.2.1
启用laptop-mode，通过修改laptop-mode.conf中的相关设置达到控制Load/Unload的目的**

**2.2.2 直接在/etc/acpi/start.d,
resume.d等目录下放置脚本，通过hdparm命令修改APM级别和spin down time.**

具体内容见文后附注。归根结底，这两种方法都是利用hdparm工具，通过-B参数修改高级电源管理(APM)级别，通过-S参数修改旋转超时时间
(Spin Down
Timeout)，从而控制硬盘的Load/Unload次数。所谓APM级别就是我们上面介绍过的1~255，而Spin-down
Timeout就是指硬盘空闲(或者旋转?这个拿不准)多久后才会Spin
Down，也就是停转，做Unload操作。相对应的，有一个Spin up
Time，这是指硬盘重新启动到正常运转所需要的时间。

Windows下也有一款HDDScan软件可以很方便地做到这一点。这样的软件改法确实有效，但由于hdparm不会将设置写入固件，因此在关机、休眠以及待机之后，由于硬盘掉电，这些通过软件的设置会失效，需要重新启用一次。目前这两种方法在我的机器上的测试结果是待机唤醒之后参数不会重新启用。实际上，laptop-mode只会在开机的时候才会应用我们设定的参数，而
acpi的resume.d目录下放置的脚本并不会被执行，不知道这是不是个别现象。
所以如果大家非要用软件的修改方法时，推荐下面这一种。

**2.2.3 pm.utils大法 （推荐使用）**

除了这两种修改方法之外，还有另外一种通过pm.utils来调用hdparm的方法。这实际上是Suse的一个解决方案。pm.utils全称是
Power Management
Utilities，与acpi类似，它可以通过加入Hook脚本的方法在待机、休眠和唤醒的时候修复一些待机/休眠方面的Bug或者实现某些特定的功能。pm.utils很有可能会在8.10中就取代acpi，所以从这个意义上来讲这个方案也会有更长的效用。具体步骤如下：

1)
首先做一些配置，主要就是设置省电模式开启和关闭的模式下hdparm的参数，具体的内容脚本中有注释。

你可能需要将“/dev/sda"修改成你的硬件设备,比如你有两个硬盘，可以修改为"/dev/sda
/dev/sdb"。

`$ sudo vi /etc/pm/config.d/disk`

# Configure disk power management settings to ensure both  
# long disk life and good power management.  
#  
# Space delimited list of disk devices this affects.  
#  
DEVICES\_DISK\_PM\_NAMES="/dev/sda"  
#  
#  
# Power management modes  
#  
# Powersave mode off  
# Set APM as 192  
# Set spin-down for 30 minutes  
#  
DEVICES\_DISK\_PM\_POWERSAVE\_OFF="hdparm -q -B 192 -q -S 241 -q -M
128"  
#  
# Powersave mode on  
# Enable APM to conservative 192 and set spin-down for 21 minutes  
#  
DEVICES\_DISK\_PM\_POWERSAVE\_ON="hdparm -q -B 192 -q -S 252 -q -M 128"

2)
在power.d中加入Hook脚本，作用是在使用电池和AC电源的时候可以自动切换省电模式。  
` $ cd /etc/pm/power.d $ sudo vi disk`


    #!/bin/bash
    . /usr/lib/pm-utils/functions
    . /etc/pm/config.d/disk

    if test -z "${DEVICES_DISK_PM_NAMES}"; then
        exit 1
    fi

    case "$1" in
        true)
            echo "**enabled pm for harddisk"
            for DISK_NAME in `echo ${DEVICES_DISK_PM_NAMES}`; do
                ${DEVICES_DISK_PM_POWERSAVE_ON} ${DISK_NAME}
            done ;;
        false)
            echo "**disabled pm for harddisk"
            for DISK_NAME in `echo ${DEVICES_DISK_PM_NAMES}`; do
                ${DEVICES_DISK_PM_POWERSAVE_OFF} ${DISK_NAME}
            done ;;
    esac

`$ sudo chmod +x disk`

3)
在sleep.d中加入脚本，目的是在休眠/待机之后唤醒的时候重新设定hdparm的参数：  
` $ cd /etc/pm/sleep.d/ $ sudo vi disk`


    #!/bin/bash
    . /usr/lib/pm-utils/functions
    . /etc/pm/config.d/disk

    if test -z ${DEVICES_DISK_PM_NAMES}; then
        exit 1
    fi

    case "$1" in
        thaw|resume)
            /usr/bin/on_ac_power;
            if [ "$?" -eq 0 ]; then
                echo "**disabled PM for harddisk"
                for DISK_NAME in `echo ${DEVICES_DISK_PM_NAMES}`; do
                    ${DEVICES_DISK_PM_POWERSAVE_OFF} ${DISK_NAME}
                 done
           elif [ "$?" -eq 1 ]; then
                echo "**enabled PM for harddisk"
                for DISK_NAME in `echo ${DEVICES_DISK_PM_NAMES}`; do
                    ${DEVICES_DISK_PM_POWERSAVE_ON} ${DISK_NAME}
                done               
           fi
           ;;
    esac

`$ sudo chmod +x disk`

＊＊＊注意最后一定要为disk脚本添加执行权限。否则pm.tuils不会自动执行这段脚本

4\) 如果你没有启用laptop mode （默认是不启用的），可以跳过这部分了。

由于Ubuntu中acpi和pm.utils是共存的，所以如果你启用了laptop
mode，那么在改变电源状态(指电池->AC电源或者反之)的时候，acpi会在启用/停用laptop
mode的同时设置hdparm参数，会覆盖掉pm-utils所做的设置。

所以如果你启用了laptop mode的话，需要做如下修改：

1' `$ sudo vi /etc/default/acpi-support`

将最后的

SPINDOWN\_TIME=12

修改为

SPINDOWN\_TIME=241

2' `$ sudo vi /etc/acpi/power.sh`

将function laptop\_mode\_enable部分的

$HDPARM -B 1 /dev/$drive 2>/dev/null

修改成

$HDPARM -B 192 /dev/$drive 2>/dev/null

上述的解决方案在Dell Inspiron 700m + Ubuntu
8.04.1上测试通过。在待机唤醒之后参数会重新被设置，但是由于我的机器上休眠有问题，所以没有办法测试休眠。但理论上来也是可以的。

**3. 我想定期检测Load\_Cycle\_Count，怎么办？**

好办，这里是一个脚本，具体用法在注释里面粗体标明了。(不好意思...注释好像比代码都长)


    #!/bin/bash
    #
    # @Description:
    #  
    #   check_lcc v0.2
    #
    #   Check Load_Cycle_Count from S.M.A.R.T info of your hard drive
    #   when power on and off and Save them to $FILE in following format:
    #
    #          LCC         TIME
    #   ON      110044      18:05:00 2008-09-08
    #   OFF     110044      18:10:03 2008-09-08
    #
    #   "ON" indicates POWER ON while "OFF" indicates POWER OFF, LCC is
    #   exactly Load_Cycle_Count of your hard drive at TIME.
    #
    # @Usages:
    #  
    #   1. sudo vi /etc/init.d/check_lcc
    #   2. copy all the contents of this script to it
    #     *** Note that u need to modify "FILE" as what u want.
    #      save and quit.
    #   3. sudo chmod +x /etc/init.d/check_lcc
    #   4. sudo update-rc.d check_lcc start 1 2 . stop 99 0 6 .
    #   5. Have fun.
    #  
    #   This script was tested under Ubuntu 8.04.1.
    #
    # @Author:
    #
    #   breaddawson@gmail.com
    #   2008/09/07

    FILE="/home/bread/lcc_report.txt"
    STAT=`smartctl -a /dev/sda | grep 193 | sed -nr "s/.*[[:space:]]([[:digit:]]{1,})$/\1/p"`"\t "`date +'%T  %F'`

    case "$1" in
    start)
        STAT="ON \t"$STAT
        ;;
    stop)
        STAT="OFF\t"$STAT
        ;;
    *)
        echo "Usages: $0 {start|stop}" >&2
        exit 2
        ;;
    esac

    echo -e $STAT >> $FILE 

按照上面的说明操作之后，LCC的结果就会存在你定义的log文件里面了。可以定期打开查看。

**4. 最后附上之前的两种方法，启用laptop mode和添加acpi脚本。**

**4.1. 加入acpi脚本**

1)
为使用电源和电池的时候定制不同的hdparm参数。你可能需要把/dev/sda修改成你的硬盘设备。

`$sudo vi 99-hdd-ugly-fix.sh`  

` #!/bin/bash if on_ac_power; then   # on AC so don't do any head parking   hdparm -B 254 /dev/sda # you might need 255 or a different value else   # either on battery or power status could not be determined   # so quickly park the head to protect the disk   hdparm -B 192 /dev/sda fi`

2\) 将如上脚本安装到如下4个地方  

` $sudo install 99-hdd-ugly-fix.sh  /etc/acpi/resume.d/ $sudo install 99-hdd-ugly-fix.sh  /etc/acpi/start.d/ $sudo install 99-hdd-ugly-fix.sh  /etc/acpi/ac.d/ $sudo install 99-hdd-ugly-fix.sh /etc/acpi/battery.d/`

这个方案比开启laptop简单且方便。因此如果你实在是不想用pm.utils的时候，推荐使用这种方法。

**4.2. 启用laptop mode**

Ubuntu 8.04测试有效，但是待机/休眠唤醒之后设置会丢失。laptop mode
模块在Ubuntu 8.04中是默认包含的，只是没有启用。下面是具体的设置方法。

**1) /etc/default/acpi-support中修改**

# 启用laptop模式  
ENABLE\_LAPTOP\_MODE=true

# 将spin down 时间改成 (241-240)*30min = 30min  
# spin down
time决定硬盘闲置多久以后关闭主轴电动机以节省功耗，0表示永远不关闭  
# 具体的解释看 man hdparm的-S部分  
SPINDOWN\_TIME=241

**2) /etc/laptop-mode/laptop-mode.conf中修改**

# 即便是接上电源也用laptop mode  
ENABLE\_LAPTOP\_MODE\_ON\_AC=1

# 显示器关闭的时候也用laptop mode  
ENABLE\_LAPTOP\_MODE\_WHEN\_LID\_CLOSED=1

# 让laptop mode控制硬盘闲置多长时间才卸载  
CONTROL\_HD\_IDLE\_TIMEOUT=1

# 改成半小时  
LM\_AC\_HD\_IDLE\_TIMEOUT\_SECONDS=1800  
LM\_BATT\_HD\_IDLE\_TIMEOUT\_SECONDS=1800  
NOLM\_HD\_IDLE\_TIMEOUT\_SECONDS=7200

# 让laptop mode来控制硬盘的电源管理  
CONTROL\_HD\_POWERMGMT=1

# 192表示不关闭，从128-254都表示不关闭，越大能耗越大  
# 具体可以 man hdparm 看-B  
BATT\_HD\_POWERMGMT=192  
LM\_AC\_HD\_POWERMGMT=254  
NOLM\_AC\_HD\_POWERMGMT=254

**3) /etc/acpi/power.sh中**

把 "$HDPARM -B 1 /dev/$drive 2>/dev/null"  
修改为 "$HDPARM -B 192 /dev/$drive 2>/dev/null"

**4) 禁用pm.utils的部分功能**

`$ sudo chmod -x /usr/lib/pm-utils/power.d/laptop-tools`

否则laptop-mode不会随机启动。

**5) 重启后，cat /proc/sys/vm/laptop\_mode**

结果是2表示laptop-mode已经启动，是0表示还未启动，请仔细检查上面的设置是否有遗漏。

###############我是很郁闷的分割线###############

附:关于为啥要禁用pm.utils，具体的解释如下：

我从网上找到了laptop
mode的解决方案之后，按照说明一步步操作，但是重新启动之后，查看cat
/proc/sys/vm/laptop\_mode，发现仍然是0.(是2才表示已经启动)。查看/etc/rc2.d/目录下确实有
S99laptop-mode，这说明系统确实会加载这个服务(这个目录下的文件都是个符号链接，会链接到/etc/init.d目录下的同名脚本)。后来Google了一下发现这样的解释：

首先来说/proc/sys/vm/laptop\_mode这个变量和初始化进程laptop-mode并不是一个意思。前者是个内核控制的变量，作用是将磁盘写操作聚簇，后者是一个脚本。

其次，Hardy加入了pm-utils，会覆盖或忽略一部分根据linux传统的配置。为了解决这个问题，可以修改/usr/lib/pm-utils/power.d/laptop-tools中相关的内容或者运行下述命令：

`$ sudo chmod -x /usr/lib/pm-utils/power.d/laptop-tools`

这条命令会禁用pm-utils的部分功能，从而修复你所遇到的问题(指laptop-mode不会随机启动)。注意得重启以后设置才会生效。

实际上pm-utils盲目地覆盖掉laptop-mode或者是/etc/sysctl.conf中的配置，所以chmod -x禁用相关脚本后,
在从AC
POWER转到电池供电的时候，pm-utils就不会执行相关的脚本(laptop-tools)，从而也就不会覆盖相关的设置。这种做法改动最小，如果之后你想重新启用pm-utils的这部分功能，只需要chmod +x就可以了。

###############很郁闷的分割线又来啦###############

**5. 最后是References:**

日立关于Load/Unload技术的解释:
[Load/Unload白皮书下载](http://www.hitachigst.com/tech/techlib.nsf/techdocs/9076679E3EE4003E86256FAB005825FB/$file/LoadUnload_white_paper_FINAL.pdf)  

StorageView关于Load/Unload技术的解释：<http://www.storagereview.com/guide2000/ref/hdd/perf/qual/featuresHead.html>  

西部数据的规格：<http://www.wdc.com/en/library/portable/2879-001121.pdf>  
日立的Feature
Tool下载:<http://www.hitachigst.com/hdd/support/download.htm#FeatureTool>  
Bug报告页面： <https://launchpad.net/bug59695.html>  
Ubuntu Wiki的Bug总结：<https://wiki.ubuntu.com/DanielHahler/Bug59695>  
Ubuntu Dev解释：<http://www.advogato.org/person/mjg59/diary/82.html>  
laptop
mode的解决方案：<https://launchpad.net/ubuntu/+source/acpi-support/+bug/59695/comments/63>  
acpi的解决方案：<http://ubuntuforums.org/showthread.php?p=5031046>  
Suse的解决方案：<http://en.opensuse.org/Disk_Power_Management>  

休眠后重新设置pm.utils的方案：<https://bugs.launchpad.net/ubuntu/+source/pm-utils/+bug/235105>  
pm.utils的wiki:<http://pm-utils.freedesktop.org/wiki/>  
Suse的pm.utils介绍：<http://en.opensuse.org/Pm-utils>  
CnBeta的报道：<http://www.cnbeta.com/articles/42191.htm>  
CnBeta的一个总结：<http://www.cnbeta.com/articles/42421.htm>  
国内用户的一个解决方案:
<http://lymanrb.blogspot.com/2008/01/loadunload-bug.html>  
Ubuntu中文论坛的讨论:
<http://forum.ubuntu.org.cn/viewtopic.php?p=555500>  
关于laptop
mode和pm.utils冲突的解释：<http://ubuntuforums.org/showthread.php?t=867728>  
Windows下修改硬盘APM和Spin-down time的工具：<http://hddscan.com/>

**6. 最最后**

折腾这个问题费了我一整天(实际上是半天，不过那天我中午才起...)，总结这些破烂方法，再加上反复试验确定某个方法是否有效，硬着头皮分析脚本的功能，零零碎碎加起来也有一整天的时间，再加上写这篇总结，又花去一整天加上两节入学教育的时间(罪过啊罪过啊)。到此为止距离开始解决这个问题就已经过去整整一周了。就这还没总结全，好多东西都还没有写上来。不过倒是学到了不少东西，硬盘的原理是确确实实复习了一遍了又，另外学了些写Shell脚本的技巧以及
ACPI和pm.utils的机制。感觉系统里面同时有俩搞电源管理的东西实在是太FT了，因为会有冲突的部分，好在据说Intrepid要搞掉acpi
只用pm.utils，也许会清净一些。

无论如何总算是写完了。一边实验一边记录，一度想放弃了(实在是太费时间，感觉也没太大的意义)，但一个是为了我的宝贝硬盘考虑(钱啊钱啊！)，又觉得折腾了那么多不记录下来，功夫不就都白费了。正好今天有两节入学教育，于是就勇敢地抱本过去，写完最后一段哈哈哈。

贴到这里，希望会对遇到这个问题的人有所帮助。

[[原文链接](http://afita.spaces.live.com/blog/cns!D26666E8B226D1A6!1501.entry)]
