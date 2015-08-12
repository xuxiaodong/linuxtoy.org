Title: Cisco 宣布 Thor 开放视频格式
Author: lovenemesis
Date: 2015-08-12
Category: Codec
Tags: codec, h265, vp9, daala, mozilla, thor
Slug: cisco-announces-thor
Summary: 这几年 Cisco 在视频格式上对于开源社区相当友好，继早先的 OpenH264 项目，现在有宣布它们开发的下一代视频格式 Thor。

Cisco 在其[发布博客](http://blogs.cisco.com/collaboration/world-meet-thor-a-project-to-hammer-out-a-royalty-free-video-codec)上介绍了不少关于 Thor 的研发背景和目的，但是对于其技术细节描述并不多：

* 围绕 H265 已经成立了两个授权池，获得 H265 的授权费用将达到之前单一授权池的 H264 的 16 倍！
* H265 的授权条例基本排除了在开源甚至闭源免费软件中获得许可的可能性，因此 Cisco 认为其不合适作为通用型的视频编码标准
* Thor 项目的开发团队包括 Gisle Bjøntegaard 和 Arild Fuldseth 在内的业界专家和有经验的专利律师，确保其既能在技术上符合要求又不会掉入专利雷区
* Thor 已经被提交至 Internet Engineering Task Force (IETF)，和来自 Mozilla 的 Daala 一起将成为下一代[网络通讯视频格式 NetVC](http://tools.ietf.org/wg/netvc/charters) 的基石（编者注：参考 Opus 是如何诞生的）
* Cisco 希望能邀请更多的开发者加入到 Thor 开发以及 NetVC 的讨论中。

[Thor 的源码已经在 Github 发布](http://thor-codec.org/)，包含编码器及解码器。

PS：Cisco 文中仅提到 VP9 一次，由于其封闭开发的特性称其为私有格式。