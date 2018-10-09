#!/bin/sh
# -*- coding:utf-8 -*-

# 记录一下开始时间
echo `date` >> /Users/hume/Documents/Python/XiaoMi/log.txt &&
# 进入helloworld.py程序所在目录
cd /Users/hume/Documents/Python/XiaoMi &&
# 执行python脚本（注意前面要指定python运行环境/usr/bin/python，根据自己的情况改变）
/Applications/anaconda3/bin/python3 mi.py
# 运行完成
echo 'finish' >> /Users/hume/Documents/Python/XiaoMi/log.txt