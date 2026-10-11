# {key:value},mutable, key cannot be duplicated,indexed
student={"name":"Amit","age":21,"course":"computer science","Tech":"computer science","status":True}
print(student)
student={"name":"Amit","name":"Rahul","age":21,"course":"computer science","Tech":["computer science","Python","Sql"]}
print(student)
student["age"]=25
student.update({"cgpa":8.5})
student.update({"cgpa":8.5,"Gender":"Male"})
print(student["age"])
print(student,type(student),len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))
print(student.pop("course"))
student.popitem()
#del student
print(student)
student={"name":"Rahul","age":23,"Tech":["Python","SQL"]}
student.setdefault("age",22)
print(student)
keys=["name","age","course"]
student=dict.fromkeys(keys,"Not available")
print(student)
keys=["name","age","course"]
y=0
student=dict.fromkeys(keys,y)
print(student)

my_dict=student.copy()
print(my_dict)
my_dict.update({"name":"Amit"})
print(my_dict) 

#Looping of dictionaries
student={"name":"Rahul","Language":"java","marks":88}
for x in student:
    print(f"{x}= {student[x]}")
for x in student.items():
    print(x)
for x in student.keys():
    print(x)
for x in student.values():
    print(x)
#Nested dictionaries
students={"stu1":{"Name":"Rahul","age":23,"Tech":["Java","SQL"]},"stu2":{"Name":"Amit","age":22,"Tech":["Python","Sql"]}}
print(students)
print(students["stu2"]["Name"])
for x in students:
    print(x)
    for y in students[x]:
        print(y,students[x][y])

