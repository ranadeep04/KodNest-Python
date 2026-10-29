import json
name="Rana"
marks=45

print(name,type(name))
print(marks,type(marks))

person={"name":name, "marks":marks}

print(person,type(person))

strObj=json.dumps(person)

print(strObj,type(strObj))

with open("data.json", "w") as f:
    f.write(strObj)