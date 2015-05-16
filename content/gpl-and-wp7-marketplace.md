Title: GPL 与 WP7 Marketplace
Date: 2011-02-18 08:28
Author: lovenemesis
Category: Featured
Tags: GPL, oss, wp7
Slug: gpl-and-wp7-marketplace

WP7 的 Marketplace 使用条款中**明确禁止了采用 ~~GPLv3 系列~~排他性协议
a.k.a 开源协议的软件**发布。

根据 [H Open
的报道](http://www.h-online.com/open/news/item/Microsoft-bans-free-software-from-Windows-Phone-Marketplace-1191524.html)，在
WP7 Marketplace 当前的使用条款 5.e
章节中，明确禁止使用**排他性协议**的软件发布，包括但不局限于 GPLv3
系列协议(*Excluded Licenses include, but are not limited to the GPLv3
Licenses*)，其中包括 GPLv3(General Public Licnce (GPL) version
3)、AGPLv3(GNU Affero GPL version 3)、LGPLv3(GNU Lesser GPL version 3)
。

Marketplace 中的内容包含 DRM
锁，意味着即使是**免费的程序用户也无法通过非 Marketplace
的方式与他人分享**。

在下借此机会提醒诸位希望在 WP7 Marketplace 上发布软件的朋友：

-   **避免移植或使用 ~~GPLv3 系列授权~~任何开源软件的程序或软件库**。
-   使用**双重授权方式**，但是需要**得到所有代码贡献者的同意**。

同时，希望也能看到你们的程序出现在 GPL-compatible 的 Android Market 中。

**PS: Marketplace 关于排他性协议定义的章节原文**

*“Excluded License” means any license requiring, as a condition of use,
modification and/or distribution of the software subject to the license,
that the software or other software combined and/or distributed with it
be **(i) disclosed or distributed in source code form; (ii) licensed for
the purpose of making derivative works; or (iii) redistributable at no
charge**. Excluded Licenses include, but are not limited to the GPLv3
Licenses. For the purpose of this definition, “GPLv3 Licenses” means the
GNU General Public License version 3, the GNU Affero General Public
License version 3, the GNU Lesser General Public License version 3, and
any equivalents to the foregoing.*

[WP7 Marketplace
协议授权官方英文全文](http://create.msdn.com/en-us/home/legal/Windows_Phone_Marketplace_Application_Provider_Agreement)

**非官方翻译（仅供参考）：**

排他性协议指依据其内容，在使用、修改或者分发的过程中，允许该软件或者该软件集成或一并分发的软件存在1)源代码开放或允许分发；2）允许衍生产品工作；3）免费再次分发
的协议。排他性协议包括但不限于 GPLv3 协议。这里的 GPLv3 协议包括
GPLv3(General Public Licnce (GPL) version 3)、AGPLv3(GNU Affero GPL
version 3) 和 LGPLv3(GNU Lesser GPL version 3)。

**更新：**

[根据进一步的报道](http://blogs.computerworlduk.com/simon-says/2011/02/microsoft-bans-its-own-licenses/index.htm)，**GPLv2
系列、EPL(Eclipse Public License) 、 MPL(Mozilla Public License)
、BSD、MIT 和 APLv2(Apache Public License)
协议的程序和软件库也被符合"排他性协议"**的定义，甚至包括 M$ 自己的
**Microsoft Reciprocal License 和 Microsoft Public License 协议**！

值得特别注意的是，**采用Nokia Qt GPL/LGPL 开源版本编写的程序也不可加入
WP7 Marketplace**，甚至**基于 Mono 的程序(MIT X11, Microsoft Public
License 和 APLv2 授权)也不可以！**
