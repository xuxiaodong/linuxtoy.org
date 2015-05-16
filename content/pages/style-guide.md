Title: 格式指南
Date: 2008-11-02 16:27
Author: toy
Slug: style-guide
Status: hidden

请各位作者在 LinuxTOY 上发文时采用以下格式。

### 常用语法

**小节标题**

可使用 h3 标签：

`<h3>这是一个 h3 标题</h3>`

输出：

### 这是一个 h3 标题

**强调**

加粗，可使用 strong 标签：

`<strong>加粗</strong>`

输出：

**加粗**

斜体，可使用 em 标签：

`<em>斜体</em>`

输出：

*斜体*

**列表**

无序列表，可使用 ul 标签，列表项目用 li 标签：


    <ul>
    <li>项目 1</li>
    <li>项目 2</li>
    <li>项目 3</li>
    </ul>

输出：

-   项目 1
-   项目 2
-   项目 3

有序列表，可使用 ol 标签，列表项目用 li 标签：


    <ol>
    <li>项目 1</li>
    <li>项目 2</li>
    <li>项目 3</li>
    </ol>

输出：

1.  项目 1
2.  项目 2
3.  项目 3

**引用**

可使用 blockquote 标签：

`<blockquote>这里是引用的内容。</blockquote>`

输出：

> 这里是引用的内容。

**插入链接**

可使用 a 标签：

`<a href="http://linuxtoy.org">LinuxTOY</a>`

输出：

[LinuxTOY](http://linuxtoy.org)

**插入图像**

可使用 img 标签：

`<img src="http://linuxtoy.org/spreadlinuxtoy.png" alt="Spread LinuxTOY" />`

输出：

![Spread LinuxTOY](http://linuxtoy.org/spreadlinuxtoy.png)

**插入代码**

可使用 code 标签：

`<code>ls -lsh</code>`

输出：

`ls -lsh`

### 撰文提示

1.  在适当的位置插入 more (`<!--more-->`)
    标记，可以让其前面的内容作为文章摘要显示在网站首页。
2.  加入 Featured 分类的文章将额外添加到网站首页的 Featured entries 区。
3.  请适当编辑文章标题下面的
    Permalink，尽量避免使用中文，以确保文章网址在某些浏览器中不出现乱码。
4.  可使用 `<!--nextpage-->` 对文章进行分页。
5.  不要随意删除 Post，若不满意，可保存为草稿，再作修改。

