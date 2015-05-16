Title: Gemfury
Date: 2014-12-04 13:02
Author: lovenemesis
Category: News
Tags: gemfury
Slug: gemfury

Gemfury 是一个提供私有包托管的服务站点，提供对于 Ruby Gems, Node.js npm,
php Composer, Python PyPl, Debian apt/deb 及 RPM yum
多种包管理格式的支持。适合个人开发者及中小企业。

常见的 PPA 或者 COPR
均是公开的，不适合小范围传播或者封闭开发。固然可以在 VPS
上自己搭建，不过过程及维护就麻烦不少了。Gemfury
的运行理念很简单，提供您一个**非公开**的在线仓库，方便进行部署或多人协作。个人的仓库的地址中都包含访问仅有自己可知的访问密钥。以它页面上
RPM YUM 仓库为例：

[fury]  
name=Gemfury Private Repo  
baseurl=https://SeCrEt-ToKeN@yum.fury.io/me/  
enabled=1  
gpgcheck=0

可见其中的私人密钥。

不过 Gemfury 并非一个完全免费的服务，在 [14
天的免费试用](https://gemfury.com/signup)后，您需要在限制包数但**不限协作者**的[商业计划](https://gemfury.com/plans)或**不限包数但限制协作者**的[个人计划](https://gemfury.com/plans/personal)中选择，价格还算可以接受。每月
9
美元可以获得**不限制包数量、历史版本的公共或私有软件仓库**托管，对于个人开发者来说完全够用。若是
2 -3 个人的小团队，每月 14 美元即可将其提升至最多 5
个协作者。此外成为协作者是免费的，整个小团队只需付一次费用即可。

[Gemfury 主页](https://gemfury.com/)
