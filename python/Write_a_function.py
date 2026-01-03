def is_leap(year):
    l=year%4
    if(l==0):
        leap = True
        return leap
    else:
        leap = False
    return leap
year = int(input())
print(is_leap(year))
