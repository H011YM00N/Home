#! /usr/bin/env python
# -*- coding:utf8 -*-

import urllib2
from bs4 import BeautifulSoup
import re


class ZHILIAN:

    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def get_page_content(self, page_index):
        try:
            url = 'http://www.highpin.cn/zhiwei/ci_160500_jt_405' + '_p_' + str(page_index) + '.html'
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            page_content = response.read()
            return page_content
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print 'Fail to connect to ZHILIAN, reason', e.reason
                return None

    def get_job_item(self, page_index):
        page_content = self.get_page_content(page_index)
        soup = BeautifulSoup(page_content, 'lxml')
        print soup.title.get_text()
        job_items = soup.find('div', id='c-list-box', class_='c-list-box').find_all('div', class_="jobInfoItem clearfix bor-bottom add-bg")
        for item in job_items:
            publish_date = item.find('div', class_="c-list-search c-wid122 line-h44").get_text()
            job_name = item.find('p', class_="jobname clearfix").get('title')
            company_name = item.find('p', class_="companyname").get('title')
            salary = item.find('p', class_="s-salary").get_text().strip()
            print publish_date, '\t', salary, '\t', job_name, '\t', company_name

    def start(self):
        for page_index in range(1, 4):
            self.get_job_item(page_index)


class EETOP:

    def __init__(self):
        self.page_index = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        self.jobs = []

    def get_page(self, page_index):
        try:
            url = 'http://bbs.eetop.cn/forum-97-'+str(page_index)+'.html'
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            page_code = response.read()
            return page_code
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Fail to connect to EETOP, reason', e.reason
                return None

    def get_page_item(self, page_index):
        page_code = self.get_page(page_index)
        if not page_code:
            print 'Fail to load page'
            return None
        pattern = re.compile('<tbody id="normalthread.*?">.*?<a href="thread-.*?.html">(.*?)</a>.*?<td class="author">.*?<em>(.*?)</em>',re.S)
        items = re.findall(pattern, page_code)
        page_jobs = []
        for item in items:
            page_jobs.append([item[1],item[0]])
        return page_jobs

    def load_page(self):
        if len(self.jobs) <2:
            page_jobs = self.get_page_item(self.page_index)
            if page_jobs:
                self.jobs.append(page_jobs)
                self.page_index += 1

    def get_one_job(self, page_jobs, page):
        raw_input()
        print u'第%d页\n' % page
        for job in page_jobs:
            self.load_page()
            print job[0], '\t', job[1]

    def start(self):
        print u'正在读取EETOP，按回车查看新job'
        self.load_page()
        now_page = 0
        while True:
            if len(self.jobs)>0:
                page_jobs = self.jobs[0]
                now_page += 1
                del self.jobs[0]
                self.get_one_job(page_jobs, now_page)


class MOORE:

    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent}

    def get_page_content(self, page_index):
        try:
            url = 'http://www.moore.ren/job/list/128/?q=&p=' + str(page_index)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            page_content = response.read()
            return page_content
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print 'Fail to connect to MOORE, reason', e.reason
                return None

    def get_job_item(self, page_index):
        page_content = self.get_page_content(page_index)
        soup = BeautifulSoup(page_content, 'lxml')
        print soup.title.get_text()
        job_items = soup.find('div', class_='search-job-list').find_all('li', class_='job-list-item')
        for item in job_items:
            publish_date = item.find('div', class_='job-list-top').find('span', class_='job-publish-time').get_text()
            salary = item.find('div',class_='job-list-top').find('span', class_='job-salary').get_text()
            job_name = item.find('div', class_='job-list-top').find('div', class_='job-left').find('a', class_='job-title').get_text()
            company_name = item.find('div', class_='job-list-top').find('div', class_='job-right').find('a', class_='job-title').get_text()
            print publish_date, '\t', salary, '\t', job_name, '\t', company_name

    def start(self):
        for page_index in range(1, 3):
            self.get_job_item(page_index)



if __name__ == '__main__':
    select_mode = raw_input()
    if select_mode == 'zhilian':
        zhilian = ZHILIAN()
        zhilian.start()
    elif select_mode == 'moore':
        moore = MOORE()
        moore.start()
    elif select_mode == 'eetop':
        eetop = EETOP()
        eetop.start()

