Title: Dpkg 常用指令操作快速参考
Date: 2006-10-15 15:36
Author: toy
Category: Tutorials
Slug: dpkg_reference

Debian，以及基于 Debian 的系统，如 Ubuntu 等，所使用的包格式为
deb。以下为操作 deb 包的常用 Dpkg 指令表，供初学的朋友参考。

  --------------------------- ------------------------
  命令                        作用
  dpkg -i package.deb         安装包
  dpkg -r package             删除包
  dpkg -P package             删除包（包括配置文件）
  dpkg -L package             列出与该包关联的文件
  dpkg -l package             显示该包的版本
  dpkg --unpack package.deb   解开 deb 包的内容
  dpkg -S keyword             搜索所属的包内容
  dpkg -l                     列出当前已安装的包
  dpkg -c package.deb         列出 deb 包的内容
  dpkg --configure package    配置包
  --------------------------- ------------------------

注意：更多选项可通过 dpkg -h 查询，有些指令需要超级用户权限才能执行。
