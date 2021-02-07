class Employee:

    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.name} ({self.salary})'

    def rise_salary(self, amount):
        self.salary += amount

class Manager(Employee):
    subordinates = []

    def __str__(self):
        return f'{self.name}! ({self.salary}), подчиненные: {len(self.subordinates)}'

    def rise_salary_for_all(self, amount):
        for employee in self.subordinates:
            employee.rise_salary(amount)

manager = Manager('Ivanov', 10000000)
#manager.rise_salary(8888)

employee = Employee('Sidorov', 100000)

manager.subordinates.append(employee)

print(employee, manager)

manager.rise_salary_for_all(150000)
print(employee, manager)