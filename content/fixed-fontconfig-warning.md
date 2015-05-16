Title: 解决 Fontconfig warning 问题
Date: 2007-02-04 14:48
Author: toy
Category: Tips
Slug: fixed-fontconfig-warning

最近，在将目前所用的 Ubuntu Edgy 升级到 Feisty 之后，终端中时常会见到
Fontconfig warning 的提示信息。究其原因，乃是由于 Fontconfig
的配置文件缺少某些内容而造成的。下面，我们就来解决这个问题。

Fontconfig 在终端中的 warning 提示信息如下：  

` Fontconfig warning: no <cachedir> elements found. Check configuration. Fontconfig warning: adding <cachedir>/var/cache/fontconfig</cachedir> Fontconfig warning: adding <cachedir>~/.fontconfig</cachedir>`

为了解决该问题，你需要编辑 fonts.conf 文件：  
`sudo vim /etc/fonts/fonts.conf`

然后找到：  
`<dir>~/.fonts</dir>`

在其下面添加：  
` <!-- Font cache directory list -->`

<cachedir>/var/cache/fontconfig</cachedir>  
<cachedir>~/.fontconfig</cachedir>  

最后保存即可。
