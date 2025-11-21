
def staircase(n):
    for i in range(1,n+1):
      sp=n-i
      print(' '*sp+'#'*i)
        
         

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
