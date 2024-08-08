for num in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        print(num,end=',')
