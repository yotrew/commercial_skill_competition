#110商業技藝競賽模擬試題
#Problem D 化學廢料--其他語言解法
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
n=int(input())
in_str=input().split()
chem=[]

'''
for i in range(n): #模仿for loop(for()i=0;i<0;i++)做法
    if not in_str[i] in chem:
        chem.append(in_str[i])
'''
for i in in_str(n):
    if not i in chem: #<---其他語用可以用循序搜尋(for loop)
        chem.append(in_str[i])
        
print(len(chem))
