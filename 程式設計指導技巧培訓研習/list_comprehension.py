usd=[199,299,399]
c=28 #å¯į,1įžé=?NTD

ntd=[]
for p in usd:
  q=p*c
  ntd.append(q)

print(ntd)

ntd2=[p*c for p in usd]#list comprehension
print(ntd2)
