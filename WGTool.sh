
#!/bin/bash

# 存储获取的配置信息
conf='';

# api
# url=http://192.168.1.167:888/upload
url=http://127.0.0.1:888/upload

# 检测当前时钟，凌晨0点到3点不更新，给服务器节省资源
checkHours(){
    hour=$(date "+%k")
    if [ $hour -le 3 ]; then
        echo "凌晨3点之后再执行脚本吧"
        sleep 0.5
        exit;
    else
        echo "时间校验通过"
        sleep 0.5
    fi
}

# 找出当天配置文件
findConf(){
    time=$(date "+%Y%m%d")
    echo "当天日期：$time"
    sleep 0.5
    path=$PWD
    echo "当前路径：$path"
    sleep 0.5
    filenameArr=($(ls $path|grep $time));
    fileArrLength=${#filenameArr[@]}

    if [[ fileArrLength -eq 0 ]]; then
        echo "未获取到当天的配置，\n请打开联通手机营业厅重新连接试试，请确认使用的是自动输出日志的版本"
        exit;
    else
        echo "获取到${fileArrLength}配置，默认取第一个"
        filename=${filenameArr[0]};
        conf=$(cat $filename|grep ^{)
        echo "获取到的沃游戏配置->$conf"
    fi
}

# 上传配置文件
upload(){
    # 组装curl命令
    curl -H "Content-Type: application/json" -d "$conf" $url
}

main (){
    checkHours
    echo "准备查找配置了"
    findConf
    upload
}

main

