#107商業技藝競賽模擬試題
#Problem 2：數學問題 子題2：十進位轉二進位
#最簡單方式就是使用上課教,整數部分使用輾轉相除法,小數部份使用乘法
n=int(input())
for i in range(0,n):
    x=float(input())
    i=int(x)#整數部份
    f=x-int(x)#小數部份
    out_str=""
    while i > 0 :
        r=i%2
        i=int(i/2)
        out_str=str(r)+out_str
    out_str+="."
    for a in range(0,5):
        f=f*2
        out_str+=str(int(f))
        f=f-int(f)
    print(out_str)
    
