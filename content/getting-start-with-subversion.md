Title: Subversion 应用初步
Date: 2007-05-15 21:30
Author: toy
Category: Tutorials
Slug: getting-start-with-subversion

[Subversion](http://subversion.tigris.org/)
被称为“下一代的版本控制系统”，当前风头正劲，已有盖过 CVS
之势。作为一种开放源码的全新版本控制系统，Subversion
支持本地访问或通过网络访问文件存储库，具有比较、修补、提交、分支等功能，可应用于包括开发在内的诸多领域。

本文是我在学习 Subversion 应用过程中的笔记心得，比较初步，兹供
Subversion 的新用户参考。

在本文中将用到 Subversion 的两个命令：

1.  svn－命令行的 Subversion 客户端程序
2.  svnadmin－该工具用于创建、调整、以及修补 Subversion 存储库

使用 Subversion 的一般过程大致包含以下几个步骤：

-   创建一个新的 Subversion 存储库。我们可以使用 svnadmin
    工具来完成该任务。假设我的 Subversion 存储库的位置在
    /home/xu/repos，则使用如下命令建立：  
    `svnadmin create /home/xu/repos`
-   整理相关文件及目录。如果我们需要对一些项目文件进行版本控制，首先创建三个目录：branches、tags
    和 trunk，并将所有的项目文件保存到 trunk 中。假定项目位于
    /home/xu/project，则在该目录中创建上述三个目录，且数据文件保存到
    trunk 目录。
-   导入 Subversion 存储库。现在，我们可以使用 svn
    命令行客户端将已整理好的项目文件导入存储库中。执行下列指令即可：  

    `svn import /home/xu/project file:///home/xu/repos/project -m "initial import"`
-   检出项目。该过程实际上是从 Subversion
    存储库创建一个用于工作的副本。你可以对这个工作副本进行常规的操作，如编辑、修改、添加、删除等等。总之，和我们平常的处理一样。为了从
    Subversion 存储库检出一个项目，可以使用下面的指令：  
    `svn checkout file:///home/xu/repos/project/trunk project`
-   查看修改。我们可以使用 `svn diff`
    指令来对所检出项目文件的修改情况进行查看。
-   提交修改。如果你需要把对于检出项目文件的修改提交回 Subversion
    存储库，则可用 `svn commit` 指令。
-   与存储库同步。若是你想要将检出的项目与当前的 Subversion
    存储库进行同步，可以执行 `svn update` 命令。

