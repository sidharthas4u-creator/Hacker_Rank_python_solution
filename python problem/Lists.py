if __name__ == '__main__':
    N = int(input())
    li=list()
    for i in range(N):
        l=input()
        li.append(l)
    lis=list()
    for i in li:
        if 'insert' in i:
            op,m,c=i.split()
            lis.insert(int(m),int(c))
        elif 'print' in  i:
            print(lis)
        elif 'remove' in i:
            op,m=i.split()
            lis.remove(int(m))
        elif 'append' in i:
            op,m=i.split()
            lis.append(int(m))
        elif 'sort' in i:
            lis.sort()
        elif 'reverse' in i:
            lis.reverse()
        else:
            lis.pop()
