'''
Author       : Yuki
Date         : 2021-02-24 19:45:49
LastEditors: Please set LastEditors
LastEditTime: 2021-02-27 14:34:58
FilePath     : \\suzhou_hjzl\\getWeatherinfoD2.py
'''
# python 3.8
# coding=utf-8
import requests
import json
import pandas as pd
import datetime
import saveToFile
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


# 生成前一天的日期文本（xxxx年xx月xx日）
def yesterdayStr():
    today = datetime.date.today()  # !本机当天时间（确保运行的终端时间正确）
    oneday = datetime.timedelta(days=1)  # 一天的时间
    yesterday = today - oneday  # 获取到昨天的日期
    return yesterday.strftime('%Y年%m月%d日')  # 返回经过格式化的值


# 获取request返回信息(给爬虫方法提供)
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
def CSRBinfo():
    """
    Returns:
        [dict]: [aqi and key values]
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
    CSDATE = yesterdayStr()
    CSinfo = {'CSDATE': CSDATE, 'CSAQI': CSAQI[1], 'CSSYWRW': CSSYWRW}
    return CSinfo


def SZHJJinfo():
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # 苏州市空气质量实时报
    url_getCityHourAQI = "http://sthjj.suzhou.gov.cn/consultfront/consult/getCityHourAQI"  # 空气质量实时报request URL
    CityHourvalue = getReq(url_getCityHourAQI)
    getTime = getJsonVal(CityHourvalue, "times")  # 时报时间
    airClass = getJsonVal(CityHourvalue, "LIEBIE")  # 空气类别
    airLevel = getJsonVal(CityHourvalue, "DENGJI")  # 空气等级

    AQINUM = getJsonVal(CityHourvalue, "AQI")  # AQI指数
    SYWRW = getJsonVal(CityHourvalue, "SYWLW")  # 首污染物
    NONGDU = getJsonVal(CityHourvalue, "nongdu")  # 浓度
    # print("苏州市空气质量实时报：")
    SZHOURINFO = {'SZRETIME': getTime, 'SZREAL': airLevel, 'SZREAC': airClass, 'SZREAQI': AQINUM, 'SZREWRW': SYWRW, 'SZREND': NONGDU}  # !返回的字典值
    # print(SZHOURINFO)
    return SZHOURINFO


def RTCSweather():
    # API接口（GET方式）// 天气API网站说明：https://www.tianqiapi.com/index/doc?version=v6
    # 常熟市实时天气
    # !每天免费仅限300次调用
    url_api = "https://tianqiapi.com/api?version=v6&appid=57527268&appsecret=NnpIc7MS&city=常熟"
    responsejsonVal = requests.get(url_api)
    if(responsejsonVal.status_code == 200):
        jsonresult = responsejsonVal.text
        json2 = json.loads(jsonresult)  # 字典格式
        return json2  # !返回的字典值
    else:
        print("调用天气API出错")


# 主函数
def main():
    print("执行时间：" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  # 本机当前时间
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>苏州空气质量实时报告>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(SZHJJinfo())  # 苏州空气质量实时报告
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>常熟空气质量日报>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(CSRBinfo())  # 常熟空气质量日报
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>常熟实时天气预报>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(RTCSweather())  # 常熟实时天气预报
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    NEWDICTTOFILE = saveToFile.DICTTOFILE('./csv/data.csv', SZHJJinfo(), CSRBinfo(), RTCSweather())  # 实例化一个新的类
    NEWDICTTOFILE.dict_to_csv()  # 调用类中的函数转换为csv


if __name__ == '__main__':
    main()
