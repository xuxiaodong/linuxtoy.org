Title: Storm: 轻松管理 SSH 连接
Date: 2013-12-10 21:05
Author: toy
Category: Apps
Slug: storm

如果你有多台 SSH 主机需要管理，每次直接手输 `ssh user@ip`  
自然麻烦。虽然我们可以将其[添加到 `~/.ssh/config`][c] 配置  
文件中，不过也得手动编辑才行。[Storm][s] 则使这一过程像风  
一样轻盈完成。

Storm 使用 Python 编写而成，允许你对 SSH 连接进行管理，包括  
执行添加、编辑、列出、搜索等操作。

安装 Storm 可以使用 Python 包管理器 `pip`:

pip install stormssh

#### 添加 SSH 连接

假如我们要添加 `www@linuxtoy.org` 为 vps，则可以执行：

storm add vps www@linuxtoy.org

命令执行后会有如下信息：

success vps added to your ssh config. you can connect it by typing "ssh  
vps".

这样，我们通过 `ssh vps` 就可以登上 linuxtoy.org 了。

#### 编辑 SSH 连接

编辑已添加的 vps 连接：

storm edit vps vps@linuxtoy.org

同样有信息提示：

success "vps" updated successfully.

#### 列出 SSH 连接

要列出已添加的连接，执行：

storm list

输出结果为：

ubox -> ubox@172.16.10.201:22  
[custom options] serveralivecountmax=120 serveraliveinterval=30

vps -> www@linuxtoy.org:22

#### 搜索 SSH 连接

搜索也是可以的，例如搜索包含 vp 的 SSH：

storm search vp

将显示：

Listing results for vp:  
vps -> www@linuxtoy.org:22

除了命令行使用界面外，Storm 也包含 Web UI，感兴趣的朋友  
不妨自行尝试看看。

[s]: https://github.com/emre/storm  
[c]: https://linuxtoy.org/archives/ssh-tip-creating-shortcut.html
