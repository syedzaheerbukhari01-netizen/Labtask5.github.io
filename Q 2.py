employees = []
for i in range(3):
    print("information for employee", i + 1)
    name = input("ur name: ")
    age = int(input("write age: "))
    salary = float(input("enter salary: "))
    employee = (name,age,salary)
    employees.append(employee)
print("Employee Information:")
for employee in employees:
    print(employee)