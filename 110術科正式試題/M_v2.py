#110商業技藝競賽正式試題
#Problem M 矩陣的直積
#Author: Yotrew Wing
#2022/12/07
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
#直接輸出版本


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
                        print(A[a][b]*B[c][d],end=" ") #最後一個空白評測系統不會做比對...此題來說
                print()


    except Exception as e:
        break


