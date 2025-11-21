def miniMaxSum(arr):
    # Write your code here
    a=list(arr)
    arrmm=arr
    arrmx=arr
    mn= min(a)
    mx=max(a)
    arrmm.remove(mn)
    arrmx.remove(mx)
    for i in arrmm:
        mn+=i
    for i in arrmx:
        mx+=i
    print(mn,mx)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
