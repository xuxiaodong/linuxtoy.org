Title: ngxtop: 实时监视 NGINX
Date: 2014-03-31 09:40
Author: toy
Category: Apps
Slug: ngxtop

[ngxtop][n] 允许你对 NGINX 的访问日志 (access log) 进行实时解析，  
并输出类似 top 的有用信息。

通过下列命令可以安装 ngxtop:

pip install ngxtop

在执行 ngxtop 后，它将默认输出如下信息：

$ ngxtop  
running for 411 seconds, 64332 records processed: 156.60 req/sec

Summary:  
| count | avg\_bytes\_sent | 2xx | 3xx | 4xx | 5xx |  
|---------+------------------+-------+-------+-------+-------|  
| 64332 | 2775.251 | 61262 | 2994 | 71 | 5 |

Detailed:  
| request\_path | count | avg\_bytes\_sent | 2xx | 3xx | 4xx | 5xx |  

|------------------------------------------+---------+------------------+-------+-------+-------+-------|  
| /abc/xyz/xxxx | 20946 | 434.693 | 20935 | 0 | 11 | 0 |  
| /xxxxx.json | 5633 | 1483.723 | 5633 | 0 | 0 | 0 |  
| /xxxxx/xxx/xxxxxxxxxxxxx | 3629 | 6835.499 | 3626 | 0 | 3 | 0 |  
| /xxxxx/xxx/xxxxxxxx | 3627 | 15971.885 | 3623 | 0 | 4 | 0 |  
| /xxxxx/xxx/xxxxxxx | 3624 | 7830.236 | 3621 | 0 | 3 | 0 |  
| /static/js/minified/utils.min.js | 3031 | 1781.155 | 2104 | 927 | 0 |
0 |  
| /static/js/minified/xxxxxxx.min.v1.js | 2889 | 2210.235 | 2068 | 821
| 0 | 0 |  
| /static/tracking/js/xxxxxxxx.js | 2594 | 1325.681 | 1927 | 667 | 0 |
0 |  
| /xxxxx/xxx.html | 2521 | 573.597 | 2520 | 0 | 1 | 0 |  
| /xxxxx/xxxx.json | 1840 | 800.542 | 1839 | 0 | 1 | 0 |

关于 ngxtop 的更多用法，可通过 `ngxtop -h` 查询。

[n]: https://github.com/lebinh/ngxtop
