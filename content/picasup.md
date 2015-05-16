Title: picasup: picasa相册上传脚本
Date: 2008-08-11 22:11
Author: lwl
Category: Apps, Cli
Slug: picasup

[picasup](http://code.google.com/p/picasup/)是一个python脚本，利用google的API来上传照片到picasa，仅仅41行。谢谢作者[王元涛](http://todwang.blogspot.com/2008/07/simple-picasa-synchronizer-in-console.html)。

安装使用作者都已经说得[很清楚](http://todwang.blogspot.com/2008/07/simple-picasa-synchronizer-in-console.html)（英文），这儿就不赘述了。

我使用后的感觉是还缺少多个目录上传的功能，所以就写了一个bash脚本来实现：

> #! /bin/bash  
>  # picasa\_upload\_multi\_directory.sh
>
> if [ "$#" -eq "0" ]  
>  then  
>  upload\_dir="/path/to/upload\_dir"   #若无参数  
>  else  
>  upload\_dir="$1"       #或有第一个参数  
>  fi
>
> # upload\_dir下所有的子目录都会被上传  
>  cd $upload\_dir  
>  albums=`ls -l | grep ^d | awk '{print $8}'`
>
> # upload to picassa  
>  for album in $albums  
>  do  
>  echo "--------------------"  
>  echo "processing $album ..."  
>  cd $album  
>  python /path/to/picu.py  
>  cd ..  
>  done

不过要记得把picu.py中的

> id = raw\_input("Username:") + "@gmail.com"  
>  ps = getpass.getpass()

改成

> id = "你的用户名"  
>  ps = "你的密码"

就不会每次都询问密码了。这样可以使用Cron进行自动上传。另外为了安全起见，可以

> chmod 700 picu.py

-   [作者博客介绍](http://todwang.blogspot.com/2008/07/simple-picasa-synchronizer-in-console.html)
-   [picasup](http://code.google.com/p/picasup/)
-   本站还介绍了[GPPM](http://linuxtoy.org/archives/google-picasa-perl-module.html)，perl版本的picasa上传。

