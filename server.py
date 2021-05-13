# -*- coding: utf-8 -*

import flask, json, os, time, qrcode, io
import ImgUtil
from flask import request


localPath = "../conf/"

 
# '''
# flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
# 登录接口，需要传url、username、passwd
# '''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式

@server.errorhandler(404)
def page_not_found(e):
    return {"404":"Not Found"}

# @server.route('/login', methods=['get', 'post'])
# def login():
#     # 获取通过url请求传参的数据
#     username = request.values.get('name')
#     # 获取url请求传的密码，明文
#     pwd = request.values.get('pwd')
#     # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
#     if username and pwd:
#         if username=='xiaoming' and pwd=='111':
#             resu = {'code': 200, 'message': '登录成功'}
#             return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
#         else:
#             resu = {'code': -1, 'message': '账号密码错误'}
#             return json.dumps(resu, ensure_ascii=False)
#     else:
#         resu = {'code': 10001, 'message': '参数不能为空！'}
#         return json.dumps(resu, ensure_ascii=False)

@server.route('/upload', methods=['post'])
def upload():
    # 获取通过url请求传参的数据
    confStr = request.stream.read();
    if len(confStr) > 0 :
        print("获取到配置了");
        handleConf(confStr);
        return {"code":200,"msg":"提交成功"};
    # 获取url请求传的密码，明文
    return {"code":408,"msg":"参数不合法，请重新尝试获取"};
    # pwd = request.values.get('pwd')
    # # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    # if username and pwd:
    #     if username=='xiaoming' and pwd=='111':
    #         resu = {'code': 200, 'message': '登录成功'}
    #         return json.dumps(resu, ensure_ascii=False)  # 将字典转换为json串, json是字符串
    #     else:
    #         resu = {'code': -1, 'message': '账号密码错误'}
    #         return json.dumps(resu, ensure_ascii=False)
    # else:
    #     resu = {'code': 10001, 'message': '参数不能为空！'}
    #     return json.dumps(resu, ensure_ascii=False)

def handleConf (conf):
    confDic = json.loads(conf)
    address = confDic["clientIp"];
    dns = confDic["clientDns"];
    privateKey = confDic["clientKey"];
    allowedIPs = "0.0.0.0/0";
    endpoint = confDic["serverIp"];
    publicKey = confDic["serverKey"];

    if len(address)>0 and len(dns)>0 and len(privateKey)>0 and len(endpoint)>0 and len(publicKey)>0 :
        resConf = f'[Interface]\nAddress = {address}\nDNS = {dns}\nPrivateKey = {privateKey}\n[Peer]\nAllowedIPs = 0.0.0.0/0\nEndpoint = {endpoint}\nPublicKey = {publicKey}';
        # 保存文件到本地
        saveResConf(resConf);
    else:
        print("参数不正确");

def saveResConf (res):
    print(res)
    timeStr = time.strftime("%Y%m%d-%H:%M:%S", time.localtime());
    filePath = f'{localPath}/{timeStr}.txt'
    # 生成二维码
    img = qrcode.make(data=res)
    # 将二维码保存为图片
    tmpPath = "./test.png";
    with open(tmpPath, 'wb') as f:
        img.save(f)
    # exit
    ImgUtil.uploadImage(tmpPath);

 
if __name__ == '__main__':
    server.run(debug=True, port=888, host='0.0.0.0')# 指定
