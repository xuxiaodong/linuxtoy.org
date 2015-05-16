Title: urxvt 插件实现被选单词的快速翻译
Date: 2011-03-28 19:10
Author: vern
Category: Cli
Slug: urxvt-word

双击选中一个英文单词后，右键弹出中文翻译，松开右键后翻译结果消失。

![](http://du1abadd.org/images/2011/selection-dict-3.png)
![](http://du1abadd.org/images/2011/selection-dict-2.png)

自从
[换种方式使用星际译王](http://linuxtoy.org/archives/awesome-窗口管理器——换种方式使用星际译王.html)
之后，在终端查看一个英文单词的翻译结果，还非得按一下组合键的方式越来越让我觉得麻烦，如果你用
urxvt，而且不喜欢用 stardict
的划词翻译功能，英文不好手还懒，那么你应该试试这个插件。

该插件依赖 sdcv 和可用的英汉字典。插件安装步骤大致如此：

1.  修改 urxvt 的配置文件
    ~/.Xresources，设定插件所在目录，声明使用的插件
2.  执行 `xrdb ~/.Xresources` 命令使配置文件生效
3.  复制以下代码并另存为 /your/folder/translate-selection 文件

<!-- -->

    #! perl

    sub on_start {
        my ($self) = @_;
        $self->grab_button (3, urxvt::ControlMask);
        ()
    }

    sub on_button_press {
        my ($self, $event) = @_;

        if ($event->{button} == 3) {
            my $popup = $self->popup ($event)
                or return 1;

            my ($word) = $self->selection =~ m/([a-zA-Z]+)/;

            open PIPE, "export LANG=zh_CN.UTF-8; /usr/bin/sdcv -n --utf8-output -u 'XDICT英汉辞典' '$word' | tail -n +5 | head -15 | head -n -1 |"
                or close PIPE;

            for my $eachline (<PIPE>) {
                chomp $eachline;
                $eachline = $self->locale_decode($eachline);
                $popup->add_title ($eachline);
            }
            close PIPE;

            $popup->show;
        }

        ()
    }
