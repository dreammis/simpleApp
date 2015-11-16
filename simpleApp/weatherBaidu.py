#-* coding:utf8 -*-
import json,requests
from ConfigParser import ConfigParser
import re

url = "http://api.map.baidu.com/telematics/v3/weather?location=Hangzhou&output=json&ak="

config = ConfigParser()
config.read('akID.ini')
akID = config.get('ak','akID')
newUrl = url+akID

content = requests.get(newUrl)
decodejson = json.loads(content.text)

city = decodejson['results'][0]['currentCity']
pm25 = decodejson['results'][0]['pm25']
weather = decodejson['results'][0]['weather_data'][0]['temperature']
suggestion = decodejson['results'][0]['index'][0]['des']
nowTemperature = re.search(u'实时：(.*?)\)',decodejson['results'][0]['weather_data'][0]['date']).group(1)


print u'''今天%s的天气是 %s，当前温度是
%s,
万恶的PM2.0是%s,%s'''%(city,weather,nowTemperature,pm25,suggestion)

