#110商業技藝競賽模擬試題
#Problem E所有位數和
#Author: Yotrew Wing
#2021/10/18

while True:
    try:
        n=list(map(int,list(input())))
        print(sum(n))
    except EOFError:
        break
