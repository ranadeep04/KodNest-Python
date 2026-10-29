import student_details,totalaverage,resultgrade


name=input("Enter Name:")
roll_no=int(input("Enter Roll No:"))

m1=int(input("Enter Marks1:"))
m2=int(input("Enter Marks2:"))
m3=int(input("Enter Marks3:"))

student_details.student_details(name,roll_no)
total=totalaverage.calculate_total(m1,m2,m3)
average=totalaverage.calculate_average(m1,m2,m3)
print(average)

resultgrade.get_result(average)
resultgrade.show_grade(average)
