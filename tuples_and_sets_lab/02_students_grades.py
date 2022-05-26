"""
On the first line, you will receive the number of students – N.
On the following N lines, you will be receiving a student's name and their grade.
For each student print all his/her grades and finally his/her average grade.

5
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00

"""

def avg(values):
    return sum(values) / len(values)


students_number = int(input())

students_dict = {}
for _ in range(students_number):
    name, grade = input().split(" ")
    grade_int = float(grade)
    if name not in students_dict:
        students_dict[name] = []

    students_dict[name].append(grade_int)

for name, grades in students_dict.items():
    grade_str = ' '.join(f"{grade:.2f}" for grade in grades)
    aver_grade = avg(grades)

    print(f'{name} -> {grade_str} (avg: {aver_grade:.2f})')
