#! /usr/bin/env python
# -*- coding:utf8 -*-

import urllib2
import urllib
import time
import socket

ip_check_url = 'http://www.google.com.hk/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
socket_timeout = 30

def check_proxy(protocol, pip):
    try:
        proxy_handler = urllib2.ProxyHandler({protocol:pip})
        opener = urllib2.build_opener(proxy_handler)
        #opener.addheaders = [('User-agent', user_agent)]
        urllib2.install_opener(opener)

        req = urllib2.Request(ip_check_url)
        time_start = time.time()
        conn = urllib2.urlopen(req)
        time_end = time.time()
        detected_pip = conn.read()

        proxy_detected = True
    except urllib2.HTTPError, e:
        print 'ERROR: Code', e.code
        return False
    except Exception, detail:
        print 'ERROR: ', detail
        return False

    return proxy_detected

def main():
    socket.setdefaulttimeout(socket_timeout)
    protocol = 'http'
    current_proxy = '192.99.120.19:8080'
    proxy_detected = check_proxy(protocol, current_proxy)
    if proxy_detected:
        print 'WORKING : ' + current_proxy
    else:
        print 'FAILED : ' + current_proxy

if __name__ == '__main__':
    main()