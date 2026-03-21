# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s=input()
m=int(s.split(" ")[-1])
s=s.split(" ")[-2]
for i in range(1,m+1):
    for j in list(combinations(sorted(s),i)):
        print(''.join(j)) 
