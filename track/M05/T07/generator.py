#normal function
# def count_num(n):
#     numbers=[]
#     count=0
#     while count<=n:
#         numbers.append(count)
#         count+=1
#     return numbers

# n=int(input("Enter your number"))

# for i in count_num(n):
#     print(i)


#Genertor funtion

def count_num(n):
    count=0
    while count<=n:
        yield count
        count+=1

n=int(input())

for i in count_num(n):
    print(i)
