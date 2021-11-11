#109商業技藝競賽模擬試題
#Problem 1：子題2：給一個整數數字，轉為羅馬數字符號。(程式執行限制時間: 2 秒)
'''
一位一位數看,就只1~3,4,5,6~8,9,9種狀況
'''

n=int(input())
sign=["I","V","X","L","C","D","M"]

for i in range(0,n):
    x=int(input())
    out=""
    t=0
    cnt=0#目前要處理第幾位數,0是個位數,2是十位數
    while x>0:
        t=x%10
        if(t<=3):
            for a in range(0,t):
                out=sign[cnt]+out
        if(t==4):
            out=sign[cnt]+sign[cnt+1]+out
        if(t==5):
            out=sign[cnt+1]+out
        if(6<=t<=8):
            for a in range(0,t-5):
                out=sign[cnt]+out
            out=sign[cnt+1]+out
        if(t==9):
            out=sign[cnt]+sign[cnt+2]+out
        x=int(x/10)
        cnt+=2
    
    print(out)
    
