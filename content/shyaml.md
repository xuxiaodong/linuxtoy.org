Title: shyaml：在命令行下处理 YAML
Date: 2016-04-19 16:52:48
Authors: toy
Category: Cli
Tags: shell, yaml
Slug: shyaml

对人类而言，[YAML][y] 是一种十分友好的数据交换格式。如果你需要在 Linux 命令行下处理 YAML，那么不妨来使用 shyaml。

<!-- PELICAN_END_SUMMARY -->

通过 shyaml，可以直接获取键、值、键值对或对应的类型。要安装 shyaml，只需执行以下命令即可：

    pip install shyaml

因 shyaml 从标准输入读取 YAML 内容，并将结果打印到标准输出，所以其一般用法为：

    cat <file.yaml> | shyaml ACTION KEY [DEFAULT]

这里的 `ACTION` 可以为：

+ `get-type`：获取相应的类型
+ `get-value`：获取值
+ `get-values{,-0}`：对序列类型来说，获取值列表
+ `keys{,-0}`：返回键列表
+ `values{,-0}`：返回值列表
+ `key-values,{,-0}`：返回键值对

结果默认是加 `\n` 换行符，若用 `-0` 形式则以 `NUL` 字符填充。

`KEY` 为要查询的键，如不提供，则使用 `DEFAULT`。

例如，我们的 file.yaml 文件内容为：

```
---
idc_group:
  name: bx
  bx: 
    news_bx: news_bx
    web3_bx: web3_php-fpm_bx

```

如果要获取 `idc_group.name` 的值则可以执行：

    cat file.yaml | shyaml get-value idc_group.name

想获取 `idc_group.bx` 的键值对可执行：

    cat file.yaml | shyaml key-values idc_group.bx

若是你想在 Linux 命令行下处理 JSON 数据格式，那么在此我强烈推荐 [jq]({filename}/jq.md) 这个好用的工具。

&rarr; [shyaml](https://github.com/0k/shyaml)

[y]: http://yaml.org/
