Title: 给 ATI 显卡降温
Date: 2014-04-09 14:46
Author: toy
Category: Tips
Slug: ati-tip

随着最近气温的逐日升高，爱机也开始发起热来了。近日，偶同事本本的温度更是一度飚升至 90 多度，虽然采取了拆机除灰等手段，但效果并不好。

后来发现该机为 ATI 显卡，于是向 Kernel 传递了如下引导参数：
  
  :::bash
  radeon.dpm=1

没想到效果非常好，现在降到了 50 多度。

经查证，Linux 内核从 3.11 开始，为 Radeon 卡添加了动态电源管理功能，上述参数就是用来激活这项特性的。

此外，可以使用如下命令来检查动态电源管理的状态：

  :::bash
  cat /sys/class/drm/card0/device/power_dpm_state

还可以加以更改：

  :::bash
  echo "performance" > /sys/class/drm/card0/device/power_dpm_state

其他有效的选项值包括 battery 和 balanced。

有遇到类似问题的同学不妨一试。

[see also](https://wiki.gentoo.org/wiki/Radeon)
