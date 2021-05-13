# -*- coding: utf-8 -*
import re
import requests,json

## 搜狐图床
url = 'https://image.kieng.cn/upload.html?type=sh'

def uploadImage(image):
    files = {'image': ('avatar.jpeg', open(image, 'rb'))}
    response = requests.post(url, files=files)
    result = response.json();
    print(result);
    if  result["code"] == 200 :
        ## 返回成功，获取图片url
        qrURL = result["data"]["url"];
        return qrURL;
    else :
        ## 图片上传失败
        print(result["msg"]);
        return '';


        

    