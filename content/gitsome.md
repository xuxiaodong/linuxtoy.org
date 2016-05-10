Title: gitsome：非常棒的 Git/Shell 自动补全工具
Date: 2016-05-10 11:29:50
Authors: toy
Category: Cli
Tags: git, github, shell, python
Slug: gitsome
Via: gitsome|https://github.com/donnemartin/gitsome

作为一个每天都会使用 Git 的用户，对于要记太多命令这件事来说，我感觉真是乏味透了。有没有什么省力而又能提高效率的工具呢？在此，我强烈推荐 gitsome。

<!-- PELICAN_END_SUMMARY -->

[![gitsome]({filename}/images/gitsome.thumb.png)]({filename}/images/gitsome.png)

gitsome 不仅能够为你补全 Git 命令、选项、分支、标签，而且也支持补全 Shell 命令、文件、目录、环境变量、manpages 等。甚至更好的是，gitsome 还集成了对于 GitHub 的支持，这样你不用在命令行与浏览器之间进行切换便可完成各种操作。

gitsome 所具有的类似 Fish 的自动建议用起来十分方便，此外，它也包含命令历史，以及可定制语法着色等其他特色。

**安装**

gitsome 使用 Python 编写，只需通过 `pip` 即可安装：

    pip install gitsome

**使用**

直接执行：

    gitsome

**与 GitHub 集成**

使用前，需先按提示配置：

    gh configure
