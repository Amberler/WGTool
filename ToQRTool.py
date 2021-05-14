# -*- coding: utf-8 -*
## 将配置组装，转成二维码图片，再上传到图床，将返回的图片URL存起来
import json,qrcode,time,os
import DataUtil
import ImgUtil

## 存放二维码图片的本地路径
qrPathList = [];

def start () :
    ## 获取至多个配置
    confsArr = DataUtil.searchConfs();
    if len(confsArr) > 0:
        ## 有数据
        for conf in confsArr:
            print(conf);
            ##json 转 字典，组装生成二维码
            handleConf(conf);
        ## 创建二维码结束，判断是否有结果，是否需要上传
        updateQR()

    else:
        ## 无数据
        print("未获取到数据")

## 组装WG配置
def handleConf (conf):
    confDic = json.loads(conf);
    address = confDic["clientIp"];
    dns = confDic["clientDns"];
    privateKey = confDic["clientKey"];
    allowedIPs = "0.0.0.0/0";
    endpoint = confDic["serverIp"];
    publicKey = confDic["serverKey"];

    if len(address)>0 and len(dns)>0 and len(privateKey)>0 and len(endpoint)>0 and len(publicKey)>0 :
        resConf = f'[Interface]\nAddress = {address}\nDNS = {dns}\nPrivateKey = {privateKey}\n[Peer]\nAllowedIPs = 0.0.0.0/0\nEndpoint = {endpoint}\nPublicKey = {publicKey}';
        print(resConf);
        createQR(resConf);
        # 保存文件到本地
        # DataUtil.writeConf(resConf);
        # saveResConf(resConf);
    else:
        print("参数不正确");
        exit;

## 组装好的WG配置，转成二维码，保存
def createQR(conf):
    timeStr = time.strftime("%Y%m%d-%H:%M:%S", time.localtime());
    qrPath = "./"+timeStr+".png";
    # 生成二维码
    img = qrcode.make(data=conf)
    # 将二维码保存为图片
    with open(qrPath, 'wb') as f:
        img.save(f)
    f.close;
    qrPathList.append(qrPath);

## 上传图片到三方图床，并保存数据
def updateQR():
    for qrPath in qrPathList:
        qrURL = ImgUtil.uploadImage(qrPath);
        if len(qrURL) > 0:
            ## 上传成功，保存url到本地
            DataUtil.writeConf(2,qrURL);
            if os.path.exists(qrPath):
                os.remove(qrPath)
    ## 删除本地生成的二维码图片


            

start()