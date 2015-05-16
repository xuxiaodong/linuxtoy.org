Title: 两个 Shell 网站: explainshell 和 shellcheck
Date: 2013-12-03 23:15
Author: toy
Category: News
Slug: shell-sites

今天向大家介绍两个有意思的 Shell 网站，一个是
[explainshell.com][e]，另一个是  
[shellcheck.net][c]。

**explainshell**

![explainshell](/img/2013/12/explainshell.png)

先说 explainshell。explainshell
能够对命令行进行解析，然后对命令及其选项和参数  
提供相应的帮助说明。要是你遇到难以理解的复杂命令行，没准可以请求
explainshell  
来获得帮助。

explainshell 解析了 29761 篇 manpage（含 1 到 8 节），主要由  
Python、NLTK、d3.js、以及 Flask 打造而成。

**shellcheck**

![shellcheck](/img/2013/12/shellcheck.png)

再来说说 shellcheck。shellcheck 可以分析 sh/bash  
脚本，能够自动找出其中的问题，比如语法错误和陷阱。貌似对 sh/bash  
新手很有帮助。

explainshell 和 shellcheck
两个都提供有源代码，感兴趣的同学不妨亲自动手研究。

[e]: http://www.explainshell.com/  
[c]: http://www.shellcheck.net/
