def plusMinus(arr):
    # Write your code here
    t=len(arr)
    cp=0
    cn=0
    cz=0
    for i in range(t):
        if(arr[i]>0):
            cp+=1
        elif(arr[i]==0):
            cz+=1
        else:
            cn+=1
    print(cp/t)
    print(cn/t)
    print(cz/t)
    return cp/t,cn/t,cz/t
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
