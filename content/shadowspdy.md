Title: ShadowSPDY: 基于 Shadowsocks 和 SPDY 的隧道代理
Date: 2014-04-15 09:41
Author: toy
Category: Apps
Slug: shadowspdy

[ShadowSPDY][s] 是基于 [Shadowsocks][h] 和 [SPDY][p] 而构建的轻量级  
隧道代理。经我试用，ShadowSPDY 用来穿墙的效果不错，与 Shadowsocks  
相比，浏览网页时感觉明显变快了。

要使用 ShadowSPDY，可按如下步骤安装和配置。

**安装**

先安装 Node.js，以 Debian 例：

apt-get install nodejs  
ln -s /usr/bin/nodejs /usr/bin/node

再克隆一份 ShadowSPDY：

cd  
git clone https://github.com/clowwindy/ShadowSPDY.git  
cd ShadowSPDY  
npm install

**准备配置**

准备一份扩展名为 json 的配置文件，如我的是 ~/.shadowsocks.json：

{  
"server":"服务器 IP",  
"server\_port":8899,  
"local\_port":1080,  
"password":"密码",  
"timeout":600,  
"method":"aes-256-cfb"  
}

其中项目说明如下：

* server：填写服务器 IP 地址  
* server\\\_port：填写服务器端口  
* local\\\_port：填写本机端口  
* password：填写密码  
* timeout：设置超时  
* method：设置加密方法

**启动 ShadowSPDY**

在服务端使用以下指令启动：

./ShadowSPDY/bin/spserver -c ~/.shadowsocks.json

在本机使用下列指令启动：

./ShadowSPDY/bin/splocal -c ~/.shadowsocks.json

**配置浏览器**

以 Firefox 为例，在“首选项 > 高级 > 网络 > 设置”中选择“  
手动代理配置”，并在“SOCKS 主机”中填入“127.0.0.1”、端口中  
填入本机端口、选中“SOCKS v5”保存即可。

[s]: https://github.com/clowwindy/ShadowSPDY  
[h]: https://github.com/clowwindy/shadowsocks  
[p]: http://www.chromium.org/spdy
