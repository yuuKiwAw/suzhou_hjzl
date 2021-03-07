'''
Author       : Yuki
Date         : 2021-02-24 19:45:49
LastEditors: Please set LastEditors
LastEditTime: 2021-02-27 14:35:08
FilePath     : \\suzhou_hjzl\\saveToCSV.py
'''
# python 3.8
# coding=utf-8
import pandas as pd
import json


class DICTTOFILE:
    def __init__(self, path, SZKQZL, CSKQZL, CSTQ):
        """[summary]
        Args:
            path (str): 存放地址和文件名
            SZKQZL (dict): 苏州空气质量dict
            CSKQZL (dict): 常熟空气质量dict
            CSTQ (dict): 常熟天气
        """
        self.SZKQZL = SZKQZL
        self.CSKQZL = CSKQZL
        self.CSTQ = CSTQ
        self.path = path

    def dict_to_csv(self):
        """[summary]
        传入存放文件地址
        支持传入三个字典变量
        并导出csv格式文件
        """
        allDict = {}
        allDict.update(self.SZKQZL)
        allDict.update(self.CSKQZL)
        allDict.update(self.CSTQ)
        pd.DataFrame(allDict, index=[0]).to_csv(self.path, encoding='utf-8_sig')

    def dict_to_json(self):
        allDict = {}
        allDict.update(self.SZKQZL)
        allDict.update(self.CSKQZL)
        allDict.update(self.CSTQ)
        jsonStr = json.dumps(allDict, ensure_ascii=False)
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(jsonStr)
