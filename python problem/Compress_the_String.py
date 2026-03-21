from itertools import groupby
re=[(len(list(s)),int(k))for k,s in groupby(input())]
print(*re)
