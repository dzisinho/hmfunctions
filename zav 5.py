def a_in_range(start,end):
    if start>end:
        start,end=end,start
    a=1
    for i in range(start,end+1):
        a*=i
    return a
b=a_in_range(2,5)
print(b)