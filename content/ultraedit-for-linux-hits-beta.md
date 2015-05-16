Title: UltraEdit 的 Linux 版本已进入 Beta 测试阶段
Date: 2009-08-18 15:00
Author: toy
Category: News
Tags: UltraEdit
Slug: ultraedit-for-linux-hits-beta

{ 撰文/netstu }

UltraEdit 是 Win 下较出名的一款小型 IDE 工具，和 EditPlus 一样受欢迎。在
Win  
下工作时查看代码最常用的就是这两个工具了。

[![UltraEdit](http://i.linuxtoy.org/images/2009/08/ultraedit\_linux\_thumb.jpg)](i.linuxtoy.org/images/2009/08/ultraedit\_linux.jpg)

UltraEdit  

在三月份的时候就已经放出[消息](http://linuxtoy.org/archives/uex-ultraedit-for-linux.html)，开发一款
Linux 桌面上的编辑器。去看过 UEX 几次，只是有截图，没有任何下载连接。

前几天又看了一下，好象可以测试了，偶就试着发了封邮件到 。

大概一天的功夫就给回了邮件，邮件内容包含了各个 Linux 版本的  
package 及一个临时的测试帐号和密码。

Hello,

Thank you for your message. Open beta testing for UEX has already begun,
and I  
have added you to the beta list so you will receive all future updates
on UEX.  
Below is a copy of the current beta message as well as download
instructions  
for the beta.

Thanks,

Ian and Team

==========================================

Hello,

This message is being sent to all beta testers that have requested to be
on  
the UltraEdit for Linux beta list. And a special welcome to all the new
testers.

We are pleased to bring you Beta III of UltraEdit for Linux. Please give
us  
any feedback you may have and report any problems.

NOTICE: This update will overwrite all UEX configuration files. This
action  
was necessary to address existing issues and to provide an improved
configuration  
system. We apologize for the inconvenience.

All the changes since Beta II are listed later in this email.

**File Download Instructions:**

Installation Packages:

* Ubuntu v8.04 32-bit:  
* Ubuntu v8.04 64-bit:  
* Ubuntu v8.10 32-bit:  
* Ubuntu v8.10 64-bit:  
* Ubuntu v9.04 32-bit:  
* Ubuntu v9.04 64-bit:  
* Fedora 11 32-bit:  
* Fedora 11 64-bit:  
* openSUSE 11.1 32-bit:  
* openSUSE 11.1 64-bit:  
* TAR 32-bit:  
* TAR 64-bit:

Username: uex100beta  
  
Password: uex1b7681

Tar Installation Instructions

1. Download tar.gz  
2. Open terminal and cd to tar.gz location  
3. Type: tar zxvf  
4. Type: cd uex/bin  
5. Type: ./uex

Your feedback is very important to us as well as the user community.
Please  
email feedback, including problem reports, what you like and issues
relating  
to the new features to support@idmcomp.com

When reporting issues, please be sure to indicate what OS the issue
occurs on  
as well as any other information necessary to reproduce the issue.
Please  
include sample files/images along with your report as a zipped
attachment if  
appropriate.

In response to beta tester requests, we are excited to announce that we
have  
added a private "UEX Beta" forum as a new resource to beta testers
here:  
http://www.ultraedit.com/support/forums.html

Only registered forum users who have been added to the UEX Beta group
(in the  
forums) will see this forum in the index upon login. We have included
brief  
descriptive information regarding the features included in this beta
here and  
offer this forum as a venue where beta testers may discuss the features
new to  
this beta. Please note, this is intended only for discussion between
beta  
testers related to implementation of the new features or issues that
are  
encountered in using them. Bug reports or enhancements requests related
to  
these new features should still be reported to us via email.

Our QA staff will be posting known issues related to this beta in this
private  
forum so that beta testers will be aware of these during the beta
process.

Special Note: If you would like access to the beta forum, please reply
to  
this message and provide us your forum login ID and we will add you to
the beta  
forum group and enable your permissions.

Thanks as always for your continued support!

**New to this build:**

- Added 64-bit tar package  
- Added Tabs to spaces  
- Added Spaces to tabs  
- Added Trim trailing spaces  
- Added To Upper Case  
- Added To Lower Case  
- Added Capitalize  
- Added Invert Case  
- Added Bash language to the wordfile  
- Added syntax information to the status bar  
- Moved Word Wrap to the View menu  
- Renamed Menu "Advanced" to "Tools"  
- Moved Configuration to Edit menu and renamed to "Preferences"

**Changes since last Beta II update:**

- Fixed issue with re-creating menus and toolbars for Project and User
tools  
- Fixed issue with toolbar perspective (position) for project tools on
Project  
Close  
- Fixed "assertion failure" with Recent File History when users try to
re-open  
projects  
- Fixed issue with remembering page size selected in Page Setup dialog  
- Fixed menu text for clipboard commands  
- Invoking UltraEdit from the command line shows many errors in the
terminal  
window  
- Only "Index" and "About" work in the Help menu  
- Attempting to open deleted/moved file from Recent Files list causes
crash  
- Project Menu doesn't list recently used projects at bottom  
- Printer settings lost after UltraEdit restart  
- Error messages in terminal when attempting to print  
- Down Arrow not working in Customize Toolbar dialog  
- No "Project Specific" indication in Tool Configuration dialog for
Project  
tools  
- Pressing OK in Set Colors dialog causes crash

As you may know, the UEX Beta has been in progress for a while and we
are now  
expanding the participants significantly. There are several important
items  
that should be taken into account prior to installing this Beta.

1. Currently auto-detection of file type on load works for UTF-8, ASCII
and  
UTF- 16 (if it has a BOM present) only. The default system code page
will be used.  
Because of this, when loading any file that is not one of these, it
will be  
necessary to select the proper encoding in the Open dialog for these
files to  
be opened correctly. If a Unicode file is opened without selecting the
proper  
encoding, it will appear to be a blank file. If you reload the file
and  
select the proper encoding you will see that the file contents were not
altered by  
the incorrect encoding detection. (This will be corrected in the near
future.)

2. The function list window is available via the View menu, but is
currently  
not functional.

3. Configuration options that are subdued are not currently functional
but are  
intended to be fully functional prior to release.

Again, thank you for your participation in this process. Your community  
contributions are greatly appreciated. Please send us any feedback you
may  
have and report any problems you may encounter while using the Beta
to:  
(support@idmcomp.com) Subject: UEX Beta feedback

While we will be reviewing and actioning all feedback emails we receive,
we  
may not be able to respond to each one individually as our priority is
to address  
the issues and continue to make progress.

Thanks again for the help!

Ian and Team

To unsubscribe from this specific mailing list, please reply to  
support@idmcomp.com and insert the text "Unsubscribe Beta" into the
subject  
line.

Special Notice: This communication is intended only for the party to
whom it  
is addressed and may contain information which is privileged or
confidential. Any  
other delivery, distribution, copying or disclosure is strictly
prohibited and  
is not a waiver of privilege or confidentiality.

测试一下，感觉用着还不错。
