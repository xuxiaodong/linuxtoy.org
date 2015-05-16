Title: 编译 Chromium OS
Date: 2009-11-24 16:08
Author: toy
Category: Tips
Tags: Chromium OS
Slug: building-chromium-os

{ 撰文/[yang](http://www.sgtalk.cn) }

粗略的介绍一下 Chromium OS 的编译过程。

安装下面的依赖：


    sudo apt-get install subversion pkg-config python perl g++ g++-multilib bison
    flex gperf libnss3-dev libgtk2.0-dev libnspr4-0d libasound2-dev libnspr4-dev
    msttcorefonts libgconf2-dev libcairo2-dev libdbus-1-dev wdiff lighttpd php5-cgi
    sun-java6-fonts git-core  

然后，使用 gclient 获取 Chromium OS 的源码目录（四百多兆）：


    mkdir chromiumos  
    cd chromiumos  
    gclient config http://src.chromium.org/git/chromiumos.git  
    gclient sync  

编译脚本都在 chromiumos/src/scripts 下面，依次执行下面几个脚本：

./make\_local\_repo.sh

运行这个脚本之前，确保安装了
reprepro，否则会提示找不到命令，这时，需要将 chromiumos/repo
目录删除才可以重新执行 make\\\_local\\\_repro.sh 脚本，汗～这个搞了好久
Orz。

./make\_chroot.sh

创建 chroot 编译环境后，需要下载 Chrome 浏览器，改名为
chrome-chromeos.zip 并放到
~/chromiumos/src/build/x86/local\_assets，这个目录需要自己依次创建。

然后进入 chroot 环境：

./enter\_chroot.sh

这时，可以创建一个脱机用户，为了防止没有网络链接的情况下无法登录：

cd ../platform/pam\_google && ./enable\_localaccount.sh USERNAME

再依次编译软件包和内核，创建磁盘镜像：

./build\_platform\_packages.sh  
./build\_kernel.sh  
./build\_image.sh

脚本执行完毕后，会如下提示：

    Done. Image created in
    /home/yang/trunk/src/build/images/999.999.32809.061105-a1

然后会生成 rootfs.image 磁盘镜像，可以将该镜像转为虚拟机磁盘（vmdk）：

./image\_to\_vmware.sh --from=~/Downloads/chromiumos/chromiumos.git/src/build/images/999.999.32809.061105-a1 --to=~/Downloads/chromiumos/chromiumos.git/src/build/images/999.999.32809.061105-a1/rootfs.vmdk

截图：

[![ChromiumOS](http://i.linuxtoy.org/images/2009/11/chromeos\_on\_vmware-thumb.jpg)](http://i.linuxtoy.org/images/2009/11/chromeos\_on\_vmware.jpg)

在 VMware 没有体验到好处，看来要用到我的 Wind U100 上网本了^^

{ [Source](http://www.sgtalk.cn/656868.html). Thanks yang. }
