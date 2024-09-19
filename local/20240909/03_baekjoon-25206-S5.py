Grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
Point = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total = 0
total_point = 0
for _ in range(20):
    name, point, grade = input().split()
    point = float(point)
    if grade != 'P':
        total += point
        total_point += point * Point[Grade.index(grade)]

print(total_point / total)