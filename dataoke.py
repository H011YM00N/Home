#! /usr/bin/env python
# -*- coding:utf8 -*-

import requests
import json

#parameters = {'type': 'qq_quan', 'appkey': '18xsbsrjep', 'v': '1', 'page': '2'}
parameters = {'type': 'top100', 'appkey': '18xsbsrjep', 'v': '1'}
#url = 'http://api.dataoke.com/index.php?r=goodsLink/qq'
url = 'http://api.dataoke.com/index.php?r=Port/index'
res = requests.get(url=url, params=parameters)


items = res.json()['result']
for item in items:
    print item['Title']

