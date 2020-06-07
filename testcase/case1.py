# -*- coding: utf-8 -*-

import json,unittest
from lib import TestCaseKeyWord
from lib.ApiRequest import ApiRequest
from lib import getData


class Case1(unittest.TestCase):
    """客户端api"""

    def setUp(self):
        send_requests=ApiRequest()

    def tearDown(self):
        pass

    def test_api(self):



        # get_excel = Operate_Execl()
        # # 获取用例数
        # print(get_excel.get_sheet_nrows()-1)
        # # 返回用例名称关键字的列值
        # case_name_col = int(TestCaseKeyWord.get_case_name())
        # print(case_name_col)
        # # 获取第一条用例的名称
        # get_name = get_excel.get_sheet_cell(1,case_name_col)
        # print(get_name)


        get_data=getData.getData()
        print("获取是否运行key: ",get_data.get_is_run(1))
        print("获取接口url:",get_data.get_url(1))
        print("获取接口请求方法：",get_data.get_method(1))
        print("获取接口请求数据：",get_data.get_data(1))
        ur12=get_data.get_url(1)
        print("url12:"+ur12)
        method=get_data.get_method(1)
        print("method:"+method)
        data=get_data.get_data(1)
        print("data:"+data)
        ir2=ApiRequest()
        result=ir2.run_method(url=ur12,method=method,data=data)
        print(result)
