class Employee:
    name = ''
    salary = 0

    def rise_salary(self, amount):
        self.salary += amount

class Manager(Employee):
    subordinates = []
    def rise_salary_for_all(self, amount):
        for employee in self.subordinates:
            employee.rise_salary(amount)

manager = Manager()
manager.name = 'Ivanov'
manager.salary = 10000000
manager.rise_salary(8888)

employee = Employee()
employee.name = 'Sidorov'
employee.salary = 100000


manager.subordinates.append(employee)

print(f"Sidorov DO: {employee.salary}")

manager.rise_salary_for_all(150000)
print(f"Sidorov POSLE: {employee.salary}")