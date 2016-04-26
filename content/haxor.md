Title: haxor-news：从终端浏览 Hacker News
Date: 2016-04-26 22:18:34
Authors: toy
Category: Cli
Tags: terminal
Slug: haxor
Via: haxor-news|https://github.com/donnemartin/haxor-news

[Hacker News][h] 是我经常访问的一个网站，在它上面有网友提交的各种技术文章链接，浏览时常有意外发现。虽然我们可以通过 Web 浏览器访问它，但是 haxor-news 却提供了另一种浏览方式——从终端命令行——可谓别有风味。

<!-- PELICAN_END_SUMMARY -->

[![haxor-news]({filename}/images/haxor.thumb.png)]({filename}/images/haxor.png)

haxor-news 使用 Python 语言编写而成，通过 `pip` 工具即可将其安装到系统中：

    pip install haxor-news

当执行 `haxor-news` 后，即进入 haxor-news 的命令模式，便可按如下方式进行浏览：

    hn <command> [params] [options]

比如，我们执行 `hn top` 可以查看最热门的 10 条信息；如果要浏览某个具体链接的内容，则执行 `hn view 2`（其中 2 为所在连接的序号）即可。值得一提的是，haxor-news 具有命令自动补全功能，它会根据所选命令加以提示，并不需要专门去记忆。

[h]: https://news.ycombinator.com/
