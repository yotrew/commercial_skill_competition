#108商業技藝競賽模擬試題
#Problem 3： 子題 2：網段網路位址和網段廣播位址
#Author:Yotrew
#20210709
#110商業技藝競賽模擬試題
#Problem H 網段網路位址和網段廣播位址
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
'''
#同106商業技藝競賽正式試題Problem 3-1,多一個網路位址
2進位運算和10進位運算沒什麼不同
題目已告訴你運算方式,所以就直接使用位元運算
<<	向左位移
>>	向右位移
&	位元且
|	位元或
^	位元互斥或
~	位元非

'''
192.15.156.205/255.255.255.224
n=int(input())

for i in range(0,n):
    in_str=input().strip().split("/")
    ip=list(map(int,in_str[0].split(".")))
    netmask=list(map(int,in_str[1].split(".")))
    mask_len=0
    for a in range(0,3):
        print(ip[a] & netmask[a],end=".")
    print(ip[3] & netmask[3],end="")#第四個byte(第四組數字)另外處理
    print("/",end="")
    for a in range(0,3):
        print(256+(ip[a] |( ~netmask[a])),end=".")
    print(256+(ip[3] |( ~netmask[3])))#第四個byte(第四組數字)另外處理
    #print(ip[a] & netmask[a])
    
    
