lst = eval(input())
cnt_dict = {}

for i in lst:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

for key, value in cnt_dict.items():
    print(f"{key} = {value}")
