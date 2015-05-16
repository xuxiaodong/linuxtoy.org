Title: 用命令行部分解决 CNNIC 证书问题
Date: 2010-02-07 09:39
Author: toy
Category: Cli
Slug: ca-certificate-problem

{ 撰文/[fcicq](http://www.fcicq.net/wp/) }

下面写的，比现有大家正在应用的方法麻烦的多。有怕麻烦的请用各类图形版方法。  
方法对 Firefox 3.6 & Chrome & Wget & cURL 有效。作者不用  
Opera，有知道怎么办的可以冒泡。

**0 删除系统原装证书**

本部分只适合 Debian / Ubuntu。其他发行版可能不是这个文件，如有错请指正。

`sudo rm /usr/share/ca-certificates/mozilla/Entrust.net\_Secure\_Server\_CA.crt`

注：如果 ca-certificates
包升级了，这个文件还会回来的，这个问题怎么办呢？

Debian / Ubuntu 还需要 `dpkg-reconfigure ca-certificates`
才算完事。其他发行版怎么做偶不知道。  
原因是这样的，/etc/ssl/certs/ca-certificates.crt 是证书的集合。

检验成功的方法
(这是刚才被删的那个文件的有用部分第一行)，无匹配为成功的标志。

`grep "MIIE2DCCBEGgAwIBAgIEN0rSQzANBgkqhkiG9w0BAQUFADCBwzELMAkGA1UEBhMC" /etc/ssl/certs/ca-certificates.crt`

**1 装个包**

    # 发行版之间还不一样
    # Debian / Ubuntu Users. fcicq loves sudo :D
    sudo apt-get install libnss3-tools
    # Fedora Users
    su -c "yum install nss-tools"
    # Arch Linux Users
    sudo pacman -S nss
    # Gentoo Users 还要加 USE
    sudo sh -c "echo 'dev-libs/nss utils' >> /etc/portage/package.use"
    sudo emerge dev-libs/nss

作者只在 Ubuntu 下做了测试，不保证其他系统安装一定正确。  
完成后应该就能执行 certutil 了，不能的话请留言。

**2 下载证书**

下载 并解压到 ~。事后会清理的，请放心 :D

    # 别说你没 p7zip，没有的话自己解压
    cd; wget https://dl.dropbox.com/u/1356279/proxys/CNNIC.7z
    p7zip -d CNNIC.7z

**3.1 Firefox 清理**

先进入 Profile 目录

    # 如果你的 Firefox 有多个 Profile，或者放别处去了，那自己想办法...
    cd ~/.mozilla/firefox/*.default

原理是先试着修改原证书，再添加新证书。

    # 有出错信息是正常现象
    certutil -d . -M -t "" -n "CNNIC SSL" || certutil -d . -A -i ~/CNNIC/CNNICSSL.crt -n "CNNIC SSL" -t ""
    certutil -d . -M -t "" -n "CNNIC ROOT" || certutil -d . -A -i ~/CNNIC/CNNICROOT.crt -n "CNNIC ROOT" -t ""
    certutil -d . -M -t "" -n "Entrust.net Secure Server CA" || certutil -d . -A -i ~/CNNIC/Entrust.netSecureServerCertificationAuthority.crt -n "Entrust.net
    Secure Server CA" -t ""

查看结果的方法

`certutil -d . -L`

**3.2 Chrome 清理**

用 Chrome 的同学可能注意到
[LinuxCertManagement](http://code.google.com/p/chromium/wiki/LinuxCertManagement)
了

    # 出错都是正常的，不出错那是因为你执行了两遍
    certutil -d sql:$HOME/.pki/nssdb -M -t "" -n "CNNIC SSL" || certutil -d sql:$HOME/.pki/nssdb -A -i ~/CNNIC/CNNICSSL.crt -n "CNNIC SSL" -t ""
    certutil -d sql:$HOME/.pki/nssdb -M -t "" -n "CNNIC ROOT" || certutil -d sql:$HOME/.pki/nssdb -A -i ~/CNNIC/CNNICROOT.crt -n "CNNIC ROOT" -t ""
    certutil -d sql:$HOME/.pki/nssdb -M -t "" -n "Entrust.net Secure Server CA" || certutil -d sql:$HOME/.pki/nssdb -A -i
    ~/CNNIC/Entrust.netSecureServerCertificationAuthority.crt -n "Entrust.net Secure Server CA" -t ""

查看结果的方法

`certutil -d sql:$HOME/.pki/nssdb -L`

**4 测试**

https://tns-fsverify.cnnic.cn/  
https://www.enum.cn/

**5 清理现场**

    # 除非你就是里面的人，否则不会有这种目录名的，对吧，有文件删错概不负责。
    rm ~/CNNIC.7z; rm -r ~/CNNIC

**6 命令参考**

[certutil](http://www.mozilla.org/projects/security/pki/nss/tools/certutil.html)

**7 后记**

偶没有用删除证书的方法，只是让证书失去了验证的能力。不喜欢的可以自己改一改，命令参考在上面。

事实上最大的问题是 Entrust.net 信任 CNNIC
了。**某些人说不升级浏览器就能防御，那就是个笑话。**

Arora
这个浏览器很有意思，可是偶对它的免疫操作失败了。**有人知道怎么做吗？**

以下和 Linux 无关。

另外，Windows Server Administration Pack 里面有
certutil.exe，有条件的可以试试做一个免疫工具出来。  
Win32 下也有 Mozilla 版
certutil.exe（可能需要自己编译），这两个程序在名字上要打架了。

{ Thanks fcicq. }
