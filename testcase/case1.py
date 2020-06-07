# -*- coding: utf-8 -*-


from lib.ApiRequest import ApiRequest
from lib import getData
import json


get_data=getData.getData()
for i in range(1,get_data.get_case_nums()):
    print("获取是否运行key: ",get_data.get_is_run(i))
    print("获取接口url:",get_data.get_url(i))
    print("获取接口请求方法：",get_data.get_method(i))
    print("获取接口请求数据：",get_data.get_data(i))
    url=get_data.get_url(i)
    # print("url12:"+ur12)
    method=get_data.get_method(i)
    # print("method:"+method)
    data=json.loads(get_data.get_data(i))
    # print("data:"+str(data))
    ir2=ApiRequest()
    result=ir2.run_method(url=url,method=method,data=data)
    print(result)
