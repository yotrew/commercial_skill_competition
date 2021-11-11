#107商業技藝競賽模擬試題
#Problem 3： 子題2：模數 (Modulo)
#餘數小於0,不過在python中餘數沒有負的,VB有,所以本題型應該不會再出了
n=int(input())

for i in range(0,n):
    dend,dsor=map(int,input().split(","))
    r=dend%dsor
	
    if(r<0):#餘數小於0,不過在python中餘數沒有負的,VB有
        print((dsor)+r)
    else:
        print(r)
