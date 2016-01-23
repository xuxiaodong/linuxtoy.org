Title: Vimium: 以 Vim 的方式操作 Google Chrome
Date: 2009-12-13 18:05
Author: toy
Category: Google Chrome Extension
Tags: Google Chrome, Vim, Vimium
Slug: vimium

vi/Vim 的按键设置方案可说是非常经典，有的程序或对其直接予以支持（如 bash），或通过插件/扩展的形式实现一定程度的模拟。Vimium 就是这样一个 Google Chrome 扩展，它让你以 Vim 的方式来操作 Google Chrome 网络浏览器，既可以减少学习新按键设置的成本，又能够提高操作的效率。

![Vimium](http://i.linuxtoy.org/images/2009/12/vimium.png)

目前，Vimium 包括页面浏览、历史、标签页等方面的按键设置以及通过字母形式的 Hint 来处理链接的打开。相比另一个 Google Chrome 扩展 [Vimlike Smooziee](http://linuxtoy.org/archives/vimlike-smooziee.html)， Vimium 的功能要少点儿，但基本可用。

### 安装 Vimium

Vimium 的源代码主机在 github 上，因此要获取它，你需要 Git 工具，在准备好之后，在终端中执行以下命令：

    git clone git://github.com/philc/vimium.git

然后在 Google Chrome 的扩展页面中通过“Load unpacked extension...”按钮并定位到 Vimium 的源代码目录，接着按提示操作即可。

### Vimium 用法

**页面浏览**

+ j、k、h、l：向下/上/左/右滚动  
+ gg 和 G：移至页顶/页底  
+ Ctrl + d 和 Ctrl + u：下/上翻页  
+ zi 和 zo：放大/缩小

**历史**

+ H：后退  
+ L：前进

**标签页**

+ t：打开新标签  
+ d：关闭标签  
+ u：还原标签  
+ J/K：下/上一个标签

**Hint 模式**

+ f/F：进入 Hint 模式，后者会在新标签页中打开链接

### 提示

通过更改源代码目录中的 background\_page.html 文件可以重新绑定新的按键，以适合你的使用习惯。
