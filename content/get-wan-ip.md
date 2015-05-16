Title: 获取 WAN IP
Date: 2011-09-07 13:05
Author: shuge.lee
Category: Cli
Tags: ip
Slug: get-wan-ip

命令行下获取 WAN IP 。

如果你在 router 或者 firewall 后面，你直接查询 interface ，拿到可能不是
WAN 的 IP 。

很久很久以前的一个版本，把它们贴到 .bashrc (Bash 专用) 或者 .profile (非
Bash 专用)里面去

```  
alias myip='curl -s www.123cha.com | grep -o
"[0-9]\\{1,3\\}.[0-9]\\{1,3\\}.[0-9]\\{1,3\\}.[0-9]\\{1,3\\}" |
head -n 1'  
```

. .bashrc 或者 . .profile 即可生效，输入 myip 就能拿到 WAN IP。

[@muzuiget](http://twitter.com/#!/muzuiget)
同学今天提到的另外一个简化版本

```  
curl ifconfig.me  
```

muzuiget 同学说后者有风险可能会被封。我觉得不会，拿个 WAN IP
跟他妈派对有毛关系？

我觉得 ifconfig.me 版本更 pythonic 些，返回 MIME 的是
text/plain，比前一个的 text/html 要快、干净。

csslayer 同学对此文也有贡献。

扩展阅读：
[获取计算机外网ip的几种写法](http://forum.ubuntu.org.cn/viewtopic.php?f=21&t=288217&start=0)

（完）
