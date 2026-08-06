number_count=int(input())

pos_counter=0
neg_counter=0
zero_counter=0
total=0

for i in range(number_count):
    number=int(input())
    total+=number

    if number>0:
        pos_counter+=1
    elif number<0:
        neg_counter+=1
    else:
        zero_counter+=1

print("Positive count:",pos_counter)
print("Negative count:",neg_counter)
print("Zero count:",zero_counter)
print("Total:",total)