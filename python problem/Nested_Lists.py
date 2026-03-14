if __name__ == '__main__':
    n=list()
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n.append(name)
        s.append(score)
    s1=sorted(list(set(s)))
    second=s1[1]
    ind=list()
    for i in range(len(s)):
        if s[i]==second:
            ind.append(i)
    a=list()
    for i in ind:
        a.append(n[i])
    a=sorted(a)
    for i in a:
        print(i)
