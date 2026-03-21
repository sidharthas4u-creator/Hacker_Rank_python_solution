# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=map(int,input().split())
b=map(int,input().split())
for i in list(product(a,b)):
    print(i,end=" ")
