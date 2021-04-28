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
# date_now = tool.setTime(time_record,date_str)

time_record = "固定时间"
date_str = '2021-1-01'
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
sql_conn,sql_cur = tool.connectDatabase(key)
#---------------自动操作---------------#

#---------------SQL存放地址---------------#
sql_path = r'./SQL/'
sql_array = os.listdir("./SQL/")
sql_array = list(filter(lambda i: ".sql" in i,sql_array))
#---------------SQL存放地址---------------#

#---------------字典---------------#
dic_col_name = {"project_name":"项目名称","project_gid":"项目GID","project_manager_name":"项目经理姓名"}
dic_ = {}
#---------------字典---------------#

# In[ ]:
# ###方法
def dealDataFrame(df,funcOfDeal):
    #修改格式
    #funcOfDeal 为外部函数
    df_deal = funcOfDeal(df)

    #修改格式
    tool.changeDatetimeToDateStr(df_deal,'estimated_end_date')#修改日期Datetime格式为Str方便输出
    tool.changeColData(df_deal,"milestone_status",dic_milestone_status)#字典修改列数据
    tool.changeCol(df_deal,dic_col_name, inplace = True)#最后修改列名

    return df_deal



# In[ ]:
# ###主体函数
sql_var_names = locals()
replacing = {}
tool.getDataFromSQLList(sql_var_names, sql_cur, sql_path, sql_array, replacing)




# In[ ]:
# ###写入文件

sql_cur.close()
sql_conn.close()
with pd.ExcelWriter(output_path + output_name, engine='xlsxwriter') as writer:
    df_.to_excel(writer, sheet_name='【sheet1】', index=False)#dataframe to excel
    
    print('='*15 + "成功写入文件" + '='*15)


# In[ ]:
# ###修改文件
if 1 == 1:
    print('↓'*15 + "开始修改格式" + '↓'*15)
    wb = openpyxl.load_workbook(output_path + output_name)
    ws1 = wb["【sheet1】"]

    dic_col_width = {"项目名称":23,"项目GID":19,"项目经理姓名":14}#需要修改列宽的列名
    middle_list = ["项目GID","项目经理姓名","项目总监姓名"]#需要居中的列名

    #修改列宽
    tool.changeColWidthByDic(ws1, dic_col_width)

    #全框线
    tool.drawAllaround(ws1)

    #根据列名居中
    tool.changeToMiddleByList(ws1,middle_list)

    #保存
    wb.save(output_path + output_name)
    print('='*15 + "成功修改格式" + '='*15)