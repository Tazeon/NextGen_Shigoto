
x = int(input())

if 90 <= x <= 100:
    grade = 'A'
elif 85 <= x < 90:
    grade = 'B+'
elif 80 <= x < 85:
    grade = 'B'
elif 70 <= x < 80:
    grade = 'C+'
elif 60 <= x < 70:
    grade = 'C'
elif 55 <= x < 60:
    grade = 'D+'
elif 50 <= x < 55:
    grade = 'D'
else:
    grade = 'F'

print(grade)