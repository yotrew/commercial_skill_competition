#107商業技藝競賽正式試題
#Problem 1：子題 1：計算字數及含有s 或 S 字母的字數
#同106商業技藝競賽正式試題Problem 1：子題 1
'''
我是多行註解:
題目:計算字數及含有s或S字數
輸入說明:第一列的數字n代表有幾組資料要測試
'''
fd=open("ex1_2.txt","r")
line=fd.readline()
n=int(line)

for i in range(1,n+1):
    space=0 #計算有幾個空白,1個空白代表有2個字,2個有3個字
    s_count=0 #s的個數
    line=fd.readline()
    flag=False
    for j in range(0,len(line)):
        if(line[j]==' ' or line[j]==';'): #遇空白或分號就是下一個字
            space+=1
            flag=False #遇到空格代表換下一個字了,如This is a book.,原本在This,遇到空格就代表換is了
        if((line[j]=='s' or line[j]=='S') and flag==False):
            s_count+=1
            flag=True #代表這個字已被計算過了,如SOS,遇到第1個S後,第2個S還是在同一個字
    print("%d,%d"%(space+1,s_count))