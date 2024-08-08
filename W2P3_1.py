n = int(input("n : "))
term = n // 5
sum = 0
for i in range(1, term + 1):
  sum += 5 * i
print(sum)
