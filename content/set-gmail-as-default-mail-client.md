Title: 小技巧: 如何将 Gmail 设置为默认的邮件客户端
Date: 2007-11-23 10:45
Author: toy
Category: Tips
Slug: set-gmail-as-default-mail-client

对于日常使用 Gmail
的朋友来说，这是一个十分有用的小技巧。该技巧将引导你如何在 Linux 中将
Gmail 设置为默认的电子邮件客户端。通过这样设置之后，的确能够给我们使用
Gmail 带来方便。比如，点击电子邮件地址就会直接进入 Gmail
的撰写邮件界面。

[![Gmail
setting](http://i.linuxtoy.org/i/2007/11/gmail-thumb.png)](http://i.linuxtoy.org/i/2007/11/gmail.png)

1.  你需要创建具有如下内容的 shell 脚本：  

    ``  #!/bin/sh firefox https://mail.google.com/mail?view=cm&tf=0&to=`echo $1 | sed 's/mailto://'` ``

    如果你想要在现有 Firefox 窗口的新标签中打开，则替换为下面的内容：

    `` firefox -remote "openurl(https://mail.google.com/mail?view=cm&tf=0&to=`echo $1 | sed 's/mailto://'`,new-tab)" ``

2.  将该脚本保存为 open\_mailto.sh，并加上可执行权限：
    `chmod u+x ~/open_mailto.sh`
3.  点击 **System → Preferences → Preferred Applications**，在 Mail
    Reader 下选择 Custom，并在 Command 右边输入
    /home/username/open\_mailto.sh %s。注意，你需要将其中的 username
    换成自己的。

[[via](http://www.howtogeek.com/howto/ubuntu/set-gmail-as-default-mail-client-in-ubuntu/)]
