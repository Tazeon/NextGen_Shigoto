number = list(map(int, input().split()))

max_num = max(number)
min_num = min(number)

sumall = sum(number) - max_num- min_num

print(sumall)
