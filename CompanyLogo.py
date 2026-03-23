from collections import Counter
if __name__ == '__main__':
    s = input()
    s1=dict(Counter(s))
    c=0
    for i in s1:
        c+=1
        if c<=3:
            print(i,s1[i])
