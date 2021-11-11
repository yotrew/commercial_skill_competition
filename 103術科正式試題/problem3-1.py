#103商業技藝競賽正式試題
#Problem 3：其他 子題 1：撲克牌遊戲 (程式執行限制時間: 2 秒)
#Author:Yotrew
#20210713
#可使用查表,或使用mod(餘數)
n=int(input())
for i in range(0,n):
    x=list(map(int,input().strip().split(" ")))
    card=[0 for i in range(0,53)]#記錄輸入的6張牌是那52張的那幾張,0不用
    card_num=[0 for i in range(0,15)]#記錄點數的張數,0不用,index1和14代表1
    card_type=[0,0,0,0]#記錄花色的張數
    for a in x:
        card[a]=1
        card_num[(a-1)%13+1]+=1 #點數,type:0黑桃,1紅桃,2方塊,3梅花
        if ((a-1)%13+1)==1:
            card_num[14]+=1
        card_type[int((a-1)/13)]+=1
    #card=sorted(card,key=lambda x:x[0])
    point=0
    #print(card_num)
    #print(card)
    #print(card_type)

    cnt=0
    max_cnt=0
    start=-1
    for a in range(1,15):#找出有沒有順子
        if(card_num[a]>0):
            cnt+=1
            if(cnt==1):
                start=a
            if(max_cnt<cnt):
                max_cnt=cnt
            continue
        
        cnt=0
    #print(start,max_cnt)
    
    if(max_cnt>=5):#若是順子找出是不是同花
        flag=True
        type1=0
        for a in range(1,4):#找出花色最多張的地方
            if card_type[type1]<card_type[a]:
                type1=a               
        start=start+(type1*13)#點數+花色*13==>才會真正牌連續的地方
        
        for a in range(start,start+5):
            if ((a-1)%13+1)==1:#1點特別處理<--10-J-Q-K-A
                a-=13
            #print(a,card[a])
            if card[a]==0:
                flag=False
                break
        if flag:
            point=7
        else:
            point=4
    g1=0 
    g2=0
    for a in range(1,14):
        if g1==0 and card_num[a]>=2:
            g1=card_num[a]
            continue
        if g1!=0 and card_num[a]>=2:
            g2=card_num[a]

    #判斷何種牌型
    if(g1==4 or g2==4):#4條,因為6張牌,所以可能是 4,2
        if point<6:
            point=6
    elif(g1==3 and g2>=2) or (g1==3 and g2>=2):#葫蘆,因為6張牌,所以可能是 3,3或3,2或2,3
        if point<5:
            point=5
    elif(g1==3):#3條
        if point<3:
            point=3
    elif((g1==2 and g2>=2) or (g2==2 and g1>=3)):#2對
        if point<2:
            point=2
    elif(g1==2):#1對
        if point<1:
            point=1
    print(point)
        

