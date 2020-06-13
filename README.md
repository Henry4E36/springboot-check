# springboot-check
# 介绍
由于在网上没有找到满意的springboot敏感目录检测的工具，于是就自己简单写了一个，dir_springboot.txt为检测的字典，都是从网上收集来的，各位大佬也可以自己根据自己需要进行添加。
# 安装
```
pip3 install requests
```
# 使用
```
python3 springboot_check.py url
python3 springboot_check.py url cookie
```
# 注意事项
* 由于在平时使用过程中，发现部分springboot的站会对cookie进行检测，因此碰到这种站，可以加上cookie参数去检测
* cookie参数的格式为`{'parameter1':'value1','parameter2':'value2'}`，一定要仔细检查自己的cookie格式有没有问题，如果有问题可能会对程序运行结果造成影响。

# 示例
```
> python3 springboot_check.py https://www.xxx.com
404 /druid/login.html
200 /druid/index.html
404 /druid/basic.json
404 /autoconfig
404 /auditevents
```
![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
