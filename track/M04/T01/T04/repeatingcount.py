names=["amit","arjun","ajay","ansh","amit","arjun","arav"]
# dic={}

# for i in names:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1

# print(dic)

from collections import Counter

frequency=Counter(names)

print(frequency)