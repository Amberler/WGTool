# -*- coding: utf-8 -*

import flask, json, os, io
import DataUtil
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

@server.route('/upload', methods=['post'])
def upload():
    # 获取通过url请求传参的数据
    confBytes = request.stream.read();
    if len(confBytes) > 0 :
        confStr = str(confBytes, encoding = "utf-8")
        ## 获取到数据，准备写入本地
        print(confStr);
        DataUtil.writeConf(1,confStr);
        return {"code":200,"msg":"success"};
    else:
         # 获取url请求传的密码，明文
        return {"code":408,"msg":"The parameter is not valid. Please try getting it again"};



@server.route('/search', methods=['get'])
def search():
    print("准备查找数据了")
    confsArr = DataUtil.searchConfs(2);

    ##组装返回数据
    resDic = {};
    if len(confsArr) > 0:
        ## 有数据
        resDic["code"] = 200;
        resDic["msg"] = "success";
        resDic["confs"] = confsArr;
    else:
        ## 无数据
        resDic["code"] = 200;
        resDic["msg"] = "no data, please try later";
    
    res = json.dumps(resDic, separators=(',', ':'),ensure_ascii=False)
    
    return res;

 
if __name__ == '__main__':
    server.run(debug=False, port=9099, host='0.0.0.0')# 指定
