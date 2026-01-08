import numpy as np
n, m = map(int, input().split())
my_array = np.array([input().split() for _ in range(n)], int)
d=list(set(np.min(my_array,axis=1)))
print(max(d))
