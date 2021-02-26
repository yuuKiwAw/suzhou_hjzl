'''
Author       : Yuki
Date         : 2021-02-24 19:45:49
LastEditors  : Yuki
LastEditTime : 2021-02-26 23:29:29
FilePath     : \suzhou_hjzl\getWeatherinfoD2.py
'''
# coding=utf-8
import requests
import json
import pandas as pd
import time
from lxml import etree
from lxml import html


# Json数据取值
def getJsonVal(strFile, keyName):
    """[summary]

    Args:
        strFile ([jsonString]): [reponse json info]
        keyName ([str]): [key value]

    Returns:
        [type]: [str]
    """
    try:
        listVal = json.loads(strFile)  # str转换为list
        df = pd.DataFrame(listVal)  # list转换为df
        dictVla = pd.DataFrame.to_dict(df)  # df转换为dict
        firstResult = dictVla[keyName]  # 取值
        return firstResult[0]
    except Exception as err:
        print("发生错误：错误位置1-1：", err)
    # json_data = json.dumps(dict_data)  # 字典转换成json
    # keyValue = dict_data.get(keyName)  # 获取键值


# 获取request返回信息
def getReq(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE '
    }
    htmlReq = requests.get(url, headers=headers)
    Request_Status_Code = htmlReq.status_code  # 返回值为int类型
    htmlReq.encoding = "utf-8"
    strVal = htmlReq.text
    if Request_Status_Code == 200:
        # print("请求成功")
        return strVal
    else:
        # print("请求失败")
        return Request_Status_Code


# etee Xpath爬取常熟市的AQI和污染源信息
def getinfoFromXpath():
    """
    Returns:
        [dict]: [aqi and wry values]
    """
    url_getCityDaily = "http://sthjj.suzhou.gov.cn//szhbj/kqzlrb/airshow.shtml"
    reponseHtml = getReq(url_getCityDaily)
    reponseEtreeVla = etree.HTML(reponseHtml)
    AQIresultList = []
    WRWresultList = []
    for row in reponseEtreeVla.xpath("//td/span"+"/text()"):
        AQIresultList.append(row)
    for row in reponseEtreeVla.xpath("//tr/td"+"/text()"):
        WRWresultList.append(row)
    CSAQI = AQIresultList[0]
    CSAQI = str(CSAQI).split('：')  # 字符切片并取值
    CSSYWRW = WRWresultList[5]
    CSinfo = {'CSAQI': CSAQI[1], 'CSSYWRW': CSSYWRW}
    return CSinfo


# 主函数
def main():
    print("执行时间：" + time.asctime(time.localtime(time.time())))

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # 苏州市空气质量实时报
    url_getCityHourAQI = "http://sthjj.suzhou.gov.cn/consultfront/consult/getCityHourAQI"  # 空气质量实时报request URL
    CityHourvalue = getReq(url_getCityHourAQI)
    getTime = getJsonVal(CityHourvalue, "times")  # 时报时间
    airClass = getJsonVal(CityHourvalue, "LIEBIE")  # 空气类别
    airLevel = getJsonVal(CityHourvalue, "DENGJI")  # 空气等级

    AQINUM = getJsonVal(CityHourvalue, "AQI")  # AQI指数
    SYWRW = getJsonVal(CityHourvalue, "SYWLW")  # 首污染物
    NONGDU = getJsonVal(CityHourvalue, "nongdu")  # 浓度
    print("苏州市空气质量实时报：", getTime, airLevel, airClass, AQINUM, SYWRW, NONGDU)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # 常熟市空气质量日报
    print("常熟市的AQI指数和首要污染物：")
    changshuInfoDaily = getinfoFromXpath()  # !返回的字典值
    print(changshuInfoDaily)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


if __name__ == '__main__':
    main()
