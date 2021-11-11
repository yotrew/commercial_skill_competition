#107商業技藝競賽模擬試題
#Problem 2：數學問題 子題2：十進位轉二進位
#偷懶做法,只偷到整數部份...有更偷懶的方法嗎???
n=int(input())
for i in range(0,n):
    x=float(input())
    i=int(x)#整數部份
    f=x-int(x)#小數部份
    out_str=format(i,"b")+"."
    for a in range(0,5):
        f=f*2
        out_str+=str(int(f))
        f=f-int(f)
    print(out_str)
