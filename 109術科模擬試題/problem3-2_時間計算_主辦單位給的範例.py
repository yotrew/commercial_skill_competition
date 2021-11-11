#109商業技藝競賽模擬試題
#Problem 3：子題2：時間計算
'''

#Ref:https://stackoverflow.com/questions/2518706/python-mktime-overflow-error
time.mktime會呼叫作業系統的C library的mktime function
這個函數在不同作業系統的實作方式不一樣.
'''
'''
主辦單位提供的解法 https://hackmd.io/@biz-pg/example
import time
import datetime

date_time = 0
end_date = '1970-01-01'
end_sec2 = time.mktime(time.strptime(end_date,'%Y-%m-%d')) + date_time * (24*60*60)
print(time.strftime("%Y-%m-%d", time.localtime(end_sec2)) )
'''

#不受作業系統影響的解法
n=int(input())
import datetime
for i in range(0,n):
    x=int(input().strip())
    d = datetime.datetime.strptime("1970-01-01", '%Y-%m-%d')
    delta = datetime.timedelta(days=x)
    
    print((d+delta).strftime('%Y-%m-%d'))
