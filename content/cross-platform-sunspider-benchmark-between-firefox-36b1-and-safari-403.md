Title: 跨平台 Firefox 3.6 Beta 1 与 Safari 4.0.3 Sunspider 评测比较
Date: 2009-11-03 02:15
Author: lovenemesis
Category: Featured
Tags: Firefox, safari, sunspider
Slug: cross-platform-sunspider-benchmark-between-firefox-36b1-and-safari-403

随着 Google Chrome 版本号的猛增和 Firefox 3.6 Beta
版本的发布，新一轮的浏览器大战又将开始了。今天的比试的两个JavaScript
引擎是 Mozilla Firefox 的 SpiderMonkey 和 Apple Safari 的
Nitro，与之前不同的是，这次战场在苹果“小白”上展开。

**参评软件：**

Mozilla Firefox 3.6 Beta 1  
Apple Safari 4.0.3

**测试工具：**

[Sunspider 0.9 JavaScript
Benchmark](http://www2.webkit.org/perf/sunspider-0.9/sunspider.html)

**硬件平台：**

**CPU：**Intel Core 2 Duo T7200 2GHz  
**内存：** DDR2 667MHz 2GB

**软件平台：**

Windows XP SP2  
Mac OS X 10.6.1 Snow Leopard

**第一轮：Mac OS X 10.6.1 Snow Leopard**

Firefox @ OSX: [1239.4ms +/-
1.0%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B59,60,58,58,60%5D,%223d-morph%22:%5B33,34,34,34,37%5D,%223d-raytrace%22:%5B88,86,84,84,86%5D,%22access-binary-trees%22:%5B58,62,57,56,53%5D,%22access-fannkuch%22:%5B80,78,74,78,78%5D,%22access-nbody%22:%5B37,38,38,37,38%5D,%22access-nsieve%22:%5B16,17,16,17,15%5D,%22bitops-3bit-bits-in-byte%22:%5B3,2,2,2,2%5D,%22bitops-bits-in-byte%22:%5B13,13,11,13,15%5D,%22bitops-bitwise-and%22:%5B4,3,3,4,4%5D,%22bitops-nsieve-bits%22:%5B30,32,30,31,32%5D,%22controlflow-recursive%22:%5B43,43,42,42,43%5D,%22crypto-aes%22:%5B41,40,41,40,38%5D,%22crypto-md5%22:%5B18,17,17,17,17%5D,%22crypto-sha1%22:%5B14,10,10,10,10%5D,%22date-format-tofte%22:%5B116,110,112,112,113%5D,%22date-format-xparb%22:%5B91,88,88,88,87%5D,%22math-cordic%22:%5B13,12,12,13,12%5D,%22math-partial-sums%22:%5B19,19,20,20,19%5D,%22math-spectral-norm%22:%5B9,8,8,9,9%5D,%22regexp-dna%22:%5B73,69,70,72,69%5D,%22string-base64%22:%5B16,16,17,16,16%5D,%22string-fasta%22:%5B90,90,91,92,90%5D,%22string-tagcloud%22:%5B119,118,125,119,120%5D,%22string-unpack-code%22:%5B133,135,133,134,133%5D,%22string-validate-input%22:%5B40,39,38,38,39%5D%7D)  
Safari @ OSX: [570.8ms +/-
1.9%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B22,24,22,22,24%5D,%223d-morph%22:%5B32,26,29,31,30%5D,%223d-raytrace%22:%5B23,26,22,23,23%5D,%22access-binary-trees%22:%5B8,7,7,7,7%5D,%22access-fannkuch%22:%5B21,20,21,21,21%5D,%22access-nbody%22:%5B14,15,15,16,16%5D,%22access-nsieve%22:%5B14,10,11,11,12%5D,%22bitops-3bit-bits-in-byte%22:%5B5,4,5,4,5%5D,%22bitops-bits-in-byte%22:%5B12,12,12,11,12%5D,%22bitops-bitwise-and%22:%5B7,7,7,7,7%5D,%22bitops-nsieve-bits%22:%5B12,9,11,10,11%5D,%22controlflow-recursive%22:%5B6,4,5,5,5%5D,%22crypto-aes%22:%5B16,17,16,16,16%5D,%22crypto-md5%22:%5B8,8,9,9,8%5D,%22crypto-sha1%22:%5B7,7,8,8,7%5D,%22date-format-tofte%22:%5B34,37,36,37,35%5D,%22date-format-xparb%22:%5B42,45,41,43,44%5D,%22math-cordic%22:%5B13,13,14,15,15%5D,%22math-partial-sums%22:%5B25,26,28,27,27%5D,%22math-spectral-norm%22:%5B10,10,12,12,12%5D,%22regexp-dna%22:%5B30,31,27,27,28%5D,%22string-base64%22:%5B21,22,21,23,21%5D,%22string-fasta%22:%5B39,45,39,40,38%5D,%22string-tagcloud%22:%5B45,45,42,42,43%5D,%22string-unpack-code%22:%5B63,67,60,60,60%5D,%22string-validate-input%22:%5B44,47,40,42,41%5D%7D)

在 OS X 系统下，Safari 比 Firefox 快了 2.17x 倍！  

[点击此下载PDF测试报告](http://dl.getdropbox.com/u/464139/Firefox_vs_Safari/Firefox_vs_Safari_OSX.pdf)

**第二轮：Windows XP SP2**

Firefox @ WIN: [1734.0ms +/-
5.2%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B89,86,93,46,88%5D,%223d-morph%22:%5B110,112,110,110,108%5D,%223d-raytrace%22:%5B138,133,133,123,73%5D,%22access-binary-trees%22:%5B88,93,91,89,89%5D,%22access-fannkuch%22:%5B140,144,143,143,149%5D,%22access-nbody%22:%5B54,51,52,51,52%5D,%22access-nsieve%22:%5B27,26,26,27,27%5D,%22bitops-3bit-bits-in-byte%22:%5B3,3,4,3,3%5D,%22bitops-bits-in-byte%22:%5B28,19,29,28,28%5D,%22bitops-bitwise-and%22:%5B7,6,7,7,6%5D,%22bitops-nsieve-bits%22:%5B57,55,54,54,52%5D,%22controlflow-recursive%22:%5B71,94,96,92,95%5D,%22crypto-aes%22:%5B49,34,71,77,68%5D,%22crypto-md5%22:%5B17,29,30,29,30%5D,%22crypto-sha1%22:%5B11,17,17,18,17%5D,%22date-format-tofte%22:%5B84,144,145,113,151%5D,%22date-format-xparb%22:%5B78,130,133,100,139%5D,%22math-cordic%22:%5B69,68,70,70,71%5D,%22math-partial-sums%22:%5B38,39,39,26,40%5D,%22math-spectral-norm%22:%5B15,15,14,8,16%5D,%22regexp-dna%22:%5B63,64,64,82,65%5D,%22string-base64%22:%5B23,23,23,11,24%5D,%22string-fasta%22:%5B128,130,121,131,135%5D,%22string-tagcloud%22:%5B86,95,87,89,102%5D,%22string-unpack-code%22:%5B95,99,94,93,92%5D,%22string-validate-input%22:%5B61,72,43,65,66%5D%7D)  
Safari @ WIN: [1465.6ms +/-
1.7%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B112,107,107,108,105%5D,%223d-morph%22:%5B109,106,108,107,109%5D,%223d-raytrace%22:%5B80,81,84,82,82%5D,%22access-binary-trees%22:%5B13,13,12,12,12%5D,%22access-fannkuch%22:%5B36,35,35,36,36%5D,%22access-nbody%22:%5B77,79,78,77,78%5D,%22access-nsieve%22:%5B15,14,15,14,14%5D,%22bitops-3bit-bits-in-byte%22:%5B6,7,7,7,7%5D,%22bitops-bits-in-byte%22:%5B16,16,16,17,16%5D,%22bitops-bitwise-and%22:%5B12,8,8,8,8%5D,%22bitops-nsieve-bits%22:%5B37,36,37,38,37%5D,%22controlflow-recursive%22:%5B8,8,7,7,7%5D,%22crypto-aes%22:%5B31,31,30,29,29%5D,%22crypto-md5%22:%5B39,38,39,40,40%5D,%22crypto-sha1%22:%5B41,42,40,41,40%5D,%22date-format-tofte%22:%5B67,67,69,68,67%5D,%22date-format-xparb%22:%5B88,84,92,92,93%5D,%22math-cordic%22:%5B69,70,71,71,71%5D,%22math-partial-sums%22:%5B109,113,112,111,110%5D,%22math-spectral-norm%22:%5B37,37,37,38,37%5D,%22regexp-dna%22:%5B55,51,51,51,50%5D,%22string-base64%22:%5B50,48,51,50,50%5D,%22string-fasta%22:%5B92,95,91,95,89%5D,%22string-tagcloud%22:%5B87,85,86,85,85%5D,%22string-unpack-code%22:%5B121,120,122,118,121%5D,%22string-validate-input%22:%5B73,73,73,73,38%5D%7D)

在 Windows 系统下， Safari 依然领先，不过仅仅快了 1.18 倍。  

[点击此下载PDF测试报告](http://dl.getdropbox.com/u/464139/Firefox_vs_Safari/Firefox_vs_Safari_WIN.pdf)

根据上面两轮得到的数据，再对同一浏览器在两个平台上的结果进行比较。

**第三轮：Mozilla Firefox 3.6 Beta 1**

Firefox @ OSX: [1239.4ms +/-
1.0%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B59,60,58,58,60%5D,%223d-morph%22:%5B33,34,34,34,37%5D,%223d-raytrace%22:%5B88,86,84,84,86%5D,%22access-binary-trees%22:%5B58,62,57,56,53%5D,%22access-fannkuch%22:%5B80,78,74,78,78%5D,%22access-nbody%22:%5B37,38,38,37,38%5D,%22access-nsieve%22:%5B16,17,16,17,15%5D,%22bitops-3bit-bits-in-byte%22:%5B3,2,2,2,2%5D,%22bitops-bits-in-byte%22:%5B13,13,11,13,15%5D,%22bitops-bitwise-and%22:%5B4,3,3,4,4%5D,%22bitops-nsieve-bits%22:%5B30,32,30,31,32%5D,%22controlflow-recursive%22:%5B43,43,42,42,43%5D,%22crypto-aes%22:%5B41,40,41,40,38%5D,%22crypto-md5%22:%5B18,17,17,17,17%5D,%22crypto-sha1%22:%5B14,10,10,10,10%5D,%22date-format-tofte%22:%5B116,110,112,112,113%5D,%22date-format-xparb%22:%5B91,88,88,88,87%5D,%22math-cordic%22:%5B13,12,12,13,12%5D,%22math-partial-sums%22:%5B19,19,20,20,19%5D,%22math-spectral-norm%22:%5B9,8,8,9,9%5D,%22regexp-dna%22:%5B73,69,70,72,69%5D,%22string-base64%22:%5B16,16,17,16,16%5D,%22string-fasta%22:%5B90,90,91,92,90%5D,%22string-tagcloud%22:%5B119,118,125,119,120%5D,%22string-unpack-code%22:%5B133,135,133,134,133%5D,%22string-validate-input%22:%5B40,39,38,38,39%5D%7D)  
Firefox @ WIN: [1734.0ms +/-
5.2%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B89,86,93,46,88%5D,%223d-morph%22:%5B110,112,110,110,108%5D,%223d-raytrace%22:%5B138,133,133,123,73%5D,%22access-binary-trees%22:%5B88,93,91,89,89%5D,%22access-fannkuch%22:%5B140,144,143,143,149%5D,%22access-nbody%22:%5B54,51,52,51,52%5D,%22access-nsieve%22:%5B27,26,26,27,27%5D,%22bitops-3bit-bits-in-byte%22:%5B3,3,4,3,3%5D,%22bitops-bits-in-byte%22:%5B28,19,29,28,28%5D,%22bitops-bitwise-and%22:%5B7,6,7,7,6%5D,%22bitops-nsieve-bits%22:%5B57,55,54,54,52%5D,%22controlflow-recursive%22:%5B71,94,96,92,95%5D,%22crypto-aes%22:%5B49,34,71,77,68%5D,%22crypto-md5%22:%5B17,29,30,29,30%5D,%22crypto-sha1%22:%5B11,17,17,18,17%5D,%22date-format-tofte%22:%5B84,144,145,113,151%5D,%22date-format-xparb%22:%5B78,130,133,100,139%5D,%22math-cordic%22:%5B69,68,70,70,71%5D,%22math-partial-sums%22:%5B38,39,39,26,40%5D,%22math-spectral-norm%22:%5B15,15,14,8,16%5D,%22regexp-dna%22:%5B63,64,64,82,65%5D,%22string-base64%22:%5B23,23,23,11,24%5D,%22string-fasta%22:%5B128,130,121,131,135%5D,%22string-tagcloud%22:%5B86,95,87,89,102%5D,%22string-unpack-code%22:%5B95,99,94,93,92%5D,%22string-validate-input%22:%5B61,72,43,65,66%5D%7D)

从中可以看出， Firefox 3.6 Beta 1 在 Windows 平台下的表现要略逊于 OS X
平台，大约慢了 1.4 倍。  

[点击此下载PDF测试报告](http://dl.getdropbox.com/u/464139/Firefox_vs_Safari/Firefox_OSX_vs_WIN.pdf)

**第四轮： Apple Safari 4.0.3**

Safari @ OSX: [570.8ms +/-
1.9%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B22,24,22,22,24%5D,%223d-morph%22:%5B32,26,29,31,30%5D,%223d-raytrace%22:%5B23,26,22,23,23%5D,%22access-binary-trees%22:%5B8,7,7,7,7%5D,%22access-fannkuch%22:%5B21,20,21,21,21%5D,%22access-nbody%22:%5B14,15,15,16,16%5D,%22access-nsieve%22:%5B14,10,11,11,12%5D,%22bitops-3bit-bits-in-byte%22:%5B5,4,5,4,5%5D,%22bitops-bits-in-byte%22:%5B12,12,12,11,12%5D,%22bitops-bitwise-and%22:%5B7,7,7,7,7%5D,%22bitops-nsieve-bits%22:%5B12,9,11,10,11%5D,%22controlflow-recursive%22:%5B6,4,5,5,5%5D,%22crypto-aes%22:%5B16,17,16,16,16%5D,%22crypto-md5%22:%5B8,8,9,9,8%5D,%22crypto-sha1%22:%5B7,7,8,8,7%5D,%22date-format-tofte%22:%5B34,37,36,37,35%5D,%22date-format-xparb%22:%5B42,45,41,43,44%5D,%22math-cordic%22:%5B13,13,14,15,15%5D,%22math-partial-sums%22:%5B25,26,28,27,27%5D,%22math-spectral-norm%22:%5B10,10,12,12,12%5D,%22regexp-dna%22:%5B30,31,27,27,28%5D,%22string-base64%22:%5B21,22,21,23,21%5D,%22string-fasta%22:%5B39,45,39,40,38%5D,%22string-tagcloud%22:%5B45,45,42,42,43%5D,%22string-unpack-code%22:%5B63,67,60,60,60%5D,%22string-validate-input%22:%5B44,47,40,42,41%5D%7D)  
Safari @ WIN: [1465.6ms +/-
1.7%](http://www2.webkit.org/perf/sunspider-0.9/sunspider-results.html?%7B%223d-cube%22:%5B112,107,107,108,105%5D,%223d-morph%22:%5B109,106,108,107,109%5D,%223d-raytrace%22:%5B80,81,84,82,82%5D,%22access-binary-trees%22:%5B13,13,12,12,12%5D,%22access-fannkuch%22:%5B36,35,35,36,36%5D,%22access-nbody%22:%5B77,79,78,77,78%5D,%22access-nsieve%22:%5B15,14,15,14,14%5D,%22bitops-3bit-bits-in-byte%22:%5B6,7,7,7,7%5D,%22bitops-bits-in-byte%22:%5B16,16,16,17,16%5D,%22bitops-bitwise-and%22:%5B12,8,8,8,8%5D,%22bitops-nsieve-bits%22:%5B37,36,37,38,37%5D,%22controlflow-recursive%22:%5B8,8,7,7,7%5D,%22crypto-aes%22:%5B31,31,30,29,29%5D,%22crypto-md5%22:%5B39,38,39,40,40%5D,%22crypto-sha1%22:%5B41,42,40,41,40%5D,%22date-format-tofte%22:%5B67,67,69,68,67%5D,%22date-format-xparb%22:%5B88,84,92,92,93%5D,%22math-cordic%22:%5B69,70,71,71,71%5D,%22math-partial-sums%22:%5B109,113,112,111,110%5D,%22math-spectral-norm%22:%5B37,37,37,38,37%5D,%22regexp-dna%22:%5B55,51,51,51,50%5D,%22string-base64%22:%5B50,48,51,50,50%5D,%22string-fasta%22:%5B92,95,91,95,89%5D,%22string-tagcloud%22:%5B87,85,86,85,85%5D,%22string-unpack-code%22:%5B121,120,122,118,121%5D,%22string-validate-input%22:%5B73,73,73,73,38%5D%7D)

Safari 显然水土不服，在 Windows 平台下的表现的远远不如在 OS X
平台下的，足足慢了 2.57 倍！  

[点击此下载PDF测试报告](http://dl.getdropbox.com/u/464139/Firefox_vs_Safari/Safari_OSX_vs_WIN.pdf)

**总结：**

Mozilla Firefox 3.6 Beta 1 相对于 3.5.X 系列对于 SpiderMonkey
的有大约10%的提升，但是相比 Apple Safari 的 Nitro
引擎，还是有不小的差距，尤其是在 OS X 平台上。当然，在 JavaScript
引擎本地化方面，Mozilla Firefox
做为横跨多个操作平台的浏览器工作量可能要大些，Apple 而只需要关注 Windows
和 OS X 即可。

在跨平台应用方面，两款浏览器的表现在 Windows 平台下都有下降，Safari
下降幅度惊人。此点要不是证明了 Safari 在 OS X 优化做的好，要不就是
Safari 在 Windows
的优化做的太差。不过两款浏览器在同样硬件条件下，平台的切换导致的下降似乎也可以归咎于
Windows 系统本身。

Mozilla Firefox
用了10年的时间，证明了浏览器在互联网时代桌面应用的地位，让很多人意识到原来上网不仅可以用那个蓝色的e。  
曾经，JavaScrpit 的执行速度是它藐视 IE 的王牌，现在有了速度更快的 Apple
Safari 和 Google Chrome。  
曾经，开放源代码和跨平台是它受到开源爱好者的欢迎，现在 Google Chrome
也是开源和（即将）跨平台的了。  
Mozilla Firefox
曾经的王牌的正在一个个被竞争对手超越，目前唯一尚未被超越的是十年积攒下来的庞大的扩展库。

评测结束了，思考还在继续。Mozilla Firefox
的未来的道路依然坎坷：面对新晋的对手，面对偏安一隅的
Opera，面对性能吊车尾但是占有率排第一的 IE……
在此，只能由衷祝福这只热情的小狐狸了……

**致谢：**

十分感谢舍友 [VF22](mailto:MACROSS7@qq.com) 童鞋提供苹果小白做测试！

**参考资料：**

[History of Mozilla Project](http://www.mozilla.org/about/history.html)

**PS:**  
SpiderMonkey 是 Mozilla Firefox 的 JavaScript 的代号，而在 3.5.X 引进的
TraceMonkey 是 SpiderMonkey 的本地化 C
实现。详情见[这里](https://wiki.mozilla.org/JavaScript:TraceMonkey)。
