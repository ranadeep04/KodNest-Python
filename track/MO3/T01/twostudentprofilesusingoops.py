class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance variables
        self.student_id=student_id
        self.name=name
        self.course=course
        pass

first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

# Create the first StudentProfile object
student1=StudentProfile(first_id,first_name,first_course)
# Create the second StudentProfile object
student2=StudentProfile(second_id,second_name,second_course)

# Print the first student's data
print("Student 1")
print("ID:",student1.student_id)
print("Name:",student1.name)
print("Course:",student1.course)

print("Student 2")
print("ID:",student2.student_id)
print("Name:",student2.name)
print("Course:",student2.course)