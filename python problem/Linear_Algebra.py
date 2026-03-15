import numpy as n
row=int(input())
l=list()
for i in range(row):
        r=list(map(float,input().split()))
        l.append(r)
print(round((n.linalg.det(n.array(l))),2))
