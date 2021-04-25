import pandas as pd

path = 'D://Python//'+'buildingdata_list.xlsx'

print('start read')
df = pd.read_excel(path,sheet_name = 'Sheet1')
print('end read')

a,b = df.shape

print('start sum')
sum = 0
for i in range(0,a):
    sum = sum + df[0][i]
print('end sum')

print('start max min')
sum_part = 0
for i in range(0,a):
    sum_part = sum_part + df[0][i]
    if sum_part/sum>=0.25:
        print('min 0.25 is %d' %i)
        break
print('end min')

sum_part = 0
for i in range(0,a):
    sum_part = sum_part +df[0][a-i-1]
    if sum_part/sum>=0.25:
        print('max 0.25 is %d' %(a-i))
        break
print('end max')


#还可以用tf做拟合