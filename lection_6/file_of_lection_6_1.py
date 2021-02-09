
"""
employee = {
    'name': 'Иванов',
    'salary': 30000,
    'boss': 'Сидоров'
}
employee_1 = dict(employee)
employee_2 = dict(employee)
employee_3 = dict(employee)

employees = [
    employee,
    employee_1,
    employee_2,
    employee_3
]

def avarange_slary(employees):
    total_salary = sum([emp['salary'] for emp in employees])
    return total_salary / len(employees) if len(employees) > 0 else 0
print(avarange_slary(employees))
"""

class Employee:
    name = ''
    salary = 0

employee = Employee()
employee.name = 'ZZZZZ'
employee.salary = 236457

employee_1 = Employee()
employee.name = 'QQQQQ'
employee.salary = 8478378

employees = [
    employee,
    employee_1
]

def avarange_slary(employees):
    total_salary = sum([emp.salary for emp in employees])
    return total_salary / len(employees) if len(employees) > 0 else 0
print(avarange_slary(employees))