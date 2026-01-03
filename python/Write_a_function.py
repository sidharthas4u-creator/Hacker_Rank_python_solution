def is_leap(year):
    if(year>=2100):
        l=int(year%400)
        if(l==0):
            leap = True
        else:
            leap = False
        return leap
    else:
        l=int(year%4)
        if(l==0):
            leap = True
        else:
            leap = False
        return leap
year = int(input())
print(is_leap(year))
