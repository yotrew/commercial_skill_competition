#110商業技藝競賽正式試題
#Problem M 矩陣的直積
#Author: Yotrew Wing
#2021/12/02
#https://github.com/yotrew/commercial_skill_competition
'''
先推出行列變化,再觀察...
ex.
[0][0]*[0][0]
[0][0]*[0][1]
[0][1]*[0][0]
[0][1]*[0][1]
--換列---(<--對於最後的大矩陣來說)
[0][0]*[1][0]
[0][0]*[1][1]
[0][1]*[1][0]
[0][2]*[1][1]
--換列---(<--對於最後的大矩陣來說)
[1][0]*[0][0]
[1][0]*[0][1]
[1][1]*[0][0]
[1][1]*[0][1]
--換列---(<--對於最後的大矩陣來說)
[1][0]*[1][0]
[1][0]*[1][1]
[1][1]*[1][0]
[1][2]*[1][1]
--換列---(<--對於最後的大矩陣來說)

以[a][b][c][d]來看..
先變的是d,再來是[b],再來是[c],最後是[a]
所以先變的在最裡面,最後變的在外面
for a in range():
     for c in range():
         for b in range():
             for d in range():
                [][]=A[a][b]*B[c][d]

'''

#先建立大矩陣--其他語言的寫法
matrix=[[0 for i in range(20*20+1)] for j in range(20*20+1)]
while True:
    try:
        A=[]
        B=[]
        m,n,p,r=map(int,input().split(" "))

        #輸入資料處理
        for i in range(m):
            A.append(list(map(int,input().split(" "))))
        for i in range(p):
            B.append(list(map(int,input().split(" "))))


        for a in range(m):
            for c in range(p):
                for b in range(n):
                    for d in range(r):
                        matrix[a*p+c][b*r+d]=A[a][b]*B[c][d]

        #資料輸出(可以在上面就直接輸出,就不用建大矩陣了-->matrix[a*p+c][b*r+d]=A[a][b]*B[c][d])
        outs=""
        for a in range(m):
            for c in range(p):
                for b in range(n):
                    for d in range(r):
                        outs+=str(matrix[a*p+c][b*r+d])+" "
                print(outs[:-1])
                outs=""
    except Exception as e:
        break


