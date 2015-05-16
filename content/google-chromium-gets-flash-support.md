Title: Google Chromium 已添加 Flash 支持
Date: 2009-07-09 11:47
Author: toy
Category: News
Tags: Chromium, Google, Google Chrome
Slug: google-chromium-gets-flash-support

据网友 gDD 向我们报料，Google Chrome 网络浏览器的开源开发版本 Chromium
现在已经有了 Flash 支持。

![Google Chrome](http://i.linuxtoy.org/images/2009/01/chrome.jpg)

不过，在 Linux 平台上要享受此功能，还需要小小的
[hack](http://groups.google.com/group/chromium-discuss/browse\_thread/thread/abafff74e2f9e4cd)
一下：

1. cd /usr/lib/chromium-browser/plugins  
2. sudo ln -s ../../mozilla/plugins/flashplugin-alternative.so
flashplugin.so  
3. 重启 Chromium

若你的 flashplugin-alternative.so 路径与上不同，请自行调整。

Google Chromium 的最新 Snapshot
可从[这里获取](http://build.chromium.org/buildbot/snapshots/chromium-rel-linux/)。
