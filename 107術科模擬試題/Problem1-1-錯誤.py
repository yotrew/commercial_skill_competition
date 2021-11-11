#107商業技藝競賽模擬試題
#Problem 1：子題 1：剪刀、石頭、布
n=int(input())
for i in range(0,n):
    x=input().split(",")
    print(len(x[0]),len(x[1])) #這樣x[1]包含"\n"
    if x[0]==x[1]:
        print(0)
    elif x[0]=='Y':
        if x[1]=='O':
            print(2)
        else:#if x[1]=='P':
            print(3)
    elif x[0]=='O':
        if x[1]=='P':
            print(2)
        else:#if x[1]=='Y':
            print(1)
    elif x[0]=='P':
        if x[1]=='Y':
            print(2)
        else:#if x[1]=='O':
            print(1)
