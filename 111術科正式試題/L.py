#111商業技藝競賽正式試題
#Problem #L 二進制bit為1
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#轉2進位後,會是字串形式,直接使用count數有幾個1
while True:
    try:
        n=int(input())
        cnt=0
        for i in range(n+1):
            cnt+=bin(i).count("1")
        print(cnt)
    except:
        break
    
        
'''
Sample Input 1
7
Sample Output 1
12
Sample Input 2
6
Sample Output 2
9
Sample Input 3
5
Sample Output 3
7
'''
