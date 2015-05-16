Title: Beagle 0.2.16（附 Ubuntu Edgy 安装源）
Date: 2007-02-08 22:13
Author: toy
Category: Apps
Slug: beagle-0216-released

桌面端搜索工具 [Beagle](http://beagle-project.org/) 于昨日发布了新的
0.2.16 版，该版本主要是修正了大量的 bug，其次的明显变化是对于 Mono
的需求回滚到了 1.1.13.5 版。此外，也包含对于一些翻译文件的更新。

Beagle 0.2.16 的显著变化包括：

> * Roll back the Mono requirement to 1.1.13.5. The .NET 2.0 support
> should be good enough in it, and it gives us access to more released
> distros (like Ubuntu Edgy and SUSE 10.1).
>
> * Change our method of setting up limits on external extractor
> processes, because running JITted code in a child process sometimes
> causes runtime deadlocks. [bgo #402065]
>
> * Fix a problem in our Sqlite schema where Beagle could loop crawling
> directories that started with zeros.
>
> * Correctly handle filter versions while indexing, so that if a
> filter is upgraded to index more information, those files will be
> reindexed.
>
> * Fix a problem where KMail folders were not being indexed. [bgo
> #391647 and #401767, bnc #238161]
>
> * Fix an issue with the file system backend reporting that it is
> indexing even after it has finished.
>
> * Fix an issue with the Evolution mail backend reporting that it is
> doing the initial crawl even if it is only reprocessing a changed
> mailbox.
>
> * Fix an issue with the Konversation backend always reporting that it
> is indexing, prompting the info box in beagle-search.
>
> * Many robustness improvements to the Konversation backend.
>
> * Fixes to the image filter (extracting JFIF comments and IPTC data,
> among others).
>
> * Fix a potential deadlock on PDF files that cause pdftotext to spam
> output to stderr.
>
> * Fix the SVG filter to handle undeclared namespaces gracefully. [bgo
> #404787]
>
> * Handle JavaScript comments inside HTML files properly.
>
> * Workaround certain archive files that cause SharpZipLib to loop
> infinitely. [bgo #402280]
>
> * Fix bugs caused by a change in behavior after switching to the .NET
> 2.0 profile, mostly date-related.
>
> * Fixed a problem where beagle-crawl-system was not being properly
> generated at configure-time. [bgo #401504]

Ubuntu Edgy 目前所包含的 Beagle 为 0.2.9
版，通过以下的源你可以安装最新的 0.2.16 版：  
`deb http://beagle-project.org/files/ubuntu/edgy/ ./`

或者：  
`deb http://kubasik.net/ubuntu/edgy ./`

Enjoy it!

Download [Beagle
0.2.16](http://ftp.gnome.org/pub/GNOME/sources/beagle/0.2/)
