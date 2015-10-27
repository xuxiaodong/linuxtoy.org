Title: Let's Encrypt 试用记
Date: 2015-10-27 18:02:05
Authors: toy
Category: Tips
Tags: 
Slug: lets-encrypt

早上收到 Let's Encrypt 的邮件，说偶之前申请的已经通过了，于是马上开始试用。Let's Encrypt 是一个新的数字证书认证机构，它通过自动化的过程消除创建和安装证书的复杂性，为网站提供免费的 SSL/TLS 证书。

<!-- PELICAN_END_SUMMARY -->

以下是使用 Let's Encrypt 的过程：

1. 获取客户端并执行

    git clone https://github.com/letsencrypt/letsencrypt
    cd letsencrypt
    ./letsencrypt-auto --agree-dev-preview --server \
        https://acme-v01.api.letsencrypt.org/directory auth

2. 选择认证方式

    在安装一些依赖包后，Let's Encrypt 将弹出 TUI
    界面要求选择认证的方式：手动或独立。这里为了省事，选择独立认证。

3. 接着输入 Email 地址

4. 同意许可协议

5. 输入域名

    在此，输入 linuxtoy.org 和 www.linuxtoy.org，多个域名使用逗号或空格分隔。

6. 完成

    当看到下列消息时，说明认证已经成功完成：

    - Congratulations! Your certificate and chain have been saved at
    /etc/letsencrypt/live/linuxtoy.org/fullchain.pem. Your cert will
    expire on 2016-01-25. To obtain a new version of the certificate in
    the future, simply run Let's Encrypt again.

Let's Encrypt 将认证的信息保存于 `/etc/letsencrypt` 目录。

然后，在 NGINX 的配置文件中将下面两行设置成 Let's Encrypt 的实际路径即可：

    ssl_certificate /etc/letsencrypt/live/linuxtoy.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/linuxtoy.org/privkey.pem;

值得注意的是，目前 Let's Encrypt 的证书有效期为 90 天，之后需要手动续期。另外，在请求证书认证时会有频率限制。总的来说，证书的认证过程还是非常容易的，而且又是免费，所以对此有需要的朋友不妨一试。
