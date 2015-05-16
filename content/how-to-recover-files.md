Title: 求助: 怎样才能恢复文件?
Date: 2009-04-18 10:25
Author: toy
Category: AskLinuxtoy
Slug: how-to-recover-files

这是署名为 kiki 的网友发来的求助信，请大家给予帮助。该信的内容如下：

冒昧给您写信求救，如果能在你这里得到帮助我将非常感激!

情况是今天光盘安装ubuntu 9.04（不是升级安装，原来的系统是8.10），  
安装时使用了一个新的用户名（原来的用户名是kiki，新的用户名是ki）。

新系统很顺利的安装完成， 随后上网下载语言支持， 重新启动后又安装了  
mplayer、smplayer、nmap等软件，安装软件的同时将原来 home/kiki/ 中  
的很多文件移动到 home/ki/ 中；

在安装完上面说的软件后就关机回家了，回家后重新打开电脑发现能够登  
录，登录后就没有出现桌面等，鼠标正常移动。

开始怀疑安装的软件或系统不好，就用光盘重新安装还是使用 ki 这个用户  
名（home/ki），安装过程也很顺利，但是重新启动系统后情况还是一样！

今天上午上班后又安装了一次用户名还是 ki ，安装完成后情况依旧！想了  
一下又重新安装这次换了用户名使用 kiki ，安装完成后桌面出来了！随后发  
现在 /home/ki/ 中有一个目录 .Private ，里面全是乱码文件名，文件名很长  

“ECRYPTFS\_FNEK\_ENCRYPTED.FWZkJ2E3Cx3TWERcuMh6s5Bi-Ygv5m2At3t2yXwrfgYUqTbe49v8AoLNpE--“

在google了很久，用ecryptfs mount -t /home/ki/.Private /home/ki 用当初  
使用的密码可以mount，但是挂载的文件名都还是乱码，文件不能打开。这  
方法试过多次了，也没有改变。

现在求助希望兄弟能帮忙，文件很重要！否则很多需要重写了！！！
