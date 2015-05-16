Title: Geany 更新到 0.12 版
Date: 2007-10-11 10:44
Author: toy
Category: Apps
Slug: geany-updated-to-012

[Geany](http://linuxtoy.org/archives/geany.html)
是一个轻量级的集成开发环境。近日，Geany 的开发者将程序更新到了 0.12
版。新版本不仅添加了很多新特性，而且也包括一些改进和 bug
修订。此外，该版本还添加了插件接口，通过开发插件可以扩展 Geany 的功能。

[![Geany](http://i.linuxtoy.org/i/2007/10/geany_s.png)](http://i.linuxtoy.org/i/2007/10/geany.png)  
*Geany 屏幕截图*

Geany 0.12 的详细更新情况如下：

Bugs fixed:  
- Fixed opening the same file twice from the message
window/command-line.  
- Fixed Ctrl-Shift keybindings not working when caps lock is on.  
- Fixed saving the wrong document when using Save All with unnamed
documents.  
- Fixed replacing with '^' or '$' regex chars.  
- Fixed hang with Find All/Find Usage with '^' or '$' regex chars.  
- Fixed hang when replacing all '[ ]*' regex matches (closes
#1757748).  
- Fixed displaying error indicators with Make after entering a
subdirectory.  
- Fixed a possible segfault when parsing tags (a vString bug).  
- Fixed clipboard problems with some applications.  
- Fixed crash when trying to open the Save As dialog on Windows.  
- Fixed crash when saving a file after setting encoding "None".  
- Fixed scrolling bugs when searching text and the cursor is outside of
current visible area.

Filetypes:  
- Added reStructuredText filetype and parser.  
- Added Haskell tags support (thanks to Peter Strand).  
- Added decorator styling for Python.  
- Parse Python global variables and class variables.  
- Added support for Java Apache Ant compiler error messages (thanks to
Jon Senior).  
- Added new filetypes CSharp and FreeBasic.  
- Added filetype Haxe (patch by blackdog, thank you).

Plugins:  
- Added basic plugin support (developers: see the HACKING file).  
- Added 'Enable plugin support' preference and -p, --no-plugins
options.  
- Added Class Builder plugin (thanks to Alexander Rodin).  
- Added Export plugin to export current file as HTML or LaTeX.

Keyboard shorcuts:  
- Common bash Ctrl-[a-z] keyboard shortcuts now work when the VTE is
focused, and there is an 'enable\_bash\_keys' hidden preference.  
- Added 'Move document left' and 'Move document right' keybindings.  
- Added Find keybinding.  
- Made fixed keybindings overridable.  
- Added fixed keybindings for switching to leftmost/rightmost document,
Ctrl-Shift-{PageUp,PageDown}.  
- Change Previous/Next Paragraph fixed commands to Ctrl-{Up,Down};
adding Shift extends selection by paragraph. (Scroll by line is now
Alt-{Up,Down}).  
- Made pressing escape focus the editor when using incremental search
or Goto Line toolbar fields.  
- Added keybinding for select current paragraph.  
- Added keybindings for smart indent and indent/deindent by one space.  
- Removed convert to lower-/upper-case keybindings.  
- Added toggle case keybinding and change shortcut to Ctrl-Alt-U.

General:  
- Added preference for 'smart' home key behaviour (thanks to Jeff
Pohlmeyer).  
- Added symbol list icons (thanks to Jean-François Wauthy, and KDevelop
for the icons).  
- Added 'Current chars' indentation mode (closes #1726880).  
- Save and restore the current notebook page when quitting.  
- Added support for f in project run command.  
- Ignore punctuation chars when moving by word, and use word end
boundaries when moving by word to the right (like most GTK+ widgets).  
- Added hidden editor preference 'use\_gtk\_word\_boundaries'.  
- Added auto\_complete\_whilst\_editing hidden preference.  
- Speed up Save All for C-like files.  
- Don't show file opened/saved/closed messages on the status bar.  
- Added --no-preprocessing, -P option when generating tags files to
disable preprocessing of C/C++ source files.  
- Added default startup directory option (closes #1704988).  
- Use current locale as default encoding for new files.  
- Added simple code navigation (thanks to Dave Moore).  
- Re-maximize the main window on startup when closed in maximized state
(closes #1730369).  
- Added auto focus (to auto focus widgets below mouse cursor).  
- Complete rewrite of auto completion to make it user-definable and
much more flexible (please read documentation).  
- Added option to set a default encoding when opening files and disable
auto detection of the file encoding.  
- Improved comment toggling by adding an additional character to mark.  
- Changed the background colour of the search bar in the toolbar
according to the search result.  
- Use intltool to make geany.desktop translatable  
- Replace Geany's icon by a new one by Sebastian Kraft (thanks).
(Thanks also to Christoph Berg for updating the icon code).

Docs:  
- Changed documentation generation tools from DocBook to reST (thanks
to John Gabriele for his great work on this).  
- Added Plugins section.  
- Added 'Inserting unicode characters' Editing section (thanks to John
Gabriele).  
- Added 'Hidden preferences' appendix.  
- Added 'Switching documents' keybindings section.

HACKING:  
- Added notes on adding a filetype.

Internationalisation:  
- New translations: en\_GB.  
- Updated translations: ca, cs, de, es, fi, fr, hu, it, pl, pt\_BR,
zh\_CN.

- [Download Geany 0.12](http://geany.uvena.de/Download/Releases)
