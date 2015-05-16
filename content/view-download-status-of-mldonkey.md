Title: 实用小脚本: 查看 MLDonkey 下载进度
Date: 2009-03-16 10:41
Author: toy
Category: Apps
Tags: MLdonkey
Slug: view-download-status-of-mldonkey

想想看，你怎样查看 MLDonkey 的下载进度，是通过自身所带的 Web
UI，还是诸如 Sancho 这样的第三方
GUI，亦或其它方式，总之都有点麻烦。bones7456 和 Shellex
同学各写了一段小脚本，将其定义成 alias 后，在命令行下只需输入 m 即可查看
MLDonkey 的下载情况，非常方便实用。

[code='sh']alias m='pgrep mlnet >/dev/null 2>&1 && echo vd | nc -q 1
localhost 4000 | awk '"'"'/\\[D/{print
"\\033[0;32m"$7"\\t\\033[4;31m"$8"%\\033[0m\\t",$14"KB/s"}
/Down:/'"'"[/code]  
*使用 Awk 实现（by bones7466）*

[code='sh']alias m="pgrep mlnet >/dev/null 2>&1 && echo vd | nc -q 1
localhost 4000 |python -c \\"import re,sys;
str=sys.stdin.read();a=re.compile('.*?\\[D\\s*(.*?)\\].*mldonkey
(.*?)[\\s*](\\d.*?)[\\s*](\\d.*?)[\\s*](\\d.*?)[\\s*](\\d.*?)[\\s*](\\d.*?)[\\s*](\\d.*?)[\\s*]([\\d|-].*?)[\\s|\\n]').findall(str);b=[(name.strip(),
p.strip(), cs.strip(), ts.strip(), spd.strip()) for id, name, p, cs, ts,
sn, old, act, spd in a]; map(lambda (n, p, cs, ts, spd):
sys.stdout.write('(%s%%)%s...%s\\t %s/%s\\t %skb/s\\n' % (p, n[:20],
n[-8:], cs, ts, spd)), b);print ''\\""[/code]  
*使用 Python 实现（by Shellex）*

将上面的代码之一加入 $HOME/.bashrc 或 $HOME/.zshrc，然后 source 一下
.bashrc 或 .zshrc 即可。注意，你可能需要安装 netcat 这个包。

另外，hmy 同学对此也有补充：

[code='sh']#!/bin/bash  
mldonkey\_command -u hmy -p youpass 'vd'[/code]

[via [ShelleX is Not
ShelleXetend](http://www.sxnsx.com/a-bash-script-to-view-download-status-of-mldonkey/)
& [bones7456's blog](http://li2z.cn/2009/01/15/mldonkey_/)]
