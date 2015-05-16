Title: 删除软件后 GConf 中无用项的清理
Date: 2009-12-26 10:51
Author: toy
Category: Tips
Tags: GConf
Slug: gconf-clean-up

{ 撰文/jqxl0205 }

不知道大家有没有这样的经历，删除某个使用 GConf 的软件后，通过
gconf-editor  
你会发现在左侧边栏中与它相关的内容仍然存在。

比如我使用 Archlinux 安装了 Compiz 后，它会在 GConf 的 /apps  
中生成一些东东。删除 Compiz 后那些东东还是存在于 GConf
中，虽然这不影响使用，但看着还是挺不舒服的。Archlinux 下安装 iBus
然后卸载后也会出现这种情况。（呵呵，删除 ~/.gconf 也不顶用）

通过 Goolge 搜索一番，找到 gconf-cleaner
这个软件（呵呵，估计它已经处于半死不活状态）。怀着试一试的心态 yaourt -S
gconf-cleaner 安装了这个软件，可惜使用后还是不能解决上面的问题。

想一想，这种情况肯定是系统某处对那些东西进行了缓存，又 Goolge
之，终于找到一个方法可以解决上面出现的问题（可在 Archlinux
中使用，其他发行版也可，但需要自己更改相应路径）。

方法如下：


        #!/bin/bash
        
        rm /etc/gconf/gconf.xml.defaults/*
        
        export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
        find /usr/share/gconf/schemas -name "*.schemas" | xargs   
         /usr/bin/gconftool-2 --makefile-install-rule > /dev/null
        
        chmod 755 /etc/gconf/gconf.xml.system
            
        PID=`pidof gconfd-2`
        if [ ! -z "${PID}" ]; then
            kill ${PID}
        fi

使用 root 用户运行上述 shell 即可。

{ Thanks jqxl0205. }
