#Created by 4AMAlan

import random

ListToBeSearchedFrom = [0 for i in range(100)] #创建一个拥有100个元素的列表
ItemToBeSearched = 1

for i in range(100):
    ListToBeSearchedFrom[i] = random.randint(1,1000) #给列表里所有元素赋随机整数值

print(ListToBeSearchedFrom)

Found = False #标志型变量，找到值为True，没找到值为False

for i in ListToBeSearchedFrom: #遍历列表
    if ListToBeSearchedFrom[i] == ItemToBeSearched：
        Found = True #找到后修改标志型变量的值为True
        break

if Found == True:
    print("Found") #找到输出
else:
    print("404 Not Found") #没找到输出