Title: Bash 4.1 发布
Date: 2010-01-02 11:00
Author: toy
Category: News
Tags: Bash
Slug: bash-4-1-released

Bash 开发团队已发布 4.1 版本。Bash 是 Linux 系统中的标准  
Shell，该新版本为用户带来了下列新功能：

+ Here-documents within $(...) command substitutions may once more be  
delimited by the closing right paren, instead of requiring a newline.

+ Bash's file status checks (executable, readable, etc.) now take file  
system ACLs into account on file systems that support them.

+ Bash now passes environment variables with names that are not valid  
shell variable names through into the environment passed to child  
processes.

+ The `execute-unix-command' readline function now attempts to clear
and  
reuse the current line rather than move to a new one after the command  
executes.

+ `printf -v' can now assign values to array indices.

+ New `complete -E' and `compopt -E' options that work on the
"empty"  
completion: completion attempted on an empty command line.

+ New complete/compgen/compopt -D option to define a `default'
completion:  
a completion to be invoked on command for which no completion has been  
defined. If this function returns 124, programmable completion is  
attempted again, allowing a user to dynamically build a set of
completions  
as completion is attempted by having the default completion function  
install individual completion functions each time it is invoked.

+ When displaying associative arrays, subscripts are now quoted.

+ Changes to dabbrev-expand to make it more `emacs-like': no space
appended  
after matches, completions are not sorted, and most recent history
entries  
are presented first.

+ The [[ and (( commands are now subject to the setting of `set -e'
and the  
ERR trap.

+ The source/. builtin now removes NUL bytes from the file before
attempting  
to parse commands.

+ There is a new configuration option (in config-top.h) that forces bash
to  
forward all history entries to syslog.

+ A new variable $BASHOPTS to export shell options settable using
`shopt' to  
child processes.

+ There is a new confgure option that forces the extglob option to be  
enabled by default.

+ New variable $BASH\\\_XTRACEFD; when set to an integer bash will
write xtrace  
output to that file descriptor.

+ If the optional left-hand-side of a redirection is of the form {var},
the  
shell assigns the file descriptor used to $var or uses $var as the
file  
descriptor to move or close, depending on the redirection operator.

+ The < and > operators to the [[ conditional command now do string  
comparison according to the current locale if the compatibility level  
is greater than 40.

+ Programmable completion now uses the completion for `b' instead of
`a'  
when completion is attempted on a line like: a $(b c.

+ Force extglob on temporarily when parsing the pattern argument to  
the == and != operators to the [[ command, for compatibility.

+ Changed the behavior of interrupting the wait builtin when a SIGCHLD
is  
received and a trap on SIGCHLD is set to be Posix-mode only.

+ The read builtin has a new `-N nchars' option, which reads exactly
NCHARS  
characters, ignoring delimiters like newline.

+ The mapfile/readarray builtin no longer stores the commands it invokes
via  
callbacks in the history list.

+ There is a new `compat40' shopt option.

Bash 4.1 的源代码可从 GNU 的 [FTP](http://ftp.gnu.org/gnu/bash/)
站点下载。
