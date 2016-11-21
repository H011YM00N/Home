#! /usr/bin/env python
# -*- coding:utf8 -*-

import requests
import json
import sqlite3
import time


data_base = time.strftime('%Y-%m-%d-%H%M%S', time.localtime()) + '-dataoke.db'
conn = sqlite3.connect(data_base)

conn.execute('''CREATE TABLE DATAOKE
        (CID            TEXT PREMARY KEY     NOT NULL,
        D_TITLE         TEXT    NOT NULL,
        TITLE           TEXT NOT NULL,
        DSR             TEXT NOT NULL,
        COMMISSION_QUEQIAO  TEXT    NOT NULL,
        QUAN_RECEIVE    TEXT    NOT NULL,
        QUAN_PRICE      TEXT    NOT NULL,
        QUAN_TIME       TEXT    NOT NULL,
        JIHUA_LINK      TEXT    NOT NULL,
        PRICE           TEXT    NOT NULL,
        JIHUA_SHENHE    TEXT    NOT NULL,
        INTRODUCE       TEXT    NOT NULL,
        SALES_NUM       TEXT    NOT NULL,
        QUAN_LINK       TEXT    NOT NULL,
        ISTMALL         TEXT    NOT NULL,
        GOODSID         TEXT    NOT NULL,
        COMMISSION_JIHUA    TEXT    NOT NULL,
        ID              TEXT    NOT NULL,
        QUE_SITEID      TEXT    NOT NULL,
        COMMISSION      TEXT    NOT NULL,
        PIC             TEXT    NOT NULL,
        ORG_PRICE       TEXT    NOT NULL,
        QUAN_M_LINK     TEXT    NOT NULL,
        QUAN_ID         TEXT    NOT NULL,
        QUAN_CONDITION  TEXT    NOT NULL,
        QUAN_SURPLUS    TEXT    NOT NULL)''')

#parameters = {'type': 'qq_quan', 'appkey': '18xsbsrjep', 'v': '1', 'page': '2'}
parameters = {'type': 'top100', 'appkey': '18xsbsrjep', 'v': '1'}
#url = 'http://api.dataoke.com/index.php?r=goodsLink/qq'
url = 'http://api.dataoke.com/index.php?r=Port/index'
res = requests.get(url=url, params=parameters)

items = res.json()['result']
for item in items:
    print 'D_title:' + item['D_title']
#    print 'Title:' + item['Title']
#    print 'Dsr:' + item['Dsr']
#    print 'Commission_queqiao:' + item['Commission_queqiao']
#    print 'Quan_receive:' + item['Quan_receive']
#    print 'Quan_price:' + item['Quan_price']
#    print 'Quan_time:' + item['Quan_time']
#    print 'Jihua_link:' + item['Jihua_link']
#    print 'Price:' + str(item['Price'])
#    print 'Jihua_shenhe:' + item['Jihua_shenhe']
#    print 'Introduce:' + item['Introduce']
#    print 'Cid:' + item['Cid']
#    print 'Sales_num:' + item['Sales_num']
#    print 'Quan_link:' + item['Quan_link']
#    print 'IsTmall:' + item['IsTmall']
#    print 'GoodsID:' + item['GoodsID']
#    print 'Commission_jihua:' + item['Commission_jihua']
#    print 'ID:' + item['ID']
#    print 'Que_siteid:' + item['Que_siteid']
#    print 'Commission:' + item['Commission']
#    print 'Pic:' + item['Pic']
#    print 'Org_Price:' + item['Org_Price']
#    print 'Quan_m_link:' + item['Quan_m_link']
#    print 'Quan_id:' + item['Quan_id']
#    print 'Quan_condition:' + item['Quan_condition']
#    print 'Quan_surplus:' + item['Quan_surplus']
    print 'Begin to write data base!!'
    conn.execute('''INSERT INTO DATAOKE(CID, D_TITLE, TITLE, DSR, COMMISSION_QUEQIAO, QUAN_RECEIVE, QUAN_PRICE,
        QUAN_TIME, JIHUA_LINK, PRICE, JIHUA_SHENHE, INTRODUCE, SALES_NUM, QUAN_LINK, ISTMALL, GOODSID,
        COMMISSION_JIHUA, ID, QUE_SITEID, COMMISSION, PIC, ORG_PRICE, QUAN_M_LINK, QUAN_ID, QUAN_CONDITION, QUAN_SURPLUS)
        VALUES
        (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\",
        \"%s\", \"%s\", \"%s\", \"%s\", \"%s\",
        \"%s\", \"%s\", \"%s\", \"%s\", \"%s\",
        \"%s\", \"%s\", \"%s\", \"%s\", \"%s\",
        \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\"
        )''' % (item['Cid'], item['D_title'], item['Title'], item['Dsr'], item['Commission_queqiao'], item['Quan_receive'],
                item['Quan_price'], item['Quan_time'], item['Jihua_link'], str(item['Price']), item['Jihua_shenhe'],
                item['Introduce'], item['Sales_num'], item['Quan_link'], item['IsTmall'], item['GoodsID'], item['Commission_jihua'],
                item['ID'], item['Que_siteid'], item['Commission'], item['Pic'], item['Org_Price'], item['Quan_m_link'],
                item['Quan_id'], item['Quan_condition'], item['Quan_surplus'])
                 )
    conn.commit()


conn.close()





