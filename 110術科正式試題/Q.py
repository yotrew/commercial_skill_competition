#110商業技藝競賽正式試題
#Problem Q 果⼦堆合併
#Author: Yotrew Wing
#2021/12/02
'''
Huffman Tree
(*第3組測資少了3個:32,59,60*)
'''

n=int(input())
cnt=0
huffman=list(map(int,input().split(" ")))

while len(huffman)>1:
    huffman.sort()
    #print(huffman)
    t=huffman[0]+huffman[1]
    huffman.pop(0)
    huffman[0]=t
    cnt+=t
print(cnt)
'''
61
2 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 63 65
'''
