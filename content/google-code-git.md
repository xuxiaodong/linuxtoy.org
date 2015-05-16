Title: 在 Google Code 中使用 Git
Date: 2008-10-15 18:14
Author: toy
Category: Tutorials
Tags: Git, Google Code
Slug: google-code-git

[撰文/[1help1](http://vm-kernel.blogspot.com/)]

相比sf，googlecode的使用更加简单和方便。虽然在功能方面没有sf多，但是对于一个开源项目来说，基本上够用了。googlecode的功能有wiki，下载，svn，issue
report。最近googlecode的svn中又增加了一个code
review的功能，也就是说别人可以浏览SVN中代码并且留下comment。详细见google的介绍：<http://code.google.com/p/support/wiki/CodeReviews>

虽然google提供的SVN功能不错，但是我喜欢在本地用GIT来管理我的代码。之前我的使用方法是用svn
co下来一份代码，然后git建一个本地仓库，所有的代码修改log都进入本地仓库。当完成一个功能后，用svn
commit进googlecode。这样做的缺点在于本地git的log不能反应到svn中。也就是说svn中的log信息都是比较粗线条的，不能很细化的反应项目的变化情况。

于是就需要请出我们今天的主角：git-svn。首先在ubuntu中安装它。

`sudo apt-get install git-svn`

安装完以后，需要checkout出google code svn中的东西来。

`git-svn clone https://omap3emu.googlecode.com/svn -T trunk -b branches -t tags`

这会在本地生成一个文件夹svn。里面就是google code
svn中的东西。请记住，GIT的远端仓库和本地目录都是在一起的。我们来看一下目前的GIT仓库中有哪些branch。


    root@kill-bill:/home/root/sdc/omap3emu/svn#git-branch -a

    * master
    trunk

为什么有两个branch呢？请注意，git-svn会为svn中的trunk在GIT中建立一个branch，并且新建另外一个branch与其对应。比如目前omap3emu的svn中只有一个trunk，没有branch和tag，因此git会建立一个git的branch叫做trunk，并且还会建另外一个branch：master。master和trunk有对应关系。也就是说，git
master对应到git
trunk，git的trunk又对应到svn的trunk。至于这个对应关系有什么用，接下来会解释。

接下来就是在git的master中进行修改，然后git-commit，再修改，再commit。不过请记住，在git中进行的commit都是在本地。如果想commit到svn中怎么办呢？那就需要dcommit了。还有一个问题，我怎么知道是commit到svn的哪一个分支中呢？是trunk，还是branch，还是tag？上面的对应关系就显出作用了。由于GIT中的master和svn中的trunk有对应关系，因此在master中所做的改变使用dcommit到svn的时候是commit到svn的trunk中的。如果不知道将要进行的commit是commit到svn的哪里，可以在dcommit后加入参数 -n
来查看。


    root@kill-bill:/home/root/sdc/omap3emu/svn# git-svn dcommit -n
    Committing to https://omap3emu.googlecode.com/svn/trunk ...
    diff-tree 8dab0ad6120a4ffc6bf4d7598098ec94f251216f~1 8dab0ad6120a4ffc6bf4d7598098ec94f251216f

上面的显示告诉我们，将要进行的commit是commit'到svn的trunk中。别担心，加上参数-n后并没有进行真正的svn
commit。如果想commit的话，去掉-n 参数。


    root@kill-bill:/home/root/sdc/omap3emu/svn# git-svn dcommit
    Committing to https://omap3emu.googlecode.com/svn/trunk ...
            A       doc/codingstyle.txt
            A       doc/git-svn.txt
            A       doc/misc.txt
    Committed r2
            A       doc/codingstyle.txt
            A       doc/git-svn.txt
            A       doc/misc.txt
    r2 = 7bf572689c8fbd3852c5d5d197c434cc8b1c7345 (trunk)
    No changes between current HEAD and refs/remotes/trunk
    Resetting to the latest refs/remotes/trunk

如果其他项目成员有了新改动并且commit到svn中去了。那么可以通过git-svn
rebase来获得svn上的最新内容。


    root@kill-bill:/home/root/sdc/omap3emu/svn# git-svn rebase
            M       doc/misc.txt
    r3 = b279f0326a313acf8da146566ef3853edca91628 (trunk)
    First, rewinding head to replay your work on top of it...
    HEAD is now at b279f03... jsut a test
    Fast-forwarded master to refs/remotes/trunk.

暂时算是简单的把git-svn用起来了，以后有什么复杂的情况，再继续介绍。这里有一篇更详细的文章[using
Git with Google code
hosting](http://quirkygba.blogspot.com/2007/10/using-git-with-google-code-hosting.html)。非常不错。

[[原文链接](http://vm-kernel.blogspot.com/2008/10/google-codegit.html)]
