Title: Fedora 12 下安装 Firefox Lorentz Beta
Date: 2010-04-13 16:53
Author: toy
Category: Tips
Tags: Fedora, Firefox
Slug: installing-firefox-lorentz-beta-on-fedora-12

{ 撰文/[DNA24](http://szlug.org) }

如果你想要在 Fedora 12 下安装 Firefox Lorentz Beta 3.6.3  
的话，那么只要执行以下三个简单的步骤即可：

1. `$ cd /etc/yum.repos.d/`

2. `$ su -c 'wget http://rpms.famillecollet.com/remi-fedora.repo'`

3. `$ su -c 'yum --enablerepo=remi-test update firefox'`

{ Thanks DNA24. via
[Linuxers](http://linuxers.org/howto/install-firefox-lorentz-beta-and-gwibber-229921-fedora-12-constantine)
}
