#Problem 2：
#子題1：時間計算
#除了這個計算方式,可以使用內建時間變數/函數來做處理
N=int(input())
birth=[]
for i in range(0,N):
    birth.append((input(),input()))

for i in range(0,N):
    a=birth[i][0].split("/")
    b=birth[i][1].split("/")
    #print(a[2])
    #print(b[2])
    age=int(a[2])-int(b[2])
    diff_month=12-int(b[1])+int(a[1])
    #print(diff_month,end=" ")
    if(diff_month<12):
        age=age-1
    if(diff_month==12):
        if int(a[0]) < int(b[0]):
            age=age-1

    print(age)
