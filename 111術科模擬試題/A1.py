#111商業技藝競賽模擬試題
#Problem A1 內積
#Author: Yotrew Wing
#2022/10/17
#https://github.com/yotrew/commercial_skill_competition

while True:
  try:
    x1,x2,x3=map(int,input().split())
    y1,y2,y3=map(int,input().split())
    print(x1*y1+x2*y2+x3*y3)
  except:
    break
