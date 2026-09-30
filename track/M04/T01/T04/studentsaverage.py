students=[
    ["Alice",85,90,78],["Bob",70,88,92],["Charlie",95,80,89],["David", 60,75,68],["Eva",88,92,95],["Frank",72,65,80],["Grace",90,85,91]
]
#1.AVERAGE
for student in students:
    name=student[0]
    marks=student[1:]

    average=sum(marks)/len(marks)

    print(f"{name} --> Average: {average:.2f}")

#2.TOP STUDENTS
top_students=[student[0] for student in students if all(mark>=80 for mark in student[1:])]

print("Top Students:\n",top_students )

#3.WEAK STUDENTS

weak_students=[student[0] for student in students if any(mark<=70 for mark in student[1:])]

print("Students needing improvement:\n", weak_students)

#4.HIGH scoring Student

high_performers={student[0]:average for student in students if average>=80}

print("High Performers:",high_performers)