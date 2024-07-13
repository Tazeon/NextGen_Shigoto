number = input().split()
a = float(number[0])
b = float(number[1])
c = float(number[2])
d = float(number[3])
e = float(number[4])

# ตรวจสอบว่าลำดับจากซ้ายไปขวาของจำนวนเหล่านี้เรียงจากน้อยไปมากหรือไม่
if a <= b <= c <= d <= e : 
    print(True)
else:
    print(False)