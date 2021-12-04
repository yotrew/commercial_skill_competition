#110商業技藝競賽正式試題
#Problem H 校驗和

#Author: Yotrew Wing
#2021/12/02
'''
按照題目方法做
16進位,10進位,2進位的加法,除法,乘法都會是一樣
所以讀入16進位字串轉成10進位數字直接做加法運算,最後再以16進位輸出
'''

n=int(input())
for a in range(n):
    data=input().split(" ")
    checksum=0
    for i in range(20//2):
        checksum=checksum + int("0x"+data[i*2]+data[i*2+1],16)#串成16進位字串後轉10進位
    if checksum > 0xffff:
        checksum=checksum+checksum//0x10000
    print(hex(checksum^0xffff)[-4:]) #轉hex時會有前面的0xff要去掉
