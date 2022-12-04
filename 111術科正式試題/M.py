#111商業技藝競賽正式試題
#Problem M 格雷碼（Gray Code）
#110商業技藝競賽模擬試題
#Problem G 格雷碼（Gray Code）
#2022/12/04
#https://github.com/yotrew/commercial_skill_competition
#排列
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

n=int(input())
gcode=[]


gray_code(n)

#'\n'.join(gcode)
for i in range(0,len(gcode)):
    print(gcode[i])
