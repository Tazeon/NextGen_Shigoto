n1 = int(input("num1 : "))
n2 = int(input("num2 : "))
def gcd(n1, n2):
  while n2:
      n1, n2 = n2, n1 % n2
  return n1

print(gcd(n1, n2))
