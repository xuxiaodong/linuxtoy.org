linuxtoy.org
------------

这是 [LinuxTOY][l] 网站的源代码，原来采用 WordPress，现迁移到 Pelican，其中包括：

- content：所有文章，为 Markdown 格式
- themes：Pelican 主题
- plugins：Pelican 插件
- pelicanconf.py：Pelican 配置文件
- develop_server.sh：开发脚本
- Makefile：Make 构建脚本

## 如何使用

参照 [Pelican 快速入门][p] 安装 Pelican。

## 新建文章

为了保持一致性，推荐 Markdown 格式，包括文章元数据和正文两个部分，例如：

    Title: (标题)
    Date: 2010-12-03 10:20 (创建日期)
    Modified: 2010-12-05 19:30 (修改日期)
    Category: Python (分类)
    Tags: pelican, publishing (标签)
    Slug: my-super-post (slug，将用于 url)
    Authors: (作者)
    Summary: (摘要)

    这是正文。

## 添加语法

可对引用代码添加语法高亮显示，写法如下：

    A block of text. (正常文本)

        :::identifier (标识符，如 python)
        <code goes here> (具体的代码)

[l]: http://linuxtoy.org
[p]: http://docs.getpelican.com/en/3.5.0/quickstart.html
