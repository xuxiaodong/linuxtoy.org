Title: End of Sun RPC License 
Date: 2010-08-27 05:52
Author: lovenemesis
Category: News
Tags: Fedora, nfs, Sun
Slug: end-of-sun-rpc-license

1984 年 Sun Microsystem 对 [RFC 707](http://tools.ietf.org/html/rfc707)
的实现，影响着所有类 Unix 系统（包括Linux）的 NFS
相关组件。而它的授权协议类型，却并不是和自由软件协议相兼容的。直到 2010
年8月18日……摘译自 [spot 博客](http://spot.livejournal.com/315383.html)

由于 Sun RPC 授权协议，做为一个发行版的，只有如下三种选择：

-   选择不支持 NFS。
-   用其他自由软件相兼容授权的代码取代。问题是 Sun 的 RPC 几乎是 Unix
    类的标准，绕过它而使用其他替代品很麻烦。
-   尝试获得代码的自由软件相兼容授权。

Fedora 和 Debian 一样，选择了第3个方式。

经过和 Sun 多次交涉后，2009年3月，Red Hat 获得了 rpcbind
0.1.6、nfs-utils-lib 1.1.3、nfs-utils 1.1.3、libtirpc-0.1.9 和
portablexdr 4.0.11 中该 RPC 相关实现代码的 BSD
再授权权利。但是，还剩下了 glibc、krb5 和 netkit-rusers
中的相关代码没有。

又经过一番努力，在 2010 年8月18日，现在的 Oracle 终于允许将 glibc、krb5
和 netkit-rusers 中的 RPC 代码以 BSD 协议分发了。

意味着什么？ 100% Free 发行版从这一天可以真的 100% Free 了。

**后记：**只为传达些自由软件界一些非代码的动态，Free Software is not
just about coding。翻译粗糙，望见谅~
