Title: 我的屏幕截图脚本
Date: 2006-08-01 14:07
Author: toy
Category: Apps
Slug: my_take_screenshot_script

    #!/bin/bash

    # Location to save files
    WORKINGDIR=$HOME/screenshots
    # Default delay before taking screenshots
    DELAY=3
    #Prefix to use for images captured. 
    PREFIX=screenshot

    # Check if the dir to store the screenshots exists, else create it: 
    if [ ! -d "${WORKINGDIR}" ]; then mkdir "${WORKINGDIR}"; fi 

    i=`ls -l $WORKINGDIR/$PREFIX*.png | wc -l` 
    ((i = i+1))

    sleep $DELAY
    import -frame -depth 8 -dither -quality 9 $WORKINGDIR/$PREFIX-$i.png

提示：

1.需要安装 imagemagick 才能使用此脚本  
2.截取的图像默认保存到用户主目录的 screenshots  
3.在截图时，会延迟 3 秒
