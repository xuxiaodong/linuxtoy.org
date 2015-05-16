Title: 在 Bash 中删除除某些文件外的所有文件
Date: 2014-06-04 13:01
Author: toy
Category: Tips
Slug: rm_tip

我的一位同事曾经问过我这样一个问题：在 Linux 下，如何  
删除目录中除某些文件之外的所有文件？当时，我告诉他可  
以通过模式匹配的方法解决。但其实，除此之外，还有其他  
的方法，正所谓“条条大路通罗马”。让我们来逐一看看。

假设要删除 ~/Downloads 目录中除 *.iso 和 *.zip 外的  
所有文件，那么在 bash 中可以按以下方法处理。

**模式匹配法**

shopt -s extglob # 确认开启 extglob 选项  
cd ~/Downloads  
rm -v !(*.iso|*.zip)

`!(pattern list)` 的作用是匹配除 pattern list 之外  
的文件。

**设置变量法**

在 bash 中，`GLOBIGNORE` 可用来设置要忽略的模式匹配  
文件，多个模式通过 : 分隔。

cd ~/Downloads  
export GLOBIGNORE=*.zip:*.iso  
rm -v *  
unset GLOBIGNORE

**find 搜索法**

熟悉 find 的朋友想必知道，find 的威力异常强大，因此  
利用它也可解决此问题。

cd ~/Downloads  
find . -type f -not \\( -name '*.zip' -or -name '*.iso' \\) -delete

{
[via](http://www.cyberciti.biz/faq/linux-bash-delete-all-files-in-directory-except-few/)
}
