def get_result(average):
    if average>=40:
        print("Pass")
    else:
        print("Fail")

def show_grade(average):
    if average>=90:
        print("A")
    elif average>=75 and average<90:
        print("B")
    elif average>=60:
        print("C")
    elif average>=40:
        print("D")
    else:
        print("F")