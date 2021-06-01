name = input("Enter your name")
print('Hello',name)

h=float(input('Enter hours: '))
r=float(input('Enter Rates'))
print("Pay",h*r)

h=float(input('Enter hours:'))
r=float(input('Enter Rates:'))
if h<=40:
    result=h*r
else:
    result=40.0*r+((h-40.0)*(1.5*r))
print(result)

flag=True
try:
    score=float(input('Enter Score: '))
except Exception as e:
    print('Invalid')
    flag=False
if flag:
    if score<0.0 and score>1.0:
        print('error')
    elif score>=0.9:
        print('A')
    elif score>=0.8:
        print('B')
    elif score>=0.7:
        print('C')
    elif score>=0.6:
        print('D')
    else:
        print('F')