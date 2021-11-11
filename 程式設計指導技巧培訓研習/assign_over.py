str=1
a=[1,2,3,4]
#print(a[0]+"2")# Error
print(str(a[0])+"2")# <--'int' object is not callable
#**warning,常常不小心就會蓋掉python的關鍵字或內建函式
list=[0,7,6,3,1,3]
list(range(5))

input="076313"
a=input()
