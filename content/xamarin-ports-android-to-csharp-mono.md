Title: Xamarin 移植 Android 至 C# Mono
Date: 2012-05-02 10:13
Author: lovenemesis
Category: Development
Tags: Android, Mono
Slug: xamarin-ports-android-to-csharp-mono

Xamarin 宣布基于 Android 的 XobotOS 操作系统，它使用 C# Mono
虚拟机替换了 Dalvik VM Java 虚拟机。

早先 Xamarin 已经为开发者提供了 [Mono for
Android](http://xamarin.com/monoforandroid)，使得应用程序开发者可以使用
C# 开发 Android 应用程序，提高已有 .Net 代码的重用率。

现在 Xamarin 更近一步，完全移除 Java Dalvik VM 虚拟机，用“更为成熟的”
C# Mono 虚拟机替换，带来了 XobotOS 操作系统。

[![](http://linuxtoy.org/img/2012/05/screenshot-androidcsharp.png "screenshot-androidcsharp")](http://linuxtoy.org/img/2012/05/screenshot-androidcsharp.png)

根据 Xamarin 发布的测试报告，使用 **C# Mono 虚拟机的 XobotOS 在 Structs
和 Generics 测试中比 Java Dalvik VM 用时少了 3 到 7 倍**。

此外，Xamarin 也进一步**完善了 Java 至 C# 的翻译器**
[Sharpen](https://github.com/xamarin/XobotOS/tree/master/sharpen)。

Xamarin 表示使用 C# Mono 是比 Oracle/Sun Java
在专利纠纷上更好的一个选择，原因如下：

-   M$ 已经将
    [C#](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=36768)
    和 [.Net
    虚拟机](http://www.iso.org/iso/catalogue_detail.htm?csnumber=42927)提交给
    [ECMA](http://www.ecma-international.org/) 审核并标准化。
-   .Net 框架被包含的 [M$
    社区承诺中，比较缓和的针对专利问题。](http://www.microsoft.com/openspecifications/en/us/programs/community-promise/default.aspx)

下一步 Xamarin 计划将为 Mono for Android 提供直接访问 Android Skia
底层渲染库的方式，完全绕过 Java 一层。

[Xamarin
消息原文](http://blog.xamarin.com/2012/05/01/android-in-c-sharp/)
