import random
import pandas as pd
import os

qualif = [0,2,4,8,14,25,36,52,73,102,136,200]   #入场资格
cost = [0,1,3,5,8,10,14,20,26,32,40,50] #门票扣除
get = [0.5,3,8,13,20,25,34,47,60,73,90,111] #获得奖金
#subsidy = [0,1,2,3,4,5,6,7,8,9,10,11]   #场外补贴


zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
eleven = 11


class Chives():
    #总金额
    money = 1
    #胜率
    #win = 0.5

    #入场资格，门票，获得奖金
    chi_qualif = 0
    chi_cost = 0
    chi_get = 0.5
    #chi_subsidy = 0



def changefour(self,num):
    self.chi_qualif = qualif[num]
    self.chi_cost = cost[num]
    self.chi_get = get[num]
    #self.chi_subsidy = subsidy[number]


def group(Chi):
    #按钱数分组
    inThree = [[],[],[],[],[],[],[],[],[],[],[],[]]

    for i in range(0,len(Chi)):
        if Chi[i].money>=qualif[eleven]:
            changefour(Chi[i],eleven)
            inThree[eleven].append(Chi[i])


        elif Chi[i].money>=qualif[ten]:
            changefour(Chi[i],ten)
            inThree[ten].append(Chi[i])


        elif Chi[i].money>=qualif[nine]:
            changefour(Chi[i],nine)
            inThree[nine].append(Chi[i])


        elif Chi[i].money>=qualif[eight]:
            changefour(Chi[i],eight)
            inThree[eight].append(Chi[i])


        elif Chi[i].money>=qualif[seven]:
            changefour(Chi[i],seven)
            inThree[seven].append(Chi[i])


        elif Chi[i].money>=qualif[six]:
            changefour(Chi[i],six)
            inThree[six].append(Chi[i])


        elif Chi[i].money>=qualif[five]:
            changefour(Chi[i],five)
            inThree[five].append(Chi[i])


        elif Chi[i].money>=qualif[four]:
            changefour(Chi[i],four)
            inThree[four].append(Chi[i])


        elif Chi[i].money>=qualif[three]:
            changefour(Chi[i],three)
            inThree[three].append(Chi[i])


        elif Chi[i].money>=qualif[two]:
            changefour(Chi[i],two)
            inThree[two].append(Chi[i])


        elif Chi[i].money>=qualif[one]:
            changefour(Chi[i],one)
            inThree[one].append(Chi[i])


        elif Chi[i].money>=qualif[zero]:
            changefour(Chi[i], zero)
            inThree[zero].append(Chi[i])


    return inThree


def contest(Chi1,Chi2):
    a = random.randint(0,9)
    if a<=4:#1号输
        Chi1.money = Chi1.money-Chi1.chi_cost
        Chi2.money = Chi2.money-Chi2.chi_cost+Chi2.chi_get
    else:#2号输
        Chi2.money = Chi2.money-Chi2.chi_cost
        Chi1.money = Chi1.money-Chi1.chi_cost+Chi1.chi_get

    return Chi1.money,Chi2.money

#start

print('start')
ChivesGroup = []
#制作1000000个顾客
for i in range(0,1000000):
    temp = Chives()
    ChivesGroup.append(temp)

#10月25日到11月9日比赛16次
for i in range(0,16):

    #对所有玩家分组
    temp = group(ChivesGroup)
    ChivesGroup = temp

    #对每一组进行处理
    #可以做多进程来加速运算
    for j in range(0,12):
        que = []

        for k in range(0,len(ChivesGroup[j])):
            que.append(k)
        random.shuffle(que)

        # 随机两个进行比赛
        m=0
        while m<len(ChivesGroup[j])-1:
            ChivesGroup[j][m].money,ChivesGroup[j][m+1].money = contest(ChivesGroup[j][m],ChivesGroup[j][m+1])
            m = m+2


    #分组解构
    temp = []
    for j in range(0,12):
        for k in range(0,len(ChivesGroup[j])):
            temp.append(ChivesGroup[j][k])
    ChivesGroup = temp
    print('deal %d' %i)




#成data
print('write in')
data = []
for i in ChivesGroup:
    data_part = []
    data_part.append(i.money)
    data.append(data_part)




#写入
print('create xlsx')
dir = os.path.abspath('.') + 'data.xlsx'

datein = pd.DataFrame(data)

nan_excel = pd.DataFrame()
nan_excel.to_excel(dir)

writer = pd.ExcelWriter(dir)
datein.to_excel(writer,'Sheet1')

print('save xlsx')
writer.save()












