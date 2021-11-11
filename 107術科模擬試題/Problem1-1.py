#107商業技藝競賽模擬試題
#Problem 1：子題 1：剪刀、石頭、布
n=int(input())
for i in range(0,n):
    x=input().split(",")
    a=x[0].strip()
    b=x[1].strip()
    if a==b:
        print(0)
    elif a=='Y':
        if b=='O':
            print(2)
        else:#if x[1]=='P':
            print(1)
    elif a=='O':
        if b=='P':
            print(2)
        else:#if x[1]=='Y':
            print(1)
    elif a=='P':
        if b=='Y':
            print(2)
        else:#if x[1]=='O':
            print(1)
			
'''
import random
電腦=random.randint(1,3) #1:剪刀 2.石頭 3.布
使用者=int( input("請輸入1~3的一個數字,1:剪刀 2.石頭 3.布:") )
d={1:"剪刀",2:"石頭",3:"布",0:"亂出"}
if(not 1<=使用者<=3):
  print("阿伯出事了!!")
  使用者=0

if(電腦==使用者):
  print("平手")
if(電腦==1 and 使用者==2) or (電腦==2 and 使用者==3) or (電腦==3 and 使用者==1):
  print("you win!!!")
if(電腦==2 and 使用者==1) or (電腦==3 and 使用者==2) or (使用者==3 and 電腦==1):
  print("you lose!!!")
'''
