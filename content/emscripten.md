Title: Emscripten
Date: 2011-12-21 14:55
Author: lovenemesis
Category: Development
Tags: emscripten, javascript
Slug: emscripten

Emscripten 是 Mozilla 的 Alon Zakai 开发的一个独特 LLVM 后端，可以将任意
[LLVM 中间码](www.aosabook.org/en/llvm.html)编译成
JavaScript，大大简化了现有代码在 Web 时代的重用。

和[Google
Chrome](http://linuxtoy.org/archives/google-chrome-14-beta.html)尝试通过自有的
[Native Client](https://developers.google.com/native-client/) 在 Web
中利用现有 C/C++ 库的方式不同，Mozilla 寻求了一条普适性更强的解决方案。

Emscripten 并非通常的 LLVM 后端，本身使用 JavaScript
写成。它可以**将任何通过 LLVM 前端(比如 C/C++ Clang )生成的 LLVMIR
中间码编译成 JavaScript**，从而显著降低移植现有代码库到 Web 环境的损耗。

目前 **Emscripten 已经比较成熟，准备发布 2.0
版本**了。很多大型的项目已经可以使用 Emscripten 转换为 JavaScript
了，比如 [Python, Ruby, Lua](http://repl.it/) 和
[Doom](http://linuxtoy.org/archives/javascript-doom.html)。

根据 [2011 年 5 月份的演示中用 Firefox
的测试结果](http://syntensity.com/static/jsconf_eu_Emscripten_lo.pdf)显示，通过
Emscripten 1.0 得出的 JavaScript 在未经优化的情况，在不同的测试中比
gcc -O3 的原始 C/C++ 代码约慢了 89% ~ 375% 左右。Alon
表示在使用了[类型推测](http://blog.mozilla.com/futurereleases/2011/11/10/type-inference-to-firefox-beta/)等优化后性能会有进一步提升。

[使用 Emscripten 转换后的 Bullet/WebGL
物理引擎演示](http://www.syntensity.com/static/ammo.html)

[Alon Zakai 在 LLVM 邮件列表中关于 Emscripten
的说明](http://lists.cs.uiuc.edu/pipermail/llvmdev/2011-December/046294.html)

[Emscription Github 首页](https://github.com/kripken/emscripten/wiki)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTAzMDk)
