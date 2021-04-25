#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import json
import datetime
from dateutil.relativedelta import relativedelta
import tool
import pytz
import os
import openpyxl
from openpyxl.styles import Border,Side,Alignment,PatternFill,Font

# In[ ]:
# 修改输入输出

#time_record = "当前时间"

time_record = "固定时间"
date_str = '2020-11-01'

date_now = tool.setTime(time_record,date_str)

datetime_now = pd.to_datetime(date_now)
datetime_now = datetime_now.replace(tzinfo=pytz.timezone('Asia/Shanghai'))#加时区

#---------------目标项目名称---------------#
all_project_gid = []
project_gid_to_be_search = ['']
#---------------目标项目名称---------------#

date_attach = str(date_now)

#---------------文件输出地址---------------#
output_path = r'./OUTPUT'
output_name = r'/sample' + date_attach + '.xlsx'
#---------------文件输出地址---------------#


# In[ ]:
# ###处理各项文件地址
tool.pandasPrettyPrinting()#修改pandas的print状态，用于调试
#---------------目标数据库密钥---------------#
# key_flag = "测试环境"
key_flag = "真实环境"

key_path = r'./KEY'
key_test = r'/test.json'
key_orgin = r'/origin.json'

#---------------目标数据库密钥---------------#

#---------------自动操作---------------#
key = tool.getKeyFromJson(key_path,key_test,key_orgin,key_flag)
sql_cur = tool.connectDatabase(key)
#---------------自动操作---------------#

#---------------SQL存放地址---------------#
sql_path = r'./SQL/'
sql_array = os.listdir("./SQL/")
sql_array = list(filter(lambda i: ".sql" in i,sql_array))
#---------------SQL存放地址---------------#

#---------------字典---------------#
dic_ = {}
#---------------字典---------------#

# In[ ]:
# ###方法






# In[ ]:
# ###主体函数
sql_var_names = locals()
replacing = {}
tool.getDataFromSQLList(sql_var_names, sql_cur, sql_path, sql_array, replacing)




