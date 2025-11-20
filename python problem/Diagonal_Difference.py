def diagonalDifference(arr):
    # Write your code here
    s=0
    for i in range(len(arr)):
       s+=(arr[i][i]) 
    s1=0
    for i in range(len(arr)):
        s1+=(arr[i][(len(arr)-1)-i])
    if(s1>s):
        return s1-s
    else:
        return s-s1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
