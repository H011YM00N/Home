#! /usr/bin/env python
# -*- coding: utf8 -*-
import xlrd
import sqlite3
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

book = xlrd.open_workbook('1212.xls')
num_sheets = len(book.sheets())
print 'There are ' + str(num_sheets) + ' sheets in this excel file!'
name_sheets = []
for i in range(num_sheets):
    name_sheets.append(book.sheet_names()[i])

'''
for item in name_sheets:
    sheet = book.sheet_by_name(item)
    nrows = sheet.nrows
    ncols = sheet.ncols
'''
sheet = book.sheet_by_name(name_sheets[0])
nrows = sheet.nrows
ncols = sheet.ncols
print nrows
print ncols
ID = 0

if os.path.exists('dataoke.sdb'):
    os.remove('dataoke.sdb')

conn = sqlite3.connect('dataoke.sdb')
# sql_command = 'CREATE TABLE youpinhui (ID INTEGER PRIMARY KEY, 品类 TEXT, 商品名称 TEXT, 日常价 TEXT,
# 双12价 TEXT, 商品链接 TEXT, 推荐理由 TEXT)'
# conn.execute(sql_command)

for nrow in range(nrows):
    if nrow == 0:
        sql_command = 'CREATE TABLE youpinhui (ID INTEGER PRIMARY KEY, \"%s\" TEXT, \"%s\" TEXT, \"%s\" TEXT, ' \
                      '\"%s\" TEXT, \"%s\" TEXT, \"%s\"  TEXT)' % (sheet.cell_value(nrow, 0),
                                                                   sheet.cell_value(nrow, 1),
                                                                   sheet.cell_value(nrow, 2),
                                                                   sheet.cell_value(nrow, 3),
                                                                   sheet.cell_value(nrow, 4),
                                                                   sheet.cell_value(nrow, 5)
                                                                   )
        conn.execute(sql_command)
        continue
    else:
        print ID
        print sheet.cell_value(nrow, 0)
        print sheet.cell_value(nrow, 1)
        print sheet.cell_value(nrow, 2)
        print sheet.cell_value(nrow, 3)
        print sheet.hyperlink_map.get((nrow, 4)).url_or_path
        print sheet.cell_value(nrow, 5)
        insert_item_comand = 'INSERT INTO youpinhui(ID, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\") VALUES ' \
                             '(%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")' % (sheet.cell_value(0, 0),
                                                                                       sheet.cell_value(0, 1),
                                                                                       sheet.cell_value(0, 2),
                                                                                       sheet.cell_value(0, 3),
                                                                                       sheet.cell_value(0, 4),
                                                                                       sheet.cell_value(0, 5),
                                                                                       ID, sheet.cell_value(nrow, 0),
                                                                                       sheet.cell_value(nrow, 1),
                                                                                       sheet.cell_value(nrow, 2),
                                                                                       sheet.cell_value(nrow, 3),
                                                                                       sheet.hyperlink_map.get((nrow, 4)).url_or_path,
                                                                                       sheet.cell_value(nrow, 5))
        conn.execute(insert_item_comand)
        conn.commit()
        ID += 1

conn.close()



