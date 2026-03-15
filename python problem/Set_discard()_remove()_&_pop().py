n = int(input())
s = set(map(int, input().split()))
m=int(input())
op=list()
for i in range(m):
    w=input()
    op.append(w)
for i in op:
    if i=='pop':
        s.pop()
    elif 'remove' in i:
        s.remove(int(i[-1]))
    elif 'discard' in i:
        s.discard(int(i[-1]))      
sum=0
for i in list(s):
    sum=sum+i
if s:
    print(sum)
else:
    print(0)
