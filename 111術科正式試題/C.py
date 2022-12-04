#111商業技藝競賽正式試題
#Problem #C 翻轉數字
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition

while True:
    try:
        line=input().strip()[-1::-1] #輸入後直接倒著取
        print(int(line))  #字串轉整數後,前面的0會不見
    except:
        break
'''
Sample Input 1
123456
Sample Output 1
654321
Sample Input 2
12345
Sample Output 2
54321
Sample Input 3
230400
Sample Output 3
4032
'''
