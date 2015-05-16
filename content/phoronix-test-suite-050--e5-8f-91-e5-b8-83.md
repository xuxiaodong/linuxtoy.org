Title: Phoronix Test Suite 0.5.0 发布(更新0.5.1版本)
Date: 2008-05-02 22:32
Author: lovenemesis
Category: Apps
Tags: phoronix
Slug: phoronix-test-suite-050-%e5%8f%91%e5%b8%83

5月1日，Phoronix 发布其名下的 Phoronix Test Suite 0.5.0
版本。该版本包含了多达40项的重大变化，并且宣布了1.0版本将在7月上旬发布的消息。

5月5日，Phoronix再度发布了该测试套件的0.5.1修正版本。  
  

首次引入了基于espeak的文本发音引擎测试。压缩／解压缩评测在原先GZip的基础上增加了
7z 和并行 Bzip2
的测试。针对多核系统添加了一个专用的测试集合，该测试包含了 mplayer, php,
imagemagick 的编译，以及 sunflow, 7z 压缩和并行 bzip2
压缩测试。现在，Phoronix Test Suite 0.5.0
总共包含了34个测试预置文件和12个测试集合。

Phoronix Test Suite 0.5.0
强化用脚本管理测试用文件下载过程的能力，方便了有大量测试工作的批量化标准化进行。测试套件的安装、预运行和测试后动作都可以用
PHP 写成的脚本进行管理，以前只能用 BASH
脚本管理。与此配套的，测试套件可以正确处理绝大多数发行版中 php 和 php5
的符号连接问题，从而获得正确的 php 解析程序。

同时，该版本包括了全新的温度探测功能，不仅可以探测出系统使用的是何种节能技术处于何种工作状态，还可以监视在测试过程中
CPU 和 GPU
的运行温度变化，配合改进的图表生成程序，还可以得到详细的温度变化折线图。目前GPU温度的探测仅支持
Nvidia，AMD 显卡的支持需要 AMD 方面在接口做出一些改进后很快就能实现。  

![温度测试折线图](http://www.phoronix.com/data/img/results/pts_050/1.png)  
此外，还增加了一些新的命令行选项，如：emove-all-results, force-install,
version, 和 sensor-options。

Phoronix Test Suite 0.5.1版本更新情况：

-   修正一个关于屏幕保护探测的Bug。
-   将所有的XML接口路径指向到*pts-core/functions/pts-functions\_interfaces.php*
-   增加了一个OpenSSL RSA 测试 (该测试同样包含在多核测试集里)。
-   该版本同时引入了PCQS (**P**horonix **C**ertification &
    **Q**ualification **S**uite)
    测试预置文件。该文件用来对服务器/工作站的主板提供相关评测，并反馈到Phoronix上。

[测试套件主页及下载地址](http://www.phoronix-test-suite.com/)  

