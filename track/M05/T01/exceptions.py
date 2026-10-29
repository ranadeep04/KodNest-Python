
try:
    # num1=10
    # num2=0
    # res=num1//num2
    # print(res)
    # lst=[1,2,3]
    # print(lst[3])
    a=int(input("Enter the number"))
    print(a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index out of range")
except Exception:
    print("Invalid input")
finally:
    print("Execution Completed")