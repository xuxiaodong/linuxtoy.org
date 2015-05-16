Title: APG：密码生成器
Date: 2008-08-25 09:51
Author: toy
Category: Apps
Tags: APG, Password Generator
Slug: apg

为了得到安全的保障，我们在很多时候、很多地方都会用到密码。如果密码设得太简单，则安全性将大打折扣。想设置复杂的密码，又怕费脑力，何不使用密码生成工具来助你一臂之力。Automated
Password Generator（简称“APG”）就是这样一个专门的密码生成器。

**安装 APG**

APG 这个工具在大多数 Linux
发行版的软件仓库中都有。因此，要安装它，你只需使用该发行版的包管理工具自动获取即可。

-   Archlinux：`# pacman -S apg`
-   Debian/Ubuntu：`# apt-get install apg`

**使用 APG**

不加任何参数在终端中执行 apg，将默认生成 6 个随机密码：  
` vodokByp BappOtfo dyocvith9 TeucOfPai RyudEnbo NantEcMa`

上面是在我的系统中执行 apg 的结果。

为了增加密码的难度，可以给 apg 加一些参数：

-   m - 指生成密码的最小位数，默认是 8
-   M mode -
    使用什么模式来生成密码，如密码包含大小写字母、数字、特殊字符等

例如，假设我们要生成一个 16
位且必须包含大写字母、小写字母、数字及特殊字符的密码，可以执行：

`apg -M SNCL -m 16`

其结果如下：  

` lev}TwookVadtak6 $onOdcedVoacyig8 Cyd6SlogOpchoik- 5Phu:SlujlepShug vig4draynItbycs- cevyet=ojRodreb3`

关于 apg 更详细的用法，可以 man apg。

**建议**

生成密码不妨考虑“84”规则，即密码至少 8 位，外加至少 1 个大写字母、1
个小写字母、1 个数字及 1 个特殊字符。
