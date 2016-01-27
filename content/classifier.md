Title: Classifier：自动整理文件
Date: 2016-01-26 21:52
Authors: toy
Category: Apps
Tags: classifier
Slug: classifier

我一般将网上下载的各种文件存放在临时目录里面，时间一长这个目录便会变得杂乱不堪。现在好了，有了 [Classifier][c] 的帮助，临时目录也可以变得整洁无比。

<!-- PELICAN_END_SUMMARY -->

Classifier 根据文件类型，比如音乐、PDF、图像等，来对当前目录的文件进行整理。它的整理方法是将不同类型的文件放到不同的目录里，其结果看起来井然有序。例如，如下目录的文件：

```
Downloads
├── project.docx
├── 21 Guns.mp3
├── Sultans of Swing.mp3
├── report.pdf
├── charts.pdf
├── VacationPic.png
├── CKEditor.zip
├── Cats.jpg
├── archive.7z
```

整理后将变成：

```
Downloads
├── Music
│   └── 21 Guns.mp3
│   ├── Sultans of Swing.mp3
|
├── Documents
│   └── project.docx
│   └── report.pdf
│   ├── charts.pdf
├── Archives
│   └── CKEditor.zip
│   └── archive.7z
├── Pictures
│   └── VacationPic.png
│   └── Cats.jpg
```

Classifier 使用 Python 编写而成，可通过以下指令安装：

```
pip install classifier
```

[c]: http://bhrigu123.github.io/classifier/
