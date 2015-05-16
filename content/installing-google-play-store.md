Title: 给 Android 国行手机安装 Google Play 商店
Date: 2013-03-12 11:28
Author: toy
Category: Android
Slug: installing-google-play-store

最近偶入手一台三星国行 Android 手机，这货将 Google
相关应用剔除得一干二净。鉴于之前使用安卓市场安装到被注入了酷仔广告的游戏，遂萌发了要使用
Google Play 商店的决心。在此略记加装 Google Play
商店以及实现付费购买应用的过程，希望对类似遭遇的同学有用。

**安装 Google Play 商店**

1. 首先要 root 手机。这个可以请教 Google 大神，毕竟不同的手机型号，在
root
方法上会略有差异。我是利用[深度刷机](http://shuaji.shendu.com/)拿到了
root 权限。如果不行，你可以多试试其他类似工具。

2. 准备 Google Play 商店依赖包。如果单纯安装 Google Play
商店，经常出现闪退现象，总之无法正常使用。这是因为 Google Play
需要一些依赖包方能正常运行。从 可以下载到适合自己 Android 版本的 Google
应用包。解压后从中复制
GoogleServicesFramework.apk、GoogleLoginService.apk （在 system/app
目录下）到手机 SD 卡备用。

3. 从手机默认市场安装 Root Explorer 和 Google Play 商店。

4. 执行 Root Explorer，将第 2 步的依赖包复制到手机的 /system/app
目录；同时将第 3 步安装的 Google Play 商店（在手机的 /data/app
目录下，名称为 com.android.vending-1.apk）也移动到该位置。

5. 重启手机。注意这一步很重要，重启时将出现升级系统应用的进度条。

至此，加装 Google Play
商店的过程完成，如果不出意外的话，应该可以正常使用了。

**实现 Google Play 商店付费购买**

1. 到 [Google
电子钱包](https://wallet.google.com/manage/)绑定信用卡。绑定成功后发卡银行会有预扣款授权的短信提醒。注意在绑定时是没有中国这项选择的，可以选择其他区域代替，我选择的是香港。

2. 在手机上安装市场解锁（Market
Unlcoker）用于伪装区域，可设定好某个美国区域。

3. 在手机上安装 [AppCobber](http://appco.us/) 这个 VPN，每月可免费使用 3
小时，你也可以选择其他 VPN 代替。

4. 开动 VPN，执行 Google Play 商店就可购买付费应用了。
