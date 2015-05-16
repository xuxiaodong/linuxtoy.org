Title: Linuxbrew: Homebrew for Linux
Date: 2014-03-12 11:39
Author: toy
Category: Apps
Slug: linuxbrew

在 OS X 平台上非常流行的包管理器 [Homebrew][h] 最近正被移植  
到 Linux 上而成为 [Linuxbrew][l]。虽然各种 Linux 发行都带有  
自己的包管理工具，诸如 apt-get、yum、pacman、emerge 等等，  
但 Linuxbrew 在以下情况下仍有用武之地：

* Linuxbrew 允许将包安装到用户的 HOME 目录，这样的话，就不再  
需要执行 `sudo`；  
* 对于在 Linux 包管理器中缺少的包，可以通过 Linuxbrew 来搞定；  
* 如果 Linux 包管理器中所带包的版本过旧，那么利用 Linuxbrew  
能够安装该包的最新版本。

**安装 Linuxbrew**

在安装 Linuxbrew 之前，需要先准备好依赖：

Debian/Ubuntu：

% sudo apt-get install build-essential curl git ruby libbz2-dev \\  
libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev

Fedora：

% sudo yum groupinstall 'Development Tools' && sudo yum install \\  
curl git ruby bzip2-devel curl-devel expat-devel ncurses-devel
zlib-devel

接着，将 Linuxbrew 从 GitHub clone 下来：

% git clone https://github.com/Homebrew/linuxbrew.git ~/.linuxbrew

并将下列内容添加到 `~/.bashrc` 或 `~/.zshrc`：

export PATH="$HOME/.linuxbrew/bin:$PATH"  
export LD\_LIBRARY\_PATH="$HOME/.linuxbrew/lib:$LD\_LIBRARY\_PATH"

然后执行：

% source ~/.bashrc

或：

% source ~/.zshrc

这样子 Linuxbrew 就算装好了。

**使用 Linuxbrew**

通过 `brew help` 可以了解 Linuxbrew 的基本用法，例如：

% brew search # 搜索包  
% brew install # 安装包  
% brew uninstall # 删除包  
% brew list # 列出 pkg 的文件  
% brew info # 关于 pkg 的信息  
% brew update # 更新包  
% brew upgrade # 升级包

关于 Linuxbrew 更详细的用法，可执行 `man brew` 查阅。

[h]: https://github.com/Homebrew/homebrew  
[l]: https://github.com/Homebrew/linuxbrew
