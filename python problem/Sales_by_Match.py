def sockMerchant(n, ar):
    # Write your code here
    s=tuple(set(ar))
    dic=dict()
    for i in s:
        c=0
        for j in ar:
            if i==j:
                c=c+1
        dic[i]=c//2
    c=0
    for i in dic.values():
        c+=i
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
