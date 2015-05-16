Title: Apt 使用参考
Date: 2006-09-22 10:34
Author: toy
Category: Tutorials
Slug: apt_reference

  ---------------------------------------------- ----------------------------------------
  命令                                           作用
  apt-cache search package                       搜索包
  apt-cache show package                         获取包的相关信息，如说明、大小、版本等
  sudo apt-get install package                   安装包
  sudo apt-get install package - - reinstall     重新安装包
  sudo apt-get -f install                        强制安装
  sudo apt-get remove package                    删除包
  sudo apt-get remove package - - purge          删除包，包括删除配置文件等
  sudo apt-get autoremove                        自动删除不需要的包
  sudo apt-get update                            更新源
  sudo apt-get upgrade                           更新已安装的包
  sudo apt-get dist-upgrade                      升级系统
  sudo apt-get dselect-upgrade                   使用 dselect 升级
  apt-cache depends package                      了解使用依赖
  apt-cache rdepends package                     了解某个具体的依赖
  sudo apt-get build-dep package                 安装相关的编译环境
  apt-get source package                         下载该包的源代码
  sudo apt-get clean && sudo apt-get autoclean   清理下载文件的存档
  sudo apt-get check                             检查是否有损坏的依赖
  ---------------------------------------------- ----------------------------------------

备注：package 为软件包名称。  
更新：1.根据 [*Apt-get
Guide*](http://wiki.linuxhelp.net/index.php/Apt-get_Guide)
一文，新增了几个命令。2.新增了 apt-get autoremove 命令。

（Via [ArsGeek](http://www.arsgeek.com/?p=577), thanks!）
