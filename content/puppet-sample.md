Title: puppet：建立一个 pdns-recursor 的实例
Date: 2008-08-24 15:35
Author: hmy
Category: Tutorials
Tags: Puppet
Slug: puppet-sample

[撰文/hmy]

通过 [puppet](http://linuxtoy.org/archives/puppet.html)
脚本，在本地建立一个 dns 缓存服务器，本文针对 debian、ubuntu。

步骤如下：

1.  更新 /etc/apt/sources.list  
    `# apt-get update`
2.  安装 puppet 软件包  
    `# apt-get install puppet`
3.  复制下面内容存为"/tmp/dns.pp"文件


        # start
        package {
               "pdns-recursor":
                       ensure => installed;
               }

        file {
               "/etc/resolv.conf":
                       require => Service["pdns-recursor"],
                       content => "nameserver 127.0.0.1\n";
               }
        service {
               "pdns-recursor":
                       ensure => running,
                       pattern => "pdns_recursor" ,
                       require => Package["pdns-recursor"];
               }
        # end

4.  执行下面命令完成配置  
    `# puppet /tmp/dns.pp`

**附加内容：**

简单解释一下上面这个 puppet 文件的内容：

-   package 段，指定了一个 package
    "pdns-recursor"，要求这个包的状态是"installed"，表示要求这个包是安装好的。也可以把
    installed 换成 latest，表示让这个包保持最高的版本。
-   file 段，指定了一个文件"/etc/resolv.conf"，设置其内容为"nameserver
    127.0.0.1"。require 这行表示只有在 service pdns-recursor
    正确运行的情况下才会修改文件内容。否则不做任何操作。
-   service 段，指定了一个服务
    pdns-recursor，保证这个服务的状态是"running"，既运行中。另外 require
    这行的意思是这个 service 依赖 package pdns-recursor 正确被安装。

