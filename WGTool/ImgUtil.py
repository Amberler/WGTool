# -*- coding: utf-8 -*
import requests

## 搜狐图床
url = 'https://image.kieng.cn/upload.html?type=sh'

def uploadImage(image):
    files = {'image': ('avatar.jpeg', open(image, 'rb'))}
    r= requests.post(url, files=files)
    print(r.text)

    