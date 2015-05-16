Title: MPlayer 1.0rc2 发布
Date: 2007-10-09 08:00
Author: toy
Category: Apps
Slug: mplayer-10rc2-released

这个在 Linux 中堪称终极电影播放器的 [MPlayer](http://www.mplayerhq.hu/)
于昨日推出了 1.0rc2 版。该版本主要改进了
FFmpeg，为其添加了一些新的视频和音频编/解码器。另外，MPlayer 还提供了对
Real RTSP 验证的支持，并能够播放更多的 HDTV 流媒体。

![MPlayer](http://i.linuxtoy.org/i/2007/10/mplayer.jpg)

以下是 MPlayer 1.0rc2 的详细更新情况，供大家参考：

**DOCS:**

- console messages and XML documentation converted to UTF-8  
- Russian documentation translation finished  
- Russian man page translation finished  
- Chinese man page translation finished  
- Chinese documentation translation started  
- Documented get/set/step properties in DOCS/tech/slave.txt

**Decoders:**

- Intel Music Coder audio decoding via lavc  
- Monkey Audio audio decoding via lavc  
- Fraps v2/v4 video decoding via lavc  
- Video game codecs: 4XM audio, Electronic Arts ADPCM audio, Delphine
CIN audio and video, Interplay DPCM audio, Sierra VMD video, Tiertex SEQ
video, Westwood IMA ADPCM audio, XAN wc3 video, Id CIN video, Interplay
video, XAN ADPCM audio, Westwood SND1 audio, Feeble Files DXA video, THP
audio and video, Renderware TeXture Dictionary video, Bethesda Software
VID video via lavc  
- video game codecs: XAN wc4 video via binary DLL  
- libmpeg2 updated to 0.4.1  
- fixed resolution switching with libmpeg2  
- handle resolution switching for Real codecs  
- FFmpeg video decoder can now handle aspect ratio changes  
- AMR now handled via libamr wrapper (http://www.penguin.cz/~utx/amr)  
- SIMD optimizations for mp3lib under AMD64

**Demuxers:**

- Implemented switch\_video and switch\_program consistently with
switch\_audio (default keys are "\_" and TAB, respectively). For the
time being program switching is only available in TS streams handled by
demux\_ts.c (not libavformat), while video switching is also handled by
demux\_lavf.c and demux\_avi.c.  
- audio and video switching for the AVI demuxer (video switching
untested)  
- GIF demuxer improvements, should work with all GIFs now  
- support for VC-1 in MPEG-TS and MPEG-PS files (BD,HD)-DVD  
- support for EVO demuxing  
- support -noidx with libavformat demuxer  
- support for channel navigation with PVR input  
- text subtitles should now work with libavformat demuxer  
- cleaned up TiVo demuxer

**Streaming:**

- authentication for Real RTSP streams  
- near-precise seeking in dvd:// and dvdnav:// (dvdnav:// requires
libdvdnav from mphq)  
- speed selection when playing dvd:// streams, to make drive quieter  
- support SVQ3 and H.264 in X-QT over RTSP, now RTSP Apple keynotes
work (live555)  
- SMIL playlist over Real RTSP  
- support H.263-2000 over RTSP (live555)  
- fix AAC-LATM over RTSP (live555)  
- support AMR over RTSP (live555)  
- support H.264 over RTSP (live555)  
- "device" and "adevice" suboptions now work for the *BSD BT848 TV
driver  
- dvdnav:// now depends on MPlayer's fork of libdvdnav  
- teletext support for tv:// (v4l and v4l2 only)  
- radio support for *BSD BT848  
- channel scanner for tv://  
- fine tuning for tv://  
- driver autodetection for tv://  
- libnemesi RTSP/RTP support  
- EOF detection for RTSP (live555)

**FFmpeg/libavcodec:**

- Intel Music coder audio decoder  
- Fraps v2/v4 video decoder  
- H.264 decoding speedup  
- Slice-based parallel H.264 decoding (-lavdopts fast:threads=N)  
- native NUT demuxer updated to spec  
- native NUT muxer  
- NUT muxing and demuxing support via libnut  
- WMA encoder  
- fix MJPEG-B on big-endian systems  
- lowres support for some H.264 files  
- DTS/DCA audio decoder  
- Atrac 3 audio decoder  
- MPEG-1/2 speedups  
- RoQ muxer, video and audio encoder  
- QTRLE encoder  
- AC-3 decoder  
- Matroska muxer  
- Monkey's Audio demuxer and decoder  
- Flac encoder and decoder speedups  
- AMV demuxer and audio/video decoder

**libmpeg2:**

- iWMMXt-accelerated DCT and motion compensation for ARM processors

**Filters:**

- obsolete fame filter removed  
- vf\_geq speed-ups  
- vf\_yadif green frame fixed  
- fix af\_pan when switching audio streams  
- add audio left/right balance feature to af\_pan

**MEncoder:**

- write to output streams (currently only file:// and smb://)  
- support -ffourcc with -of lavf  
- removed B-frame warning message  
- fixed bugs that would corrupt headers in the video stream when using
telecining and not patch the TFF flag correctly

**Ports:**

- Complete Intel Mac support  
- Hitachi SuperH (SH3) support  
- Blackfin optimizations

**Drivers:**

- ALSA audio output now sets the non-audio bit for AC3 passthrough even
if the user-specified default device name tries to clear it  
- fixed internal VIDIX in Solaris/x86, also auto-enabled  
- rework of internal VIDIX, now a fully static library with builtin
drivers  
- updated VIDIX ATI drivers  
- Sun XVR-100 video output driver

**Others:**

- monitorpixelaspect=1 is now default. Set monitoraspect=4/3 to get the
old behavior (if you have non-square pixels).  
- libdvdcss updated to Subversion HEAD, now same as upstream version  
- libmpdvdkit split into libdvdread and libdvdcss  
- obsolete Xvid 3 support removed  
- long-deprecated -vop option removed  
- video stream switching  
- dvdnav:// honor -alang and -slang  
- support for doubleclick as input event  
- -really-quiet works as expected now  
- select libavformat demuxer (-lavfdopts format=)  
- internal minilzo removed in favor of FFmpeg implementation, use
liblzo2 for encoding  
- change GUI dependency from libpng to libavcodec  
- ability to change subtitle size during playback  
- ability to turn loop on/off during playback  
- Apple Remote support  
- libdvdread updated to 0.9.7  
- many compiler warning fixes

- [Download MPlayer 1.0rc2](http://www.mplayerhq.hu/design7/dload.html)
