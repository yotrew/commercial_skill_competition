#111商業技藝競賽模擬試題
#Problem #M 矩陣
#Author: wen
#2022/11/22
#https://github.com/yotrew/commercial_skill_competition
'''
轉90度
欄變列,列變欄,因為只轉90度,所以從最後一列開始當做欄輸出
'''
s=list(eval(input())) #輸入就是串列格式,直接使用eval轉成串列
t=[] 

for i in range(len(s)):
    t1=[]
    for j in range(len(s)-1,-1,-1):
       t1.append(s[j][i]) #依旋轉後順序一個一個加到每一列中
    t.append(t1) #每一列加到輸出串列中
print(str(t).replace(" ","")) #因為輸出不要有空格,所以將串列轉成字串,再把空格拿掉
       

