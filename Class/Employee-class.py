

class Employee(object):
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def get_salary(self):
        print("Your salary is {0}".format(self.salary))

    def update_salary(self, salary):
        self.salary = salary

    def get_employee(self):
        return "{0} his position is {1} and his salary is {2}".format(self.name, self.position, self.salary)

emp1 = Employee("Eli", 9000, "Sound Engineer")
my_emp = emp1.get_employee()
print(my_emp)

emp1.get_salary()
emp1.update_salary(10000)
emp1.get_salary()