#111商業技藝競賽正式試題
#Problem #H 分組反轉字
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#字串,倒序

while True:
    try:
        line=input().strip().split(" ")
        if line[0]=="0":
            break
        n=int(line[0]) #組數
        l=len(line[1]) #字串總長度
        g=l//n         #每一組有多少個,就全部長度除以組數求商數,ex.22//5=4 ==>每組4個字
        out_str=""
        for i in range(0,l,g):
            out_str+=line[1][i:i+g][::-1] #一組一組取,然後再直接倒序
        print(out_str)
    except:
        break
    
        
'''
Sample Input 1
3 ABCEHSHSH
5 FAOETASINAHGRIONATWONOQAONARIO
0

Sample Output 1
CBASHEHSH
ATEOAFGHANISTANOIRAQONOWOIRANO

Sample Input 2
8 EFUIEHVOAUCQWNCNWVBNXDAHCBWBGIWX
8 TOBENUMBERONEWEMEETAGAINANDAGAINUNDERBLUEICPCSKY
5 ERURU
1 A
2 OF
0
Sample Output 2
IUFEOVHEQCUANCNWNBVWHADXBWBCXWIG
UNEBOTNOREBMEEMEWENIAGATAGADNAEDNUNIIEULBRYKSCPC
ERURU
A
OF
'''
