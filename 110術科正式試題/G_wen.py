#110商業技藝競賽正式試題
#Problem G 猜數字

#Author: wen
#2022/11/29
'''
只判斷相不相同,使用字串,不必轉成數字
1.先做?A
2.再做?B
'''

t=input().split(" ") #讀入電腦設定正確答案
n=int(input())
for i in range(n):
    a=0
    b=0
    nums=list(input().split(" ")) #存成字串
    ans=t.copy() #因為會有多筆與此筆記錄(電腦設定正確答案)做比較
    for j in range(len(ans)): #先對A的處理
        if ans[j]==nums[j]: #位置一樣,數字也一樣
            ans[j]='o'  #從ans中拿掉此數字
            nums[j]='x' #從nums中拿掉此數字,避免重覆計算
            a+=1
    for j in range(len(ans)): #再對B的處理
        for k in range(len(ans)):
            if ans[j]==nums[k] and j!=k: #位置不一樣,數字也一樣
                ans[j]='o'  #從ans中拿掉此數字
                nums[k]='x' #從nums中拿掉此數字,避免重覆計算
                b+=1
    print(f"{a}A{b}B")
