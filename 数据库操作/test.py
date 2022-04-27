import os
from pprint import pprint

root = os.walk(top='./tables')
for i in root:
    print(i)

tables_list = os.listdir('./tables')
print(tables_list)

tables_dict = {}
item_dict = {}
for i in tables_list:
    if i == '用户信息表.xls':
        item_dict = {'name': i,
                     'sql': 'sql1'}
        tables_dict['user'] = item_dict
    if i == '院系信息表.xls':
        item_dict = {'name': i,
                     'sql': 'sql2'}
        tables_dict['college'] = item_dict
    if i == '学生信息表.xls':
        item_dict = {'name': i,
                     'sql': 'sql3'}
        tables_dict['student'] = item_dict
    if i == '教师信息表.xls':
        item_dict = {'name': i,
                     'sql': 'sql4'}
        tables_dict['teacher'] = item_dict
    if i == '课程信息表.xls':
        item_dict = {'name': i,
                     'sql': 'sql5'}
        tables_dict['course'] = item_dict
    if i == '开课信息表.xls':
        item_dict = {'name': i,
                     'sql': 'sql6'}
        tables_dict['open_course'] = item_dict

pprint(tables_dict)
print('=========================')
for key, value in tables_dict.items():
    print(key, value)











