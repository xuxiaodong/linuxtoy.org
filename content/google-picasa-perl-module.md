Title: 简化 Picasa 图片上传
Date: 2007-07-02 10:30
Author: toy
Category: Apps
Slug: google-picasa-perl-module

GPPM (Google Picasa Perl Module) v0.1 版本经过我两天调试，从连
HTTP::Message 都不太清楚到 Google::Picasa
模块的发布，学习到了不少的东西。

**GPPM 出现的历史原因**

由于 Google 的 Picasa 浏览器插件不支持 Linux，所以在 Linux
下只能一次选五个文件进行上传，上传速度慢，同时浏览器的响应也会变慢。其次，该模块对权限，认证做了封装。故此就有了
GPPM 这个模块，该模块主要是为了帮助大家更加方便快速的上传图片到 Picasa。

现在还在测试阶段，很可能里面还存在不少的
Bug，但是我已经可以正常的使用了。

**GPPM 现有的功能**

1.  列出 Picasa 里面的所有的相册
2.  创建新的相册
3.  上传图片到相册

**将来会加入的新功能**

1.  列出指定相册的图片
2.  图片的删除
3.  图片及相册相关信息的添加功能

大家可以通过 GPPM
的接口，方便的只上传图片，甚至自己按照本地的目录建立相册，然后迭代的上传所有必要的图片到相册。

**存在的问题**

1.  由于 Google 服务器同步的原因，创建的相册不能马上查询，但是可以使用。
2.  由于不能及时查到相册的名称，如果创建两个相同的相册，相册的名称是
    xxx01..xxx02 的方式增长，而不是原有的指定的标题。
3.  由于 Google 没有提供相册删除功能，所以还不能删除相册。

**举例**

这个例子先打印当前有所有的相册列表，然后创新新的相册，并将三个图片文件上传到新相册。

**源码**

     1 #!/usr/bin/perl
     2
     3 #Author: updatedb
     4 #Mail: dongqiang@gmail.com
     5
     6 use strict;
     7 use lib ".";
     8
     9 use Google::Picasa;
    10
    11 print "UserName:";
    12 chomp ( my $username=<> );
    13 print "Password:";
    14 chomp ( my $password=<> );
    15
    16 #new a object
    17 my $picasa = Google::Picasa->new( $username, $password );
    18
    19 #get album list
    20 my %albums = $picasa->get_album_list();
    21 print "==================All album List=====================\n";
    22 print "ID                     =>     Album Name\n";
    23 foreach my $key ( keys %albums )
    24 {
    25     my $value = $albums{ $key };
    26     print $value, "    =>     ", $key, "\n";
    27 }
    28 print "=====================================================\n";
    29
    30 #create a new album if the album didn't exsit.
    31 my $new_album_name = "current";
    32 my ( $id, $name );
    33 if ( exists( $albums{ $new_album_name } ) )
    34 {
    35     $id = $albums{ $new_album_name };
    36     $name = $new_album_name;
    37 }
    38 else
    39 {
    40     print "Try to create album<$new_album_name>...\n";
    41     ( $id, $name ) = $picasa->create_album( $new_album_name );
    42 }
    43
    44 #upload picture files
    45 my @picnames = qw( mollusk.jpeg mollusk_bak.jpeg mollusk.png );
    46 my $picname;
    47 foreach $picname ( @picnames )
    48 {
    49     if ( $picasa->upload_file( $id, $name, $picname ) )
    50     {
    51         print "Upload $picname Successful\n";
    52     }
    53 }

**结果**

    ==================All album List=====================
    ID                     =>     Album Name
    5080358959752961841    =>     GameScreen
    5071179941904459073    =>     LinuxSpread
    5072209707558315729    =>     OfficeDiff
    =====================================================
    Try to create album...
    Upload mollusk.jpeg Successful
    Upload mollusk_bak.jpeg Successful
    Upload mollusk.png Successful

若需代码，可向我发邮件：<[dongqiang#gmail.com](mailto:dongqiang@gmail.com)>（发邮件时请将
# 替换为 @）。

- [Download Google Picasa Perl Module
v0.1](http://linuxtoy.org/projects/gppm/picasa.tar.gz)

[撰文/updatedb]

PS. 很高兴看到最近一些朋友将自己开发的 Linux 东东拿到 LinuxTOY
上来与大家分享。LinuxTOY
能够作为作者与用户之间交流的一个平台，我们感到十分荣幸。如果你正在开发
Linux 下的应用程序，我们非常乐意为你提供这方面的帮助。
