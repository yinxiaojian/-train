import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8967'
reg =requests.get(url, verify = False)
stations = re.findall(r'([A-Z]+)\|([a-z]+)', reg.text) #match shanghai|SH
stations = dict(stations)
stations = dict(zip(stations.values(), stations.keys())) #swap the position
pprint(stations, indent = 4)