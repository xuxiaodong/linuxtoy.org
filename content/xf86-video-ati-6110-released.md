Title: xf86-video-ati 6.11.0 发布
Date: 2009-02-19 11:25
Author: toy
Category: Apps, Drivers
Tags: ATI
Slug: xf86-video-ati-6110-released

开源 ATI 显卡驱动 xf86-video-ati 6.11.0 已经发布。本版本修正了上一版
6.10.0 中的诸多 bug，重写了
Crtc/output/encoder，以及修复了渲染器重复模式中的问题。据开发者透露，在下一版
6.12.0 中将包含针对 r6xx/r7xx 芯片的加速支持。

*参阅[发布公告](http://lists.freedesktop.org/archives/xorg-announce/2009-February/000771.html)*

> Highlights:  
>  - - Lots of bug fixes since 6.10.0  
>  - - Crtc/output/encoder rework  
>  - - Render repeat mode fixes
>
> 6.12.0 will be soon to follow with accel support for r6xx/r7xx chips
>
> Alan Coopersmith (2):  
>  Remove xorgconfig & xorgcfg from See Also list in man page  
>  Add README with pointers to mailing list, bugzilla & git repos
>
> Alex Deucher (66):  
>  Fix colors on tv-out  
>  properly handle EnableYUV  
>  Make sure we hit the right bios reg  
>  missed one in last commit  
>  Allow arbitrary tv-out modes  
>  ATOM: rework object table parsing  
>  ATOM: handle cases where TMDS uses linkb  
>  ATOM: Adjust PLL setup for recent atom changes  
>  ATOM: refactor output dpms  
>  ATOM: rework encoder/transmitter setup  
>  Bump version post release  
>  RV280: add another AGP quirk  
>  RV280 Add another AGP quirk  
>  DCE30: LVTMA requires DIG2 encoder  
>  ATOM: combine DAC setup functions  
>  ATOM: switch to define for external tmds  
>  start to re-org outputs  
>  ATOM: round 1 of output rework  
>  First pass at converting legacy code to encoder objects  
>  clean up encoder setup  
>  Fixup encoder setup on pre-ATOM chips  
>  ATOM: more output cleanup  
>  Switch legacy output code to use new encoder objects  
>  ATOM: fix encoder init  
>  fix legacy crtc routing and add some debugging info  
>  More legacy rework  
>  Fix logic cut and paste error  
>  Move active\_device setup to detect()  
>  Fix compilation with RADEON\_TRACE\_FALL set  
>  few more logic pasto's bits I missed  
>  Remove TMDSType, DACType, LVDSType from output rec  
>  track encoder state  
>  Remove some unused cruft  
>  Remove OutputType and other cruft  
>  Additional output cleanup  
>  Fix off by one when printing encoder name  
>  Move legacy output setup functions to legacy\_output.c  
>  Warning fixes  
>  ATOM: print useful output info for DPMS events  
>  Fix legacy output setup  
>  Encoders not assigned yet, use supported devices  
>  Move encoder specific data to encoder dev\_priv  
>  Return NULL for encoder if no active device is assigned  
>  Fix bad rv710 pci id  
>  Fix encoder accounting  
>  AVIVO: fix rotation  
>  AVIVO: better fix for rotation  
>  Add some missing r6xx/r7xx pci ids  
>  Bump for rc release  
>  RV350: add AGP quirk  
>  ATOM: warning fixes  
>  Bump version post RC release  
>  Radeon EXA: wait for the engine to be idle before sw access  
>  Revert "Radeon EXA: wait for the engine to be idle before sw access"  
>  AVIVO: fix dualhead/rotation for real  
>  R3xx-R5xx EXA: fix texture setup for non-repeat case  
>  R1xx/R2xx EXA: fix non repeat texture setup  
>  RV280: add another agp quirk  
>  RV350: add another AGP quirk  
>  Fix crtc routing on pre-DCE3.2 systems  
>  ATOM: don't unblank uninitialized crtcs  
>  ATOM: reset crtc initialized flag on CloseScreen()  
>  DCE3.2+: allow output cloning  
>  Set default RMX type to FULL on LVDS  
>  R6xx: Connector quirk for asus board  
>  bump for release
>
> Christiaan van Dijk (1):  
>  R3xx/R4xx: Maximize the use of clipped triangles for Xv rendering
>
> Dave Airlie (3):  
>  radeon: r500 PAL timings are slightly incorrect  
>  r500: re-enable TV out  
>  radeon: r500 tv-out force scaler values to nice set that looks
> correct
>
> David Miller (2):  
>  DRI: Fix page size used in RADEONDRIGetPciAperTableSize().  
>  GART: Save/restore GART table consistently.
>
> Fabio (1):  
>  man page updates
>
> Maciej Cencora (1):  
>  Make sure gb\_num\_pipes is initialized when DRI is disabled
>
> Michel Dänzer (5):  
>  Don't transform EXA Composite mask coordinates when there's no mask.  
>  Drop memcpy fallbacks from EXA UploadToScreen and  
>  DownloadFromScreen hooks.  
>  EXA: Accelerate Composite of RepeatPad/Reflect pictures when
> possible.  
>  EXA: The source tiling code can't handle RepeatReflect yet.  
>  EXA: If making a pixmap offscreen fails, return ~0ULL as texture
> offset.
>
> Nicos Gollan (1):  
>  Fixed enumerations in radeon-output.c
>
> Thomas Jaeger (1):  
>  Fall back to software for unsupported repeat modes
>
> Tormod Volden (1):  
>  Add yet another AGP quirk for RV280
>
> Wolke Liu (1):  
>  AVIVO: Save/restore vga pll registers
>
> airlied (1):  
>  rs780: include RS780 in the InitMemory to leave alone

你可以从这里[下载 xf86-video-ati 6.11.0
的源代码](http://xorg.freedesktop.org/archive/individual/driver/xf86-video-ati-6.11.0.tar.bz2)。
