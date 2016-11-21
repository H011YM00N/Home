#! /usr/bin/env python
# -*- coding:utf8 -*-


import smtplib
from email.mime.text import MIMEText

mailto_list = ['739051925@qq.com']
mail_host = 'smtp.sina.com'
mail_user = 'nevermore_xd@sina.com'
mail_pass = 'jing14081019ai'
mail_postfix = 'sina.com'


def send_mail(to_list, sub, content):
    me = 'hello' + '<' + mail_user + '@' + mail_postfix + '>'
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ';'.join(to_list)

    try:
        server = smtplib.SMTP(timeout=120)
        print 'smtplib.SMTP'
        server.set_debuglevel(True)
        server.connect(mail_host)
        print 'server.connect'
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, 'hello', 'hello world1'):
        print 'Successful'
    else:
        print 'Failed'