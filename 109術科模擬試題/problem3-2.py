#109商業技藝競賽模擬試題
#Problem 3：子題2：時間計算
'''
Ref:https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/364548/
方法1:非比賽做法(一般寫應用程式方法),就直接使用內鍵日期時間操作函數/物件
方法2:手算,要考慮閏年等,正式比賽有出日期題,所以本題要你自己手算
      正式比賽:109正式試題_p2-1:時間計算 <--此題是算2日期的天數,當然也可以使用內建函數
'''

n=int(input())
import datetime
for i in range(0,n):
    x=int(input().strip())
    d = datetime.datetime.strptime("1970-01-01", '%Y-%m-%d')
    delta = datetime.timedelta(days=x)
    
    print((d+delta).strftime('%Y-%m-%d'))
