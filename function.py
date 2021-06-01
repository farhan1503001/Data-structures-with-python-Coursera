def computepay(h,r):
    pay=0.0
    if h>=40:
        return (r*40)+(h-40.0)*(r*1.5)
    else:
        return r*h

hrs=float(input('Enter Hours: '))
rate=float(input('Enter Rate: '))
p=computepay(hrs,rate)
print(p)
        