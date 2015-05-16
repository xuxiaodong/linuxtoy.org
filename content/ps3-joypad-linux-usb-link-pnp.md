Title: 如何在 Linux 下使用 PS3 手柄
Date: 2009-01-21 13:58
Author: lovenemesis
Category: Tips
Tags: joypad, ps3
Slug: ps3-joypad-linux-usb-link-pnp

如果你想在 Linux 系统下使用 Sony PS3
随机附带的六轴手柄，怎么办呢？Google 显示只有 Windows 版本驱动……

首先，你需要有一个 PS3 的六轴手柄 (DualShock 3 未测试)以及一条 mini-USB
连接线(随机附赠的即可)。

然后，将 PS3 六轴手柄通过 USB 线连接到电脑的 USB
接口上。注意：请注意接口尺寸，B端接手柄，A端接电脑。连接成功后手柄上的4盏指示灯会闪烁。  
此时如果在终端使用 `dmesg` 会显示如下信息：

`usb 4-4: new full speed USB device using ohci_hcd and address 3 usb 4-4: configuration #1 chosen from 1 choice input: Sony PLAYSTATION(R)3 Controller as /devices/pci0000:00/0000:00:04.0/usb4/4-4/4-4:1.0/input/input10 input,hiddev96,hidraw1: USB HID v1.11 Joystick [Sony PLAYSTATION(R)3 Controller] on usb-0000:00:04.0-4 usb 4-4: New USB device found, idVendor=054c, idProduct=0268 usb 4-4: New USB device strings: Mfr=1, Product=2, SerialNumber=0 usb 4-4: Product: PLAYSTATION(R)3 Controller usb 4-4: Manufacturer: Sony`

之后，按下手柄中部的 PS
按键，此时手柄上的4盏指示灯会依然会闪烁，无变化。

最后，启动游戏，配置手柄按键。:)

在 Fedora 10 2.6.27.9-159.fc10.i686.PAE 测试通过， wine 1.1.13 和 GNOME
FCE Ultra 0.6.0 测试全部按键+摇杆可用。

哈哈，你预想中会有多复杂呢？其实我在文章连结中已经透露了， Plug & Play !

附：[如何在 Windows 下使用 PS3
手柄](http://www.ps2-scene.org/forums/latest-news/50907-use-ps3-sixaxis-controller-in-windows.html#800080]http://www.ps2-scene.org/forums/showthread.php?t=50907)。
