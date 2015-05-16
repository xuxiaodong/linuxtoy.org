Title: 自动修复 FileSystem 错误
Date: 2006-11-10 15:42
Author: toy
Category: Tips
Slug: auto_fix_filesystem_error

如果 FileSystem
包含错误，使用以下小提示将使系统在引导时自动修复那些错误。方法是将
`/etc/default/rcS` 文件中的选项 `FSCKFIX=no` 设置为 yes。
