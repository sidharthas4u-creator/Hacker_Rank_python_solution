x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                a.append([i, j, k])
    c=0
    ch=list()
    for i in range(len(a)):
        for j in range(len(a[0])):
            c+=a[i][j]
        ch.append(c)
        c=0
    ab=a.copy()
    for i in range(len(ch)):
        if ch[i]==n:
            ab.remove(a[i])
    print(ab)
