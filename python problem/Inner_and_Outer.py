import numpy as n
A=n.array([input().split()],int)
B=n.array([input().split()],int)
s=n.inner(A,B)
print(s[0,0])
print(n.outer(A,B))
