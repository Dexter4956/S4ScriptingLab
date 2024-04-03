num = int(input('Enter a number: '))

is_prime = True
if num > 1:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print('Entered number is prime')
else:
    print('Entered number is not prime')
