lst = input()
def left_more_right(lst):
  count = 0
  n = len(lst)
  for i in range(n):
      for j in range(i + 1, n):
          if lst[i] < lst[j]:
              count += 1
  return count
print(left_more_right(lst))