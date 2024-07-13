scale = str(input())
cheese = str(input())
extra = str(input())
price = 0
if scale == "S":
  price += 99
  if cheese == "Y":
    price += 20
elif scale == "M":
  price += 199
  if cheese == "Y":
    price += 30
elif scale == "L":
  price += 299
  if cheese == "Y":
    price += 40
if extra == "Y":
  price += 20
print(price)
