
#!/bin/bash

# 配置文件标识
fileNameId='com.sinovatech.unicom.ui.App';

# android默认绝对路径
defaultPath='/storage/emulated/0/MT2/logs';

# 存储获取的配置信息
conf='';

# api
# url=http://192.168.1.167:888/update
url=https://wg.late.run/upload

# 检查目录
checkPath(){
    ## 先检测当前目录是否有文件
    path=$PWD;
    confsArr=($(ls $path|grep $fileNameId));
    confsNum=${#confsArr[@]}
    if [[ confsNum -eq 0 ]]; then
        ## 当前目录没有，绝对路径查询下
        if  [ ! -x "$defaultPath" ]; then
            echo "路径${defaultPath}不存在，请将该脚本移动到MT2/log目录再次尝试"
            exit;
        else
            ## 绝对路径存在，判断是否有生成配置文件
            confsArr=($(ls $defaultPath|grep $fileNameId));
            confsNum=${#confsArr[@]}
            if [[ confsNum -eq 0 ]]; then
                echo "未查询到配置文件，请确认已经使用带日志的版本的联通app运行了免流量游戏"
                exit
            else
                echo "目录定位成功，为$defaultPath"
                sleep 0.5;
            fi
        fi
    else
        echo "目录定位成功，为$PWD"
        sleep 0.5;
        defaultPath=$path;
    fi
}

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
    filenameArr=($(ls $defaultPath|grep $time));
    fileArrLength=${#filenameArr[@]}

    if [[ fileArrLength -eq 0 ]]; then
        echo "未获取到当天的配置，\n请打开联通手机营业厅重新连接试试，请确认使用的是自动输出日志的版本"
        exit;
    else
        echo "获取到${fileArrLength}配置，默认取第一个"
        filename=${filenameArr[0]};
        filePatn="${defaultPath}/${filename}";
        conf=$(cat $filePatn|grep ^{)
        echo "获取到的沃游戏配置->$conf"
    fi
}

# 上传配置文件
upload(){
    echo "准备提交数据了，感谢你的分享！"
    sleep 0.5;
    curl -H "Content-Type: application/json" -d "$conf" $url
    exit;
}

main (){
    checkPath
    checkHours
    echo "准备查找配置了"
    findConf
    upload
}

main

