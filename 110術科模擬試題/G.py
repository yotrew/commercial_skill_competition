#110商業技藝競賽模擬試題
#Problem G 格雷碼（Gray Code）
#Author: Yotrew Wing
#2021/10/18
#https://github.com/yotrew/commercial_skill_competition
n=int(input())
gcode=[]
def gray_code(n):
    global gcode
    if n==1:
        gcode=["0","1"]
        return
    gray_code(n-1)
    tmp=[]
    for i in range(len(gcode)):
        tmp.append("0"+gcode[i])
    for i in range(len(gcode)-1,-1,-1):
        tmp.append("1"+gcode[i])
    gcode=tmp

gray_code(n)
for i in range(0,len(gcode)):
    print(gcode[i])
