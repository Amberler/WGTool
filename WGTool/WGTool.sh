
#!/bin/bash


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
    filename=$(ls $path|grep $time)
    if [[ -z "$filename" ]]; then
        echo "未获取到当天的配置，\n请打开联通手机营业厅重新连接试试，请确认使用的是自动输出日志的版本"
        exit;
    else
        echo "获取到的文件名：$filename"
        conf=$(cat $filename|grep ^{)
        echo "获取到的沃游戏配置->$conf"
    fi
}

main (){
    checkHours
    echo "准备查找配置了"
    findConf
}

main


# path=$1
# echo "I am good -\"${path}\"- Script"
# files=$(ls $path)
# echo $files
# for filename in $files
# do
#    echo $filename >> filename.txt
# done


# your_name="runoob"
# # 使用双引号拼接
# greeting="hello, "$path" !"
# greeting_1="hello, ${your_name} !"
# echo $greeting  $greeting_1
# # 使用单引号拼接
# greeting_2='hello, '$your_name' !'
# greeting_3='hello, ${your_name} !'
# echo $greeting_2  $greeting_3