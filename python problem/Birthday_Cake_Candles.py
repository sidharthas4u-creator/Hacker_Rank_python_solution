def birthdayCakeCandles(arr):
    # Write your code here
    mx=max(arr)
    c=0
    for i in arr:
        if(mx==i):
            c=c+1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
