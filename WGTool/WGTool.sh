
#!/bin/bash
# get all filename in specified path

path=$PWD
echo "当前路径->$path"

time=$(date "+%Y%m%d")
echo "当前时间->$time"

filename=$(ls $path|grep $time)
echo "获取到的文件名->$filename"

if [ -z "$filename" ]; then
    echo "未获取到当天的配置，\n请打开联通手机营业厅重新连接试试，请确认使用的是自动输出日志的版本"
else
    conf=$(cat $filename|grep ^{)
    echo "获取到的沃游戏配置->$conf"
fi

exit 0





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