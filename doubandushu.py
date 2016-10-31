#! /usr/bin/env python
# -*- coding: utf8 -*-
import urllib2
from bs4 import BeautifulSoup
import sqlite3
import os


base_url = 'https://book.douban.com/review/best/?start='
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5:Windows NT)'
headers = {'User-Agent':user_agent}


def create_data_base():
    if os.path.exists('doubandushu.db'):
        os.remove('doubandushu.db')
    conn = sqlite3.connect('doubandushu.db')
    conn.execute('''CREATE TABLE SHUPING
           (ID INT PRIMARY KEY         NOT NULL,
           TITLE           TEXT        NOT NULL,
           AUTHOR          TEXT        NOT NULL,
           BOOK            TEXT        NOT NULL,
           COMMENT         TEXT        NOT NULL);''')
    return conn


def get_book_comment(data_base):
    page_list = [0, 20, 40]
    book_id = 0
    for page in page_list:
        url = base_url + str(page)
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content, 'lxml')
        print soup.title.get_text()
        items = soup.find('div', id='wrapper', class_='book-content').find_all('div', typeof='v:Review')
        for item in items:
            title = item.find('a', class_='title-link').get_text().strip()
            author = item.find('a', class_='author').get_text().strip()
            book = item.find('a', class_='subject-title').get_text().strip()
            content_url = item.find('a', class_='title-link').get('href')
            content_request = urllib2.Request(content_url,headers=headers)
            content_response = urllib2.urlopen(content_request)
            content_soup = BeautifulSoup(content_response.read().decode('utf-8'),'lxml')
            content = content_soup.find('div', id='content').find('div',class_='main-bd').find('div',class_='clearfix').get_text()
            book_id += 1
            data_base.execute("INSERT INTO SHUPING(ID, TITLE, AUTHOR, BOOK, COMMENT) VALUES (%d, \"%s\", \"%s\", \"%s\", \"%s\")" % (book_id, title, author, book, content))
            data_base.commit()
    data_base.close()
    print 'Successfully stored the book comment in doubandushu.db'


if __name__ == '__main__':
       data_base = create_data_base()
       get_book_comment(data_base)