<!--
 * @Author       : Yuki
 * @Date         : 2021-02-23 23:48:01
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2021-02-27 14:31:03
 * @FilePath     : \suzhou_hjzl\README.md
-->
# suzhou_hjzl
## 此项目获取苏州空气市质量信息

1. 苏州市空气质量实时报（AQI指数和首要污染物以及空气等级）
2. 常熟市空气质量日报（AQI指数和首要污染物）
3. 常熟市的实时天气预报
4. 数据导出到csv文件
5. 新增定时任务2021.2.28
6. 新增获取常熟最近七天的天气预报2021.3.2
7. 新增保存到json本地文件2021.3.2
---
## 参数说明
- <font color=#0099ff size=5>天气对应参数</br></font>
cityid	String	城市ID</br>
date	String	当前日期</br>
week	String	当前星期</br>
update_time	String	气象台更新时间</br>	
city	String	城市名称</br>
cityEn	String	城市英文名称</br>	
country	String	国家名称</br>
countryEn	String	国家英文名称</br>	
wea	String	天气情况</br>
wea_img	String	天气对应图标	固定9种类型(您也可以根据wea字段自己处理):
xue、lei、shachen、wu、bingbao、yun、yu、yin、qing</br>
tem	String	实时温度</br>
tem1	String	高温</br>
tem2	String	低温</br>
win	String	风向</br>
win_speed	String	风力等级</br>	
win_meter	String	风速</br>
humidity	String	湿度</br>
visibility	String	能见度</br>
pressure	String	气压hPa</br>
air	String	空气质量</br>
air_level	String	空气质量等级</br>	
air_tips	String	空气质量描述</br>
- <font color=#0099ff size=5>苏州市环境质量对应参数</br></font>
SZRETIME    String  时报时间</br>
SZREAL      String  空气等级</br>
SZREAC      String  空气类别</br>
SZREAQI     String  AQI指数</br>
SYWRW       String  首污染物</br>
SZREND      String  浓度</br>
- <font color=#0099ff size=5>常熟市质量对应参数</br></font>
CSDATE      String  日报日期</br>
CSAQI       String  AQI指数</br>
CSSYWRW     String  首污染物</br>
