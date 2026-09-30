n = int(input())
cities = []

for _ in range(n):
    cities.append(input().strip())

# Write your code here
# sorted_cities=sorted(cities)
# for i in sorted_cities:
#     print(i)
n=cities.sort()
print(n)
for i in cities:
    print(i)