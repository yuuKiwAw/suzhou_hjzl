# Create-by-Yuki-2021/2/24-09:55
# coding=utf-8
import requests
import json
import pandas as pd
import time


# Json数据取值
def getJsonVal(strFile, keyName):
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
    strVal = htmlReq.text
    if Request_Status_Code == 200:
        print("请求成功")
        return strVal
    else:
        print("请求失败")
        return Request_Status_Code


# 主函数
def main():
    print("执行时间：" + time.asctime(time.localtime(time.time())))

    # 苏州市空气质量实时报
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    url_getCityHourAQI = "http://sthjj.suzhou.gov.cn/consultfront/consult/getCityHourAQI"  # 空气质量实时报request URL
    CityHourvalue = getReq(url_getCityHourAQI)
    getTime = getJsonVal(CityHourvalue, "times")  # 时报时间
    airClass = getJsonVal(CityHourvalue, "LIEBIE")  # 空气类别
    airLevel = getJsonVal(CityHourvalue, "DENGJI")  # 空气等级
    AQINUM = getJsonVal(CityHourvalue, "AQI")  # AQI指数
    SYWRW = getJsonVal(CityHourvalue, "SYWLW")  # 首要污染物
    NONGDU = getJsonVal(CityHourvalue, "nongdu")  # 浓度
    print("苏州市空气质量实时报：", getTime, airClass, airLevel, AQINUM, SYWRW, NONGDU)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


if __name__ == '__main__':
    main()
