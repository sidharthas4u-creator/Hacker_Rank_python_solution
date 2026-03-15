import calendar as c
s=list(map(int,input().split()))
dayname=(c.day_name[c.weekday(s[-1],s[-3],s[-2])])
print(dayname.upper())
