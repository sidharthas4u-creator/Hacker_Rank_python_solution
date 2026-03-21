# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s=input()
m=int(s.split(" ")[-1])
s=s.split(" ")[-2]
for j in list(combinations_with_replacement(sorted(s),m)):
    print(''.join(j)) 
