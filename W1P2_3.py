select = int(input())
info  = input().split(",")
a = float(info[0])
b = float(info[1])
if select == 1 :
  print(a*b)
elif select == 2:
  print(1/2*a*b)