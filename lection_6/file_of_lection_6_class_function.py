
class Employee:
    name = ''
    salary = 0

    def rise_salary(self, amount):
        self.salary += amount



employee = Employee()
employee.name = 'ZZZZZ'
employee.salary = 10000000
employee.rise_salary(888)

print(employee.salary)