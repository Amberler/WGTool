# -*- coding: utf-8 -*
import os

# 处理之前的数据
confPath="./conf/conf.txt"
# 处理之后的数据
qrPath="./conf/QRUrl.txt"

def writeConf(num, conf):
    print("准备写入数据了");
    print(conf);
    temPath = confPath if num == 1 else qrPath;
    with open(temPath, mode='a') as f:
        f.write(conf)
        f.write('\n') # 换行
    f.close;

def searchConfs():
    print("工具类-查找数据");
    file = open(qrPath);
    confsArr=[];
    while 1:
        lines = file.readlines(20)
        if not lines:
            break
        for conf in lines:
             ## 去除字符串 换行符
             conf = conf.rstrip()
             confsArr.append(conf);
             ## 数组去重
             confsArr = list(set(confsArr));
    file.close
    return confsArr;
    

    

