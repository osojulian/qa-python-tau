def add():
    a = float(input('Enter a number: '))
    b = float(input('Enter another number: '))
    print(a + b)

def substraction():
    a = float(input('Enter a number: '))
    b = float(input('Enter another number: '))
    print(a - b)

def multiplication():
    a = float(input('Enter a number: '))
    b = float(input('Enter another number: '))
    print(a * b)

def division():
    a = float(input('Enter a number: '))
    b = float(input('Enter another number: '))
    print(a / b)

print('Select operation:')
print('1. Add')
print('2. Substraction')
print('3. Multiplication')
print('4. Division')
choice = input('Enter choice (1/2/3/4): ')
if choice == '1':
    add()
elif choice == '2':
    substraction()
elif choice =='3':
    multiplication()
elif choice == '4':
    division()
else:
    print('Invalid input')
