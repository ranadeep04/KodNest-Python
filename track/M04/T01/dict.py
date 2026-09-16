students=[
    {"roll":11,"name":"Rana","Marks":85},
    {"roll":22,"name":"Sai","Marks":90},
    {"roll":33,"name":"Ram","Marks":80},
    {"roll":44,"name":"Ben","Marks":95}
]
roll=int(input("Enter roll number"))

for student in students:
    if student["roll"]==roll:
        print(student["name"],student["Marks"])
        break
else:
    print("Student Not Found")