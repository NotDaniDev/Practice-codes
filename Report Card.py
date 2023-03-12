arr = []
grades = {range(90,101):'A+',
          range(80,90):'A',
          range(70,80):'B',
          range(60,70):'C',
          range(50,60):'D',
          range(0,50):'F'}
class_total = 0
student_count = int(input('Enter number of students: '))
for i in range(student_count):
    name = str(input('Enter name of student: '))
    maths = float(input('Enter maths marks of student: '))
    english = float(input('Enter english marks of student: '))
    cs = float(input('Enter computer science marks of student: '))
    total = english + maths + cs
    average = (maths+english+cs)/3
    for key in grades:
        if round(average) in key:
            grade = grades[key]
    l = [name,maths,english,cs,total,average,grade]
    arr.append(l)
    class_total += total
    print('Name: ', name)
    print('Average: ', average)
    print('Grade: ', grade)
class_average = class_total/student_count
print('Class Total: ', class_total)
print('Class Average: ', class_average)