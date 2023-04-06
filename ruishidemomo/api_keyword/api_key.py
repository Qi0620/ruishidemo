import allure
import jsonpath
import json
import requests


class ApiKey:

    @allure.step("发送http请求")
    def sendhttp(self,url=None,method=None,data=None,headers=None,par_type=None,**kwargs):

        if par_type =="json":
            try:
                da = json.dumps(data,ensure_ascii=False)  #转换成json字符串
                d = json.loads(da)   #转换成字典
            except Exception as e:
                raise Exception("无法转换json形式",e)
            res = getattr(requests,method)(url=url,json=d,headers=headers,**kwargs)
        elif par_type == "data":
            res = getattr(requests,method)(url=url,data=data, headers=headers,**kwargs)

        return res

    @allure.step("结果抽取")
    def get_data(self,res,ex):
        resp = json.loads(res.text)  #将结果转换为字典
        tem = jsonpath.jsonpath(resp,ex)   #使用jsonpath提取   提取结果是个列表
        return tem[0]
