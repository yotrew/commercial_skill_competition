#108商業技藝競賽正式試題
#Problem 3： 子題 2：循環小數
'''
直接用除,會有"不精準"問題
1.本方法:
2.另一種想法是,用字串方式去思考,但這樣好像不太好寫,且每字都要比對子字串可能會比較慢
'''
n=int(input())
for i in range(0,n):

    A,B=map(int,input().split(" "))
    Q=str(int(A/B))+"."#整數部份
    A=A % B#本次的餘數
    R=[]
    R.append(A)#餘數列表,若下次有出現一樣的餘數代表從上次出現相同餘數地方開始循環
    s1=""#小數部份字串
    cycle=""
    while A>0:#餘數為0代表整除
        A=A*10 #除法做法,就是往前移一位
        s1+=str(int(A/B))
        A=A % B#本次的餘數
        if A in R:#代表出現循環
            c=R.index(A)#找出A的位置
            cycle=s1[0:c]+"(" + s1[c:]+")" #取s1 0~c-1位置的字串 + ( c~最後 位置的字串 )
                                #s1[c:-1] <--是取到倒數第2個,不包含最後一個
            break
        else:
            R.append(A)
        if(len(s1)>=50):#題目限制小數後最多50位
            cycle+="("+s1+"...)" #題目沒說明要括號,但範例有
            break
    if(len(cycle)==0):
        print(Q+s1+"(0)")
    else:
        print(Q+cycle)
