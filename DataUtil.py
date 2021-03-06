# -*- coding: utf-8 -*
import os
import sys

# 获取当前工作目录路径
localPath = os.path.split(os.path.realpath(__file__))[0]

# 处理之前的数据
confPath = localPath + "/conf/conf.txt"
# 处理之后的数据
qrPath = localPath + "/conf/QRUrl.txt"


def writeConf(num, conf):
    print("准备写入数据了")
    print(conf)
    temPath = confPath if num == 1 else qrPath
    with open(temPath, mode='a') as f:
        f.write(conf)
        f.write('\n')
    f.close()


def searchConfs(num):
    print("工具类-查找数据")
    confsArr = []
    temPath = confPath if num == 1 else qrPath
    # 判断文件是否存在
    if os.path.exists(temPath):
        file = open(temPath)
        while 1:
            lines = file.readlines(20)
            if not lines:
                break
            for conf in lines:
                # 去除字符串 换行符
                conf = conf.rstrip()
                confsArr.append(conf)
                # 数组去重
                confsArr = list(set(confsArr))
        file.close()
    return confsArr


# 删除方法
def deleteFile(path):
    print(path)
    if os.path.exists(path):
        os.remove(path)


def deleteConfs():
    if len(sys.argv) >= 2:
        cmd = sys.argv[1]
        if cmd == "clean":
            deleteFile(confPath)
            deleteFile(qrPath)


deleteConfs()
