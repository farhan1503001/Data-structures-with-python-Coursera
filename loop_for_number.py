largest_number=None
smallest_number=None
while True:
    order=input('Enter a number: ')
    if order=='done':
        break
    try:
        number=int(order)
    except Exception as e:
        print("Invalid Input")
        continue
    if largest_number is None:
        largest_number=number
    if smallest_number is None:
        smallest_number=number
    if largest_number<number:
        largest_number=number
    if smallest_number>number:
        smallest_number=number
print(largest_number)
print(smallest_number)