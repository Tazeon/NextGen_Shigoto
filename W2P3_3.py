s = input()
s = s.strip('[]')
string_list = s.split(',')
num = [int(i) for i in string_list]
def sorted_num(num):
  for i in range(len(num)-1):
    if num[i] >= num[i+1]:
      return False
  return True
print(sorted_num(num))


