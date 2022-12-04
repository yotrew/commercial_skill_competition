#111商業技藝競賽正式試題
#Problem #I 字元出現次數
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition

while True:
    try:
        line=list(map(ord,list(input().strip()))) #輸出要用ASCII,所以讀入時直接轉
        cnt=dict() #使用字典做字數的統計
        for i in line:
            if i not in cnt.keys():
                cnt[i]=1
            else:
                cnt[i]+=1 #已存在字典中,就加1
                
        y=list(cnt.items()) #dictionary 轉list
        y.sort(key=lambda x:(x[1],127-x[0])) #次數由小到大排,次數一樣按ASCII倒著排,ASCII值應該不會超過127(不放心就用255去減)
        for i in y:
            print(i[0],i[1])
    except:
        break
        
    
        
'''
Sample Input 1
AAABBC
Sample Output 1
67 1
66 2
65 3
Sample Input 2
122333
Sample Output 2
49 1
50 2
51 3
Sample Input 3
AAABBc32433@@```
Sample Output 3
99 1
52 1
50 1
66 2
64 2
96 3
65 3
51 3
'''
