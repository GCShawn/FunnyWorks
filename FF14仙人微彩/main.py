#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import random
from itertools import permutations
from collections import Counter
import pandas as pd

import time
import random
from multiprocessing import Process

import multiprocessing as mp


# In[2]:


def dataframeToCSV(data, file_path, mode="w", index=False, encoding='utf_8_sig'):
    # index:False(不显示列名),True(显示列名);encoding:'utf_8_sig'(确保中文不乱码)
    data.to_csv(file_path, mode=mode, index=index, encoding=encoding)
    
def changeCol(df_base,dic,inplace = True):
    df = df_base.rename(columns = dic, inplace = inplace)
    return df


# In[3]:


win = {6: 10000, 7: 36, 8: 720, 9: 360, 10: 80, 11: 252,
       12: 108, 13: 72, 14: 54, 15: 180, 16: 72, 17: 180,
       18: 119, 19: 36, 20: 306, 21: 1080, 22: 144, 23: 1800, 24: 3600}
stand = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.,0.])
hide_style = [1, 1, 1, 1, 0, 0, 0, 0, 0]


# In[4]:


def bigger(mt):
    left = np.zeros((3,1))
    up_down = np.zeros((1,4))
    right = np.zeros((5,1))
    mt = np.c_[left,mt]
    mt = np.r_[mt,up_down]
    mt = np.r_[up_down,mt]
    mt = np.c_[mt,right]
    return mt

def slight(mt):
    mt = mt[1:4,1:4]
    return mt

def count_win_point(mt):
    mt_tmp = np.array(mt)
    #传入3*3矩阵
    mt_tmp = bigger(mt_tmp)
    
    #处理三行
    result_line = []
    for i in range(1,4):
        mt_tmp[4-i][0] = win[(mt_tmp[4-i][1]+mt_tmp[4-i][2]+mt_tmp[4-i][3])]
        result_line.append(mt_tmp[4-i][0])
        
    #处理对角线
    mt_tmp[0][0] = win[(mt_tmp[1][1]+mt_tmp[2][2]+mt_tmp[3][3])]
    result_line.append(mt_tmp[0][0])
    
    #处理三列
    for j in range(1,4):
        mt_tmp[0][j] = win[(mt_tmp[1][j]+mt_tmp[2][j]+mt_tmp[3][j])]
        result_line.append(mt_tmp[0][j])
        
    #处理对角线
    mt_tmp[0][4] = win[(mt_tmp[3][1]+mt_tmp[2][2]+mt_tmp[1][3])]
    result_line.append(mt_tmp[0][4])
    
    result_line = np.array(result_line)
    mt_tmp = slight(mt_tmp)
    #传出计算条
    return result_line


def count_the_possible_point(mt):
    mt_tmp = np.array(mt)
    #传入缺失元素的3*3矩阵，传出每一行的期望获得量
    mt_tmp = mt_tmp.reshape(1,9)[0]
    #找到缺失的元素并对于缺失的元素全排列
    
    miss = []
    for i in stand:
        if i not in mt_tmp:
            miss.append(i)
    localtion = np.where(mt_tmp==0)
    all_possible_miss = list(permutations(miss))
    
    point_total = np.array([0,0,0,0,0,0,0,0])
    for i in range(len(all_possible_miss)):
        for j in range(5):
            mt_tmp[localtion[0][j]] = all_possible_miss[i][j]
        mt_tmp = mt_tmp.reshape(3,3)
        point = count_win_point(mt_tmp)
        mt_tmp = mt_tmp.reshape(1,9)[0]
        point_total = point_total + point
    point_total = point_total/len(all_possible_miss)
    return point_total


# In[5]:


all_possible_hide_style = list(set(list(permutations(hide_style))))

all_possible_hide_style1 = all_possible_hide_style[:21]
all_possible_hide_style2 = all_possible_hide_style[21:42]
all_possible_hide_style3 = all_possible_hide_style[42:63]
all_possible_hide_style4 = all_possible_hide_style[63:84]
all_possible_hide_style5 = all_possible_hide_style[84:105]
all_possible_hide_style6 = all_possible_hide_style[105:]

np.array(all_possible_hide_style[1]).reshape(3,3)


# In[16]:


def count_one(all_possible_hide_style,output_path):
    style_outcome_choose = []
    for hide_style in all_possible_hide_style:
        sum_of_point = 0
        loop = 100000
        part_style_outcome_choose = []
        choose_record = []

        for i in range(loop):
            if i%2000 == 0:
                print("计算进行到了 %s " %i)

            base_mat = np.arange(1, 10, 1)
            random.shuffle(base_mat)

            #与之对应的遮掩矩阵
            hide_mat = base_mat[:]
            hide_mat = np.array(list(map(lambda x,y:x*y,hide_mat,hide_style)))

            #修改矩阵形式3*3
            base_mat = base_mat.reshape(3,3)
            hide_mat = hide_mat.reshape(3,3)

            #计算
            base_result_line = count_win_point(base_mat)
            hide_result_line = count_the_possible_point(hide_mat) 


            choose = np.where(hide_result_line == max(hide_result_line))[0][0]
            choose_record.append(choose)

        #     print("两者相差:")
            minus = max(base_result_line)-base_result_line[np.where(hide_result_line == max(hide_result_line))[0][0]]
        #     print(minus)
            sum_of_point = sum_of_point + minus

        choose_record = Counter(choose_record).most_common(3)

        print("这个遮掩矩阵为")
        print(np.array(hide_style).reshape(3,3),end = '  ')
        print("这个遮掩方式下的差距值为 %d" %(sum_of_point/loop))
        print("最喜欢选取的3种方式为")
        print(choose_record)

        part_style_outcome_choose.append(np.array(hide_style).reshape(3,3))
        part_style_outcome_choose.append((sum_of_point/loop))
        part_style_outcome_choose.append(choose_record)

        style_outcome_choose.append(part_style_outcome_choose)
        
    df_outcome = pd.DataFrame(style_outcome_choose)
    changeCol(df_outcome,{0:'遮掩方式',1:"差值",2:"前三种爱选的方式"})
    df_outcome.head()
    dataframeToCSV(df_outcome,output_path)
    return 0


# In[20]:


if __name__ == '__main__':
    
    print("make")
    p1=Process(target=count_one,args=(all_possible_hide_style1,"out1.csv",)) #必须加,号 
    p2=Process(target=count_one,args=(all_possible_hide_style2,"out2.csv",))
    p3=Process(target=count_one,args=(all_possible_hide_style3,"out3.csv",))
    p4=Process(target=count_one,args=(all_possible_hide_style4,"out4.csv",))
    p5=Process(target=count_one,args=(all_possible_hide_style5,"out5.csv",))
    p6=Process(target=count_one,args=(all_possible_hide_style6,"out6.csv",))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    print('主线程')


# In[18]:




