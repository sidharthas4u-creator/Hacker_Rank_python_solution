# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s=input()
i=int(s.split(" ")[-1])
s=s.split(" ")[-2]
l=list(permutations(s,i))
l=["".join(x) for x in l]
l=sorted(l)
for i in l:
    print(i)
