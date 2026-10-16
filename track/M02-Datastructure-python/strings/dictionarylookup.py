products={"p101":["Keyboard",1200],"p102":["Mouse",600],"p103":["Monitor",8500]}
print(products["p103"])
res=products.get("p103","Product not found")
print(res)
products["p102"][0]="Pentab"
print(products)
employees=[{"employee_id":"E101","Name":"Asha","department":"Development"},{"employee_id":"E102","Name":"Ravi","department":"Testing"},{"employee_id":"E103","Name":"Meera","department":"Support"}]
print(employees)
employee_by_id={}
for employee in employees:
    employee_id=employee["employee_id"]
    employee_by_id[employee_id]=employee
print(employee_by_id)

students=[{"name":"Asha","course":"Python","name":"Ravi","course":"java","name":"Meera","course":"Python","name":"Kiran","course":"SQL"}]
students_by_course={}
for student in students:
    course=student["course"]
    name=student["name"]
    students_by_course.setdefault(course,[]).append(name)


