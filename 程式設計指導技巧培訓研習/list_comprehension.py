usd=[199,299,399]
c=28 #匯率,1美金=?NTD

ntd=[]
for p in usd:
  q=p*c
  ntd.append(q)

print(ntd)

ntd2=[p*c for p in usd]#list comprehension
print(ntd2)
