# /usr/bin/env python
# -*- coding: utf8 -*-

import urllib2
from bs4 import BeautifulSoup
import json
import os
import sqlite3


class FENQILE:
    def __init__(self):
        self.base_url = 'http://www.fenqile.com/search/get_more.json?key_word=+%E7%AC%94%E8%AE%B0%E6%9C%AC&sort=&page='
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; rv:45.0) Gecko/20100101 Firefox/45.0'
        self.headers = {'User-Agent': self.user_agent}
        self.item_id = 1

    def create_data_base(self):
        if not os.path.exists('fenqile.db'):
            conn = sqlite3.connect('fenqile.db')
            conn.execute('''CREATE TABLE NOTEBOOK
                       (ID INT PRIMARY KEY NOT NULL,
                       DESCRIPTION    TEXT NOT NULL,
                       PRICE          TEXT NOT NULL,
                       MONTHLY_PAYMENT TEXT NOT NULL);''')
        conn = sqlite3.connect('fenqile.db')
        return conn

    def get_page_content(self, page_index):
        url = self.base_url + str(page_index)
        print url
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        json_content = response.read().decode('utf-8')
        content = json.loads(json_content)['html']
        return content

    def get_items(self, page_index, data_base):
        page_content = self.get_page_content(page_index)
        soup = BeautifulSoup(page_content, 'lxml')
        items = soup.find('ul', class_="list-li fn-clear js-noraml-li").find_all('li')
        for item in items:
            description = item.find('h3').get_text().strip()
            price = item.find('p').find('span', class_='fn-rmb').get_text().strip()
            monthly_payment = item.find('div', class_='index-li-pic').find('span', class_='fn-rmb').get_text().strip()
            data_base.execute("INSERT INTO NOTEBOOK (ID, DESCRIPTION, PRICE, MONTHLY_PAYMENT) VALUES (%d, '%s', '%s', '%s;')" % (self.item_id, description, price, monthly_payment))
            data_base.commit()
            self.item_id += 1


if __name__ == "__main__":
    spider = FENQILE()
    data_base = spider.create_data_base()
    for page_index in range(1, 6):
        print 'Starts to scrapy the %d page' % page_index
        spider.get_items(page_index, data_base)
    data_base.close()