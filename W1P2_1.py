num = input().split()
a = float(num[0])
b = float(num[1])
c = float(num[2])
if (a < b < c) or (c < b < a):
    middle = b
elif (b < a < c) or (c < a < b):
    middle = a
else:
    middle = c
print(middle)
