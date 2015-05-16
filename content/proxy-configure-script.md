Title: 浏览器自带代理服务器配置脚本
Date: 2010-02-04 19:33
Author: hmy
Category: Tips
Tags: Firefox
Slug: proxy-configure-script

Firefox  

可以利用代理服务器配置软件来配置代理服务器。其实在浏览器里面可以利用一个标准的代理服务器配置脚本来自己控制代理服务器的使用。比如下面的例子。

function FindProxyForURL(url, host)  
{  
if (isPlainHostName(host) ||  
dnsDomainIs(host, ".netscape.com")||  
dnsDomainIs(host, "docs.google.com")||  
dnsDomainIs(host, "blogger.com")||  
dnsDomainIs(host, ".blogspot.com"))  
return "PROXY 127.0.0.1:3128; DIRECT";  
else  
return "DIRECT";  
}

对 blogger、docs.google.com 等域名使用代理，其他的域名不用代理。

把这个脚本写好以后，在浏览器的代理服务器那里选择 automatic proxy
configure file URL: 填入如下的地址

file:///home/hmy/proxy

当然把上面的地址替换成你自己的配置文件路径就成。
