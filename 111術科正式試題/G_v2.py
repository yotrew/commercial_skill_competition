#111商業技藝競賽正式試題
#Problem #G 編碼
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#UVa 11541
while True:
    try:
        n=int(input())
        for a in range(n):
            line=input().strip()
            out_str=""
            ch=""
            cnt=0
            for i in line:
                if i.isdigit():
                    cnt=cnt*10+int(i)
                else:
                    out_str+=ch*cnt
                    cnt=0
                    ch=i
                    
            out_str+=ch*cnt #最後一個字元
            print(out_str)
    except:
        break

    
'''
Sample Input 1
4
A4B3C2D1E4
A1B1C1D1E1
A2B4D1A2
A12

Sample Output 1
AAAABBBCCDEEEE
ABCDE
AABBBBDAA


Sample Input 2
3
A1B1C1D1
G1O2G1L1E1
Y1A1H1O2

Sample Output 2
ABCD
GOOGLE
YAHOO


'''
