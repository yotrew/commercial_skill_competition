#111商業技藝競賽正式試題
#Problem #F 字元刪除
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#字串取代
while True:
    try:
        a=input().strip() #strip把可能出現的\n或其他不該出現的字串濾掉
        b=input().strip()
        for i in b:
            a=a.replace(i,"") #取代成空,就刪除
        print(a)
    except:
        break
    
'''
Sample Input 1
They are students
aeiou
Sample Output 1
Thy r stdnts

Sample Input 2
They are students
e
Sample Output 2
Thy ar studnts

Sample Input 3
They are students
t
Sample Output 3
They are sudens
'''
